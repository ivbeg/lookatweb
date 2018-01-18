from .consts import *

# Match rules for encodings
ENCODING_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'utf8',
        'entities' : [
            {'name' : 'page:encoding/utf8'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'utf-8',
        'entities' : [
            {'name' : 'page:encoding/utf8'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'windows-1251',
        'entities' : [
            {'name' : 'page:encoding/cp1251'},
            {'name' : 'page:lang/russian'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'cp1251',
        'entities' : [
            {'name' : 'page:encoding/cp1251'},
            {'name' : 'page:lang/russian'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ascii',
        'entities' : [
            {'name' : 'page:encoding/ascii'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'iso-8859-1',
        'entities' : [
            {'name' : 'page:encoding/iso-8859-1'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'iso-8859-2',
        'entities' : [
            {'name' : 'page:encoding/iso-8859-2'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'koi8-r',
        'entities' : [
            {'name' : 'page:encoding/koi8-r'},
            {'name' : 'page:lang/russian'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'gb2312',
        'entities' : [
            {'name' : 'page:encoding/gb2312'},
            {'name' : 'page:lang/chinese'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'MacCyrillic',
        'entities' : [
            {'name' : 'page:encoding/maccyr'},
            {'name' : 'page:lang/russian'}
        ]
    },
]
