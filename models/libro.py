from odoo import models, fields

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libros'

    #id = fields.Char(string = "Id", required= True)
    titulo = fields.Char(string = "titulo", required= True )
    isbn = fields.Char(string="Isbn", required= True)
    genero = fields.Many2many(comodel_name="biblioteca.genero", string="Genero", required=True)
    autor = fields.Many2one(comodel_name="biblioteca.autor", string="Autor", required= True)
    
    
    
    