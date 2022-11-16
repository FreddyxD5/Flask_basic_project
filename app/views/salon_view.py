from app.aplication import db
from flask import Blueprint, flash, render_template, request, url_for, redirect

from app.models.salon_model import Salon
from app.models.forms.salonform import SalonForm

bp = Blueprint('salon', __name__, url_prefix='/salon')



@bp.route('/')
def index():
    salones = Salon.query.all()
    return render_template('salones/salon_index.html', data = salones)

@bp.route('/crear', methods=('GET', 'POST'))
def crear_salonView():
    form = SalonForm()
    if request.method == 'POST':
        salon = Salon(aula=form.aula.data, horaEntrada=form.horaEntrada.data, horaSalida=form.horaSalida.data)
        db.session.add(salon)
        db.session.commit()
        return redirect(url_for('salon.index'))
    return render_template('salon.html', form= form)

@bp.route('/<int:id>/eliminar', methods=('GET','POST',))
def eliminar_salon(id):
    salon_id = id
    salon = Salon.query.filter_by(id=salon_id).first()
    if salon:
        db.session.delete(salon)
        db.session.commit()
    else:
        return "No se ha encontrado una coincidencia"
        # db.session.delete(salon)
    return "salon Eliminado correctamente"


@bp.route('/<int:id>/update', methods=('GET','POST','UPDATE'))
def editar_salon(id):
    form = SalonForm

