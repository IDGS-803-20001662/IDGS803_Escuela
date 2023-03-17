from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators # agregar validacion

# (FORM) -> Heredar de Forms los metodos y atributos
class AlumForm(Form):
    id = IntegerField('Id')
    matricula = StringField('Matricula')
    nombre = StringField('Nombre(s)')
    apellidos = StringField('Apellidos')
    correo = EmailField('Correo electrónico')

class MaestForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre(s)')
    apellidos = StringField('Apellidos')
    correo = EmailField('Correo electrónico')
    telefono = StringField('Teléfono')
    