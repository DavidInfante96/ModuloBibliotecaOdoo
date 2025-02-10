from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libros'

    name = fields.Char(string = "titulo", required= True )
    isbn = fields.Char(string="Isbn", required= True)
    genero = fields.Many2many(comodel_name="biblioteca.genero", string="Genero", required=True)
    autor = fields.Many2one(comodel_name="biblioteca.autor", string="Autor", required= True)
    imagen_image = fields.Image(string="Imagen Image")
    cantidad = fields.Integer( name = "Ejemplares", required = True )


    # @api.depends('field1')
    # def _compute_field2(self):
    #     for record in self:
    #         record.field2 =  True if record.field1 else False

    @api.constrains( "cantidad" )
    def _check_cantidad(self):
        for propertie in self:
            if propertie.cantidad < 0:
                raise ValidationError( "La cantidad tiene que ser positiva." )
            
    _sql_constraints = [
        ('isbn', 'UNIQUE(isbn)', 'El número de ISBN ya existe.'),
        ('name', 'UNIQUE(name)', 'El titulo del libro ya existe.')
    ]
    
    
    
    