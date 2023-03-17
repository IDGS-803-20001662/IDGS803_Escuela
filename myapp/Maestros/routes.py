from flask import Blueprint

from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from models import db
from db import get_connection
from models import Maestros

maestros = Blueprint('maestros', __name__)

@maestros.route('/getmaes', methods = ['GET'])
def getmaes():
    create_form = forms.MaestForm(request.form)
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consultar_maestros()')
            maestros = cursor.fetchall()

        for row in maestros:
            print(row)
    
        connection.close()

    except Exception as ex:
        print(ex)
    return render_template('ABCompletoM.html', form = create_form, maestros = maestros)

@maestros.route('/maes', methods = ['GET', 'POST'])
def maes():
    create_form = forms.MaestForm(request.form)
    if request.method == 'POST':
        nombre = create_form.nombre.data,
        apellidos = create_form.apellidos.data,
        correo = create_form.correo.data
        telefono = create_form.telefono.data

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call agregar_maestro(%s,%s,%s,%s)',(nombre, apellidos, correo, telefono))
            connection.commit()
            connection.close()

        except Exception as ex:
            print(ex)

        return redirect(url_for("maestros.getmaes"))
    
    return render_template('maes.html', form = create_form)

@maestros.route("/modificarM", methods = ['GET', 'POST'])
def modificarM():
    create_form = forms.MaestForm(request.form)

    if request.method == 'GET':
        id =  request.args.get('id')
        maestro = ()

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
            # la coma se usa para que lo tome como tupla
                cursor.execute('call consultar_maestro_id(%s)',(id))
                maestro = cursor.fetchone()
                print(maestro)
            
            connection.close()

            create_form.id.data = maestro[0]
            create_form.nombre.data = maestro[1]
            create_form.apellidos.data = maestro[2]
            create_form.correo.data = maestro[3]
            create_form.telefono.data = maestro[4]

        except Exception as ex:
            print(ex)
        
    
    if request.method == 'POST':
        id = create_form.id.data

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
            # la coma se usa para que lo tome como tupla
                cursor.execute('call consultar_maestro_id(%s)',(id,))
                maestro = cursor.fetchone()
                print(maestro)
            
            connection.close()

            maestroO = Maestros(id = maestro[0],
                                nombre = create_form.nombre.data ,
                                apellidos = create_form.apellidos.data,
                                correo = create_form.correo.data,
                                telefono = create_form.telefono.data)

            print(maestroO)

            try:
                connection = get_connection()
                with connection.cursor() as cursor:
                    cursor.execute('call modificar_maestro(%s,%s,%s,%s, %s)',(maestroO.nombre, maestroO.apellidos, maestroO.correo, maestroO.telefono, maestroO.id,))
                connection.commit()
                connection.close()

            except Exception as ex:
                print(ex)

        except Exception as ex:
            print(ex)

        return redirect(url_for("maestros.getmaes"))
    
    return render_template("modificarM.html", form = create_form)

@maestros.route("/eliminarM", methods = ['GET', 'POST'])
def eliminarM():
    create_form = forms.MaestForm(request.form)

    if request.method == 'GET':
        id =  request.args.get('id')
        maestro = ()

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
            # la coma se usa para que lo tome como tupla
                cursor.execute('call consultar_maestro_id(%s)',(id,))
                maestro = cursor.fetchone()
                print(maestro)
            
            connection.close()

        except Exception as ex:
            print(ex)

        create_form.id.data = maestro[0]
        create_form.nombre.data = maestro[1]
        create_form.apellidos.data = maestro[2]
        create_form.correo.data = maestro[3]
        create_form.telefono.data = maestro[4]
    
    if request.method == 'POST':
        id = create_form.id.data

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
            # la coma se usa para que lo tome como tupla
                cursor.execute('call consultar_maestro_id(%s)',(id,))
                resulset = cursor.fetchone()
                print(resulset)
            
            connection.close()

            try:
                connection = get_connection()
                with connection.cursor() as cursor:
                    cursor.execute('call eliminar_maestro(%s)',(id,))
                connection.commit()
                connection.close()

            except Exception as ex:
                print(ex)

        except Exception as ex:
            print(ex)

        return redirect(url_for("maestros.getmaes"))
    
    return render_template("eliminarM.html", form = create_form)