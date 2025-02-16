# -*- coding: utf-8 -*-
{
    'name': "biblioteca", 

    'summary': """
        Permite gestionar una biblioteca""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listingaalvaro a
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'web'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/inicio.xml',
        'views/prestamo.xml',
        'views/devolucion.xml',
        'views/autor.xml',
        'views/usuario.xml',
        'views/qweb_templates.xml',
        'views/libro.xml',
        'views/observacionPeticion.xml',
        'views/peticion.xml',
        'views/genero.xml',
        #'data/genero.csv',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'biblioteca/static/src/css/tarjeta.css',
        ],
    },

}
