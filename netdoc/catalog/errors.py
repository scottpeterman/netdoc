#!/usr/bin/env python3
""" Database structure """
__author__ = 'Andrea Dainese <andrea.dainese@gmail.com>'
__copyright__ = 'Andrea Dainese <andrea.dainese@gmail.com>'
__license__ = 'https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode'
__revision__ = '20170430'

import logging
from flask_restful import Api

class MyApi(Api):
    def handle_error(self, err):
        try:
            code = getattr(err, 'code', 500)  # Gets code or set default
            message = getattr(err, 'name', 'Internal Server Error')  # Gets nane or set default
            description = getattr(err, 'description', 'The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.')  # Gets description or set defailt
        except:
            code = 500
            message = 'Internal Server Error'
            description = err
            pass

        response = {
            'status': 'fail',
            'code': code,
            'message': message,
            'description': err
        }

        return self.make_response(response, code)
