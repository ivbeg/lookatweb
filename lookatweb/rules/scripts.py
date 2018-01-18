from .consts import *


# Rules to match outside scripts
SCRIPTS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'jquery.js',
        'entities' : [
            {'name' : 'web:scripts/jquery'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'jshttprequest.js',
        'entities' : [
            {'name' : 'web:scripts/jshttprequest'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'JsHttpRequest.js',
        'entities' : [
            {'name' : 'web:scripts/jshttprequest'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'prototype.js',
        'entities' : [
            {'name' : 'web:scripts/prototype'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'gemius.js',
        'entities' : [
            {'name' : 'web:counter/gemius'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'xgemius.js',
        'entities' : [
            {'name' : 'web:counter/gemius'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'swfobject.js',
        'entities' : [
            {'name' : 'web:scripts/swfobject'},
            {'name' : 'web:tech/flash'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mootools.js',
        'entities' : [
            {'name' : 'web:scripts/mootools'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'AC_RunActiveContent.js',
        'entities' : [
            {'name' : 'web:tech/flash'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'prototype.js',
        'entities' : [
            {'name' : 'web:script/prototype'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'lightbox.js',
        'entities' : [
            {'name' : 'web:scripts/lightbox'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'scriptaculous.js',
        'entities' : [
            {'name' : 'web:scripts/scriptaculous'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'drupal.js',
        'entities' : [
            {'name' : 'web:cms/drupal'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '/_layouts/1049/ows.js',
        'entities' : [
            {'name' : 'web:cms/mssharepoint'},
            {'name' : 'web:tech:lang/aspnet'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'thickbox.js',
        'entities' : [
            {'name' : 'web:scripts/thickbox'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'jquery.corner.js',
        'entities' : [
            {'name' : 'web:scripts/jquery.corner'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'ScriptResource.axd',
        'entities' : [
            {'name' : 'web:tech:lang/aspnet'},
            {'name' : 'web:os/windows'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'WebResource.axd',
        'entities' : [
            {'name' : 'web:tech:lang/aspnet'},
            {'name' : 'web:os/windows'},
        ]
    },
]


INSCRIPTS_RULES = [
    {'type' : RULETYPE_FIND, 'text' : 'http://luxup.ru/tr',
        'entities' : [
            {'name' : 'web:adv/luxupru'}
        ]
    },

    {'type' : RULETYPE_FIND, 'text' : 'http://stats.nprk.ru/cnt-gif1x1.php',
        'entities' : [
            {'name' : 'web:parking/parkingnicru'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://informer.tamognia.ru',
        'entities' : [
            {'name' : 'web:widgets:fin/tamogniaru'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://click.kmindex.ru/?uid',
        'entities' : [
            {'name' : 'web:counter/kmindex'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://c.bigmir.net/',
        'entities' : [
            {'name' : 'web:counter/bigmirnet'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://sup.adfox.ru/',
        'entities' : [
            {'name' : 'web:adv/adfox'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://ads.adfox.ru/',
        'entities' : [
            {'name' : 'web:adv/adfox'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'google-analytics.com/ga.js',
        'entities' : [
            {'name' : 'web:counter/ga'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://counter.yadro.ru/hit',
        'entities' : [
            {'name' : 'web:counter/liveinternet'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'an.yandex.ru/resource',
        'entities' : [
            {'name' : 'web:adv/yadirect'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://an.yandex.ru/system/context.js',
        'entities' : [
            {'name' : 'web:adv/yadirect'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : '//mc.yandex.ru/metrika/watch.js',
        'entities': [
            {'name': 'web:counter/yametrika'}
         ]
     },
    {'type': RULETYPE_FIND, 'text': '//www.liveinternet.ru/click',
     'entities': [
         {'name': 'web:counter/liveinternet'}
     ]
     },
    {'type': RULETYPE_FIND, 'text': '//openstat.net/cnt.js',
     'entities': [
         {'name': 'web:counter/openstat'}
     ]
     }

]



# Rules to match external scripts
EXTSCRIPTS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'http://pagead2.googlesyndication.com/pagead/show_ads.js',
        'entities' : [
            {'name' : 'web:adv/adsense'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://as\.casalemedia\.com/sd',
        'entities' : [
            {'name' : 'web:parking/fastparknet'}
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^http://userapi\.com/js/api/openapi\.js',
        'entities' : [
            {'name' : 'web:social/vk'}
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^https://apis\.google\.com/js/plusone\.js',
        'entities' : [
            {'name' : 'web:social/googleplus'}
        ]
    },
    {'type': RULETYPE_REGEXP, 'text': '^//vk\.com/js/api/openapi\.js',
     'entities': [
         {'name': 'web:social/vk'}
     ]
     },

    {'type' : RULETYPE_REGEXP, 'text' : '^http://reformal\.ru/tab\.js',
        'entities' : [
            {'name' : 'web:widgets:reviews/reformalru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://www.ozon.ru/PartnerTwinerNew.aspx',
        'entities' : [
            {'name' : 'web:widgets/ozonru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://bn\.orthodoxy\.ru/show\.bn',
        'entities' : [
            {'name' : 'web:adv/orthodoxyru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://pogoda\.mail\.ru/informer/weather\.js(.*)',
        'entities' : [
            {'name' : 'web:widgets:weather/pogodamailru'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://js\.redtram\.com/n4p/',
        'entities' : [
            {'name' : 'web:adv/redtram'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://api\.recaptcha\.net/challenge',
        'entities' : [
            {'name' : 'web:widgets:captcha/recaptcha'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'https://www.google.com/recaptcha/api.js',
     'entities': [
         {'name': 'web:widgets:captcha/recaptcha'}
     ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://b2bcontext\.ru\/services\/advertisement\/getblock',
        'entities' : [
            {'name' : 'web:adv/b2bcontext'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'popunder.ru/popunder.php',
        'entities' : [
            {'name' : 'web:adv/popunder'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit',
        'entities' : [
            {'name' : 'web:widgets:translate/googletranslate'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://api.microsofttranslator.com/V1/Widget.svc/Embed',
        'entities' : [
            {'name' : 'web:widgets:translate/mstranslate'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://lingvo.yandex.ru/cgi-bin/lingvo.pl',
        'entities' : [
            {'name' : 'web:widgets:translate/yandexlingvo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://search.freefind.com/find.html',
        'entities' : [
            {'name' : 'web:widgets:search/freefindcom'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://nigma.ru/index.php',
        'entities' : [
            {'name' : 'web:widgets:search/nigmaru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.nigma.ru/index.php',
        'entities' : [
            {'name' : 'web:widgets:search/nigmaru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.translate.ru/rus/url/tran_url.asp',
        'entities' : [
            {'name' : 'web:widgets:translate/translateru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.translate.ru/url/wideTranslation.aspx',
        'entities' : [
            {'name' : 'web:widgets:translate/translateru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.lingvo.ru/lingvo/Translate.asp',
        'entities' : [
            {'name' : 'web:widgets:translate/lingvoru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.translate.ru/text.asp#tr_form',
        'entities' : [
            {'name' : 'web:widgets:translate/translateru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.specpoisk.ru',
        'entities' : [
            {'name' : 'web:widgets:search/specpoiskru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://nigma.ru',
        'entities' : [
            {'name' : 'web:widgets:search/nigmaru'}
        ]
    },


    {'type' : RULETYPE_REGEXP, 'text' : '^http://advbroker\.ru/html\.php',
        'entities' : [
            {'name' : 'web:adv/advbroker'}
        ]
    },


    {'type' : RULETYPE_EQUAL, 'text' : '/js/client/umiBasket.js',
        'entities' : [
            {'name' : 'web:cms/umicms'},
            {'name' : 'web:tech:lang/php'},
            {'name' : 'site:classify/webshop'}
        ]
    },

    {'type' : RULETYPE_REGEXP, 'text' : '^http://garu\.hit\.gemius\.pl/hmapxy\.js',
        'entities' : [
            {'name' : 'web:counter/gemius'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://(s7|s9)\.addthis\.com/js',
        'entities' : [
            {'name' : 'web:widgets:bookmark/addthis'}
        ]
    },


    {'type' : RULETYPE_REGEXP, 'text' : '^http://(mg|js)\.dt00\.net/js',
        'entities' : [
            {'name' : 'web:adv/marketgid'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://nnn\.novoteka\.ru/show\.cgi(.*)',
        'entities' : [
            {'name' : 'web:adv/novoteka'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'img\.dt00\.net/scripts',
        'entities' : [
            {'name' : 'web:adv/marketgid'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.google-analytics.com/urchin.js',
        'entities' : [
            {'name' : 'web:counter/ga'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://bs.yandex.ru/resource/watch.js',
        'entities' : [
            {'name' : 'web:counter/yametrika'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://autocontext.begun.ru/autocontext.js',
        'entities' : [
            {'name' : 'web:adv/begun'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://autocontext.begun.ru/autocontext2.js',
        'entities' : [
            {'name' : 'web:adv/begun'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://tools.spylog.ru/counter_cv.js',
        'entities' : [
            {'name' : 'web:counter/spylog'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://tools.spylog.ru/counter2.2.js',
        'entities' : [
            {'name' : 'web:counter/spylog'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://[a-z0-9]{1,5}\.[0-9]{1,4}\.spylog\.com/cnt(.*)',
        'entities' : [
            {'name' : 'web:counter/spylog'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.google.com/coop/cse/brand?form=cse-search-box&lang=ru',
        'entities' : [
            {'name' : 'web:widgets:search/googlecse'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://edge.quantserve.com/quant.js',
        'entities' : [
            {'name' : 'web:counter/quantcast'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://mc.parkad.ru/topper/j.js',
        'entities' : [
            {'name' : 'web:parking/repark'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://pics.rbc.ru/js/rbc_indices.js',
        'entities' : [
            {'name' : 'web:widgets:fin/rbcinformer'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://partner.googleadservices.com/gampad/google_service.js',
        'entities' : [
            {'name' : 'web:adv/adsense'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://download.skype.com/share/skypebuttons/js/skypeCheck.js',
        'entities' : [
            {'name' : 'web:widgets:phone/skype'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.google.ru/coop/cse/brand?form=cse-search-box&lang=ru',
        'entities' : [
            {'name' : 'web:widgets:search/googlecse'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://informer.gismeteo.Ru/flash/fcode.js',
        'entities' : [
            {'name' : 'web:widgets:meteo/gismeteo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://js.s.webvisor.ru/c.js',
        'entities' : [
            {'name' : 'web:counter/webvisor'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.google.com/coop/cse/brand?form=cse-search-box&lang=en',
        'entities' : [
            {'name' : 'web:widgets:search/googlecse'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://news.yandex.ru/common.js',
        'entities' : [
            {'name' : 'web:widgets:news/yandexnews'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.google-analytics.com/ga.js',
        'entities' : [
            {'name' : 'web:counter/ga'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.statcounter.com/counter/counter.js',
        'entities' : [
            {'name' : 'web:counter/statcounter'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://scripts.mycounter.com.ua/counter2.0.js',
        'entities' : [
            {'name' : 'web:counter/mycountercomua'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://content.videoclik.ru/rbn.js',
        'entities' : [
            {'name' : 'web:adv/videoclick'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://odnaknopka.ru/ok2.js',
        'entities' : [
            {'name' : 'web:widgets:bookmark/odnaknopka'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://informer.gismeteo.Ru/js/showtlist.js',
        'entities' : [
            {'name' : 'web:widgets:meteo/gismeteo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://informer.gismeteo.Ru/js/ldata.js',
        'entities' : [
            {'name' : 'web:widgets:meteo/gismeteo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://img.gismeteo.ru/flash/fcode.js',
        'entities' : [
            {'name' : 'web:widgets:meteo/gismeteo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://informer.gismeteo.ru/html/js/showtlist_new.js',
        'entities' : [
            {'name' : 'web:widgets:meteo/gismeteo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://informer.gismeteo.ru/html/js/ldata_new.js',
        'entities' : [
            {'name' : 'web:widgets:meteo/gismeteo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://informer.gismeteo.ru/flash/fcode.js',
        'entities' : [
            {'name' : 'web:widgets:meteo/gismeteo'}
        ]
    },

    # Rule matcher
    {'type' : RULETYPE_REGEXP, 'text' : '^http://ajax\.googleapis\.com/ajax/libs(.*)',
        'entities' : [
            {'name' : 'web:cdn/googleapis'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^http://yabs\.yandex\.ru/show/(.*)',
        'entities' : [
            {'name' : 'web:adv/yanarod'}
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'www/delivery/ag.php',
        'entities' : [
            {'name' : 'web:adv/openx'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '/bitrix/js/main/cphttprequest.js',
        'entities' : [
            {'name' : 'web:cms/bitrix'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '/engine/ajax/dle_ajax.js',
        'entities' : [
            {'name' : 'web:cms/dle'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'http://api-maps\.yandex\.ru/\?',
        'entities' : [
            {'name' : 'web:maps/yandex'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'http://maps\.google\.com/maps\?file=api',
        'entities' : [
            {'name' : 'web:maps/google'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/prototype\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/prototype'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/SpryMenuBar\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/spry'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/jquery(\.|\-)(min|latest)\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/jquery'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/jquery(\.dataTables\.|\-)(min|latest)\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/jquerydatatables'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/jquery\-ui\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/jqueryui'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/jquery\-ui\-[0-9a-z\-\.]{1,20}\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/jqueryui'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/sifr\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/sifr'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/jquery\-[0-9\.\-]{1,8}\.min\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/jquery'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/jquery\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/jquery'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/swfobject\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/swfobject'},
            {'name' : 'web:tech/flash'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/AC_RunActiveContent\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:tech/flash'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)drupal\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:cms/drupal'},
            {'name' : 'web:tech:lang/php'},

        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '((.*)|)mootools\-[1-9\.]{1,8}\-core\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:scripts/mootools'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)/dojo\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:script/dojotoolkit'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)scriptaculous\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:script/scriptaculous'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(.*)lightbox\.js(\?(.*)|(.*)|)',
        'entities' : [
            {'name' : 'web:script/lightbox'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '//mc.yandex.ru/metrica/watch.js',
        'entities' : [
            {'name' : 'web:counter/yametrika'}
        ]
    },
]
