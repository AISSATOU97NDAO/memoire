# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Immosenegal',
    'version' : '1.0',
    'summary': 'Immosenegal',
    'description': """Immosenegal""",
    'category': 'other',
    'website': 'https://www.immosenegal.com',
    'depends': ['base', 'sale_renting', 'website_sale_renting'],
    'data': [
        'views/templates.xml',
        'views/product_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.report_assets_pdf': [
        ],
    },
    'license': 'LGPL-3',
}
