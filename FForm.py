from wtforms import Form, StringField, validators, TextAreaField, RadioField, ValidationError
from wtforms.fields import EmailField, DateField


class SubmitFeedback(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    feedback = TextAreaField('Feedback', [validators.Optional()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    web_rating = RadioField('Website Rating', choices=[('3', '3 Star'), ('2', '2 Star'), ('1', '1 Star')], default='F')
    service_rating = RadioField('Website Rating', choices=[('3', '3 Star'), ('2', '2 Star'), ('1', '1 Star')], default='F')

    def validate_first_name(form, first_name):
        if not first_name.data.isalpha():
            raise ValidationError("must be letters only")
        if not first_name.data.isupper():
            raise ValidationError("must be capital")

    def validate_last_name(form, last_name):
        if not last_name.data.isalpha():
            raise ValidationError("must be letters only")
        if not last_name.data.isupper():
            raise ValidationError("must be capital")


class UpdateFeedback(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()], render_kw={'readonly': True})
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()], render_kw={'readonly': True})
    feedback = TextAreaField('Feedback', [validators.Optional()], render_kw={'readonly': True})
    email = EmailField('Email', [validators.Email(), validators.DataRequired()], render_kw={'readonly': True})
    web_rating = RadioField('Website Rating', choices=[('3', '3 Star'), ('2', '2 Star'), ('1', '1 Star')], default='F', render_kw={'readonly': True})
    service_rating = RadioField('Website Rating', choices=[('3', '3 Star'), ('2', '2 Star'), ('1', '1 Star')], default='F', render_kw={'readonly': True})
    status = RadioField('Status', choices=[("pending"), ('processed')])


class SearchUser(Form):
    searchUser = StringField('Search Name', [validators.DataRequired()])

    def validate_searchuser(form, searchUser):
        if not searchUser.data.isalpha():
            raise ValidationError("must be letters only")
        if not searchUser.data.isupper():
            raise ValidationError("must be capital")


class SearchStatus(Form):
    searchStatus = StringField('Search Status', [validators.DataRequired()])



