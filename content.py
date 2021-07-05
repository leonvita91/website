

from flask_wtf import FlaskForm 
from wtforms import StringField , PasswordField, SubmitField
from wtforms.validators import DataRequired, Length ,Email ,EqualTo 


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired()])
    password  = StringField('Password',validators= [DataRequired()])
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
