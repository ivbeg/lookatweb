# -*- coding: utf-8 -*-

from urllib.parse import urlparse

def tags_to_array(p, tagname, attrlist, filter=None, distinct=None):
    """Extracts list of tags into array"""
    keys = []
    res = []
    tags = p.xpath('//%s' %(tagname))

    for tag in tags:
        if filter and filter not in tag.attrib:
            continue
        if distinct and distinct in tag.attrib:
            if tag.attrib[distinct] in keys:
                continue
            else:
                keys.append(tag.attrib[distinct])
        v = {}
        for k in attrlist:
            if k in tag.attrib:
                v[k] = tag.attrib[k]
                # Dirty quick hack
                if k == 'src':
                    o = urlparse(tag.attrib[k])
                    filename = o.path.rsplit('/', 1)
                    filename = filename[1] if len(filename) > 1 else filename[0]
                    v['fname'] = filename
        res.append(v)
    return {'total' : len(res), 'list' : res}


def innerscripts_to_array(p):
    """Extracts inner scripts from page"""
    res = []
    all = p.xpath('//script')
    for tag in all:
        if 'src' in tag.attrib:
            continue
        else:
            item = {'text' : tag.text_content()}
            if 'type' in tag.attrib: item['type'] = tag.attrib['type']
            res.append(item)
    return {'total' : len(res), 'list' : res}

def links_to_array(p):
    """Extract links from page"""
    res = []
    all = p.xpath('//a')
    for tag in all:
        if 'href' not in tag.attrib:
            continue
        else:
            item = {'href' : tag.attrib['href'], 'text' : tag.text_content()}
            res.append(item)
    return {'total' : len(res), 'list' : res}


def forms_to_array(p):
    """Extracts web forms from page"""
    res = []
    formattrlist = ['name', 'id', 'action', 'class', 'method']
    inputattrlist = ['name', 'id', 'type', 'class', 'value', 'src']
    textarealist = ['name', 'id']
    buttonlist = ['name', 'id', 'value']
    tagnames = [('input', inputattrlist), ('textarea', textarealist), ('button', buttonlist)]
    allforms = p.xpath('//form')
    for form in allforms:
        fkey = {}
        for k in formattrlist:
            if k in form.attrib:
                fkey[k] = form.attrib[k]#
        for tag in form.iterdescendants():
            if not hasattr(tag, 'tag'): continue
            for tagname, tlist in tagnames:
                if tag.tag == tagname:
                    if tagname not in fkey:   fkey[tagname] = []
                    tval = {}
                    for k in tlist:
                        if k in tag.attrib:
                            tval[k] = tag.attrib[k]
                    fkey[tagname].append(tval)
        res.append(fkey)
    return {'total' : len(res), 'list' : res}

