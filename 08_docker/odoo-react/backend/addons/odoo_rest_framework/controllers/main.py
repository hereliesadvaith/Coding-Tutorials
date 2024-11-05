# -*- coding: utf-8 -*-
from odoo.http import Controller, request, route
import json
import logging

_logger = logging.getLogger(__name__)


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
        auth = request.httprequest.headers.get('Authorization')
        _logger.info(f'Response auth {auth}')
        data = json.dumps({
            'id': 201
        })
        return request.make_response(data, status=200)
