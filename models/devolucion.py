from odoo import models, fields

class Devolucion(models.Model):
    _name = 'biblioteca.devolucion'
    _description = 'Devoluciones'

    fecha_devolucion = fields.Date(string = "Fecha devolucion", required= True )
    libro = fields.Many2many(comodel_name="biblioteca.libro", string="Libro a devolver", required= True)
    persona = fields.Many2one(comodel_name="biblioteca.usuario", string="Usuario", required=True)
    profesor = fields.Many2one(comodel_name="biblioteca.usuario", string="Encargado")
    
    
    
    