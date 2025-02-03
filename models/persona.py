from odoo import models, fields, api


class persona(models.AbstractModel):
    _name = 'biblioteca.persona'
    _description = 'biblioteca.persona'


    name = fields.Char( String="Nombre", required=True )
    apellidos = fields.Char( String="Apellidos", required=True )
    dni = fields.Char( string="DNI" )

    
