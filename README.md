Tornado CORS [![ustudio](https://circleci.com/gh/ustudio/tornado-cors.svg?style=svg)](https://app.circleci.com/pipelines/github/ustudio/tornado-cors)

============

Note: this is a fork of https://github.com/globocom/tornado-cors,
which has been archived.

The primary addition is support for Tornado 6 and newer versions of
Python 3.

Makes it easier to add CORS support to tornado apps.

About Cross-Origin Resource Sharing (CORS)
------------------------------------------

- http://en.wikipedia.org/wiki/Cross-origin_resource_sharing
- http://www.w3.org/TR/cors/


Installing
----------

```
pip install ustudio-tornado-cors
```

Using
-----

```
from tornado_cors import CorsMixin


class MyHandler(CorsMixin, RequestHandler):

    # Value for the Access-Control-Allow-Origin header.
    # Default: None (no header).
    CORS_ORIGIN = '*'

    # Value for the Access-Control-Allow-Headers header.
    # Default: None (no header).
    CORS_HEADERS = 'Content-Type'

    # Value for the Access-Control-Allow-Methods header.
    # Default: Methods defined in handler class.
    # None means no header.
    CORS_METHODS = 'POST'

    # Value for the Access-Control-Allow-Credentials header.
    # Default: None (no header).
    # None means no header.
    CORS_CREDENTIALS = True

    # Value for the Access-Control-Max-Age header.
    # Default: 86400.
    # None means no header.
    CORS_MAX_AGE = 21600

    # Value for the Access-Control-Expose-Headers header.
    # Default: None
    CORS_EXPOSE_HEADERS = 'Location, X-WP-TotalPages'

    ...
```
