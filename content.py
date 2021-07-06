

from flask_wtf import FlaskForm 
from wtforms import StringField , PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length ,EqualTo ,email_validator,Email 
from wtforms.fields.html5 import EmailField



#class SignupForm(FlaskForm):
#    username =StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
#    email = EmailField('Email',validators=[DataRequired(),Email()])
#    password  = PasswordField('Password',validators=[DataRequired()])
#    conform_password  = PasswordField('Conform Password',validators=[DataRequired()])
#    submit = SubmitField('Sing Up')


class LoginForm(FlaskForm):

    email = EmailField('Email',validators=[DataRequired(),Email()])
    password  = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')



#class First_content(FlaskForm):

#    firstpost = StringField('first-content',validators=[DataRequired(),Length(min=2,max=800)])
#    submit = SubmitField('Post')


#class Second_content(FlaskForm):

#    secondpost = StringField('second-content',validators=[DataRequired(),Length(min=2,max=800)])
#    submit = SubmitField('Post')


#class Third_content(FlaskForm):

#    thirdpost = StringField('third-content',validators=[DataRequired(),Length(min=2,max=800)])
#    submit = SubmitField('Post')
