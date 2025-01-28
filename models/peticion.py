from odoo import models, fields, api


class usuario(models.Model):
    _name = 'ModuloBibliotecaOdoo.peticion'
    _description = 'ModuloBibliotecaOdoo.usuario'

    usuario = fields.Many2one( comodel_name = "ModuloBibliotecaOdoo.usuario", string = "Usuario", required = True )
    titulo = fields.Char( string = "Titulo del libro", required = True )
    nombre_autor = fields.Char( string = "Nombre autor", required = True )

    
