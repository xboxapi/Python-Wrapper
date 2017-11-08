#-*- coding: utf-8 -*-


class Gamer(object):
    ''' Xbox profile wrapper '''

    def __init__(self, gamertag=None, client=None, xuid=None):
        self.client = client
        self.gamertag = gamertag
        self.xuid = xuid if xuid is not None else self.fetch_xuid()
        self.endpoints = ['messages',
                          'conversations',
                          'recent-players',
                          'activity-feed',
                          'latest-xbox360-games',
                          'latest-xboxone-games',
                          'latest-xboxone-apps',
                          'xboxone-gold-lounge',
                          'game-details',
                          'game-details-hex']
        self.endpoints_xuid = ['achievements',
                               'profile',
                               'presence',
                               'gamercard',
                               'activity',
                               'friends',
                               'followers',
                               'game-clips',
                               'game-clips/saved',
                               'game-stats',
                               'screenshots',
                               'xbox360games',
                               'xboxonegames',
                               'game-status']

    def get(self, method=None, term=None):
        ''' Retrieve data from supported endpoints '''
        # Hack to avoid calling api again for xuid retrieval
        if method == 'xuid':
            return self.xuid

        url = self.parse_endpoints(method, term)
        if url is not False:
            return self.client.api_get(url).json()

        url = self.parse_endpoints_secondary(method, term)
        if url is not False:
            return self.client.api_get(url).json()

        return {}

    def parse_endpoints(self, method=None, term=None):
        ''' Constructs a valid endpoint url for api '''
        if method is None:
            return False

        for endpoint in self.endpoints:
            if endpoint != method:
                continue
            url = endpoint
            if term is not None:
                url = url + '/' + term
            return url

        return False

    def parse_endpoints_secondary(self, method=None, term=None):
        ''' Parse secondary endpoints that require xuid in url '''
        for endpoint in self.endpoints_xuid:
            if endpoint != method:
                continue
            url = str(self.xuid) + '/' + endpoint
            if term is not None:
                url = url + '/' + term
            return url

        return False

    def send_message(self, message=None, xuids=None):
        ''' Send a message given a list of gamer xuids '''
        payload = {}
        if message is None:
            raise ValueError('A message is required!')

        if xuids is not None and not hasattr(xuids, 'append'):
            raise TypeError('List was not given!')

        if xuids is None:
            xuids = [self.xuid]

        payload['to'] = xuids
        payload['message'] = message
        return self.client.api_post('messages', payload)

    def post_activity(self, message=None):
        ''' Post directly to your activity feed '''
        payload = {}
        if message is None:
            raise ValueError('A message is required!')
        payload['message'] = message
        return self.client.api_post('acitivity-feed', payload)

    def fetch_xuid(self):
        ''' Fetch gamer xuid from gamertag '''
        return self.client.api_get('xuid/' + self.gamertag).json()
