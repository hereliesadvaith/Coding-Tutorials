# -*- coding: utf-8 -*-
from odoo.http import Controller, request, route
import json


class RestFramework(Controller):
    """
    Class for Rest Framework Controller
    """
    @route('/rest/', type='http', auth='none',
           csrf=False, methods=['GET'], cors='*'
           )
    def rest_framework(self, **kw):
        """
        Rest Framework
        """
        data = json.dumps({
            'id': 200
        })
        return request.make_response(data, status=200)
