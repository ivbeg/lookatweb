from .consts import *

#  Rules to march CSS
STYLE_RULES = [
    {'type' : RULETYPE_REGEXP, 'text' : '^http://advancedparking\.ru/templates/',
        'entities' : [
            {'name' : 'web:parking/advancedparkingru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^/bitrix/templates(.*)',
        'entities' : [
            {'name' : 'web:cms/bitrix'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^/modules/system/defaults.css\?[0-9a-z]{1}$',
        'entities' : [
            {'name' : 'web:cms/drupal'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^/bitrix/components(.*)',
        'entities' : [
            {'name' : 'web:cms/bitrix'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://img.sedoparking.com/templates(.*)',
        'entities' : [
            {'name' : 'web:parking/sedo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '/components/com_artbannersplus/artbannersplus.css',
        'entities' : [
            {'name' : 'web:cms/joomla'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^/components/com_jcomments(.*)',
        'entities' : [
            {'name' : 'web:cms/joomla'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
]

