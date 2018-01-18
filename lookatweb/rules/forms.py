from .consts import *

# Rules to match forms actions
FORMS_ACTION_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.hristianstvo.ru/search',
        'entities' : [
            {'name' : 'web:widgets:search/hristianstvoru'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.gramota.ru/dic/rsearch.php3',
        'entities' : [
            {'name' : 'web:widgets:search/gramotaru'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.gramota.ru/slovari/dic/',
        'entities' : [
            {'name' : 'web:widgets:search/gramotaru'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://dic.gramota.ru/search.php',
        'entities' : [
            {'name' : 'web:widgets:search/gramotaru'},
        ]
    },

    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.hristianstvo.ru/search',
        'entities' : [
            {'name' : 'web:widgets:search/hristianstvoru'},
        ]
    },

    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.tigvote.ru/cgi-bin/vote/tigvote.cgi',
        'entities' : [
            {'name' : 'web:widgets:voting/tigvote'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.maillist.ru/cgi/ml_fs.cgi',
        'entities' : [
            {'name' : 'web:widgets:feeds/maillistru'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.maillist.ru/cgi/gsps.cgi',
        'entities' : [
            {'name' : 'web:widgets:feeds/maillistru'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'http://groups.yahoo.com/subscribe/',
        'entities' : [
            {'name' : 'web:widgets:feeds/yahoogroups'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.rss2email.ru/ready.asp',
        'entities' : [
            {'name' : 'web:widgets:feeds/rss2emailru'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://feedburner.google.com/fb/a/mailverify',
        'entities' : [
            {'name' : 'web:widgets:feeds/feedburneremail'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://feedburner.com/fb/a/mailverify',
        'entities' : [
            {'name' : 'web:widgets:feeds/feedburneremail'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.feedburner.com/fb/a/emailverify',
        'entities' : [
            {'name' : 'web:widgets:feeds/feedburneremail'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'https://partner.r01.ru/AUCTION/?refid=203',
        'entities' : [
            {'name' : 'web:parking/r01'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.tutu.ru/search_universal.php',
        'entities' : [
            {'name' : 'web:widgets/tuturu'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://smartresponder.ru/subscribe.html',
        'entities' : [
            {'name' : 'web:feeds/smartresponder'},
        ]
    },

    {'type' : RULETYPE_EQUAL, 'text' : 'https://www.paypal.com/cgi-bin/webscr',
        'entities' : [
            {'name' : 'web:widgets/paypal'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '/netcat/modules/auth/',
        'entities' : [
            {'name' : 'web:cms/netcat'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '/search/search_do',
        'entities' : [
            {'name' : 'web:cms/umicms'},
            {'name' : 'web:tech:lang/php'},
        ]
    },

    {'type' : RULETYPE_EQUAL, 'text' : 'modules.php?name=Your_Account',
        'entities' : [
            {'name' : 'web:cms/phpnuke'},
            {'name' : 'web:tech:lang/php'},
        ]
    },


    {'type' : RULETYPE_EQUAL, 'text' : '/netcat/modules/poll/',
        'entities' : [
            {'name' : 'web:cms/netcat'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'netcat/modules/netshop/post.php',
        'entities' : [
            {'name' : 'web:cms/netcat'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '/netcat/add.php',
        'entities' : [
            {'name' : 'web:cms/netcat'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'index.php?option=com_search',
        'entities' : [
            {'name' : 'web:cms/joomla'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://subscribe.ru/member/quick',
        'entities' : [
            {'name' : 'web:widgets:feeds/subscriberu'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://content.mail.ru/cgi-bin/subscribe.cgi',
        'entities' : [
            {'name' : 'web:widgets:feeds/mailrusubscribe'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.google.ru/custom',
        'entities' : [
            {'name' : 'web:widgets:search/googlecse'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.google.com/custom',
        'entities' : [
            {'name' : 'web:widgets:search/googlecse'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.google.ru/cse',
        'entities' : [
            {'name' : 'web:widgets:search/googlecse'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.google.com/cse',
        'entities' : [
            {'name' : 'web:widgets:search/googlecse'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://yandex.ru/sitesearch',
        'entities' : [
            {'name' : 'web:widgets:search/yandexsitesearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.yandex.ru/yandsearch',
        'entities' : [
            {'name' : 'web:widgets:search/yandexsearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.yandex.ru:8081/yandsearch',
        'entities' : [
            {'name' : 'web:widgets:search/yandexsearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://yandex.ru/yandsearch/',
        'entities' : [
            {'name' : 'web:widgets:search/yandexsearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://narod.yandex.ru/cgi-bin/yandsearch',
        'entities' : [
            {'name' : 'web:widgets:search/yandexsearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://domains.googlesyndication.com/apps/domainpark/results.cgi',
        'entities' : [
            {'name' : 'web:parking/google'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.rambler.ru/cgi-bin/rambler_search',
        'entities' : [
            {'name' : 'web:widgets:search/ramblersearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://search.rambler.ru/srch',
        'entities' : [
            {'name' : 'web:widgets:search/ramblersearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://search.rambler.ru/cgi-bin/rambler_search',
        'entities' : [
            {'name' : 'web:widgets:search/ramblersearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://search.rambler.ru/cgi-bin/rambler_search',
        'entities' : [
            {'name' : 'web:widgets:search/ramblersearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.rambler.ru/srch',
        'entities' : [
            {'name' : 'web:widgets:search/ramblersearch'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.ozon.ru',
        'entities' : [
            {'name' : 'web:widgets:search/ozonru'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'http://www.ozon.ru',
        'entities' : [
            {'name' : 'web:widgets:search/ozonru'},
        ]
    },

]
