from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    directorName = StringField('Director', validators=[DataRequired(), Length(min=1, max=70)])
    submit = SubmitField('Søk')

