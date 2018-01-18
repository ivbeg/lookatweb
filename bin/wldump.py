# -*- coding: utf-8 -*-
from lookatweb.rules import *
from lookatweb.matcher import RulesRegistry
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def extract_entities():
    entities = []
    matcher = RulesRegistry()
    matcher.register('headers', HEADERS_RULES)
    matcher.register('poweredby', POWEREDBY_RULES)
    matcher.register('server', SERVER_RULES)
    matcher.register('servermods', SERVERMODS_RULES)
    matcher.register('extscripts', EXTSCRIPTS_RULES)
    matcher.register('innerscripts', INSCRIPTS_RULES)
    matcher.register('scripts', SCRIPTS_RULES)
    matcher.register('meta', META_RULES)
    matcher.register('meta_copy', META_COPYRIGHT_RULES)
    matcher.register('images', IMAGES_RULES)
    matcher.register('headlinks_rel', HEADLINKS_RULES)
    matcher.register('headlinks_type', HEADLINKS_TYPE_RULES)
    matcher.register('styles', STYLE_RULES)
    matcher.register('iframes', IFRAMES_RULES)
    matcher.register('os', OS_RULES)
    matcher.register('forms_action', FORMS_ACTION_RULES)
    matcher.register('encoding', ENCODING_RULES)
    matcher.register('powered_cms', POWERED_CMS_RULES)
    matcher.register('generator', GENERATOR_RULES)
    matcher.register('object_clsid', OBJECTS_CLSID_RULES)
    matcher.register('object_type', OBJECTS_TYPE_RULES)
    matcher.register('embed_src', EMBED_SRC_RULES)
    matcher.register('object_data', OBJECTS_DATA_RULES)

#    for k, v in matcher.getmap().items():
#        print(yaml.dump(v))
    allrules = {}

    ruletypes = {1: 'equal', 2 : 're', 3: 'find'}
    actiontypes = {1: 'match', 2: 'ignore', 3: 'follow'}
    categories = {}

    for k, l in matcher.getmap().items():
        for rules in [l.textrules.values(), list(l.findrules.values()), l.rerules]:
            for rule in rules:
                for e in rule['entities']:
                    category_name = e['name'].split('/', 1)[0]
                    r = rule.copy()
                    v = allrules.get(e['name'], [])
                    del r['entities']
                    r['section'] = k
                    if 're' in r.keys():
                        del r['re']
                    r['code'] = e['name']
                    r['name'] = ''
                    r['description'] = ''
                    r['url'] = ''
                    r['category'] = category_name
                    r['type'] = ruletypes[r['type']]
                    r['action'] = actiontypes[r['action']] if 'action' in r.keys() else 'match'
                    v.append(r)
                    allrules[e['name']] = v
    keys = list(allrules.keys())
    keys.sort()
    all = {'categories' : list(allrules.values())}
    print(dump(all, Dumper=Dumper, default_flow_style=False))

#    for k in keys:
#        print('%s:' %(k))
#        for r in allrules[k]:
#            print('-', r)

if __name__ == "__main__":
#	convert_patterns()
	extract_entities()


