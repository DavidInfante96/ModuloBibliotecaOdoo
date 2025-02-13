from odoo import models, fields, api


class autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'biblioteca.autor'

    name = fields.Char( string = "Nombre completo", required = True )
    genero = fields.Many2one( comodel_name="biblioteca.genero", string = "Genero", required = True )

    genero_html = fields.Html(string="Género", compute="_compute_genero_html", sanitize=False)

    @api.depends('genero')
    def _compute_genero_html(self):
        for record in self:
            if record.genero:
                color = record.genero.color or "#000000"  # Usa el color hexadecimal del campo, o negro por defecto
                record.genero_html = f'<span style="background-color: {color}; color: white; padding: 5px; border-radius: 5px; margin-right: 5px;">{record.genero.name}</span>'
            else:
                record.genero_html = ""