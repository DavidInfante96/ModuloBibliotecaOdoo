from odoo import models, fields, api


class autor(models.Model):
    _name = 'ModuloBibliotecaOdoo.autor'
    _inherit = 'ModuloBibliotecaOdoo.persona'
    _description = 'ModuloBibliotecaOdoo.autor'

    genero = fields.Many2one( comodel_name="ModuloBibliotecaOdoo.genero" string = "Genero", required = True )
 

    
