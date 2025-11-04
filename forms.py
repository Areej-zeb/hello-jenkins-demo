"""
Simple forms with security validation
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import re


class NoSQLKeywords(object):
    """Prevent SQL injection"""
    def __init__(self, message=None):
        if not message:
            message = 'Invalid input - SQL keywords detected!'
        self.message = message
    
    def __call__(self, form, field):
        sql_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'CREATE', 'ALTER', 'UNION', '--', '/*', '*/']
        data = field.data.upper() if field.data else ''
        
        for keyword in sql_keywords:
            if keyword in data:
                raise ValidationError(self.message)


class NoHTMLTags(object):
    """Prevent XSS attacks"""
    def __init__(self, message=None):
        if not message:
            message = 'HTML tags not allowed!'
        self.message = message
    
    def __call__(self, form, field):
        if field.data and re.search(r'<[^>]+>', field.data):
            raise ValidationError(self.message)


class LoginForm(FlaskForm):
    """Simple login form"""
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=50),
        NoSQLKeywords(),
        NoHTMLTags()
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ContactForm(FlaskForm):
    """Simple contact form"""
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=100),
        NoSQLKeywords(),
        NoHTMLTags()
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Length(max=100),
        NoSQLKeywords(),
        NoHTMLTags()
    ])
    phone = StringField('Phone', validators=[
        DataRequired(),
        Length(min=10, max=20),
        NoSQLKeywords(),
        NoHTMLTags()
    ])
    address = StringField('Address', validators=[
        DataRequired(),
        Length(min=5, max=200),
        NoSQLKeywords(),
        NoHTMLTags()
    ])
    submit = SubmitField('Add Contact')
