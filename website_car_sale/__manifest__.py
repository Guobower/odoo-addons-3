# -*- coding: utf-8 -*-
# © 2018 Rodrigo Colombo Vlaeminch (rodrigo.covl@gmail.com).
{
    "name": "Car sale website",
    "version": "0.1",
    "author": "Rodrigo Colombo Vlaeminch",
    "website": 'https://github.com/rodrig92',
    "category": "Website",
    "license": "AGPL-3",
    'sequence': 20,
    'summary': "Car sales website",
    "depends": ["fleet",
                "product",
                "website_sale",
                "car_sale_amount"],
    "data": ['security/ir.model.access.csv',
             'security/website_fleet.xml',
             'views/templates.xml'],
    'installable': True,
}