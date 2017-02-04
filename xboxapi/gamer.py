#-*- coding: utf-8 -*-

class Gamer(object):
  ''' Xbox profile wrapper '''

  def __init__(self, gamertag=None, client=None, xuid=None):
    self.client = client
    self.gamertag = gamertag
    self.xuid = xuid if xuid is not None else self.fetch_xuid()
    self.endpoints = ['profile',
                      'messages',
                      'conversations',
                      'recent-players',
                      'activity-feed',
                      'latest-xbox360-games',
                      'latest-xboxone-games',
                      'latest-xboxone-apps',
                      'xboxone-gold-lounge']
    self.endpoints_xuid = ['presence',
                           'gamercard',
                           'activity',
                           'friends',
                           'followers',
                           'game-clips',
                           'game-clips/saved',
                           'screenshots',
                           'xbox360games',
                           'xboxonegames',
                           'game-status']

  def get(self, method=None, term=None):
    ''' Retrieve data from supported endpoints '''
    for endpoint in self.endpoints:
      if endpoint != method:
        continue
      url = endpoint
      if term is not None:
        url = url + '/' + term
      return self.client.api_get(endpoint).json()

    # Check secondary endpoints that require xuid
    for endpoint in self.endpoints_xuid:
      if endpoint != method:
        continue
      url = str(self.xuid) + '/' + endpoint
      if term is not None:
        url = url + '/' + term
      return self.client.api_get(url).json()

    return {}

  def fetch_xuid(self):
    ''' Fetch gamer xuid from gamertag '''
    return self.client.api_get('xuid/' + self.gamertag).json()
