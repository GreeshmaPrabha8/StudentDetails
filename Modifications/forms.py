from flask_wtf import Form
from wtforms import TextField, IntegerField, SelectField, SubmitField, BooleanField, PasswordField, StringField
from wtforms.validators import DataRequired, NumberRange, Length, Email, EqualTo



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

class RegistrationForm(Form):
	#id = IntegerField('id',validators=[DataRequired()])
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	
class LoginForm(Form):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')