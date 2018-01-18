from .consts import *


WHOIS_FIELDS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'whois:organization', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:net:whois_org',
        'entities' : [
            {'name' : 'whois:rectype/org'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'whois:person', 'action' : ACTION_FOLLOW, 'matcherkey' : 'r:net:whois_person',
        'entities' : [
            {'name' : 'whois:rectype/person'},
        ]
    },
]

WHOIS_PERSON_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'private person',
        'entities' : [
            {'name' : 'whois:rectype/anonymous'},
        ]
    },
]



WHOIS_ORG_RULES = [
    {'type' : RULETYPE_FIND, 'text' : 'moscow',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscow'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'moskva',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscow'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'moskvy',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscow'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'moscow region',
        'entities' : [
            {'name' : 'geo:ru:regioname/moscowobl'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'peterburg',
        'entities' : [
            {'name' : 'geo:ru:regioname/peterburg'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'petersburg',
        'entities' : [
            {'name' : 'geo:ru:regioname/peterburg'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^jsc\s(.*)',
        'entities' : [
            {'name' : 'org:type/jsc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^joint stock company\s(.*)',
        'entities' : [
            {'name' : 'org:type/jsc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^joint stok company\s(.*)',
        'entities' : [
            {'name' : 'org:type/jsc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^joint\-stock company\s(.*)',
        'entities' : [
            {'name' : 'org:type/jsc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^oao\s(.*)',
        'entities' : [
            {'name' : 'org:type/jsc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^zao\s(.*)',
        'entities' : [
            {'name' : 'org:type/cjsc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^ooo\s(.*)',
        'entities' : [
            {'name' : 'org:type/llc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^llc\s(.*)',
        'entities' : [
            {'name' : 'org:type/llc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^(.*)\sllc$',
        'entities' : [
            {'name' : 'org:type/llc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^(.*)\slimited$',
        'entities' : [
            {'name' : 'org:type/llc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)\scompany$',
        'entities' : [
            {'name' : 'org:type/commercial'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)\sinc(|\.)$',
        'entities' : [
            {'name' : 'org:type/commercial'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)\scorporation$',
        'entities' : [
            {'name' : 'org:type/commercial'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)\sltd(|\.)$',
        'entities' : [
            {'name' : 'org:type/ltd'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^ltd(\s|\.)(.*)$',
        'entities' : [
            {'name' : 'org:type/ltd'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'limited liability company',
        'entities' : [
            {'name' : 'org:type/llc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(bank\s|\sbank|\sbank\s)',
        'entities' : [
            {'name' : 'org:type/jsc'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(university\s|\suniversity|\suniversity\s)',
        'entities' : [
            {'name' : 'org:topic:edu/university'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'region administration',
        'entities' : [
            {'name' : 'org:type:gov/regadm'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'municipal administration',
        'entities' : [
            {'name' : 'org:type:gov/munadm'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'city administration',
        'entities' : [
            {'name' : 'org:type:gov/munadm'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'town administration',
        'entities' : [
            {'name' : 'org:type:gov/munadm'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'federal agency',
        'entities' : [
            {'name' : 'org:type:gov/federal'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'federal state',
        'entities' : [
            {'name' : 'org:type:gov/federal'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'federal service',
        'entities' : [
            {'name' : 'org:type:gov/federal'},
        ]
    },
]

