#-*- coding: utf-8 -*-

import requests
import logging
import json
import os

# Local libraries
from .gamer import Gamer

import xboxapi

logging.basicConfig()


class Client(object):

    def __init__(self, api_key=None, timeout=None, lang=None):

        self.api_key = api_key
        self.timeout = timeout
        self.endpoint = 'https://xboxapi.com/v2/'
        self.timeout = timeout if timeout is not None else 3  # Seconds
        self.lang = lang
        self.last_method_call = None
        self.continuation_token = None

        # Debug logging can be triggered from environment variable
        # XBOXAPI_DEBUG=1
        self.logger = logging.getLogger('xboxapi')
        log_level = logging.DEBUG if os.getenv('XBOXAPI_DEBUG') else logging.INFO
        self.logger.setLevel(log_level)

        if self.api_key is None:
            raise ValueError('Api key is missing')

    def gamer(self, gamertag=None, xuid=None):
        ''' return a gamer object '''
        if gamertag is None:
            raise ValueError('No gamertag given!')

        return Gamer(gamertag=gamertag, client=self, xuid=xuid)

    def api_get(self, method):
        ''' GET wrapper on requests library '''
        headers = {'X-Auth': self.api_key,
                   'User-Agent': 'Python/XboxApi ' + xboxapi.__version__}

        if self.lang is not None:
            headers['Accept-Language'] = self.lang

        url = self.endpoint + method
        # Check for continuation token and the method match the last call
        if method == self.last_method_call and self.continuation_token is not None:
            url = url + '?continuationToken=' + self.continuation_token

        self.logger.debug('%s %s', 'GET', url)
        self.logger.debug('Headers: %s', headers)

        res = requests.get(self.endpoint + method,
                           headers=headers, timeout=self.timeout)
        self.xboxapi_response_error(res)
        self.logger.debug('Response: %s', res.json())

        # Track method calls and peak for continuation token
        self.last_method_call = method
        self.continuation_token = None
        if 'X-Continuation-Token' in res.headers:
            self.continuation_token = res.headers['X-Continuation-Token']

        return res

    def api_post(self, method, body):
        ''' POST wrapper on requests library '''
        headers = {
            'X-AUTH': self.api_key,
            'Content-Type': 'application/json'
        }

        url = '{}{}'.format(self.endpoint, method)

        self.logger.debug('%s %s', 'POST', url)
        self.logger.debug('Headers: %s', headers)
        self.logger.debug('Body: %s', body)

        res = requests.post(self.endpoint + method, headers=headers, data=json.dumps(body),
                            timeout=self.timeout)
        self.xboxapi_response_error(res)

        self.logger.debug('Response: %s', res.json())

        return res

    def calls_remaining(self):
        ''' Check on the limits from server '''
        server_headers = self.api_get('accountxuid').headers
        limit_headers = {}
        limit_headers['X-RateLimit-Reset'] = server_headers['X-RateLimit-Reset']
        limit_headers['X-RateLimit-Limit'] = server_headers['X-RateLimit-Limit']
        limit_headers['X-RateLimit-Remaining'] = server_headers['X-RateLimit-Remaining']
        return limit_headers

    def xboxapi_response_error(self, response):
        """
        Check for an errors returned from the XboxAPI. Errors from the XboxAPI
        have the following format.

        Example:
        {
            "success": false,
            "error_code": 402,
            "error_message": "Paid subscriber feature only"
        }
        """
        if not response.ok:
            self.logger.error('XboxAPI error: (%s) %s', response.status_code, response.reason)
            return
