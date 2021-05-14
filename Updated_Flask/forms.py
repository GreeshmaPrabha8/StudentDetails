from flask_wtf import Form
from wtforms import TextField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class queryform(Form):
	rollno = IntegerField('Student ID', validators=[DataRequired()])

class itemform(Form):
	name= TextField("Name ",validators = [DataRequired()])
	standard = SelectField('Standard', choices = [('LKG', 'LKG'), ('UKG', 'UKG'), (1 ,1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7,7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], validators=[DataRequired()])
	division = SelectField('Division', choices = [('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D'),('E', 'E')],validators=[DataRequired()])
	rollno = IntegerField('ID',validators=[DataRequired()]) 
	passed = SelectField('Passed', choices = [(0, 0),(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)],validators=[DataRequired()])
	failed = SelectField('Failed', choices = [(0, 0),(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)],validators=[DataRequired()])
	missed = SelectField('Missed', choices = [(0, 0),(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)],validators=[DataRequired()])
	submit = SubmitField("Submit")

