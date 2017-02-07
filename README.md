# Description #

This is a Python wrapper for the unofficial [Xbox API](https://xboxapi.com)

[![Build Status](https://travis-ci.org/xboxapi/Python-Wrapper.svg?branch=master)](https://travis-ci.org/xboxapi/Python-Wrapper)

# Installation #
For now you will have to install manually, as I didn't upload the initial version to pypi (`pip`).

1. Clone this repo
2. Place the `xboxapi` directory in your project

The only dependency is [requests](https://github.com/kennethreitz/requests) library.

# Usage #

This is a basic example of how to create a client and fetch a gamers profile information from their gamertag.

```python
from xboxapi import Client

client = Client(api_key=<api_key>)
gamer = client.gamer('voidpirate')

profile = gamer.get('profile')
```

`Client` class constructor takes the following optional arguments except `api_key`.

| Argument | Value | Short Description |
|---       |---    |---                |
| api_key        | string  | api token from [Xbox API](https://xboxapi.com)    |
| debug          | boolean | print debug information to stdout                 |
| timeout        | int     | how long until the request times out (seconds)    |
| lang           | string  | country language code (e.g. for German (`de-DE`)) |


`Client` class public methods.

| Method | Value | Optional | Short Description |
|---       |---    |---              |---       |
| `gamer(gamertag=<string>)`        | string  | `xuid=<string>` | gamertag to lookup |
| `calls_remaining()` | n/a | n/a | Return headers about api rate limits |

A note about the gamer method. If you already know the gamers xuid you can use that instead to avoid an additional api call when using only a gamertag.

`Gamer` class public methods, returned from gamer method in `Client`.

| Method | Value | Optional | Short Description |
|---       |---    |---              |---       |
| `get(method=<string>)`        | string  | `term=<string>` | API calls. |
| `send_message(message=<string>, xuids=[])` | string, list | n/a | Send a message to the following xuids |
| `send_activity(message=<string>)` | string | n/a | Update your activity feed with a message |

Pagination is supported in this client and all handled through `get` method. It works by detecting the response header for pagination, any subsequent calls to the same api endpoint will return paged data. If another api call is made to a different endpoint, the pagination token will be cleared and results will not be paged.