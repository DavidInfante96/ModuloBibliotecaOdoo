from odoo import models, fields, api


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

    
