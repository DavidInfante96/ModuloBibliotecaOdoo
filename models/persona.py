from odoo import models, fields, api


class persona(models.AbstractModel):
    _name = 'ModuloBibliotecaOdoo.persona'
    _description = 'ModuloBibliotecaOdoo.persona'

    dni = fields.Char( string="DNI" )
    nombre = fields.Char( String="Nombre", required=True )
    apellidos = fields.Char( String="Apellidos", required=True )

    
