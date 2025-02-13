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

    genero_html = fields.Html(string="Género", compute="_compute_genero_html", sanitize=False)

    @api.depends('genero')
    def _compute_genero_html(self):
        for record in self:
            tags = []
            for genero in record.genero:
                color = genero.color or "#000000"  # Usa el color hexadecimal del campo, o negro por defecto
                tags.append(f'<span style="background-color: {color}; color: white; padding: 5px; border-radius: 5px; margin-right: 5px;">{genero.name}</span>')
            record.genero_html = " ".join(tags)





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
    
    
    
    