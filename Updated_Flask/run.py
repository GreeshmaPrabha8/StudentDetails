from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from forms import queryform, itemform



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

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
        




@app.route("/")
def index():
    return render_template("index.html")



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
			error = "No items"
	return render_template('query.html', form=form, error=error)


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
			flash("Item updated")
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
			flash("Item deleted")
		except Exception as e:
			error = e
	return render_template('query.html', error=error)





if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
