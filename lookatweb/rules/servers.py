from .consts import *


# Rules to match web servers
SERVER_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'Apache',
        'entities' : [
            {'name' : 'web:server/apache'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'nginx',
        'entities' : [
            {'name' : 'web:server/nginx'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Microsoft-IIS',
        'entities' : [
            {'name' : 'web:server/iis'},
            {'name' : 'web:os/windows'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ZX_Spectrum',
        'entities' : [
            {'name' : 'web:server/yandex_zx'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'DataPalm',
        'entities' : [
            {'name' : 'web:server/datapalm'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Lotus-Domino',
        'entities' : [
            {'name' : 'web:server/lotusdomino'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'uServ',
        'entities' : [
            {'name' : 'web:server/userv'},
            {'name' : 'web:cms/ucoz'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Jino.ru',
        'entities' : [
            {'name' : 'web:server/jinoru'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'domainserver',
        'entities' : [
            {'name' : 'web:parking/google'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'lighttpd',
        'entities' : [
            {'name' : 'web:server/lighttpd'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Apache-Coyote',
        'entities' : [
            {'name' : 'web:server/tomcat'},
            {'name' : 'web:tech:lang/java'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Zope',
        'entities' : [
            {'name' : 'web:server/zope'},
            {'name' : 'web:tech:lang/python'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'CommuniGatePro',
        'entities' : [
            {'name' : 'web:server/communigate'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : '0W',
        'entities' : [
            {'name' : 'web:server/0w'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Sun-ONE-Web-Server',
        'entities' : [
            {'name' : 'web:server/sunone'},
            {'name' : 'web:tech:lang/java'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'IBM_HTTP_Server',
        'entities' : [
            {'name' : 'web:server/ibmhttpd'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'squid',
        'entities' : [
            {'name' : 'web:server/squid'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'IBM_HTTP_SERVER',
        'entities' : [
            {'name' : 'web:server/ibmhttpd'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Resin',
        'entities' : [
            {'name' : 'web:server/resin'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'WebSphere Application Server',
        'entities' : [
            {'name' : 'web:server/websphere'}
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '^Mongrel(.*)$',
        'entities' : [
            {'name' : 'web:server/mongrel'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'LiteSpeed',
        'entities' : [
            {'name' : 'web:server/litespeed'}
        ]
    },
]


# Operating system matching rules
OS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'Windows',
        'entities' : [
            {'name' : 'web:os/windows'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Unix',
        'entities' : [
            {'name' : 'web:os/unix'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Linux',
        'entities' : [
            {'name' : 'web:os/linux'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'FreeBSD',
        'entities' : [
            {'name' : 'web:os/freebsd'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'CentOS',
        'entities' : [
            {'name' : 'web:os/centos'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Debian',
        'entities' : [
            {'name' : 'web:os/debian'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Fedora',
        'entities' : [
            {'name' : 'web:os/fedora'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Red Hat',
        'entities' : [
            {'name' : 'web:os/redhat'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Ubuntu',
        'entities' : [
            {'name' : 'web:os/ubuntu'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ASPLinux',
        'entities' : [
            {'name' : 'web:os/asplinux'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Red-Hat/Linux',
        'entities' : [
            {'name' : 'web:os/redhat'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Hat Linux',
        'entities' : [
            {'name' : 'web:os/redhat'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Linux/SuSE',
        'entities' : [
            {'name' : 'web:os/suse'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'NETWARE',
        'entities' : [
            {'name' : 'web:os/netware'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Darwin',
        'entities' : [
            {'name' : 'web:os/darwin'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Gentoo',
        'entities' : [
            {'name' : 'web:os/gentoo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Gentoo/Linux',
        'entities' : [
            {'name' : 'web:os/gentoo'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'UNIX',
        'entities' : [
            {'name' : 'web:os/unix'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'HP-UX',
        'entities' : [
            {'name' : 'web:os/hpux'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'OS/2',
        'entities' : [
            {'name' : 'web:os/os2'}
        ]
    },
]



# Rules to match server modules
SERVERMODS_RULES = [
    {'type' : RULETYPE_EQUAL, 'text' : 'PHP',
        'entities' : [
            {'name' : 'web:tech:lang/php'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_ssl',
        'entities' : [
            {'name' : 'web:tech:module/mod_ssl'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'OpenSSL',
        'entities' : [
            {'name' : 'web:tech:module/openssl'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Suhosin-Patch',
        'entities' : [
            {'name' : 'web:tech:module/suhosin'},
            {'name' : 'web:tech:lang/php'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'with', 'action' : ACTION_IGNORE,
        'entities' : [
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'FrontPage',
        'entities' : [
            {'name' : 'web:tech:module/frontpage'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'DAV',
        'entities' : [
            {'name' : 'web:tech:module/dav'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_bwlimited',
        'entities' : [
            {'name' : 'web:tech:module/mod_bwlimited'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'rus',
        'entities' : [
            {'name' : 'web:tech:module/rus'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_auth_passthrough',
        'entities' : [
            {'name' : 'web:tech:module/mod_auth_passthrough'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_perl',
        'entities' : [
            {'name' : 'web:tech:module/mod_perl'},
            {'name' : 'web:tech:lang/perl'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Python',
        'entities' : [
            {'name' : 'web:tech:lang/python'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_python',
        'entities' : [
            {'name' : 'web:tech:module/mod_python'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_fastcgi',
        'entities' : [
            {'name' : 'web:tech:module/mod_fastcgi'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_dp',
        'entities' : [
            {'name' : 'web:tech:module/mod_dp'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_gzip',
        'entities' : [
            {'name' : 'web:tech:module/mod_gzip'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Ruby',
        'entities' : [
            {'name' : 'web:tech:lang/ruby'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_ruby',
        'entities' : [
            {'name' : 'web:tech:module/mod_ruby'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_dp20',
        'entities' : [
            {'name' : 'web:tech:module/mod_dp20'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_log_bytes',
        'entities' : [
            {'name' : 'web:tech:module/mod_log_bytes'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Perl',
        'entities' : [
            {'name' : 'web:tech:lang/Perl'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_deflate',
        'entities' : [
            {'name' : 'web:tech:module/mod_deflate'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_jk',
        'entities' : [
            {'name' : 'web:tech:module/mod_jk'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_throttle',
        'entities' : [
            {'name' : 'web:tech:module/mod_throttle'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_psoft_traffic',
        'entities' : [
            {'name' : 'web:tech:module/mod_psoft_traffic'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_accel',
        'entities' : [
            {'name' : 'web:tech:module/mod_accel'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'SVN',
        'entities' : [
            {'name' : 'web:tech:module/mod_svn'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_defer',
        'entities' : [
            {'name' : 'web:tech:module/mod_defer'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'GNU',
        'entities' : [
            {'name' : 'web:tech:module/gnu'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Phusion_Passenger',
        'entities' : [
            {'name' : 'web:tech:module/phusion_passenger'},
            {'name' : 'web:tech:lang/ruby'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_tsunami',
        'entities' : [
            {'name' : 'web:tech:module/mod_tsunami'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Resin',
        'entities' : [
            {'name' : 'web:tech:module/resin'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'PHP-CGI',
        'entities' : [
            {'name' : 'web:tech:module/phpcgi'},
            {'name' : 'web:tech:lang/php'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_wsgi',
        'entities' : [
            {'name' : 'web:tech:module/mod_wsgi'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_mono',
        'entities' : [
            {'name' : 'web:tech:module/mod_mono'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_scgi',
        'entities' : [
            {'name' : 'web:tech:module/mod_scgi'},
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_auth_pgsql',
        'entities' : [
            {'name' : 'web:tech:module/mod_auth_pgsql'},
            {'name' : 'web:tech:db/postgresql'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_macro',
        'entities' : [
            {'name' : 'web:tech:module/mod_macro'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Ben-SSL',
        'entities' : [
            {'name' : 'web:tech:module/benssl'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_accounting',
        'entities' : [
            {'name' : 'web:tech:module/mod_accounting'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'AuthPG',
        'entities' : [
            {'name' : 'web:tech:module/authpg'},
            {'name' : 'web:tech:db/postgresql'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_webapp',
        'entities' : [
            {'name' : 'web:tech:module/mod_webapp'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_autoindex_color',
        'entities' : [
            {'name' : 'web:tech:module/mod_autoindex_color'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'ApacheJServ',
        'entities' : [
            {'name' : 'web:tech:module/apachejserv'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'AuthMySQL',
        'entities' : [
            {'name' : 'web:tech:module/authmysql'},
            {'name' : 'web:tech:db/mysql'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_ipdrop',
        'entities' : [
            {'name' : 'web:tech:module/mod_ipdrop'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod-xslt',
        'entities' : [
            {'name' : 'web:tech:module/mod_xslt'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'mod_gnutls',
        'entities' : [
            {'name' : 'web:tech:module/mod_gnutls'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'Sun-ONE-ASP',
        'entities' : [
            {'name' : 'web:tech:module/sunoneasp'}
        ]
    },
    {'type' : RULETYPE_EQUAL, 'text' : 'proxy_html',
        'entities' : [
            {'name' : 'web:tech:module/proxy_html'}
        ]
    },
]

