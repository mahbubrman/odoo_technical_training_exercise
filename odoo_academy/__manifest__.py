# -*- coding: utf-8 -*-
{
    'name': "odoo_academy",

    'summary': """Technical Essential Training""",

    'description': """This module is developed""",

    'author': "Mahbubur Rahman",
    'website': "https://mahbubnotes.com",
    'category': 'Services/Training',
    'version': '15.0.1.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'website'],

    # always loaded
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_templates.xml',
        'views/academy_web_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ]

}
