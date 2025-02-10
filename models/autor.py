from odoo import models, fields, api


class autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'biblioteca.autor'

    name = fields.Char( string = "Nombre completo", required = True )
    genero = fields.Many2one( comodel_name="biblioteca.genero", string = "Genero", required = True )
 

    
