{
    "name": "iBees Website",
    "summary": """
        iBees mod for website customizations""",
    "author": "iBees",
    "website": "http://www.ibees.biz",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/
    # addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Website/Website",
    "version": "14.0.0.0.0",
    # any module necessary for this one to work correctly
    "depends": ["website", "portal"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/assets.xml",
        "views/debranding.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "application": True,
}
