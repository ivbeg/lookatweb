from .consts import *

# Rules to match images
IMAGES_RULES = [
    {'type' : RULETYPE_FIND, 'text' : 'http://stats.nprk.ru/cnt-gif1x1.php',
        'entities' : [
            {'name' : 'web:parking/parkingnicru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://[a-z0-9]{1,5}\.[0-9]{1,4}\.spylog\.com/cnt(.*)',
        'entities' : [
            {'name' : 'web:counter/spylog'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://hit[0-9]{1,2}\.hotlog.ru/cgi-bin/hotlog/count(.*)',
        'entities' : [
            {'name' : 'web:counter/hotlogru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://stat\.aport\.ru/show\.pl(.*)',
        'entities' : [
            {'name' : 'web:counter/aportru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://catalog\.metka\.ru/counter/counter\.php(.*)',
        'entities' : [
            {'name' : 'web:counter/metkaru'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://pics.rbc.ru/img/grinf/complex',
        'entities' : [
            {'name' : 'web:widgets:fin/rbcinformer'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://(count\.|)yandeg\.ru/cnt.php(.*)',
        'entities' : [
            {'name' : 'web:counter/yandeg'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://(www\.|)directrix\.ru/cgi-bin/counter/counter\.cgi(.*)',
        'entities' : [
            {'name' : 'web:counter/directrix'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://(www\.|)directrix\.ru/cgi-bin/counter/counter\.cgi(.*)',
        'entities' : [
            {'name' : 'web:counter/directrix'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://radionet\.pp\.ru/top/cnt\.cgi(.*)',
        'entities' : [
            {'name' : 'web:counter/radionetppru'}
        ]
    },


    {'type' : RULETYPE_REGEXP, 'text' : '^http://top\.lipetsk\.name/cgi-bin/cnt\.cgi(.*)',
        'entities' : [
            {'name' : 'web:counter/toplipetskname'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://counter\.co\.kz/CounterCoKz',
        'entities' : [
            {'name' : 'web:counter/countercokz'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://top\.net\.ru/cgi-bin',
        'entities' : [
            {'name' : 'web:counter/topnetru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://top([0-9]{1,2}|)\.mail\.ru/counter(.*)',
        'entities' : [
            {'name' : 'web:counter/topmailru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://(.*)\.top\.mail\.ru/counter(.*)',
        'entities' : [
            {'name' : 'web:counter/topmailru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://top\.list\.ru/counter(.*)',
        'entities' : [
            {'name' : 'web:counter/topmailru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://(.*)\.top\.list\.ru/counter(.*)',
        'entities' : [
            {'name' : 'web:counter/topmailru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://top100-images\.rambler\.ru/top100/(.*)',
        'entities' : [
            {'name' : 'web:counter/ramblertop100'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://www\.warlog\.ru/counter/(.*)',
        'entities' : [
            {'name' : 'web:counter/warlogru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://cnt\.one\.ru/cgi\-bin/cnt\.cgi/(.*)',
        'entities' : [
            {'name' : 'web:counter/one.ru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://counter\.rambler\.ru/top100\.jcn/(.*)',
        'entities' : [
            {'name' : 'web:counter/ramblertop100'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://cnt\.rambler\.ru/top100\.jcn/(.*)',
        'entities' : [
            {'name' : 'web:counter/ramblertop100'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://ad\.adriver\.ru/cgi-bin/rle\.cgi(.*)',
        'entities' : [
            {'name' : 'web:adv/adriver'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://p[0-9]{1,5}\.adskape\.ru/adout\.js',
        'entities' : [
            {'name' : 'web:adv/adscape'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^/wps/themes/html/(.*)',
        'entities' : [
            {'name' : 'web:cms/websphere'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://counter\.24log\.ru/buttons/(.*)',
        'entities' : [
            {'name' : 'web:counter/24logru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://(www\.|)info\.weather\.yandex\.net/informer/(.*)',
        'entities' : [
            {'name' : 'web:widgets:weather/yandexweather'}
        ]
    },

    {'type' : RULETYPE_EQUAL, 'text' : 'http://info.maps.yandex.net/traffic/moscow/current_traffic_150.gif',
        'entities' : [
            {'name' : 'web:widgets:cars/yandextraffic'}
        ]
    },

    {'type' : RULETYPE_EQUAL, 'text' : 'http://info.maps.yandex.net/traffic/moscow/current_traffic_100.gif',
        'entities' : [
            {'name' : 'web:widgets:cars/yandextraffic'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://info.maps.yandex.net/traffic/moscow/current_traffic_88.gif',
        'entities' : [
            {'name' : 'web:widgets:cars/yandextraffic'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://info.maps.yandex.net/traffic/moscow/current_traffic_234.gif',
        'entities' : [
            {'name' : 'web:widgets:cars/yandextraffic'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'http://(www\.|)yandex\.ru/cycounter',
        'entities' : [
            {'name' : 'web:widgets:ranks/cycounter'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://images\.rambler\.ru/top100/(.*)',
        'entities' : [
            {'name' : 'web:counter/ramblertop100'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://img\.sedoparking\.com/templates/(.*)',
        'entities' : [
            {'name' : 'web:parking/sedo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.narod.ru/counter.xhtml',
        'entities' : [
            {'name' : 'web:counter/narodru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://www\.tns-counter\.ru/V13a(.*)',
        'entities' : [
            {'name' : 'web:counter/tns'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://[0-9a-z]{2}\.extreme-dm\.com',
        'entities' : [
            {'name' : 'web:counter/extremetrack'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'top\.list\.ru/counter\?',
        'entities' : [
            {'name' : 'web:counter/mailrutop'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://counter\.yadro\.ru/logo(.*)',
        'entities' : [
            {'name' : 'web:counter/liveinternet'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.vsego.ru/images/bkat8831.gif',
        'entities' : [
            {'name' : 'web:banner/vsego_ru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.uaportal.com/banners/8831_1.gif',
        'entities' : [
            {'name' : 'web:banner/uaportal'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://lenta.yandex.ru/i/addfeed.gif',
        'entities' : [
            {'name' : 'web:widgets:news/yandexlenta'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://buttons.googlesyndication.com/fusion/add.gif',
        'entities' : [
            {'name' : 'web:widgets:news/googlereader'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://narod.yandex.ru/images/u_templ/narod.gif',
        'entities' : [
            {'name' : 'web:banner/narod_ru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://site.yandex.ru/i/yandex_search.png',
        'entities' : [
            {'name' : 'web:widgets:search/yandexsitesearch'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://catalog.tut.by/images/catalog-tut.gif',
        'entities' : [
            {'name' : 'web:banner/tut_by'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.invictory.org/banners/our/counter88x31.gif',
        'entities' : [
            {'name' : 'web:counter/invictory'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.w3.org/Icons/valid-xhtml10',
        'entities' : [
            {'name' : 'web:banner/w3c'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://jigsaw.w3.org/css-validator/images/vcss',
        'entities' : [
            {'name' : 'web:banner/w3c'}
        ]
    },
]
