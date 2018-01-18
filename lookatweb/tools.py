# -*- coding: utf-8 -*-

"""
Created on 26.11.2009

@author: ivbeg
"""
import dns.resolver, dns.exception
from bs4 import UnicodeDammit
import io
import pycurl
from urllib.parse import urlparse
import datetime

from .consts import SERVER_APACHE, DEFAULT_NAMESERVERS

class HttpHeaders:
    """Class of HTTP headers"""
    def __init__(self, data):
        self.raw = data
        self.headers = HttpHeaders.headers_to_dict(data)


    def get_header(self, key):
        """Returns header"""
        if key in self.headers:
            return self.headers[key]
        return None


    def get_content_type(self):
        """Returns type of content"""
        result = self.get_header('content-type')
        if result:
            parts = result.split(';', 1)
            return parts[0].strip()
        return None

    @staticmethod
    def headers_to_dict(data):
        """Converts raw HTTP response to the dict of headers"""
        if not data:
            return {}
        data = data.decode('utf8')
        lines = data.splitlines()
        result = {}

        for line in lines[1:]:
            if len(line) > 0:
                parts = line.split(':', 1)
                if len(parts) > 1:
                    name = parts[0].lower().strip()
                    value = parts[1].strip()
                    result[name] = value
                    if name == 'content-type':
                        parts = value.split(';')
                        result['__content_type'] = parts[0].strip()
                        if len(parts) > 1:
                            vals = parts[1].split('=')
                            name = vals[0].strip()
                            if name == 'charset' and len(vals) > 1:
                                result['__encoding'] = vals[1].lower().strip()
        return result

def decode_html(html_string):
    converted = UnicodeDammit(html_string)
    if not converted.str:
        raise UnicodeDecodeError("Failed to detect encoding, tried [%s]", ', '.join(converted.triedEncodings))
    return converted.str



def resolve_info(domain, qtype, servers=None):
    """Resolves domain info records"""
    ips = []
    resolver = dns.resolver.Resolver(configure=False)
    resolver.timeout = 3
    resolver.nameservers = servers if servers else DEFAULT_NAMESERVERS

    try:
        answers = resolver.query(domain, qtype)
    except dns.resolver.NoAnswer as ex:
        return ips
    except dns.exception.Timeout as ex:
        return ips
    except dns.resolver.NXDOMAIN as ex:
        return ips
    for answer in answers:
        ips.append(str(answer))#)
    return ips

def parseContentType(s):
    """Parses content-type string and returns list of parts"""
    parts = s.lower().split(';')
    plist = {}
    if len(parts) > 1:
        for p in parts[1:]:
                v = p.split('=', 1)
                if len(v) > 1:
                    plist[v[0].strip()] = v[1].strip()
                else:
                    plist[v[0].strip()] = None
    return (parts[0], plist)



def parse_server_header(s):
    """Returns server parsed to modules"""
    result = {}
    parts = s.split('/', 1)
    server = parts[0].strip()
    if len(parts) == 1:
        result = {'server' : server}
        return result
    else:
        result = {'server' : server}
        modules = []
        vals = parts[1].split()
        version = vals[0]
        result['version'] = version
        if server == SERVER_APACHE:
            for val in vals[1:]:
                if len(val) > 1 and val[0] == '(' and val[-1] == ')':
                    result['os'] = val.lstrip('(').rstrip(')')
                else:
                    modp = val.split('/', 1)
                    if len(modp) == 1:
                        modules.append({'name' : val})
                    else:
                        modules.append({'name' : modp[0], 'version' : modp[1]})

        fixed = []
        gotK = False
        for i in range(0, len(modules)):
            m = modules[i]
            if 'version' not in m and m['name'][0] == '(':
                gotK = True
            elif gotK and m['name'][-1] == ')':
                result['os'] = ' '.join([modules[i-1]['name'], modules[i]['name']]).lstrip('(').rstrip(')')
                gotK = False
            else:
                fixed.append(m)
        result['modules'] = fixed
#       print parts
    return result


def parse_powered_by(s):
    """Parses x-powered by and returns dict of values"""
    parts = s.split('/', 1)
    result = {'name' : parts[0], 'version' : parts[1]} if len(parts) > 1 else {'name' : s}
    return result

def url_to_host(url):
    """Converts absolute URL to parsed hostname"""
    h = urlparse(url).hostname
    parts = h.split('.')
    parts.reverse()
    v = {'full' : h, 'rev' : ('.'.join(parts)), 'parts': {}, 'dl' : len(parts)}
    for i in range(0, len(parts), 1):
        v['parts']['l%d' %(i)]  = parts[i]
    return v


def fetch_page(url):
    """Fetches page"""
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    b = io.BytesIO()
    h = io.BytesIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.MAXREDIRS, 5)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
    c.perform()

    realurl = c.getinfo(pycurl.EFFECTIVE_URL)

    data = b.getvalue()
    headers = HttpHeaders.headers_to_dict(h.getvalue())

    status = c.getinfo(pycurl.HTTP_CODE)
    c.close()
    return status, headers, realurl, data



def prepareError(errorcode, results, resdata=None):
    errors = {'error:crawler' : errorcode}
    if not resdata:
        resdata = {'crawler:processed' : datetime.datetime.now().isoformat()}
    resdata.update(errors)
    results.update(errors)
    return (results, resdata)

