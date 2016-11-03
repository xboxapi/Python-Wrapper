#-*- coding: utf-8 -*-

import requests
import json

__version__ = '0.1.2'

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
        res = self.request("https://xboxapi.com/v2/accountxuid")
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

    def get_user_saved_gameclips(self, xuid):
        """Return saved game clips by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/game-clips/saved".format(xuid))
        return res.json()

    def get_user_saved_gameclips_by_title(self, xuid, title_id):
        """Return saved game clips for game by XUID and TitleId"""
        res = self.request("https://xboxapi.com/v2/{}/game-clips/{}".format(xuid, title_id))
        return res.json()

    def get_saved_gameclips(self, title_id):
        """Return saved game clips by TitleId"""
        res = self.request("https://xboxapi.com/v2/game-clips/{}".format(title_id))
        return res.json()

    def get_user_screenshots(self, xuid):
        """Return screenshots by XUID"""
        res = self.request("https://xboxapi.com/v2/{}/screenshots".format(xuid))
        return res.json()

    def get_user_saved_screenshots(self, xuid, title_id):
        """Return saved screenshots for game by XUID and TitleId"""
        res = self.request("https://xboxapi.com/v2/{}/screenshots/{}".format(xuid, title_id))
        return res.json()

    def get_saved_screenshots(self, title_id):
        """Return saved screenshots by TitleId"""
        res = self.request("https://xboxapi.com/v2/screenshots/{}".format(title_id))
        return res.json()

    def get_user_game_stats(self, xuid, title_id):
        """Return user game stats by XUID and TitleId"""
        res = self.request("https://xboxapi.com/v2/{}/game-stats/{}".format(xuid, title_id))
        return res.json()

    def get_user_xbox360games(self, xuid):
        """Return user Xbox 360 games"""
        res = self.request("https://xboxapi.com/v2/{}/xbox360games".format(xuid))
        return res.json()

    def get_user_xboxonegames(self, xuid):
        """Return user Xbox One games"""
        res = self.request("https://xboxapi.com/v2/{}/xboxonegames".format(xuid))
        return res.json()

    def get_user_achievements(self, xuid, title_id):
        """Return user achievements per game"""
        res = self.request("https://xboxapi.com//v2/{}/achievements/{}".format(xuid, title_id))
        return res.json()

    def get_game_info_hex(self, game_id):
        """Return game information (game_id in hex)"""
        res = self.request("https://xboxapi.com/v2/game-details-hex/{}".format(game_id))
        return res.json()

    def get_game_info(self, product_id):
        """Return game information from product_id"""
        res = self.request("https://xboxapi.com/v2/game-details/{}".format(product_id))
        return res.json()

    def get_game_addons(self, product_id):
        """Return game addon information from product_id"""
        res = self.request("https://xboxapi.com/v2/game-details/{}/addons".format(product_id))
        return res.json()

    def get_game_related(self, product_id):
        """Return game related information from product_id"""
        res = self.request("https://xboxapi.com/v2/game-details/{}/related".format(product_id))
        return res.json()

    def get_latest_xbox360games(self):
        """Return latest released Xbox 360 games"""
        res = self.request("https://xboxapi.com/v2/latest-xbox360-games")
        return res.json()

    def get_latest_xboxonegames(self):
        """Return latest released Xbox one games"""
        res = self.request("https://xboxapi.com/v2/latest-xboxone-games")
        return res.json()

    def get_latest_xboxoneapps(self):
        """Return latest released Xbox one apps"""
        res = self.request("https://xboxapi.com/v2/latest-xboxone-apps")
        return res.json()

    def get_xboxone_gold(self):
        """List the free Games with Gold and Deals with Gold"""
        res = self.request("https://xboxapi.com/v2/xboxone-gold-lounge")
        return res.json()

    def get_xbox360games(self):
        """Return Xbox 360 games"""
        res = self.request("https://xboxapi.com/v2/browse-marketplace/xbox360/1?sort=releaseDate")
        return res.json()

    def get_xboxonegames(self):
        """Return Xbox one games"""
        res = self.request("https://xboxapi.com/v2/browse-marketplace/games/1?sort=releaseDate")
        return res.json()

    def get_xboxoneapps(self):
        """Return Xbox one apps"""
        res = self.request("https://xboxapi.com/v2/browse-marketplace/apps/1?sort=releaseDate")
        return res.json()

    def get_user_activity_feed(self):
        """Return user activity feed"""
        res = self.request("https://xboxapi.com/v2/activity-feed")
        return res.json()

    def get_user_titlehub_achievements(self, xuid):
        """Return user Title Hub Achievements"""
        res = self.request("https://xboxapi.com/v2/{}/titlehub-achievement-list".format(xuid))
        return res.json()

    def send_message(self, message, xuids=[]):
        """Send a message to a set of user(s)"""
        payload = {
            "message": message,
            "to": []
        }

        for xuid in xuids:
            payload["to"].append(xuid)

        res = self.send_post("https://xboxapi.com/v2/messages", payload)
        return res.json()

    def send_activity_feed(self, message):
        """Send a post to a activity feed"""
        payload = {
            "message": message
        }

        res = self.send_post("https://xboxapi.com/v2/activity-feed", payload)
        return res.json()

    def request(self, url):
        """Wrapper on the requests.get"""
        headers = {"X-AUTH": self.api_key}
        res = requests.get(url, headers=headers, verify=False)  # Set `verify=False` to avoid SSLException
        return res

    def send_post(self, url, data):
        """Wrapper on the requests.post"""
        headers = {
            "X-AUTH": self.api_key,
            "Content-Type": "application/json"
        }

        res = requests.post(url, headers=headers,
                            data=json.dumps(data), verify=False)  # Set `verify=False` to avoid SSLException
        return res
