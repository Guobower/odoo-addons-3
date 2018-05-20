# -*- coding: utf-8 -*-
# © 2018 Rodrigo Colombo Vlaeminch (rodrigo.covl@gmail.com).
{
    'name': 'Cash Control',
    'version': '0.1',
    'author': 'Rodrigo Colombo Vlaeminch',
    'website': 'https://github.com/rodrig92',
    'category': 'Account',
    'license': "AGPL-3",
    'sequence': 20,
    'summary': 'Cash control in a physical box',
    'depends': ['account'],
    'data': ['security/cash_security.xml',
             'security/ir.model.access.csv',
             'views/cash_control_view.xml'],
    'application': False,
    'installable': True,
}
