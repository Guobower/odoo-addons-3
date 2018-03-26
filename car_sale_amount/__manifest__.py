# -*- coding: utf-8 -*-
# © 2018 Rodrigo Colombo Vlaeminch (rodrigo.covl@gmail.com).
{
    "name": "Car sales",
    "version": "0.1",
    "author": "Rodrigo Colombo Vlaeminch",
    "website": 'https://github.com/rodrig92',
    "category": "Sales",
    "license": "AGPL-3",
    'sequence': 20,
    'summary': "Car sales management",
    "depends": ["fleet",
                "product",
                "car_sale_base"],
    "data": ['views/fleet_view.xml'],
    'installable': True,
}