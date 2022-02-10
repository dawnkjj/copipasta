from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, DateField

class CreateRequestForm(Form):
    type_of_services = RadioField('Type of Services:', [validators.DataRequired()], choices=[('Installation', 'Installation ($200) '),('Painting', 'Painting ($400) '), ('Wall Hacking', 'Wall Hacking ($600) '),('Carpentry', 'Carpentry ($800) ')], default='')
    type_of_installation = RadioField('Type of Installation:', [validators.DataRequired()], choices=[('Full', 'Full ($2000)'),('Partial', 'Partial ($1000)')], default='')
    type_of_items = SelectField('Type of Product: ', [validators.DataRequired()], choices=[('', 'Select'), ('Lighting', 'Lighting'), ('Paint', 'Paint'),('Fan', 'Fan')], default='')
    type_of_brands = SelectField('Brands Available: ', [validators.DataRequired()], choices=[('', 'Select'),('STAR Living', 'STAR Living'), ('Penta', 'Penta')], default='')
    items_available = SelectField('Products Available: ', [validators.DataRequired()],  choices=[('', 'Select'),('Pendant Lamp', 'Pendant Lamp'),('Chandelier', 'Chandelier'),('Fairy Lights', 'Fairy Lights'),('Track Lights', 'Track Lights')], default='')



class UpdateRequestForm(Form):
    type_of_services = RadioField('Type of Services:',[validators.Optional()],choices=[('Installation', 'Installation ($200)'),('Painting', 'Painting'), ('Wall Hacking', 'Wall Hacking'),('Carpentry', 'Carpentry')], default='',render_kw = {'disabled': True})
    type_of_installation = RadioField('Type of Installation:',[validators.Optional()], choices=[('Full', 'Full'),('Partial', 'Partial')], default='',render_kw = {'disabled': True})
    type_of_items = SelectField('Type of Product: ', choices=[('', 'Select'), ('Lighting', 'Lighting'), ('Paint', 'Paint'),('Fan', 'Fan')], default='',render_kw = {'disabled': True})
    type_of_brands = SelectField('Brands Available: ', choices=[('', 'Select'),('STAR Living', 'STAR Living'), ('Penta', 'Penta')], default='',render_kw = {'disabled': True})
    items_available = SelectField('Products Available: ', choices=[('', 'Select'),('Pendant Lamp', 'Pendant Lamp'),('Chandelier', 'Chandelier'),('Fairy Lights', 'Fairy Lights'),('Track Lights', 'Track Lights')], default='',render_kw = {'disabled': True})
    startdate = DateField('Estimate Renovation Start Date ', format='%Y-%m-%d')
    enddate = DateField('Estimate Renovate End Date ', format='%Y-%m-%d')
    remarks = TextAreaField('Remarks',[validators.Optional()])
    workcompletion_status = RadioField('Work Completion Status', choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Delayed', 'Delayed'), ('Completed', 'Completed')], default='')


class SearchProductForm(Form):
    searchProduct = StringField('Search Product', [validators.DataRequired])
