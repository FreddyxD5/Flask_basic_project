from app.aplication import db
from app.models.alumno_model import Alumno

class Salon(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    aula = db.Column(db.String(20))
    horaEntrada = db.Column(db.Time)
    horaSalida = db.Column(db.Time, nullable=True)
    alumnos = db.relationship('Alumno', backref="salon", lazy="dynamic")

    def __repr__(self):
        return f"{self.id} - {self.aula}"