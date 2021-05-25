# -*- coding: utf-8 -*-
import functools

from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application, RequestHandler

import tornado_cors as cors


passed_by_custom_wrapper = False


def custom_wrapper(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        return result
    global passed_by_custom_wrapper
    passed_by_custom_wrapper = id(wrapper)
    return wrapper


class CorsTestCase(AsyncHTTPTestCase):

    def test_should_return_headers_with_default_values_in_options_request(self):
        response = self.fetch('/default', method='OPTIONS')
        headers = response.headers

        self.assertNotIn('Access-Control-Allow-Origin', headers)
        self.assertNotIn('Access-Control-Allow-Headers', headers)
        self.assertNotIn('Access-Control-Allow-Credentials', headers)
        self.assertNotIn('Access-Control-Expose-Headers', headers)
        self.assertEqual(headers['Access-Control-Allow-Methods'], 'POST, DELETE, PUT, OPTIONS')
        self.assertEqual(headers['Access-Control-Max-Age'], '86400')

    def test_should_return_headers_with_custom_values_in_options_request(self):
        response = self.fetch('/custom', method='OPTIONS')
        headers = response.headers
        self.assertEqual(headers['Access-Control-Allow-Origin'], '*')
        self.assertEqual(headers['Access-Control-Allow-Headers'], 'Content-Type')
        self.assertEqual(headers['Access-Control-Allow-Methods'], 'POST')
        self.assertEqual(headers['Access-Control-Allow-Credentials'], 'true')
        self.assertEqual(headers['Access-Control-Expose-Headers'], 'Location')
        self.assertNotIn('Access-Control-Max-Age', headers)

    def test_should_return_headers_for_requests_other_than_options(self):
        response = self.fetch('/custom', method='POST', body='')
        headers = response.headers
        self.assertEqual(headers['Access-Control-Allow-Origin'], '*')
        self.assertEqual(headers['Access-Control-Expose-Headers'], 'Location')

    def test_should_support_custom_methods(self):
        response = self.fetch('/custom_method', method='OPTIONS')
        headers = response.headers
        self.assertEqual(headers["Access-Control-Allow-Methods"], 'OPTIONS, NEW_METHOD')

    def get_app(self):
        return Application([
            (r'/default', DefaultValuesHandler),
            (r'/custom', CustomValuesHandler),
            (r'/custom_method', CustomMethodValuesHandler)
        ])


class DefaultValuesHandler(cors.CorsMixin, RequestHandler):

    async def post(self):
        self.finish()

    async def put(self):
        self.finish()

    async def delete(self):
        self.finish()


class CustomValuesHandler(cors.CorsMixin, RequestHandler):

    CORS_ORIGIN = '*'
    CORS_HEADERS = 'Content-Type'
    CORS_METHODS = 'POST'
    CORS_CREDENTIALS = True
    CORS_MAX_AGE = None
    CORS_EXPOSE_HEADERS = 'Location'

    async def post(self):
        self.finish()

    async def put(self):
        self.finish()

    async def delete(self):
        self.finish()


class CustomMethodValuesHandler(cors.CorsMixin, RequestHandler):

    SUPPORTED_METHODS = list(CustomValuesHandler.SUPPORTED_METHODS) + ["NEW_METHOD"]

    async def new_method(self):
        self.finish()
