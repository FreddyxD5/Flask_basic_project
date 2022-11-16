from app.aplication import db


class Alumno(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    idAula = db.Column(db.Integer, db.ForeignKey('salon.id'))

    def __repr__(self):
        return f"{self.id} - {self.nombre}"