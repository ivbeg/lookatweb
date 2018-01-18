from .consts import *

# Iframe matching rules
IFRAMES_RULES = [
    {'type' : RULETYPE_FIND, 'text' : '.http://link.link.ru/show?squareid=',
        'entities' : [
            {'name' : 'web:adv/linkru'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : '.cbox.ws/box/?boxid=',
        'entities' : [
            {'name' : 'web:widgets:chat/cboxws'}
        ]
    },

    {'type' : RULETYPE_FIND, 'text' : '.linkexchange.ru/cgi-bin/erle.cgi',
        'entities' : [
            {'name' : 'web:adv/linkexchange'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : '.4smi.ru/cgi-bin/iframe/',
        'entities' : [
            {'name' : 'web:adv/4smi'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : '.lbn.ru/cgi-bin/iframe/',
        'entities' : [
            {'name' : 'web:adv/lbnru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://(|click\.)readme\.ru/informer/(.*)$',
        'entities' : [
            {'name' : 'web:adv/readmeru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://api\.recaptcha\.net/noscript',
        'entities' : [
            {'name' : 'web:widgets:captcha/recaptcha'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://partner\.magna\.ru/partner/gb\.php',
        'entities' : [
            {'name' : 'web:adv/magnaru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://link\.link\.ru/show',
        'entities' : [
            {'name' : 'web:adv/linkru'}
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^http://ads\.advline\.ru/(.*)$',
        'entities' : [
            {'name' : 'web:adv/advlineru'}
        ]
    },


    {'type' : RULETYPE_REGEXP, 'text' : '^http://anons\.prbn\.ru/cgi-bin/iframe/',
        'entities' : [
            {'name' : 'web:adv/prbnru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://adv\.mabico\.ru/cgi-bin/advert\.cgi(.*)',
        'entities' : [
            {'name' : 'web:adv/mabicoru '}
        ]
    },

    {'type' : RULETYPE_FIND, 'text' : '.tbn.ru/cgi-bin/iframe/',
        'entities' : [
            {'name' : 'web:adv/tbn'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'lbs.km.ru/',
        'entities' : [
            {'name' : 'web:adv/lbskmru'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://rp5.ru/html.php',
        'entities' : [
            {'name' : 'web:widgets:meteo/rp5ru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'adfox.ru/([0-9]{1,9}/|)getCode',
        'entities' : [
            {'name' : 'web:adv/tbn'}
        ]
    },
]
