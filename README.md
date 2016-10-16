# Description #

This is a Python wrapper for the unofficial [Xbox API](https://xboxapi.com)

# Installation

This package supports Python Package Index installation:
```shell
pip install xboxapi
```

# API usage

To make any API request it requires **Xbox LIVE** authentication to get the data using your Xbox account. It means
that you need to log into your account and get API key. Then pass this key to create `XboxApi` instance:
```python
from xboxapi import XboxApi

api = XboxApi(api_key="Your API key")
```
Then you can make Xbox API requests with this object. For example, get API key owner profile info:

```python
profile_info = api.get_profile()  # returns dictionary of objects
print(profile_info)
```
>{
>  u'locale': u'en-US',  # Unicode strings
>  u'midasConsole': None,
>  ...Other fields...
>}


## Requests list

#### `get_profile()` - user profile info
#### `get_xuid()` - user personal xbox uid
#### `get_messages()` - user account messages with full preview
#### `get_conversations()` - user conversations with full preview of the last message sent/recieved
#### `get_xuid_by_gametag(gametag)` - user XUID for a specified Gamertag
#### `get_gametag_by_xuid(xuid)` - Gamertag for a specified XUID
#### `get_user_profile(xuid)` - Profile for a specified XUID
#### `get_user_gamecard(xuid)` - Gamercard information for a specified XUID
#### `get_user_presence(xuid)` - current presence information for a specified XUID
#### `get_user_activity(xuid)` - current activity information for a specified XUID
#### `get_user_activity_recent(xuid)` - recent activity information for a specified XUID
#### `get_user_friends(xuid)` - friends information for a specified XUID
#### `get_user_followers(xuid)` - followers information for a specified XUID
#### `get_recent_players()` - accounts recent players information
#### `get_user_gameclips(xuid)` - game clips for a specified XUID
#### `get_user_saved_gameclips(xuid)` - saved game clips for a specified XUID
#### `get_user_saved_gameclips_by_title(xuid, title_id)` - saved game clips for a specified XUID, and Game (titleId)
#### `get_saved_gameclips(title_id)` - saved game clips for a specified Game (titleId)
#### `get_user_screenshots(xuid)` - screenshots for a specified XUID
#### `get_user_saved_screenshots(xuid, title_id)` - saved screenshots for a specified XUID, and Game (titleId)
#### `get_saved_screenshots(title_id)` - saved screenshots for a specified Game (titleId)
#### `get_user_game_stats(xuid, title_id)` - game stats for a specified XUID, on a specified game. (i.e. Driver Level on Forza etc.)
#### `get_user_xbox360games(xuid)` - Xbox 360 Games List for a specified XUID
#### `get_user_xboxonegames(xuid)` - Xbox One Games List for a specified XUID
#### `get_user_achievements(xuid)` - Xbox Games Achievements for a specified XUID
#### `get_game_info_hex(xuid)` - Xbox Game Information (using the game id in hex format)
#### `get_game_info(product_id)` - Xbox Game Information (using the product id)
#### `get_game_addons(product_id)` - Xbox Game Information (using the product id)
#### `get_game_related(product_id)` - Xbox Game Information (using the product id)
#### `get_latest_xbox360games()` - the latest Xbox 360 Games from the Xbox LIVE marketplace
#### `get_latest_xboxonegames()` - the latest Xbox One Games from the Xbox LIVE marketplace
#### `get_latest_xboxoneapps()` - latest Xbox One Apps from the Xbox LIVE marketplace
#### `get_xboxone_gold()` - the free "Games with Gold", and "Deals with Gold" from the Xbox LIVE marketplace
#### `get_xbox360games()` - Xbox LIVE marketplace for Xbox 360 content.
#### `get_xboxonegames()` - Xbox LIVE marketplace for Xbox One Game content.
#### `get_xboxoneapps()` - Xbox LIVE marketplace for Xbox One App content.
#### `get_user_activity_feed()` - user activity feed.
#### `get_user_titlehub_achievements(xuid)` - achievements list by game with friends who also play. (New TitleHub endpoint)
#### `send_message(message, xuids)` - send message to set of users
#### `send_activity_feed(message)` - send a post to activity feed