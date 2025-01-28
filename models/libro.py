from odoo import models, fields

class Libro(models.Model):
    _name = 'ModuloBibliotecaOdoo.libro'
    _description = 'Libro'

    #id = fields.Char(string = "Id", required= True)
    titulo = fields.Char(string = "titulo", required= True )
    isbn = fields.Char(string="Isbn", required= True)
    genero = fields.Many2many(comodel_name="ModuloBibliotecaOdoo.genero", string="Genero", required=True)
    autor = fields.Many2one(comodel_name="ModuloBibliotecaOdoo.autor", string="Autor", required= True)
    
    
    
    