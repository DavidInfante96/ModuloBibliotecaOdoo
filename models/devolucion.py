from odoo import models, fields

class Devolucion(models.Model):
    _name = 'ModuloBibliotecaOdoo.devoluciones'
    _description = 'Devoluciones'

    #id = fields.Char(string = "Id", required= True)
    fecha_devolucion = fields.Date(string = "Fecha devolucion", required= True )
    libro = fields.Many2one(comodel_name="ModuloBibliotecaOdoo.libro", string="Libro a devolver", required= True)
    persona = fields.Many2many(comodel_name="ModuloBibliotecaOdoo.usuario", string="Usuario", required=True)
    profesor = fields.Many2one(comodel_name="ModuloBibliotecaOdoo.usuario", string="Encargado")
    
    
    
    