from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from forms import queryform, itemform, RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user, login_required


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)






class items(db.Model):
  name = db.Column(db.String(20), nullable=False)
  standard = db.Column(db.String(120), nullable=False)
  division = db.Column(db.String(), nullable=False)
  rollno = db.Column(db.Integer, primary_key=True)
  passed = db.Column(db.Integer, nullable=False)
  failed = db.Column(db.Integer, nullable=False)
  missed = db.Column(db.Integer, nullable=False)

  

  def __init__(self, name, standard, division, rollno, passed, failed, missed):
    self.name = name
    self.standard = standard
    self.division = division
    self.rollno = rollno
    self.passed = passed 
    self.failed = failed
    self.missed = missed




class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), primary_key=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
      



@app.route("/")
def base():
    return render_template("base.html")


@app.route("/index")
def index():
    return render_template("index.html")





@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			flash('User Authenticated Successfully', 'success')
			return redirect(url_for('index'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
	#logout_user()
	return redirect(url_for('base'))




@app.route('/add/', methods=['GET', 'POST'])
def add_item():
	error = None
	form = itemform()
	if form.validate_on_submit():
		try:
			i = items(name=form.name.data, standard=form.standard.data, division=form.division.data, rollno=form.rollno.data, passed=form.passed.data, failed=form.failed.data, missed=form.missed.data)
			db.session.add(i)
			db.session.commit()
			msg = 'Record was successfully added'
			return render_template('success_record.html',msg=msg)
		except Exception as e:
			error = e
	return render_template('add.html', form=form, error=error)


@app.route("/saverecord",methods = ["POST","GET"])
def saveRecord():
  if request.method == 'POST':

    name = request.form['name']
    standard = request.form['standard']
    division = request.form['division']
    rollno = request.form['rollno']
    passed = request.form['passed']
    failed = request.form['failed']
    missed = request.form['missed']
    my_data = items(name, standard, division, rollno, passed, failed, missed)
    db.session.add(my_data)
    db.session.commit()
    msg = 'Record was successfully added'
    #return redirect(url_for('student_info'),msg=msg)
    return render_template('success_record.html',msg=msg)





@app.route('/student_info')
def student_info():
	q = items.query.all()
	return render_template('student_info.html', items=q)

@app.route("/check_info")
def check_info():
	q = items.query.filter(or_(items.failed>=4, items.missed>=4))
	return render_template('check_info.html', items = q)


@app.route('/query/', methods=['GET', 'POST'])
def query_item():
	error = None
	form = queryform()
	if form.validate_on_submit():
		q = items.query.filter_by(rollno=form.rollno.data).all()
		if q:
			return render_template('query.html', form=form, items=q)
		else:
			msg = ('Record was not found')
			return render_template('record.html',msg=msg)

			
	return render_template('query.html', form=form)


@app.route('/edit/<int:rollno>', methods=['GET', 'POST'])
def edit_item(rollno):
	error = None
	q = items.query.filter_by(rollno=rollno).first_or_404()
	form = itemform(obj=q)
	if form.validate_on_submit():
		try:
			q.name = form.name.data
			q.standard = form.standard.data
			q.division = form.division.data
			q.rollno = form.rollno.data
			q.passed = form.passed.data
			q.failed = form.failed.data
			q.missed = form.missed.data
			db.session.commit()
			#flash("Item updated")
			msg = 'Student updated'
			return render_template('success_record.html',msg=msg)

		except Exception as e:
			error = e
	return render_template('edit.html', form=form, error=error)

@app.route('/delete/<int:rollno>', methods=['GET', 'POST'])
def delete_item(rollno):
	error = None
	q = items.query.filter_by(rollno=rollno).first_or_404()
	if q:
		try:
			db.session.delete(q)
			db.session.commit()
			msg = 'Student deleted'
			return render_template('success_record.html',msg=msg)
		except Exception as e:
			error = e
	return render_template('query.html', error=error)





if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
