from odoo import models, fields, api


class Peticion(models.Model):
    _name = 'biblioteca.peticion'
    _description = 'biblioteca.usuario'

    usuario = fields.Many2one( comodel_name = "biblioteca.usuario", string = "Usuario", required = True )
    titulo = fields.Char( string = "Titulo del libro", required = True )
    nombre_autor = fields.Char( string = "Nombre autor", required = True )

    
