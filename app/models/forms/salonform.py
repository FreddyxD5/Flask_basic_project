from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField, TimeField
from wtforms.validators import DataRequired
# id, aula, horaEntrada

class SalonForm(FlaskForm):
    aula = StringField('Nombre de aula', validators=[DataRequired(message='Se necesita nombre de aula')])
    horaEntrada = TimeField('Hora de entrada', validators=[DataRequired(message="Ingrese una hora de entrada")])
    horaSalida = TimeField('Hora de salida', validators=[DataRequired(message="Ingrese una hora de Salida")])
