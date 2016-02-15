# -*- coding: utf-8 -*-
import requests

class XboxApi:
    # XboxApi key
    api_key = ""

    def __init__(self, api_key):
        """Only requires the XboxApi key"""
        self.api_key = api_key

    def request(self, url):
        headers = {"X-AUTH" : self.api_key}
        res = requests.get(url, headers=headers)
        return res.text
