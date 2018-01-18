from .consts import *

# Rules to match cookies
COOKIE_RULES = [
    {'type' : RULETYPE_REGEXP, 'text' : '^PHPSESSID=',
        'entities' : [
            {'name' : 'web:tech:lang/php'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^whitex=',
        'entities' : [
            {'name' : 'web:tech:lang/php'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)phpbb2mysql=(.*)',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:cms/phpbb'},
            {'name' : 'web:tech:db/mysql'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)phpbb2mysql=(.*)',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:cms/phpbb'},
            {'name' : 'web:tech:db/mysql'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)phpbb2_u=(.*)',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:cms/phpbb'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^phpbb3_[0-9a-z]{1,5}_u=(.*)',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:cms/phpbb'},
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^SN[0-9a-z]{13,13}=(.*)',
     'entities' : [
         {'name' : 'web:tech:lang/php'},
         {'name' : 'web:cms/modx'},
         ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^SESS[0-9a-z]{32,32}=(.*)',
     'entities' : [
         {'name' : 'web:tech:lang/php'},
         {'name' : 'web:cms/drupal'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^X\-Mapping\-[a-z]{1,10}=(.*)',
     'entities' : [
         {'name' : 'web:cms/stingray'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^SL_SID=(.*)',
     'entities' : [
         {'name' : 'web:counter/openstat'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^__cfduid=(.*)',
     'entities' : [
         {'name' : 'web:cdn/cloudflare'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^DotNetNukeAnonymous=(.*)',
        'entities' : [
            {'name' : 'web:tech:lang/aspnet'},
            {'name' : 'web:cms/dotnetnuke'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^MoodleSession=(.*)',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:cms/moodle'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^(.*)_LAST_VISIT$',
        'entities' : [
            {'name' : 'web:cms/bitrix'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^modxcmssession=',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:cms/modx'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '\.ASPXANONYMOUS',
        'entities' : [
            {'name' : 'web:tech:lang/aspnet'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^parkinglot=1',
        'entities' : [
            {'name' : 'web:parking/domainsponsor'},
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^JSESSIOND',
        'entities' : [
            {'name' : 'web:tech:lang/jsp'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'ASPSESSIONID[A-Z]{8}=',
        'entities' : [
            {'name' : 'web:tech:lang/asp'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'ASP\.NET_SessionId=',
        'entities' : [
            {'name' : 'web:tech:lang/aspnet'}
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '(.*)umicms_session=(.*)',
        'entities' : [
            {'name' : 'web:cms/umicms'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)dle_user_id=(.*)',
        'entities' : [
            {'name' : 'web:cms/dle'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^Apache=',
        'entities' : [
            {'name' : 'web:server/apache'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^fe_typo_user=',
        'entities' : [
            {'name' : 'web:cms/typo3'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^symphony=',
        'entities' : [
            {'name' : 'web:cms/symphony'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)DokuWiki=',
        'entities' : [
            {'name' : 'web:cms/dokuwiki'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)flybb_cookies_data=',
        'entities' : [
            {'name' : 'web:cms/flybb'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)ZDEDebuggerPresent=',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:tech/zend'},
        ]
    },



    {'type' : RULETYPE_FIND, 'text' : '60767B17-9386-42ae-BBA9-D1BCA9E8837B',
        'entities' : [
            {'name' : 'web:parking/parkingnicru'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'bbsessionhash=',
        'entities' : [
            {'name' : 'web:cms/vbulletin'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'POSTNUKESID=',
        'entities' : [
            {'name' : 'web:cms/postnuke'},
            {'name' : 'web:tech:lang/php'},
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^CFID=(.*)',
        'entities' : [
            {'name' : 'web:tech:lang/coldfusion'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^XARAYASID=(.*)',
        'entities' : [
            {'name' : 'web:cms/xaraya'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^CAKEPHP=',
        'entities' : [
            {'name' : 'web:cms/cakephp'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
]
