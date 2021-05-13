
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
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
    return render_template("index.html");

@app.route("/add_student")
def add_student():
    return render_template("add_student.html")


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
    my_data = students(name, standard, division, rollno, passed, failed, missed)
    db.session.add(my_data)
    db.session.commit()
    msg = 'Record was successfully added'
    #return redirect(url_for('student_info'),msg=msg)
    return render_template('success_record.html',msg=msg)





@app.route("/student_info")
def student_info():
   return render_template('student_info.html', rows = students.query.all() )



@app.route("/check_info")
def check_info():
   return render_template('check.html', item = students.query.filter(or_(students.failed>=4, students.missed>=4)))


@app.route("/delete_student")
def delete_student():
    return render_template("delete_student.html")


@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    id = request.form["id"]
    my_data = students.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    msg="Student Deleted Successfully"
    return render_template("delete_record.html",msg=msg)


@app.route('/student_info/update/<int:id>',methods = ['GET','POST'])
def update(id):
  my_data = students.query.filter_by(rollno=id).first()
  if request.method == 'POST':
    if my_data:
      db.session.delete(my_data)
      db.session.commit()
 
      name = request.form['name']
      standard = request.form['standard']
      division = request.form['division']
      #rollno = request.form['rollno']
      passed = request.form['passed']
      failed = request.form['failed']
      missed = request.form['missed']
      my_data = students(rollno=id, name=name, standard=standard, division=division, passed = passed, failed = failed, missed = missed)
 
      db.session.add(my_data)
      db.session.commit()
      return redirect(f'/student_info')
    return f"Employee with id = {id} Does not exist"
 
  return render_template('update.html', my_data = my_data)







if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
