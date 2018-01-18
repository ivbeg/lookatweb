from .consts import *

# Rules to march x-powered-by
POWEREDBY_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'PHP',
        'entities' : [
            {'name' : 'web:tech:lang/php'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ASP.NET',
        'entities' : [
            {'name' : 'web:tech:lang/aspnet'},
            {'name' : 'web:os/windows'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ModLayout',
        'entities' : [
            {'name' : 'web:tech:module/modlayout'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'NetCat',
        'entities' : [
            {'name' : 'web:cms/netcat'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ASP.NET, PHP',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:tech:lang/asp.net'},
            {'name' : 'web:os/windows'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'PleskWin, ASP.NET',
        'entities' : [
            {'name' : 'web:cms/pleskwin'},
            {'name' : 'web:tech:lang/asp.net'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Phusion Passenger (mod_rails',
        'entities' : [
            {'name' : 'web:tech:module/mod_rails'},
            {'name' : 'web:tech:lang/ruby'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'eZ publish',
        'entities' : [
            {'name' : 'web:cms/ezpublish'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'eZ Publish',
        'entities' : [
            {'name' : 'web:cms/ezpublish'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'JSP',
        'entities' : [
            {'name' : 'web:tech/jsp'},
            {'name' : 'web:tech:lang/java'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^Servlet 2\.4; JBoss\-(.*)',
        'schema' : {'keys' : 'string'},
        'entities' : [
            {'name' : 'web:tech:lang/java'},
            {'name' : 'web:cms/jboss'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^HostCMS (?P<keys>([0-9\s]*))',
        'schema' : {'keys' : 'string'},
        'entities' : [
            {'name' : 'web:cms/hostcms'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
]
