#!/usr/bin/env python
import time

from urllib.parse import urlparse
from .collector import collect_site_data
from .matcher import *
from .rules import *


class Analyzer:
    """Analyzer class that helps to extract page information"""
    def __init__(self):
        pass


    def getDnsMatcher(self):
        """Returns rule processor for dns related rules"""
        matcher = RulesRegistry()
        matcher.register('r:dns:mailhost', DNS_MX_RULES, key='mx')
        return matcher

    def getWhoisMatcher(self):
        """Returns rule processor for whois related rules"""
        matcher = RulesRegistry()
        matcher.register('r:net:whois_fields', WHOIS_FIELDS_RULES, key='whois:fields', namekey='uri', valuekey='value', payload=['name', 'uri', 'value'], tolower=True)
        matcher.register('r:net:whois_org', WHOIS_ORG_RULES, key='fields', namekey='value', payload=['name', 'value'], tolower=True)
        matcher.register('r:net:whois_person', WHOIS_PERSON_RULES, key='fields', namekey='value', payload=['name', 'value'], tolower=True)
        return matcher


    def getMatchers(self):
        """Returns all rule processor with web related matching rules"""
        matcher = RulesRegistry()
        matcher.register('r:web:headers', HEADERS_RULES, key='web:page:headers', namekey='name', valuekey='value', payload=['name', 'value'])
        matcher.register('r:web:poweredby', POWEREDBY_RULES, key='hdr:poweredby', namekey='name', payload=['name',])
        matcher.register('r:web:server', SERVER_RULES, key='hdr:server', namekey='server', payload=['server',])
        matcher.register('r:web:servermods', SERVERMODS_RULES, key='hdr:server', subkey='modules', namekey='name', payload=['name',])
        matcher.register('r:web:extscripts', EXTSCRIPTS_RULES, key='page:scripts', subkey='list', namekey='src', payload=['src',])
        matcher.register('r:web:innerscripts', INSCRIPTS_RULES, key='page:inscripts', subkey='list', namekey='text', payload=['text',])
        matcher.register('r:web:scripts', SCRIPTS_RULES, key='page:scripts', subkey='list', namekey='src', payload=['fname',])
        matcher.register('r:web:meta', META_RULES, key='page:meta', subkey='list', namekey='name', valuekey='content', payload=['name', 'content'], tolower=True)
        matcher.register('r:web:metaprop', METAPROPERTY_RULES, key='page:metaprop', subkey='list', namekey='property', valuekey='content', payload=['property', 'content'], tolower=True)
        matcher.register('r:web:meta_copy', META_COPYRIGHT_RULES, passive=True)
        matcher.register('r:web:images', IMAGES_RULES, key='page:images', subkey='list', namekey='src', payload=['src',])
        matcher.register('r:web:headlinks_rel', HEADLINKS_RULES, key='page:headlinks', subkey='list', namekey='rel', valuekey='href', payload=['rel', 'href'], tolower=True)
        matcher.register('r:web:headlinks_type', HEADLINKS_TYPE_RULES, key='page:headlinks', subkey='list', namekey='type', valuekey='href', payload=['type', 'href'], tolower=True)
        matcher.register('r:web:styles', STYLE_RULES, passive=True)
        matcher.register('r:web:iframes', IFRAMES_RULES, key='page:iframes', subkey='list', namekey='src', payload=['src',])
        matcher.register('r:web:os', OS_RULES, key='hdr:server', namekey='os')
        matcher.register('r:web:forms_action', FORMS_ACTION_RULES, key='page:forms', subkey='list', namekey='action', payload=['method', 'action'], tolower=True)
        matcher.register('r:web:encoding', ENCODING_RULES, key='page:enc:server')
        matcher.register('r:web:cookie', COOKIE_RULES, passive=True)
        matcher.register('r:web:powered_cms', POWERED_CMS_RULES, passive=True)
        matcher.register('r:web:generator', GENERATOR_RULES, passive=True)
        matcher.register('r:web:object_clsid', OBJECTS_CLSID_RULES, key='page:objects', subkey='list', namekey='classid', payload=['classid', 'type', 'data'])
        matcher.register('r:web:object_type', OBJECTS_TYPE_RULES, key='page:objects', subkey='list', namekey='type', payload=['classid', 'type', 'data'])
        matcher.register('r:web:embed_src', EMBED_SRC_RULES, key='page:embeds', subkey='list', namekey='src', payload=['src'])
        matcher.register('r:web:object_data', OBJECTS_DATA_RULES, key='page:objects', subkey='list', namekey='data', payload=['classid', 'type', 'data'])
        matcher.register('r:net:domains_l1', L1_DOMAIN_RULES, key='site:host', subkey='parts', namekey='l0', valuekey='l1', payload=['l0', 'l1', 'l2', 'l3'])
        matcher.register('r:net:domains_ru', RU_DOMAINS_RULES, passive=True, payload=['l0', 'l1', 'l2'])
        matcher.register('r:net:domains_com', COM_DOMAINS_RULES, passive=True, payload=['l0', 'l1', 'l2'])
        matcher.register('r:net:domains_by', BY_DOMAINS_RULES, passive=True, payload=['l0', 'l1', 'l2'])
        matcher.register('r:net:domains_su', SU_DOMAINS_RULES, passive=True, payload=['l0', 'l1', 'l2'])

        netmatcher = RulesRegistry()
        netmatcher.register('r:net:ipv4', IP_RULES, key='network:addr:ipv4')
#        netmatcher.addmatcher(GeoIPMatcher(rid='r:net:ipv4_geo', rules=[], key='network:addr:ipv4'))

        return matcher, netmatcher


    def match_site(self, url, getDNS=False):
        """Processes one site by domain"""
        matcher, netmatcher = self.getMatchers()
        if getDNS:
            dnsmatcher = self.getDnsMatcher()
#        whoismatcher = self.getWhoisMatcher()

        results, resdata = collect_site_data(url, getdns=True, getwhois=True)
        res = netmatcher.match(results)
        if results:
            res.extend(matcher.match(results['profile:web']))
            if getDNS:
                res.extend(dnsmatcher.match(results['profile:dns']))
#            res.extend(whoismatcher.match(results['profile:whois']))
        vals = {}
        for item in res:
            for e in item['entities']:
                k = e['name']
                if k in list(vals.keys()):
                    vals[k] += 1
                else:
                    vals[k] = 1
        keys = list(vals.keys())
        keys.sort()
        return vals

    def match_sitelist(self, filename):
        """Processes list of websites from file"""
        matcher, netmatcher = self.getMatchers()
        f = open(filename, 'r')
        items = []
        for l in f:
            l = l.lower().strip()
            if l[0:4] == 'http:' or l[0:5] == 'https:':
                url = urlparse(l.strip()).hostname
            else:
                url = l.strip()
            results, resdata = collect_site_data(url, getdns=False)
            time.sleep(0.1)
            res = netmatcher.match(results)
            if 'profile:web' in results:
                res.extend(matcher.match(results['profile:web']))
            vals = {}
            for item in res:
                for e in item['entities']:
                    k = e['name']
                    if k in list(vals.keys()):
                        vals[k] += 1
                    else:
                        vals[k] = 1
            keys = list(vals.keys())
            keys.sort()
            items.append([l, keys])
        return items
