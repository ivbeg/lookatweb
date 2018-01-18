from .consts import *


# Object matching by classid
OBJECTS_CLSID_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'clsid:D27CDB6E-AE6D-11cf-96B8-444553540000',
        'entities' : [
            {'name' : 'web:tech/flash'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'clsid:d27cdb6e-ae6d-11cf-96b8-444553540000',
        'entities' : [
            {'name' : 'web:tech/flash'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'clsid:-D27CDB6E-AE6D-11cf-96B8-444553540000',
        'entities' : [
            {'name' : 'web:tech/flash'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'CLSID:22D6F312-B0F6-11D0-94AB-0080C74C7E95',
        'entities' : [
            {'name' : 'web:tech:activex/wmplayer'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'CLSID:22D6F312-B0F6-11D0-94AB-0080C74C7E95',
        'entities' : [
            {'name' : 'web:tech:activex/wmplayer'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'clsid:22D6F312-B0F6-11D0-94AB-0080C74C7E95',
        'entities' : [
            {'name' : 'web:tech:activex/wmplayer'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'clsid:6BF52A52-394A-11D3-B153-00C04F79FAA6',
        'entities' : [
            {'name' : 'web:tech:activex/wmplayer'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'CLSID:CFCDAA03-8BE4-11cf-B84B-0020AFBBCCFA',
        'entities' : [
            {'name' : 'web:tech:activex/realplayer'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'clsid:CFCDAA03-8BE4-11cf-B84B-0020AFBBCCFA',
        'entities' : [
            {'name' : 'web:tech:activex/realplayer'}
        ]
    },



]

# match object tags by type
OBJECTS_TYPE_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'application/x-silverlight-2',
        'entities' : [
            {'name' : 'web:tech/silverlight'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'application/x-shockwave-flash',
        'entities' : [
            {'name' : 'web:tech/flash'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'application/x-oleobject',
        'entities' : [
            {'name' : 'web:tech/activex'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'image/svg+xml',
        'entities' : [
            {'name' : 'web:tech/svg'}
        ]
    },
]


# match object tags by data
OBJECTS_DATA_RULES = [
    {'type' : RULETYPE_REGEXP, 'text' : '^http://img\.yandex\.net/i/time/clock\.swf',
        'entities' : [
            {'name' : 'web:widgets:clock/yandexclock'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://vimeo\.com',
        'entities' : [
            {'name' : 'web:media:video/vimeo'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://www\.youtube\.com',
        'entities' : [
            {'name' : 'web:media:video/youtube'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://cdn\.last\.fm/widgets/chart',
        'entities' : [
            {'name' : 'web:widgets:audio/lastfm'}
        ]
    },
]

# match object tags by embed src
EMBED_SRC_RULES = [
    {'type' : RULETYPE_REGEXP, 'text' : '^http://img\.mail\.ru/r/video2/player_v2\.swf',
        'entities' : [
            {'name' : 'web:media:video/mailru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://flv\.video\.yandex\.ru',
        'entities' : [
            {'name' : 'web:media:video/yandex'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://img\.gismeteo\.ru/flash',
        'entities' : [
            {'name' : 'web:widgets:meteo/gismeteo'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://www\.clocklink\.com/clocks/',
        'entities' : [
            {'name' : 'web:widgets:time/clocklink'}
        ]
    },

    {'type' : RULETYPE_EQUAL, 'text' : 'http://iii.ru/static/Vishnu.swf',
        'entities' : [
            {'name' : 'web:widgets:chat/iiiru'}
        ]
    },


    {'type' : RULETYPE_REGEXP, 'text' : '^http://[a-z0-9]{1,3}\.videos\.sapo\.pt/play',
        'entities' : [
            {'name' : 'web:media:video/sapovideos'}
        ]
    },

    {'type' : RULETYPE_EQUAL, 'text' : 'http://pub.tvigle.ru/swf/tvigle_single_v2.swf',
        'entities' : [
            {'name' : 'web:media:video/twigle'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://rpod\.ru/i/b/listen_240x400_01/core\.swf',
        'entities' : [
            {'name' : 'web:media:audio/rpodru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://vision\.rambler\.ru/i/e\.swf',
        'entities' : [
            {'name' : 'web:media:video/ramblervision'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://pics\.smotri\.com/scrubber_custom8\.swf',
        'entities' : [
            {'name' : 'web:media:video/smotricom'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://www\.russia\.ru/player/main\.swf',
        'entities' : [
            {'name' : 'web:media:video/russiaru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://video\.google\.(com|ru|ca|de)/googleplayer.swf',
        'entities' : [
            {'name' : 'web:media:video/googlevideo'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://www\.youtube\.com/v/',
        'entities' : [
            {'name' : 'web:media:video/youtube'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^/bitrix/templates/',
        'entities' : [
            {'name' : 'web:cms/bitrix'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^/bitrix/components/',
        'entities' : [
            {'name' : 'web:cms/bitrix'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://developer\.truveo\.com/apps/listWidget',
        'entities' : [
            {'name' : 'web:media:video/truveo'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://pics\.rbc\.ru/informer',
        'entities' : [
            {'name' : 'web:widgets:fin/rbcinformer'}
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^http://video\.rutube\.ru',
        'entities' : [
            {'name' : 'web:media:video/rutube'}
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^http://static\.twitter\.com/flash/widgets/profile/TwitterWidget\.swf',
        'entities' : [
            {'name' : 'web:widgets:blog/twitter'}
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^http://vimeo\.com/moogaloop.swf',
        'entities' : [
            {'name' : 'web:media:video/vimeo'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://www.1tv.ru/(n|p)video',
        'entities' : [
            {'name' : 'web:media:video/1tvru'}
        ]
    },
]

