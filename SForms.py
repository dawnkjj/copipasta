from wtforms import Form, StringField, TextAreaField, validators, ValidationError, DateField
class CreateStockPaintForm(Form):
    stock_name = StringField('Paint Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    stock_count = StringField('Paint Count', [validators.Length(min=1, max=150), validators.DataRequired()])
    colour = StringField('Colour', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = StringField('Price', [validators.Length(min=1, max=150), validators.DataRequired()])
    date_created = DateField('Date created', format='%Y-%m-%d')
    remarks = TextAreaField('Remarks', [validators.Optional()])

    def validate_stock_count(Form, stock_count):
        if not stock_count.data.isdigit():
            raise ValidationError("Stock must be between 1 to 500!")

    def validate_price(Form, price):
        if not price.data.isdigit():
            raise ValidationError("Price must be a number!")

class CreateStockLightingForm(Form):
    stock_name = StringField('Lighting Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    stock_count = StringField('Lighting Count', [validators.Length(min=1, max=150), validators.DataRequired()])
    colour = StringField('Colour', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = StringField('Price', [validators.Length(min=1, max=150), validators.DataRequired()])
    date_created = DateField('Date created', format='%Y-%m-%d')
    remarks = TextAreaField('Remarks', [validators.Optional()])

    def validate_stock_count(Form, stock_count):
        if not stock_count.data.isdigit():
            raise ValidationError("Stock must be between 1 to 500!")

    def validate_price(Form, price):
        if not price.data.isdigit():
            raise ValidationError("Price must be a number!")

class CreateStockFanForm(Form):
    stock_name = StringField('Fan Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    stock_count = StringField('Fan Count', [validators.Length(min=1, max=150), validators.DataRequired()])
    colour = StringField('Colour', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = StringField('Price', [validators.Length(min=1, max=150), validators.DataRequired()])
    date_created = DateField('Date created', format='%Y-%m-%d')
    remarks = TextAreaField('Remarks', [validators.Optional()])

    def validate_stock_count(Form, stock_count):
        if not stock_count.data.isdigit():
            raise ValidationError("Stock must be between 1 to 500!")

    def validate_price(Form, price):
        if not price.data.isdigit():
            raise ValidationError("Price must be a number!")

class CreateStockTileForm(Form):
    stock_name = StringField('Tile Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    stock_count = StringField('Tile Count', [validators.Length(min=1, max=150), validators.DataRequired()])
    colour = StringField('Colour', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = StringField('Price', [validators.Length(min=1, max=150), validators.DataRequired()])
    date_created = DateField('Date created', format='%Y-%m-%d')
    remarks = TextAreaField('Remarks', [validators.Optional()])

    def validate_stock_count(Form, stock_count):
        if not stock_count.data.isdigit():
            raise ValidationError("Stock must be a number!")

    def validate_price(Form, price):
        if not price.data.isdigit():
            raise ValidationError("Price must be a number!")

class CreateStockOtherForm(Form):
    stock_name = StringField('Other Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    stock_count = StringField('Other Count', [validators.Length(min=1, max=150), validators.DataRequired()])
    colour = StringField('Colour', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = StringField('Price', [validators.Length(min=1, max=150), validators.DataRequired()])
    date_created = DateField('Date created', format='%Y-%m-%d')
    remarks = TextAreaField('Remarks', [validators.Optional()])

    def validate_stock_count(Form, stock_count):
        if not stock_count.data.isdigit():
            raise ValidationError("Stock must be between 1 to 500!")

    def validate_price(Form, price):
        if not price.data.isdigit():
            raise ValidationError("Price must be a number!")

class SearchStockOther(Form):
    searchStockOther = StringField('Search Other Name', [validators.DataRequired()])

class SearchStockFan(Form):
    searchStockFan = StringField('Search Fan Name', [validators.DataRequired()])

class SearchStockLighting(Form):
    searchStockLighting = StringField('Search Lighting Name', [validators.DataRequired()])

class SearchStockPaint(Form):
    searchStockPaint = StringField('Search Paint Name', [validators.DataRequired()])

class SearchStockTile(Form):
    searchStockTile = StringField('Search Tile Name', [validators.DataRequired()])

class SearchStockFanPrice(Form):
    searchStockFan = StringField('Search Fan Price', [validators.DataRequired()])

class SearchStockLightingPrice(Form):
    searchStockLighting = StringField('Search Lighting Price', [validators.DataRequired()])

class SearchStockPaintPrice(Form):
    searchStockPaint = StringField('Search Paint Price', [validators.DataRequired()])

class SearchStockTilePrice(Form):
    searchStockTile = StringField('Search Tile Price', [validators.DataRequired()])

class SearchStockOtherPrice(Form):
    searchStockOther = StringField('Search Other Price', [validators.DataRequired()])
