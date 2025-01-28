from odoo import models, fields, api


class autor(models.Model):
    _name = 'biblioteca.autor'
    _inherit = 'biblioteca.persona'
    _description = 'biblioteca.autor'

    genero = fields.Many2one( comodel_name="biblioteca.genero", string = "Genero", required = True )
 

    
