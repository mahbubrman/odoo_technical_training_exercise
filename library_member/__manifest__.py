{
    "name": "Library Members",
    "license": "AGPL-3",
    "description": "Manage Members borrowing books",
    "depends": ["library_app", "mail"],
    "application": False,
    "data": [
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        "security/library_security.xml",
        "views/book_list_template.xml",
    ]
}
