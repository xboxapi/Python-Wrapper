# -*- coding: utf-8 -*-
import requests
import json

class XboxApi:
    # XboxApi key
    api_key = ""

    def __init__(self, api_key):
        """Only requires the XboxApi key"""
        self.api_key = api_key

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

    def get_xuid_by_gamertag(self, gamertag):
        """Return XUID by gamertag"""
        res = self.request("https://xboxapi.com/v2/xuid/{}".format(gamertag))
        return res.json()

    def get_gamertag_by_xuid(self, xuid):
        """Return gamertag by XUID"""
        res = self.request("https://xboxapi.com/v2/gamertag/{}".format(xuid))
        return res.json()

    def get_user_profile(self, xuid):
        """Return profile by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/profile".format(xuid))
        return res.json()

    def get_user_gamercard(self, xuid):
        """Return gamercard by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/gamercard".format(xuid))
        return res.json()

    def get_user_presence(self, xuid):
        """Return current presence information by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/presence".format(xuid))
        return res.json()

    def get_user_activity(self, xuid):
        """Return current activity information by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/activity".format(xuid))
        return res.json()

    def get_user_activity_recent(self, xuid):
        """Return recent activity information by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/activity/recent".format(xuid))
        return res.json()

    def get_user_friends(self, xuid):
        """Return friends by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/friends".format(xuid))
        return res.json()

    def get_user_followers(self, xuid):
        """Return followers by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/followers".format(xuid))
        return res.json()

    def get_recent_players(self):
        """Return recent players by XUID"""
        res = self.request("https://xboxapi.com/v2/recent-players")
        return res.json()

    def get_user_gameclips(self, xuid):
        """Return game clips by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/game-clips".format(xuid))
        return res.json()

    # continue with #16

    def send_message(self, message, xuids=[]):
        """Send a message to a set of user(s)"""
        payload = {
            "message": message,
            "to": []
        }

        for xuid in xuids:
            payload["to"].append(xuid)

        res = self.send_post("https://xboxapi.com/v2/messages", json.dumps(payload))
        return res.json()

    def send_activity_feed(self, message):
        """Send a post to a activity feed"""
        payload = {
            "message": message
        }

        res = self.send_post("https://xboxapi.com/v2/activity-feed", json.dumps(payload))
        return res.json()

    def request(self, url):
        """Wrapper on the requests.get"""
        headers = {"X-AUTH": self.api_key}
        res = requests.get(url, headers=headers)
        return res

    def send_post(self, url, data):
        """Wrapper on the requests.post"""
        headers = {
            "X-AUTH": self.api_key,
            "Content-Type": "application/json"
        }

        res = requests.post(url, headers=headers, data=data)
        return res
