# -*- coding: utf-8 -*-
# © 2018 Rodrigo Colombo Vlaeminch (rodrigo.covl@gmail.com).
{
    "name": "Car sale base",
    "version": "0.1",
    "author": "Rodrigo Colombo Vlaeminch",
    "website": 'https://github.com/rodrig92',
    "category": "Sales",
    "license": "AGPL-3",
    'sequence': 10,
    'summary': "Link between product and fleet",
    "depends": [
        "product",
        "fleet",
    ],
    "data": ['views/product_view.xml',
             'views/fleet_view.xml'],
    'installable': True,
    'images': [],
}