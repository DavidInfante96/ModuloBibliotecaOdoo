from odoo import models, fields, api
import re

class usuario(models.Model):
    _name = 'biblioteca.usuario'
    _description = 'biblioteca.usuario'


    name = fields.Char( string="Nombre", required=True )
    apellidos = fields.Char( string="Apellidos", required=True )
    dni = fields.Char( string="DNI" )
    direccion = fields.Char( string = "Dirección", required = True )
    telefono = fields.Char( string = "Teléfono", required = True )
    email = fields.Char( string = "Correo", required = True )
    pais = fields.Char( string = "Pais", required = True )
    es_profesor = fields.Boolean( string = "Es profesor", required = True )

    @api.constrains( "dni" )
    def _comprobar_dni(self):
        """ Validar que el DNI sea correcto según el cálculo del módulo 23. """
        letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        dni_regex = r'^\d{8}[A-Z]$'

        for record in self:
            if not record.dni:
                continue

            if not re.match(dni_regex, record.dni):
                raise ValidationError("El DNI debe tener 8 números seguidos de una letra mayúscula.")

            numero = int(record.dni[:-1])
            letra = record.dni[-1]

            if letra != letras_dni[numero % 23]:
                raise ValidationError("El DNI no es válido, la letra no coincide.")
