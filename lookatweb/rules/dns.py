from .consts import *


DNS_MX_RULES = [
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\saspmx\.l\.google\.com\.$',
        'entities' : [
            {'name' : 'dns:mailhost/googleapps'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\saspmx2\.googlemail\.com\.$',
        'entities' : [
            {'name' : 'dns:mailhost/googleapps'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\saspmx3\.googlemail\.com\.$',
        'entities' : [
            {'name' : 'dns:mailhost/googleapps'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\saspmx4\.googlemail\.com\.$',
        'entities' : [
            {'name' : 'dns:mailhost/googleapps'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx\.yandex\.ru\.$',
        'entities' : [
            {'name' : 'dns:mailhost/yandexpdd'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx02\.nicmail\.ru\.$',
        'entities' : [
            {'name' : 'dns:mailhost/nicmail_ru'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx01\.nicmail\.ru\.$',
        'entities' : [
            {'name' : 'dns:mailhost/nicmail_ru'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\sMX01\.NICMAIL\.RU\.$',
        'entities' : [
            {'name' : 'dns:mailhost/nicmail_ru'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx03\.nicmail\.ru\.$',
        'entities' : [
            {'name' : 'dns:mailhost/nicmail_ru'},
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx03\.nicmail\.ru\.$',
     'entities' : [
         {'name' : 'dns:mailhost/nicmail_ru'},
         ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx03\.nicmail\.ru\.$',
     'entities' : [
         {'name' : 'dns:mailhost/nicmail_ru'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx1\.masterhost\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/masterhost'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx\.mastermail\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/masterhost'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx2\.spaceweb\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/spaceweb'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx1\.spaceweb\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/spaceweb'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\sdial-148-240-4-32\.zone-1\.ip\.dial\.net\.mx\.$',
     'entities' : [
         {'name' : 'web:parking/sedo'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx2\.timeweb\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/timeweb'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx1\.timeweb\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/timeweb'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx\.cm\.hc\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/hcru'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx\.infobox\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/infobox'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\ssmtp\.infobox\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/infobox'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\srelay\.valuehost\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/valuehost'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smxs\.valuehost\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/valuehost'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smxs2\.valuehost\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/valuehost'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\pochta\.mtw\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/mtwru'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smxs2\.valuehost\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/valuehost'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx2\.peterhost\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/peterhost'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx3\.peterhost\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/peterhost'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\scluster\.relay\.agava\.net\.$',
     'entities' : [
         {'name' : 'web:hosting/agava'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx4\.peterhost\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/peterhost'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smxs\.majordomo\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/majordomo'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx30\.aha\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/zenon'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smailx\.hoster\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/hosterru'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smxs\.ht-systems\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/htsru'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx1\.beget\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/begetru'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^[0-9]{1,3}\smx2\.beget\.ru\.$',
     'entities' : [
         {'name' : 'web:hosting/begetru'},
         ]
    },


]
