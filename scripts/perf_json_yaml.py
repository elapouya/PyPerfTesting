import json
import yaml
from datetime import datetime
from random import randint

NB_ROW=1024

print 'Does yaml is using libyaml ? ',yaml.__with_libyaml__ and 'yes' or 'no'

dummy_data = [ { 'dummy_key_A_%s' % i: i, 'dummy_key_B_%s' % i: i } for i in xrange(NB_ROW) ]


with open('perf_json_yaml.yaml','w') as fh:
    t1 = datetime.now()
    yaml.safe_dump(dummy_data, fh, encoding='utf-8', default_flow_style=False)
    t2 = datetime.now()
    dty = (t2 - t1).total_seconds()
    print 'Dumping %s row into a yaml file : %s' % (NB_ROW,dty)

with open('perf_json_yaml.json','w') as fh:
    t1 = datetime.now()
    json.dump(dummy_data,fh)
    t2 = datetime.now()
    dtj = (t2 - t1).total_seconds()
    print 'Dumping %s row into a json file : %s' % (NB_ROW,dtj)

print "json is %dx faster for dumping" % (dty/dtj)

with open('perf_json_yaml.yaml') as fh:
    t1 = datetime.now()
    data = yaml.safe_load(fh)
    t2 = datetime.now()
    dty = (t2 - t1).total_seconds()
    print 'Loading %s row from a yaml file : %s' % (NB_ROW,dty)

with open('perf_json_yaml.json') as fh:
    t1 = datetime.now()
    data = json.load(fh)
    t2 = datetime.now()
    dtj = (t2 - t1).total_seconds()
    print 'Loading %s row into from json file : %s' % (NB_ROW,dtj)

print "json is %dx faster for loading" % (dty/dtj)
