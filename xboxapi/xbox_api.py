# -*- coding: utf-8 -*-
import requests
import json

class XboxApi:
    # XboxApi key
    api_key = ""

    def __init__(self, api_key):
        """Only requires the XboxApi key"""
        self.api_key = api_key

    def get_user_profile(self, xuid):
        res = self.request("https://xboxapi.com/v2/{}/profile".format(xuid))
        return res.json()

    def get_user_gamercard(self, xuid):
        res = self.request("https://xboxapi.com/v2/{}/gamercard".format(xuid))
        return res.json()
        
    def get_profile(self):
        """Return information for current token profile"""
        res = self.request("https://xboxapi.com/v2/profile")
        return res.json()

    def get_xuid(self):
        """Return your xuid"""
        res = self.request("https://xboxapi.com/v2/accountXuid")
        return res.json()

    def get_messages(self):
        """Return your messages"""
        res = self.request("https://xboxapi.com/v2/messages")
        return res.json()

    def get_conversations(self):
        """Return your messages"""
        res = self.request("https://xboxapi.com/v2/conversations")
        return res.json()

    def send_message(self, message, xuids=[]):
        """Send a message to a set of user(s)"""
        headers = {
                    "X-AUTH" : self.api_key,
                    "Content-Type" : "application/json"
                  }

        payload = {
            "message" : message,
            "to" : []
        }

        for xuid in xuids:
            payload["to"].append(xuid)

        res = requests.post("https://xboxapi.com/v2/messages", headers=headers, data=json.dumps(payload))
        res.json()

    def request(self, url):
        """Wrapper on the requests.get"""
        headers = {"X-AUTH" : self.api_key}
        res = requests.get(url, headers=headers)
        return res
