from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, RadioField, TextAreaField, validators, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired, Email


class CreateUserForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", [InputRequired("Please enter your email address."),
                                  Email("This field requires a valid email address")])
    gender = RadioField('Gender', choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    def validate_password(forms, password):
        if len(password.data) < 8:
            raise ValidationError("Longer Password Please")


class CreateCustomerForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", [InputRequired("Please enter your email address."),
                                  Email("This field requires a valid email address")])
    gender = RadioField('Gender', choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    password = PasswordField('Password', validators=[DataRequired()])
    membership = RadioField('Membership', choices=[('N', 'None'), ('N', 'New'), ('S', 'Senior')], default='F')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    remember = BooleanField('Remember Me')

    def validate_password(forms, password):
        if len(password.data) < 8:
            raise ValidationError("Longer Password Please")


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])


class SearchCustomerForm(Form):
    searchCustomer = StringField('Search Username', [validators.DataRequired()])


class SearchUserIDForm(Form):
    searchUserID = StringField('Search User ID', [validators.DataRequired()])

class UpdateUserForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", [InputRequired("Please enter your email address."),
                                  Email("This field requires a valid email address")])
    gender = RadioField('Gender', choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    password = PasswordField('Password', validators=[DataRequired()])
    #confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class UpdateCustomerForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", [InputRequired("Please enter your email address."),
                                  Email("This field requires a valid email address")])
    gender = RadioField('Gender', choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    password = PasswordField('Password', validators=[DataRequired()])
    membership = RadioField('Membership', choices=[('N', 'None'), ('N', 'New'), ('S', 'Senior')], default='F')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    #remember = BooleanField('Remember Me')
