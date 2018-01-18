from .consts import *


# Rules to march HTTP headers
HEADERS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'content-type', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'microsoftofficewebserver',
        'entities' : [
            {'name' : 'web:os/windows'},
            {'name' : 'web:server/iis'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-wm-out', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'vary', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'status', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-ua-compatible', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'server', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'pragma', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-powered-by', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'date', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'connection', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'cache-control', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'expires', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'last-modified', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'accept-ranges', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-cache', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'content-language', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-powered-cms', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:web:powered_cms',
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'a-powered-by', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:web:powered_cms',
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'b-powered-by', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:web:powered_cms',
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'content-location', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'via', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-pad', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-xss-protection', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-cache-lookup', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'age', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'content-encoding', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'set-cookie', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:web:cookie',
        'entities' : [
            {'name' : 'site:info/cookiesupport'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'content-length',
        'entities' : [
            {'name' : 'site:info/returnslength'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-aspnet-version',
        'entities' : [
            {'name' : 'web:tech:lang/aspnet'},
            {'name' : 'web:os/windows'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'x-pingback',
        'entities' : [
            {'name' : 'site:info/pingback'},
            {'name' : 'site:classify/blog'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'p3p',
        'entities' : [
            {'name' : 'site:info/p3p'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'etag',
        'entities' : [
            {'name' : 'site:info/etagsupported'},
        ]
    },
]
