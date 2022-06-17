# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Practise Application""",

    'description': """
        App for training and experimentation
    """,

    'author': "Mahbubur Rahman",
    'website': "https://mahbubnotes.com",

    'category': 'Services/Library',
    'version': '15.0.1.0.0',
    "license": "AGPL-3",
    "application": True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/templates.xml',
        'views/library_menu.xml',
        'views/book_list_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
