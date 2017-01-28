#-*- coding: utf-8 -*-

class User(object):
  ''' Xbox profile information '''

  user_key = None
  date_of_birth = None
  email = None
  name = None
  gamer_tag = None
  xuid = None

  def __init__(self, user_json={}, prefetch=False):
    ''' Parse json response into user struct '''
    self.user_key = user_json['userKey']
    self.date_of_birth = user_json['dateOfBirth']
    self.email = user_json['email']
    self.name = "{} {}".format(user_json['firstName'], user_json['lastName'])
    self.gamer_tag = user_json['gamerTag']
    self.xuid = user_json['userXuid']

    # Prefetch will fetch data from api endpoints (this can be slower)