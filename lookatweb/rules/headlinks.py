from .consts import *

HEADLINKS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'stylesheet','action' : ACTION_FOLLOW, 'matcherkey' : 'r:web:styles',
        'entities' : [
            {'name' : 'site:info/csssupport'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'shortcut icon',
        'entities' : [
            {'name' : 'site:info/favicon'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'icon',
        'entities' : [
            {'name' : 'site:info/favicon'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'wlmanifest',
        'entities' : [
            {'name' : 'site:info/wlmanifest'},
            {'name' : 'site:classify/blog'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'search',
        'entities' : [
            {'name' : 'site:info/search'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'openid.server',
        'entities' : [
            {'name' : 'site:info/openid'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'dns-prefetch',
     'entities' : [
         {'name' : 'site:info/dnsprefetch'}
     ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'apple-touch-icon',
        'entities' : [
            {'name' : 'site:info/appleicon'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'apple-touch-icon-precompressed',
     'entities' : [
         {'name' : 'site:info/appleicon'}
     ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'openid2.provider',
        'entities' : [
            {'name' : 'site:info/openid'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'pingback',
        'entities' : [
            {'name' : 'site:info/pingback'},
            {'name' : 'site:classify/blog'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'edituri',
        'entities' : [
            {'name' : 'site:info/edituri'},
            {'name' : 'site:classify/blog'},
        ]
    },
]


# Matching head links by type
HEADLINKS_TYPE_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'application/atom+xml',
        'entities' : [
            {'name' : 'web:feeds/atom'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'application/rss+xml',
        'entities' : [
            {'name' : 'web:feeds/rss'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'application/rsd+xml',
        'entities' : [
            {'name' : 'site:info/rsd'},
            {'name' : 'site:classify/blog'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'application/wlwmanifest+xml',
        'entities' : [
            {'name' : 'site:info/livewriter'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'application/opensearchdescription+xml',
        'entities' : [
            {'name' : 'site:info/opensearch'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'application/x-opera-widgets',
        'entities' : [
            {'name' : 'web:widgets/operawidget'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'image/vnd.microsoft.icon',
        'entities' : [
            {'name' : 'site:info/favicon'}
        ]
    },
]

