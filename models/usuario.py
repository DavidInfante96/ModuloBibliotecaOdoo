from odoo import models, fields, api


class usuario(models.Model):
    _name = 'ModuloBibliotecaOdoo.usuario'
    _inherit = 'ModuloBibliotecaOdoo.persona'
    _description = 'ModuloBibliotecaOdoo.usuario'

    direccion = fields.Char( string = "Dirección", required = True )
    telefono = fields.Char( string = "Teléfono", required = True )
    email = fields.Char( string = "Correo", required = True )
    pais = fields.Char( string = "Pais", required = True )
    es_profesor = fields.Boolean( string = "Es profesor", required = True )

    
