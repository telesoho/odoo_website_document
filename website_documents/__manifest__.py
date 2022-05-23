# -*- coding: utf-8 -*-
{
    "name": "Website Documents",
    "version": "1.0.0",
    "category": "SDL/App",
    "sequence": "1",  # 複数モジュール場合は、表示順
    "summary": "Website Documents",
    "description": """Odoo 15 website document manager
    """,
    "author": "Social Design Lab.",
    "website": "http://sdl.or.jp",
    "license": "LGPL-3",
    "depends": ["website"],
    "data": [
        "views/vue_views.xml",
    ],
    "demo": [],
    "application": True,
    "assets": {
        "website_documents.assets_importmap": [
            "https://cdn.syncfusion.com/ej2/20.1.55/material.css",
            "https://cdn.jsdelivr.net/npm/vue@2.5.16/dist/vue.min.js",
            "https://cdn.syncfusion.com/ej2/20.1.55/ej2-vue-es5/dist/ej2-vue.min.js",
        ],
        "website_documents.assets_app": ["website_documents/static/src/js/vue/app.js"],
    },
    "installable": True,
    "auto_install": False,
    "application": True,
    "live_test_url": "https://www.youtube.com/watch?v=6gB-05E5kNg",
    # 広告
    "images": ["static/description/banner.gif"],
}
