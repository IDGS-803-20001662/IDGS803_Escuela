from flask import Blueprint

from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from models import db 
from models import Alumnos # mapeo de la tabla alumnos

alumnos = Blueprint('alumnos', __name__)

@alumnos.route('/getalumn', methods = ['GET', 'POST'])
def getalumn():
    create_form = forms.AlumForm(request.form)
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form = create_form, alumnos = alumnos)

@alumnos.route('/alumn', methods = ['GET', 'POST'])
def alumn():
    create_form = forms.AlumForm(request.form)
    if request.method == 'POST':
        #objeto que permite pasarselo al db para guardarlo en la base de datos
        alum = Alumnos(matricula = create_form.matricula.data,
                       nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       correo = create_form.correo.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("alumnos.getalumn"))
    
    return render_template('alum.html', form = create_form)

@alumnos.route("/modificar", methods = ['GET', 'POST'])
def modificar():
    create_form = forms.AlumForm(request.form)

    if request.method == 'GET':
        id =  request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alum1.id
        create_form.matricula.data = alum1.matricula
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.correo.data = alum1.correo
    
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.matricula = create_form.matricula.data
        alum.nombre = create_form.nombre.data 
        alum.apellidos = create_form.apellidos.data
        alum.correo = create_form.correo.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("alumnos.getalumn"))
    
    return render_template("modificar.html", form = create_form)

@alumnos.route("/eliminar", methods = ['GET', 'POST'])
def eliminar():
    create_form = forms.AlumForm(request.form)

    if request.method == 'GET':
        id =  request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alum1.id
        create_form.matricula.data = alum1.matricula
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.correo.data = alum1.correo
    
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.matricula = create_form.matricula.data
        alum.nombre = create_form.nombre.data 
        alum.apellidos = create_form.apellidos.data
        alum.correo = create_form.correo.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("alumnos.getalumn"))
    
    return render_template("eliminar.html", form = create_form)

#__INIT__ RECONOCE LAS CARPETAS COMO MODULOS Y CREA AUTO. EL PAQUETE __PYCHACHE__