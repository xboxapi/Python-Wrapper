#-*- coding: utf-8 -*-

import requests
import types
import json

# Local libraries
from .user import User
import xboxapi

REQUEST_TIMEOUT = 5 # seconds

class Client(object):
  api_key = None
  endpoint = "https://xboxapi.com/v2/"

  user = object

  def __init__(self, api_key=None, prefetch=False, debug=True):
    self.api_key = api_key

    if debug:
      import logging
      logging.basicConfig(level=logging.DEBUG)

    res = self._get(self.endpoint + 'profile').json()

    # Fetch user settings
    self.user = User(res)

  def send_message(self, message=None, xuids=[]):
    ''' Send message to list of gamers by xuid '''
    if message is None:
      raise ValueError("You must send a message!")

    payload = {
      "message": message,
      "to": []
    }

    for xuid in xuids:
      payload["to"].append(xuid)

    res = self._post(self.endpoint + "messages", payload)
    return res.json()

  def _get(self, url):
    ''' GET wrapper on requests library '''
    headers = {'X-Auth' : self.api_key,
               'user-agent' : 'Python/XboxApi ' + xboxapi.__version__}
    return requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)

  def _post(self, url, body):
    ''' POST wrapper on requests library '''
    headers = {
        'X-AUTH': self.api_key,
        'Content-Type' : 'application/json'
    }

    return requests.post(url, headers=headers, data=json.dumps(body),
                         timeout=REQUEST_TIMEOUT)

  def calls_remaining(self):
    ''' Check on the limits from server '''
    server_headers = self._get(self.endpoint + 'accountxuid').headers
    limit_headers = {}
    limit_headers['X-RateLimit-Reset'] = server_headers['X-RateLimit-Reset']
    limit_headers['X-RateLimit-Limit'] = server_headers['X-RateLimit-Limit']
    limit_headers['X-RateLimit-Remaining'] = server_headers['X-RateLimit-Remaining']
    return limit_headers
