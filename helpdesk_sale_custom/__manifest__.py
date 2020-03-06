{
    'name': 'Sale Help desk custom',
    'version': '13.0.0.0.0',
    'summary': '',
    'description': 'User can create help desk ticket from sale order',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'author': 'Indexa',
    'website': 'https://www.indexa.do',
    'license': '',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'helpdesk_sale',
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/helpdesk_sale_custom_security.xml',
        'views/sale_order_views.xml',
        'views/res_config_settings_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
}