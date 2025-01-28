from odoo import models, fields

class Libro(models.Model):
    _name = 'ModuloBibliotecaOdoo.libro'
    _description = 'Libro'

    #id = fields.Char(string = "Id", required= True)
    nombre = fields.Char(string = "titulo", required= True )
    isbn = fields.Char(string="Isbn", required= True)
   
    
    
    
    