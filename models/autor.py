from odoo import models, fields, api


class autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'biblioteca.autor'

    name = fields.Char( string = "Nombre completo", required = True )
    genero = fields.Many2many( comodel_name="biblioteca.genero", string = "Genero", required = True )

    genero_html = fields.Html(string="Género", compute="_compute_genero_html", sanitize=False)

    @api.depends('genero')
    def _compute_genero_html(self):
        for record in self:
            if record.genero:
                record.genero_html = "".join([
                    f'<span style="background-color: {genero.color or "#000000"}; color: white; padding: 3px 8px; border-radius: 5px; margin-right: 5px;">{genero.name}</span>'
                    for genero in record.genero
                ])
            else:
                record.genero_html = ""
