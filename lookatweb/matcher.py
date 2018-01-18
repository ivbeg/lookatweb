# -*- coding: utf-8 -*-
"""
Created on 01.12.2009

@author: ivbeg
"""
import re
#import pygeoip
from .rules.consts import *

class RulesRegistry:
    """Registry of rules"""
    def __init__(self):
        self.__rulemap = {}
        pass

    def map(self):
        """Возвращает набор правил"""
        return self.__rulemap

    def register(self, rid, rules=None, passive=False, key=None, subkey=None, namekey=None, valuekey=None, payload=None,
                 tolower=False):
        if not payload: payload = []
        self.__rulemap[rid] = RuleMatcher(self, rid, rules, passive, key, subkey, namekey, valuekey, payload, tolower)

    def addmatcher(self, matcher):
        self.__rulemap[matcher.rid] = matcher

    def register_dict(self, d):
        for k, v in list(d.items()):
            self.register(k, **v)

    def keymatch(self, key, name, value=None):
#       if key == 'innerscripts':
#           print name
        return self.__rulemap[key].match_text(name, value)

    def match(self, object):
        """Match results"""
        res = []
        for v in list(self.__rulemap.values()):
            res.extend(v.match_object(object))
        return res


    def getmap(self):
        return self.__rulemap

class RuleMatcher:
    def __init__(self, registry=None, rid=None, rules=None, passive=False, key=None, subkey=None, namekey=None,
                 valuekey=None, payload=None, tolower=False):
        if not payload: payload = []
        self.textrules = {}
        self.rerules = []
        self.findrules = {}
        self.wordrules = {}
        self.rid = rid
        self.registry = registry
        self.follow = True
        self.passive = passive
        self.payload = payload
        self.key = key
        self.subkey = subkey
        self.namekey = namekey
        self.valuekey= valuekey
        self.tolower = tolower
        if rules:
            self.prepareRules(rules)

    def prepareRules(self, rules):
        for rule in rules:
            if rule['type'] == RULETYPE_EQUAL:
                self.textrules[rule['text']] = rule
            elif rule['type'] == RULETYPE_REGEXP:
                rule['re'] = re.compile(rule['text'], re.I|re.M|re.L)
                self.rerules.append(rule)
            elif rule['type'] == RULETYPE_FIND:
                self.findrules[rule['text']] = rule
#           elif rule['type'] == RULETYPE_WORD:
#               self.wordrules[rule['text']] = rule

    def match_object(self, object):
        """Matches object data by provided scheme"""
        res = []
        if self.key:
            if self.key not in object:
                return []
            data = object[self.key]
            if self.subkey is not None and self.subkey in data:
                data = data[self.subkey]
            if type(data) == type([]):
                l = data
            else:
                l = [data]
            if self.namekey is None:
                for o in l:
                    r = self.match_text(o)
                    vals = {'value' : data}
                    if r:
                        for r0 in r:
                            if self.payload and 'payload' not in r0:
                                r0['payload'] = vals
                            res.append(r0)
                return res
            elif self.valuekey is None:
                for o in l:
                    r = self.match_text(o[self.namekey] if self.namekey in o else None)
                    if r:
                        vals = {}
                        if self.payload:
                            for k in self.payload:
                                if k in o: vals[k] = o[k]
                        for r0 in r:
                            if self.payload and 'payload' not in r0:
                                r0['payload'] = vals
                            res.append(r0)
                return res
            else:
                for o in l:
                    r = self.match_text(o[self.namekey] if self.namekey in o else None, o[self.valuekey] if self.valuekey in o else None)
                    if r:
                        vals = {}
                        if self.payload:
                            for k in self.payload:
                                if k in o: vals[k] = o[k]
                        for r0 in r:
                            if self.payload and 'payload' not in r0:
                                r0['payload'] = vals
                            res.append(r0)
                return res
        return []


    def match_text(self, text, value=None):
        """Rule matcher"""
        matches = []
        if not text:
            return matches
        if self.tolower: text = text.lower()
        if text in list(self.textrules.keys()):
            r = self.textrules[text]
            if 'action' in r:
                if r['action'] == ACTION_FOLLOW and 'matcherkey' in r:
                    res = self.registry.keymatch(r['matcherkey'], value)
        #           print '---SUB', r['matcherkey'], value, res
                    for item in res:
                        item['payload'] = {'value' : value}
                        matches.append(item)
                    if len(r['entities']) > 0:
                         matches.append({'rid' : self.rid, 'text' : r['text'], 'entities' : r['entities']})
                elif r['action'] == ACTION_IGNORE:
                    # Do nothing
                    pass
                else:
                    matches.append({'rid' : self.rid, 'text' : r['text'], 'entities' : r['entities']})
            else:
                matches.append({'rid' : self.rid, 'text' : r['text'], 'entities' : r['entities']})
#       print matches
#       if len(matches) > 0: return matches
        for k, r in list(self.findrules.items()):
            if text.find(k) > -1:
                if 'action' in r:
                    if r['action'] == ACTION_FOLLOW and 'matcherkey' in r:
                        res = self.registry.keymatch(r['matcherkey'], value)
                        for item in res:
                            item['payload'] = {'value' : value}
                            matches.append(item)
                        if len(r['entities']) > 0:
                            matches.append({'rid' : self.rid, 'text' : r['text'], 'entities' : r['entities']})
#                           return matches
                    elif r['action'] == ACTION_IGNORE:
                    # Do nothing
                        pass
                    else:
                        matches.append({'rid' : self.rid, 'text' : r['text'], 'entities' : r['entities']})
#                       return matches
                else:
                    matches.append({'rid' : self.rid, 'text' : r['text'], 'entities' : r['entities']})
#                   return matches
#       if matches: return matches
        for r in self.rerules:
            if r['re'].match(text):
                if 'action' in r:
                    if r['action'] == ACTION_FOLLOW and 'matcherkey' in r:
                        res = self.registry.keymatch(r['matcherkey'], value)
                        for item in res:
                            item['payload'] = {'value' : value}
                            matches.append(item)
                    elif  r['action'] == ACTION_IGNORE:
                        pass
                    else:
                        pass
                        matches.append({'rid' : self.rid, 'text' : r['text'], 'entities' : r['entities']})
                else:
                    matches.append({'rid' : self.rid, 'text' : r['text'], 'entities' : r['entities']})
        return matches


class GeoIPMatcher(RuleMatcher):
    def __init__(self, registry=None, rid=None, rules=None, passive=False, key=None, subkey=None, namekey=None,
                 valuekey=None, payload=None):
        if not payload: payload = []
        RuleMatcher.__init__(self, registry, rid, rules, passive, key, subkey, namekey, valuekey, payload, tolower=False)
        self.gip = pygeoip.GeoIP(r'data/GeoIP.dat')


    def match_text(self, text, value=None):
        matches = []
        c = self.gip.country_code_by_addr(text)
        if c :
            entities = [{'name' : 'geo:country:code/%s' %(c.lower())},]
            matches.append({'rid' : self.rid, 'text' : text, 'entities' : entities})
        return matches







def load_known_urls(filename, encoding='windows-1251'):
    u_rules = []
    t_rules = []
    f = open(filename, 'r')
    for line in f:
        parts = line.strip().split('\t')
        name = 'ku:%s' %(parts[0])
        if len(parts[2]) > 0:
            name = name + '/' + parts[2]
        if parts[1] == '2':
            u_rules.append({'type' : RULETYPE_EQUAL, 'text' : parts[3], 'entities' : [{'name' : name},]})
        elif parts[1] == '1':

            t_rules.append({'type' : RULETYPE_EQUAL, 'text' : parts[3], 'entities' : [{'name' : name},]})
    return {'urltext' : t_rules, 'urlpart' : u_rules}
