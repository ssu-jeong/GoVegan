from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class ProductForm(FlaskForm):
     product_name = StringField("상품명", validators=[DataRequired()])