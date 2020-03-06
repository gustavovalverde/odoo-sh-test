{
    'name': 'CRM Help desk custom',
    'version': '13.0.0.0.0',
    'summary': '',
    'description': 'User can create help desk ticket from crm lead',
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
        'crm_helpdesk',
        'helpdesk_sale',
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/crm_helpdesk_custom_security.xml',
        'views/crm_lead_views.xml',
        'views/helpdesk_ticket_views.xml',
        'views/res_config_settings_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
}