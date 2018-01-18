from .consts import *

# Rules to process generator meta
GENERATOR_RULES = [
    {'type' : RULETYPE_REGEXP, 'text' : 'Joomla!',
        'entities' : [
            {'name' : 'web:cms/joomla'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^PHP-Nuke',
        'entities' : [
            {'name' : 'web:cms/phpnuke'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'RBC Contents',
     'entities' : [
         {'name' : 'web:cms/rbccontents'},
         {'name' : 'web:tech:lang/php'},
         ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^edogsCMS',
        'entities' : [
            {'name' : 'web:cms/edogs'},
            {'name' : 'web:cms/phpnuke'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'Microsoft Frontpage',
        'entities' : [
            {'name' : 'web:editor/msfrontpage'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'Microsoft Word',
        'entities' : [
            {'name' : 'web:editor/msword'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^(Wordpress|WordPress)',
        'entities' : [
            {'name' : 'web:cms/wordpress'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_FIND, 'text' : 'DataLife Engine',
        'entities' : [
            {'name' : 'web:cms/dle'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'MSHTML',
        'entities' : [
            {'name' : 'web:editor/mshtml_dll'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'Microsoft Visual Studio',
        'entities' : [
            {'name' : 'web:editor/msvs'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'Amiro\.CMS',
        'entities' : [
            {'name' : 'web:cms/amirocms'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Microsoft FrontPage Express 2\.0',
        'entities' : [
            {'name' : 'web:editor/frontpageexpress'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'TYPO3',
        'entities' : [
            {'name' : 'web:cms/typo3'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'Plone',
        'entities' : [
            {'name' : 'web:cms/plone'},
            {'name' : 'web:tech:lang/python'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'Movable Type Open Source',
        'entities' : [
            {'name' : 'web:cms/movtype'},
            {'name' : 'web:tech:lang/perl'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'vBulletin',
        'entities' : [
            {'name' : 'web:cms/vbulletin'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^CMS Danneo',
        'entities' : [
            {'name' : 'web:cms/danneocms'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^XOOPS',
        'entities' : [
            {'name' : 'web:cms/xoops'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^CMSimple',
        'entities' : [
            {'name' : 'web:cms/cmsimple'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^Mambo',
        'entities' : [
            {'name' : 'web:cms/mambo'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^Danneo CMS',
        'entities' : [
            {'name' : 'web:cms/danneocms'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^BinN S\.Builder',
        'entities' : [
            {'name' : 'web:cms/sbuilder'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'Movable Type Open Source',
        'entities' : [
            {'name' : 'web:cms/movtype'},
            {'name' : 'web:tech:lang/perl'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^Seditio by Neocrome',
        'entities' : [
            {'name' : 'web:cms/seditio'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^SLAED CMS',
        'entities' : [
            {'name' : 'web:cms/slaedcms'},
            {'name' : 'web:tech:lang/php'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^WebGUI',
        'entities' : [
            {'name' : 'web:cms/webgui'},
            {'name' : 'web:tech:lang/perl'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^CMS EDGESTILE SiteEdit',
        'entities' : [
            {'name' : 'web:cms/edgestile'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^EDGESTILE SiteEdit',
        'entities' : [
            {'name' : 'web:cms/edgestile'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Microsoft SharePoint',
        'entities' : [
            {'name' : 'web:cms/mssharepoint'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'BRUTTO CMS',
        'entities' : [
            {'name' : 'web:cms/bruttocms'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^InstantCMS',
        'entities' : [
            {'name' : 'web:cms/instantcms'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^Nucleus CMS',
        'entities' : [
            {'name' : 'web:cms/nucleuscms'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^MediaWiki',
        'entities' : [
            {'name' : 'web:cms:wiki/mediawiki'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^Joostina',
        'entities' : [
            {'name' : 'web:cms/joostina'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Blogger',
        'entities' : [
            {'name' : 'web:cms/blogger'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'blogger',
        'entities' : [
            {'name' : 'web:cms/blogger'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'MaxSite CMS',
        'entities' : [
            {'name' : 'web:cms/maxsitecms'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^NetObjects Fusion',
        'entities' : [
            {'name' : 'web:editor/netobjectsfusion'},
        ]
    },
]
