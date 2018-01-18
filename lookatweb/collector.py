# -*- coding: utf-8 -*-

import sys
import datetime
import zlib
from lxml.html import html5parser, soupparser, fromstring


from .consts import *
from .tools import prepareError, resolve_info, parseContentType, fetch_page, parse_server_header, parse_powered_by, url_to_host
from .htmltools import tags_to_array, links_to_array, innerscripts_to_array, forms_to_array


NS_CMDS = ['A', 'AAAA', 'NS', 'SOA', 'TXT', 'CNAME']

def collect_dns_data(domain):
    """Collects dns information about host"""
    results = {}
    # Normalized domain required to make MX requests
    norm_domain = '.'.join(domain.split('.')[1:]) if domain.split('.', 1)[0] == 'www' else domain
    results['mx'] = resolve_info(norm_domain, 'MX')
    for cmd in NS_CMDS:
        results[cmd.lower()] = resolve_info(domain, cmd)
    return results

def collect_web_data(domain):
    """Collects information after web site analysis"""
    results = {}
    url = 'http://' + domain
    try:
        (status, headers, realurl, data) = fetch_page(url)
    except KeyboardInterrupt:
#    except pycurl.error:
        return prepareError(ERROR_URLGETERROR, results)

    encoding = None         # Default encoding is UTF-8
    if 'content-type' in headers:
        ptypr, plist = parseContentType(headers['content-type'])
        if 'charset' in plist:
                results['page:enc:server'] = plist['charset']
                encoding = results['page:enc:server']

    resdata = {'crawler:processed' : datetime.datetime.now().isoformat(), 'page:data' : zlib.compress(data, 9), 'page:headers': zlib.compress(repr(headers).encode('utf8'), 9)}
    try:
        encoding ='utf-8'
#        edata = decode_html(data) #.decode(encoding, 'ignore')
    except KeyboardInterrupt:
        return prepareError(ERROR_ENCODING, results, resdata)
    try:
        p = fromstring(data)
    except KeyboardInterrupt:
        try:
            p = html5parser.fromstring(data)
        except KeyboardInterrupt:
            p = soupparser.fromstring(data)
            return prepareError(ERROR_PARSEERROR, results, resdata)

    # Setting basic properties
    results['site:url'] =  url
    results['site:host'] = url_to_host(url)
    results['site:realurl'] = realurl
    results['site:realhost'] = url_to_host(realurl)
    results['page:status'] = status

    hders = []
    for k, v in list(dict(headers).items()):
        try:
            hders.append({'name' : k, 'value' : v})
        except KeyboardInterrupt:
            pass    # Do nothing
    results['web:page:headers'] = hders

    # Process blocks of tags
    results['page:scripts'] = tags_to_array(p, tagname='script', attrlist=['type', 'src'], filter='src', distinct='src')
    results['page:images'] = tags_to_array(p, tagname='img', attrlist=['alt', 'title', 'width', 'height', 'src'], filter='src', distinct='src')
    results['page:meta'] = tags_to_array(p, tagname='meta', attrlist=['http-equiv', 'content',  'name', 'property'], filter=None, distinct=None)
    results['page:headlinks'] = tags_to_array(p, tagname='link', attrlist=['rel', 'type', 'title', 'href', 'media'], filter=None, distinct=None)
    results['page:iframes'] = tags_to_array(p, tagname='iframe', attrlist=['name', 'src'], filter=None, distinct=None)
    results['page:embeds'] = tags_to_array(p, tagname='embed', attrlist=['src', 'pluginspage', 'type'], filter=None, distinct=None)
    results['page:objects'] = tags_to_array(p, tagname='object', attrlist=['codetype', 'classid', 'code', 'codebase', 'type', 'data'], filter=None, distinct=None)
    results['page:forms'] = forms_to_array(p)
    results['page:applets'] = tags_to_array(p, tagname='applet', attrlist=['code', 'codebase', 'src', 'alt', 'title', 'name'], filter=None, distinct=None)
    results['page:inscripts'] = innerscripts_to_array(p)
    results['page:links'] = links_to_array(p)

    # Processing header keys
    if SERVER_KEY in list(headers.keys()):
        server = parse_server_header(headers[SERVER_KEY])
        results['hdr:server'] = server

    if POWERED_BY_KEY in list(headers.keys()):
        s = parse_powered_by(headers[POWERED_BY_KEY])
        results['hdr:poweredby'] = s

    return (results, resdata)

#def collect_whois_data(domain):
#    server = get_server_by_domain(domain)
#    data =  get_whois_rec(server.name, domain)
#    data = ""
#    results = {}
#    results['whois:fields'] = server.parse(domain, data)
#    return (results, data)


def collect_site_data(domain, getdns=True, getweb=True, getwhois=False):
    """Extracts all data about domain"""
    resdata = {}
    results = {'profiles' : {'dns' : False, 'web' : False, 'whois' : False}}
    try:
        results['network:addr:ipv4'] = resolve_info(domain, 'A')
    except KeyboardInterrupt:
        res = prepareError(ERROR_NOTRESOLVED, results)
        return  (res[0], res[1])
    if getdns:
        results['profile:dns'] = collect_dns_data(domain)
        results['profiles']['dns'] = True
    if getweb:
        res, resdata = collect_web_data(domain)
        results['profile:web'] = res
        results['profiles']['web'] = True
#    if getwhois:
#        wres, wdata = collect_whois_data(domain)
#        results['profile:whois'] = wres
#        results['profiles']['whois'] = True
    return (results, resdata)






if __name__ == "__main__":
    results, resdata = collect_site_data(sys.argv[1], getdns=True, getweb=True, getwhois=True)
