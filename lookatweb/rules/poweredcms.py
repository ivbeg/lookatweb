from .consts import *

# Rules to march x-powered-by
POWERED_CMS_RULES = [

    {'type' : RULETYPE_REGEXP, 'text' : '^Bitrix Site Manager',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:cms/bitrix'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'PleskWin',
        'entities' : [
            {'name' : 'web:cms/pleskwin'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^ABO\.CMS',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:cms/abocms'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'Aquilon CMS',
        'entities' : [
            {'name' : 'web:tech:lang/aspnet'},
            {'name' : 'web:cms/aquiloncms'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^Bitrix SM',
        'entities' : [
            {'name' : 'web:tech:lang/php'},
            {'name' : 'web:cms/bitrix'}
        ]
    },
]

