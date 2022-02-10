from wtforms import Form, TextAreaField, StringField,RadioField, SelectField, validators, ValidationError, EmailField

class RewardForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    phone_no = StringField('Mobile number:', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    reward_type = RadioField('Rewards Type Redemptions', choices=[('200p', '200 points - $100 vouchers'), ('500p', '500 points - $400 Voucher'), ('700p', '700 points- $600 Voucher')], default='200p')
    remarks = TextAreaField('Remarks', [validators.Optional()])

    def validate_phone_no(form,phone_no):
        if not phone_no.data.isdigit():
            raise ValidationError("Mobile Number must be all digits")
        if len(phone_no.data)!= 8:
            raise ValidationError("Mobile Number must be 8 digits")

class PackageFormA(Form):
    package_type = SelectField('Packages', choices=[('', 'Select'),('Package A', 'Package A')], default='')
    brand = SelectField('Brands', [validators.DataRequired()], choices=[('', 'Select'),('STAR Living', 'STAR Living'), ('Penta', 'Penta')], default='')
    service = SelectField('Installations', choices=[('', 'Select'),('Free Electrical Wiring Services and Lighting Services', 'Free Electrical Wiring Services and Lighting Services')], default='')
    installation = SelectField('Installations', choices=[('', 'Select'),('Free Installation', 'Free Installation')], default='')
    product1 = SelectField('First Product', [validators.DataRequired()], choices=[('', 'Select'),('Pendant Lamp', 'Pendant Lamp'),('Chandelier', 'Chandelier'),('Fairy Lights', 'Fairy Lights'),('TL', 'Track Lights')], default='')
    product2 = SelectField('Second Product', [validators.DataRequired()], choices=[('', 'Select'),('Pendant Lights', 'Pendant Lamp'),('Chandelier', 'Chandelier'),('Fairy Lights', 'Fairy Lights'),('Track Lights', 'Track Lights')], default='')
    product3 = SelectField('Third Product', [validators.DataRequired()], choices=[('', 'Select'),('Pendant Lights', 'Pendant Lamp'),('Chandelier', 'Chandelier'),('Fairy Lights', 'Fairy Lights'),('Track Lights', 'Track Lights')], default='')
    design = SelectField('Floor Design', [validators.DataRequired()], choices=[('', 'Select'), ('Ceramic Tiles Design', 'Ceramic Tiles Design'), ('Vinyl Floor Design', 'Vinyl Floor Design'), ('Marble Floor Design', 'Marble Floor Design')], default='')
    cost = SelectField('Price', [validators.DataRequired()], choices=[('', 'Select'), ('$3500', '$3500')], default='')

class PackageFormB(Form):
    package_type = SelectField('Packages', choices=[('', 'Select'),('Package B', 'Package B')], default='')
    brand = SelectField('Brands', [validators.DataRequired()], choices=[('', 'Select'),('Nippon Paint', 'Nippon Paint'), ('Dulux Paints', 'Dulux Paints')], default='')
    service = SelectField('Installations', choices=[('', 'Select'),('2 Free Wallpaper Design, Painting and Wallpaper Services', '2 Free Wallpaper Design, Painting and Wallpaper Services')], default='')
    installation = SelectField('Installations', choices=[('', 'Select'),('Free Installations', 'Free Installations')], default='')
    product1 = SelectField('First Colour',[validators.DataRequired()], choices=[('', 'Select'),('Crimson Red', 'Crimson Red'), ('Red', 'Red'),('Light Red', 'Light Red'),('Sky Blue', 'Sky Blue'),('Blue', 'Blue'),('Dark Blue', 'Dark Blue'),('Cyan', 'Cyan'),('Mint Green', 'Mint Green'),('Orange', 'Orange'),('White', 'White'),('G', 'Grey'),('Light Pink', 'Light Pink'),('Light Purple', 'Light Purple')],default='')
    product2 = SelectField('Second Colour', [validators.DataRequired()], choices=[('', 'Select'),('Crimson Red', 'Crimson Red'), ('Red', 'Red'),('Light Red', 'Light Red'),('Sky Blue', 'Sky Blue'),('Blue', 'Blue'),('Dark Blue', 'Dark Blue'),('Cyan', 'Cyan'),('Mint Green', 'Mint Green'),('Orange', 'Orange'),('White', 'White'),('G', 'Grey'),('Light Pink', 'Light Pink'),('Light Purple', 'Light Purple')], default='')
    product3 = SelectField('Third Colour', [validators.DataRequired()],choices=[('', 'Select'),('Crimson Red', 'Crimson Red'), ('Red', 'Red'),('Light Red', 'Light Red'),('Sky Blue', 'Sky Blue'),('Blue', 'Blue'),('Dark Blue', 'Dark Blue'),('Cyan', 'Cyan'),('Mint Green', 'Mint Green'),('Orange', 'Orange'),('White', 'White'),('G', 'Grey'),('Light Pink', 'Light Pink'),('Light Purple', 'Light Purple')], default='')
    design = SelectField('Floor Design', [validators.DataRequired()], choices=[('', 'Select'), ('Ceramic Tiles Design', 'Ceramic Tiles Design'), ('Vinyl Floor Design', 'Vinyl Floor Design'), ('Marble Floor Design', 'Marble Floor Design')], default='')
    cost = SelectField('Price', [validators.DataRequired()], choices=[('', 'Select'), ('$2400', '$2400')], default='')

class PackageFormC(Form):
    package_type = SelectField('Packages', choices=[('', 'Select'),('Package C', 'Package C')], default='')
    brand = SelectField('Brands', [validators.DataRequired()], choices=[('', 'Select'),('STAR Living', 'STAR Living'), ('Penta', 'Penta')], default='')
    service = SelectField('Installations', choices=[('', 'Select'),('Free Electrical Wiring Services and Wallpaper Services', 'Free Electrical Wiring Services and Wallpaper Services')], default='A')
    installation = SelectField('Installations', choices=[('', 'Select'),('Free Installation', 'Free Installation')], default='')
    product1 = SelectField('First Product', [validators.DataRequired()], choices=[('', 'Select'),('Pendant Lights', 'Pendant Lamp'),('Chandelier', 'Chandelier'),('Fairy Lights', 'Fairy Lights'),('Track Lights', 'Track Lights')], default='')
    product2 = SelectField('Second Product', [validators.DataRequired()], choices=[('', 'Select'),('Pendant Lights', 'Pendant Lamp'),('Chandelier', 'Chandelier'),('Fairy Lights', 'Fairy Lights'),('Track Lights', 'Track Lights')], default='')
    product3 = SelectField('Third Product', [validators.DataRequired()], choices=[('', 'Select'),('Pendant Lights', 'Pendant Lamp'),('Chandelier', 'Chandelier'),('Fairy Lights', 'Fairy Lights'),('Track Lights', 'Track Lights')], default='')
    design = SelectField('Wallpaper Design', [validators.DataRequired()], choices=[('', 'Select'), ('Marble Design', 'Marble Design'), ('Tropical Design', 'Tropical Design'), ('Brick and Stone Design', 'Brick and Stone Design'),('Tiles Design', 'Tiles Design'),('Metallic Design', 'Metallic Design'),('Geometric Design', 'Geometric Design')], default='')
    cost = SelectField('Price', [validators.DataRequired()], choices=[('', 'Select'), ('$1500', '$1500')], default='')

class PackageFormD(Form):
    package_type = SelectField('Packages', choices=[('', 'Select'),('Package D', 'Package D')], default='')
    brand = SelectField('Brands', [validators.DataRequired()],choices=[('', 'Select'),('Nippon Paint', 'Nippon Paint'), ('Dulux Paints', 'Dulux Paints'),], default='')
    service = SelectField('Installations', choices=[('', 'Select'),('Free Painting and Wallpaper Services', 'Free Painting and Wallpaper Services')], default='')
    installation = SelectField('Installations', choices=[('', 'Select'),('Free Installation', 'Free Installation')], default='A')
    product1 = SelectField('First Colour',[validators.DataRequired()], choices=[('', 'Select'),('Crimson Red', 'Crimson Red'), ('Red', 'Red'),('Light Red', 'Light Red'),('Sky Blue', 'Sky Blue'),('Blue', 'Blue'),('Dark Blue', 'Dark Blue'),('Cyan', 'Cyan'),('Mint Green', 'Mint Green'),('Orange', 'Orange'),('White', 'White'),('Grey', 'Grey'),('Light Pink', 'Light Pink'),('Light Purple', 'Light Purple')],default='')
    product2 = SelectField('Second Colour', [validators.DataRequired()], choices=[('', 'Select'),('Crimson Red', 'Crimson Red'), ('Red', 'Red'),('Light Red', 'Light Red'),('Sky Blue', 'Sky Blue'),('Blue', 'Blue'),('Dark Blue', 'Dark Blue'),('Cyan', 'Cyan'),('Mint Green', 'Mint Green'),('Orange', 'Orange'),('White', 'White'),('Grey', 'Grey'),('Light Pink', 'Light Pink'),('Light Purple', 'Light Purple')], default='')
    product3 = SelectField('Third Colour', [validators.DataRequired()],choices=[('', 'Select'),('Crimson Red', 'Crimson Red'), ('Red', 'Red'),('Light Red', 'Light Red'),('Sky Blue', 'Sky Blue'),('Blue', 'Blue'),('Dark Blue', 'Dark Blue'),('Cyan', 'Cyan'),('Mint Green', 'Mint Green'),('Orange', 'Orange'),('White', 'White'),('Grey', 'Grey'),('Light Pink', 'Light Pink'),('Light Purple', 'Light Purple')], default='')
    design = SelectField('Wallpaper Design', [validators.DataRequired()], choices=[('', 'Select'), ('Marble Design', 'Marble Design'), ('Tropical Design', 'Tropical Design'), ('Brick and Stone Design', 'Brick and Stone Design'),('Tiles Design', 'Tiles Design'),('Metallic Design', 'Metallic Design'),('Geometric Design', 'Geometric Design')], default='')
    cost = SelectField('Price', [validators.DataRequired()], choices=[('', 'Select'), ('$1000', '$1000')], default='')

class SearchReward(Form):
    searchUser = StringField('Search Name', [validators.DataRequired()])

    def validate_searchuser(form, searchUser):
        if not searchUser.data.isalpha():
            raise ValidationError("must be letters only")
        if not searchUser.data.isupper():
            raise ValidationError("must be capital")
