from .consts import *

# Rules to match page links
HREF_COMPLEX_RULES = [
    {'type' : RULETYPE_REGEXP, 'text' : 'viewtopic\.php\?f=[0-9]{1,3}(|\&t=[0-9]{1,6})(|\&sid=[0-9a-z]{16,32})',
        'entities' : [
            {'name' : 'web:cms:forum/phpbb'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'viewtopic\.php\?f=[0-9]{1,3}(|\&t=[0-9]{1,6})',
        'entities' : [
            {'name' : 'web:cms:forum/phpbb'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : 'profile\.php\?mode=viewprofile\&u=[0-9]{1,6}',
        'entities' : [
            {'name' : 'web:cms:forum/phpbb'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^/wps/(|portal|link|wcm/connect)/(.*)',
        'entities' : [
            {'name' : 'web:cms/websphere'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '(about|catalog|classify)\.(aspx|asp)\?(c_no|ob_no|CatalogId)',
        'entities' : [
            {'name' : 'web:cms/optimizer'},
            {'name' : 'web:os/windows'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^/wp-content/uploads/',
        'entities' : [
            {'name' : 'web:cms/wordpress'},
            {'name' : 'web:tech:lang/php'},
        ]
    },

]
