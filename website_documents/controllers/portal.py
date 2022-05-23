# -*- coding: utf-8 -*-
from collections import OrderedDict

from odoo import http
from odoo.http import request
from odoo.tools.translate import _


import logging

from odoo.addons.portal.controllers import portal


_log = logging.getLogger(__name__)


class WebsiteDocumentsPortal(portal.CustomerPortal):
    @http.route(
        ["/vue/documents"],
        type="http",
        auth="user",
        website=True,
        methods=["POST", "GET"],
        csrf=False,
    )
    def vue_documents(
        self,
        **kw,
    ):
        return request.render("website_documents.portal_vue_documents")

    @http.route(
        ["/fapi/GetImage"],
        type="json",
        auth="user",
        methods=["GET"],
    )
    def fapi_get_image(
        self,
        **kw,
    ):
        return request.render("website_documents.portal_vue_documents")

    @http.route(
        ["/fapi/Upload"],
        type="json",
        auth="user",
        methods=["POST"],
    )
    def fapi_upload(
        self,
        **kw,
    ):
        return request.render("website_documents.portal_vue_documents")

    @http.route(
        ["/fapi/Download"],
        type="json",
        auth="user",
        methods=["POST"],
    )
    def fapi_download(
        self,
        **kw,
    ):
        return request.render("website_documents.portal_vue_documents")

    @http.route(
        ["/fapi/"],
        type="json",
        auth="user",
        methods=["POST"],
    )
    def fapi(
        self,
        **kw,
    ):
        return request.render("website_documents.portal_vue_documents")
