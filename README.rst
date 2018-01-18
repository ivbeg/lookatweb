
About Lookatweb
=================

Lookatweb is web technology identification library and cli tool. It's still incomplete, but it's free, open and ready to be reused. It
supports many CMS, scripts and so on.

Features
========

* Supports data extraction from web pages, dns records and
* Supports 356 page/site features using more than 400 patterns


Limitations
===========

* No description to the technologies. Need some kind of knowledge base
* Not so fast as should be, regular expressions actually slow down any process. Will be rewritten in future
* Pattern library is incomplete and outdated for inner scripts
* Not yet implemented "candidate tech identification"

Command-line tool
=================
Usage: weblooker.py [URL or DOMAIN]...


Examples
========

Extracts information about gov.uk website
    python weblooker.py gov.uk

Extract information from Russian news website CNews
    python weblooker.py cnews.ru


How to use library
==================

Extracts features from 'gov.uk' website
    >>> from lookatweb import Analyzer
    >>> an = Analyzer()
    >>> an.match_site('gov.uk')
{'site:info/cookiesupport': 1, 'page:encoding/utf8': 1, 'site:info/returnslength': 1, 'site:info/appleicon': 4, 'site:info/favicon': 1, 'web:server/nginx': 1, 'page:meta/description': 1, 'site:info/opensearch': 1, 'site:info/csssupport': 7, 'site:info/search': 1}

Extracts features from each website or domain from 'list.txt'
    >>> from lookatweb import Analyzer
    >>> an = Analyzer()
    >>> an.match_sitelist('list.txt')

Collects data from web site and returns raw data for future matching. Extracted info stored in profiles for dns, web and whois and raw data also available and prints data from DNS profile
    >>> from lookatweb.collector import collect_site_data
    >>> data = collect_site_data('gov.uk', getweb=True, getdns=True)
    >>> print(data[0]['profile:dns'])
{'mx': [], 'a': ['23.235.33.144', '23.235.37.144'], 'txt': ['"v=spf1 -all"'], 'aaaa': [], 'ns': ['auth00.ns.de.uu.net.', 'ns0.ja.net.', 'ns1.surfnet.nl.', 'ns2.ja.net.', 'ns4.ja.net.', 'auth50.ns.de.uu.net.', 'ns3.ja.net.'], 'cname': [], 'soa': ['ns0.ja.net. operations.ja.net. 2018011760 28800 7200 3600000 14400']}
    >>> data = collect_site_data('infoculture.ru', getweb=True, getdns=True)
    >>> print(data[0]['profile:dns'])
{'mx': ['10 ALT4.ASPMX.L.GOOGLE.COM.', '1 ASPMX.L.GOOGLE.COM.', '10 ALT3.ASPMX.L.GOOGLE.COM.', '5 ALT2.ASPMX.L.GOOGLE.COM.', '5 ALT1.ASPMX.L.GOOGLE.COM.'], 'a': ['88.198.110.211'], 'txt': ['"detectify-verification=774b0f659d549ce5300426c13df65642"'], 'aaaa': [], 'ns': ['ns2.nameself.com.', 'ns1.nameself.com.'], 'cname': [], 'soa': ['ns1.nameself.com. support.regtime.net. 1510060906 10800 900 604800 10800']}



Requirements
============
* Python3 https://www.python.org
* click https://github.com/pallets/click
* lxml http://lxml.de/
* BeautifulSoup4 https://www.crummy.com/software/BeautifulSoup/
* PyCurl http://pycurl.io/
* dnspython http://www.dnspython.org/

