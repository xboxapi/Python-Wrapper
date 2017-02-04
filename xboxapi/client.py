#-*- coding: utf-8 -*-

import requests
import types
import json

# Local libraries
from .gamer import Gamer

import xboxapi

class Client(object):

  def __init__(self, api_key=None, debug=None, timeout=None, lang=None):

    self.api_key =  api_key
    self.timeout = timeout
    self.endpoint = 'https://xboxapi.com/v2/'
    self.timeout = timeout if timeout is not None else 3 # Seconds
    self.lang = lang
    self.last_method_call = None
    self.continuation_token = None
    self.debug = debug
    self.logger = None

    if debug is not None:
      import logging
      logging.basicConfig(level=logging.DEBUG)
      self.logger = logging.getLogger('xboxapi')

    if self.api_key is None:
      raise ValueError('Api key is missing')

  def gamer(self, gamertag=None):
    ''' return a gamer object '''
    if gamertag is None:
      raise ValueError("No gamertag given!")

    return Gamer(gamertag, self)

  def api_get(self, method):
    if self.debug is not None:
      self.logger.info('Sending (method) -> {}'.format(method))

    ''' GET wrapper on requests library '''
    headers = {'X-Auth' : self.api_key,
               'User-Agent' : 'Python/XboxApi ' + xboxapi.__version__}

    if self.lang is not None:
      headers['Accept-Language'] = self.lang

    url = self.endpoint + method
    # Check for continuation token and the method match the last call
    if method == self.last_method_call and self.continuation_token is not None:
      url = url + '?continuationToken=' + self.continuation_token

    if self.debug is not None:
      self.logger.info('Sending (request) -> {}'.format(url))
      self.logger.info('Headers (request) -> {}'.format(headers))

    res = requests.get(self.endpoint + method, headers=headers, timeout=self.timeout)

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
        'Content-Type' : 'application/json'
    }

    res = requests.post(self.endpoint + method, headers=headers, data=json.dumps(body),
                         timeout=self.timeout)
    return res

  def calls_remaining(self):
    ''' Check on the limits from server '''
    server_headers = self.api_get('accountxuid').headers
    print(server_headers)
    limit_headers = {}
    limit_headers['X-RateLimit-Reset'] = server_headers['X-RateLimit-Reset']
    limit_headers['X-RateLimit-Limit'] = server_headers['X-RateLimit-Limit']
    limit_headers['X-RateLimit-Remaining'] = server_headers['X-RateLimit-Remaining']
    return limit_headers
