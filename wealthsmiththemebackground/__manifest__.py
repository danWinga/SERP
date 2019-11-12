# -*- coding: utf-8 -*-
# Copyright 2016, 2017 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "wealthsmiththemebackground",
    "summary": "SERP  backend theme",
    "version": "11.0.1.0.4",
    "category": "Themes/Backend",
    "website": "http://walthsmith.co.ke",
	"description": """
		Backend theme for SERP 11.0 community edition.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "Dan winga, Khan ",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web_responsive',
    ],
    "data": [
        'views/assets.xml',
        'views/res_company_view.xml',
        'views/users.xml',
        'views/sidebar.xml',
        'views/web.xml',
    ],
}

