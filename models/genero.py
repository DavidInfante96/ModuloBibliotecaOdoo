from odoo import models, fields

class Genero(models.Model):
    _name = 'biblioteca.genero'
    _description = 'Genero'

    #id = fields.Char(string = "Id", required= True)
    nombre = fields.Char(string = "titulo", required= True )
    isbn = fields.Char(string="Isbn", required= True)
   
    
    
    
    