from .consts import *

L1_DOMAIN_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'ru', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:net:domains_ru',
        'entities' : [
            {'name' : 'geo:ru:country/russia'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'su', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:net:domains_su',
        'entities' : [
            {'name' : 'geo:ru:country/russia'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ua',
        'entities' : [
            {'name' : 'geo:ru:country/ukraina'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'kz',
        'entities' : [
            {'name' : 'geo:ru:country/kazakhastan'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'tj',
        'entities' : [
            {'name' : 'geo:ru:country/tadjikistan'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'by', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:net:domains_by',
        'entities' : [
            {'name' : 'geo:ru:country/belarus'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'com', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:net:domains_com',
        'entities' : [
        ]
    },
]



RU_DOMAINPART_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'msk',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscow'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'spb',
        'entities' : [
            {'name' : 'geo:ru:regioname/peterburg'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'kaluga',
        'entities' : [
            {'name' : 'geo:ru:regioname/kaluga'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'sochi',
        'entities' : [
            {'name' : 'geo:ru:city/sochi'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ufa',
        'entities' : [
            {'name' : 'geo:ru:city/ufa'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'perm',
        'entities' : [
            {'name' : 'geo:ru:city/perm'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'samara',
        'entities' : [
            {'name' : 'geo:ru:city/samara'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'msk',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscow'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'moscow',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscow'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'kazan',
        'entities' : [
            {'name' : 'geo:ru:city/kazan'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'nsk',
        'entities' : [
            {'name' : 'geo:ru:city/novosibirsk'},
        ]
    },
]

COM_DOMAINS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'blogspot',
        'entities' : [
            {'name' :'site:classify/blog'},
            {'name' :'web:hosting/blogspot'},
            {'name' : 'web:cms/staticcontent'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'livejournal',
        'entities' : [
            {'name' :'site:classify/blog'},
            {'name' :'web:hosting/livejournal'}
        ]
    },
]

SU_DOMAINS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'moy',
        'entities' : [
            {'name' : 'web:hosting/ucoz'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'clan',
        'entities' : [
            {'name' : 'web:hosting/ucoz'},
        ]
    },
]

BY_DOMAINS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'gov',
        'entities' : [
            {'name' : 'site:classify/government'},
        ]
    },
]

RU_DOMAINS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'fatal',
        'entities' : [
            {'name' : 'web:hosting/fatalru'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'narod',
        'entities' : [
            {'name' : 'web:hosting/narodru'},
            {'name' : 'web:cms/staticcontent'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'newmail',
        'entities' : [
            {'name' : 'web:hosting/pochtaru'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'nm',
        'entities' : [
            {'name' : 'web:hosting/nmru'},
            {'name' : 'web:cms/staticcontent'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'gov',
        'entities' : [
            {'name' : 'site:classify/government'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'obninsk',
        'entities' : [
            {'name' : 'geo:ru:city/obninsk'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'perm',
        'entities' : [
            {'name' : 'geo:ru:regioname/perm'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'khv',
        'entities' : [
            {'name' : 'geo:ru:regioname/khabarovsk'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'arbitr',
        'entities' : [
            {'name' : 'site:classify/government'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'roskazna',
        'entities' : [
            {'name' : 'site:classify/government'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'sudrf',
        'entities' : [
            {'name' : 'site:classify/government'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'tomsk',
        'entities' : [
            {'name' : 'geo:ru:regioname/tomsk'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mos',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscow'},
            {'name' : 'site:classify/government'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mos',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscow'},
            {'name' : 'site:classify/government'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'msk',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscow'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'edu',
        'entities' : [
            {'name' : 'site:classify/education'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '68edu',
        'entities' : [
            {'name' : 'site:classify/education'},
            {'name' : 'geo:ru:regioname/tomsk'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'msu',
        'entities' : [
            {'name' : 'site:classify/education'},
#           {'name' : 'org:theme:university/msu'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'orthodoxy',
        'entities' : [
            {'name' : 'site:classify/religion'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'religion',
        'entities' : [
            {'name' : 'site:classify/religion'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'chat',
        'entities' : [
            {'name' : 'web:hosting/chatru'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'borda',
        'entities' : [
            {'name' : 'web:hosting/bordaru'},
            {'name' : 'site:classify/forum'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mybb',
        'entities' : [
            {'name' : 'web:hosting/mybbru'},
            {'name' : 'site:classify/forum'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'forum24',
        'entities' : [
            {'name' : 'web:hosting/bordaru'},
            {'name' : 'site:classify/forum'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'sitecity',
        'entities' : [
            {'name' : 'web:hosting/sitecityru'},
        ]
    },


    {'type' : RULETYPE_EQUAL, 'text' : 'edusite',
        'entities' : [
            {'name' : 'site:classify/education'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ac',
        'entities' : [
            {'name' : 'site:classify/science'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'spb',
        'entities' : [
            {'name' : 'geo:ru:regioname/peterburg'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'nsk',
        'entities' : [
            {'name' : 'geo:ru:regioname/novosibirsk'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'nsk',
        'entities' : [
            {'name' : 'geo:ru:regioname/novosibirsk'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'nnov',
        'entities' : [
            {'name' : 'geo:ru:regioname/nnovgorod'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'boom',
        'entities' : [
            {'name' : 'web:hosting/boomru'},
            {'name' : 'web:cms/staticcontent'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '3dn',
        'entities' : [
            {'name' : 'web:hosting/ucoz'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'p0',
        'entities' : [
            {'name' : 'web:hosting/ucoz'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ucoz',
        'entities' : [
            {'name' : 'web:hosting/ucoz'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'nalog',
        'entities' : [
            {'name' : 'site:classify/government'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'kirov',
        'entities' : [
            {'name' : 'geo:ru:regioname/kirov'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'tver',
        'entities' : [
            {'name' : 'geo:ru:regioname/tver'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'kursk',
        'entities' : [
            {'name' : 'geo:ru:regioname/kursk'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'chita',
        'entities' : [
            {'name' : 'geo:ru:regioname/chita'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'lipetsk',
        'entities' : [
            {'name' : 'geo:ru:regioname/lipetsk'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ryazan',
        'entities' : [
            {'name' : 'geo:ru:regioname/ryazan'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'khv',
        'entities' : [
            {'name' : 'geo:ru:regioname/khabarovsk'},
        ]
    },
]
