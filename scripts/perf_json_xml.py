########################################################################################
#
# Small script to test json performance against xml
# Requirement :
#     pip install lxml
#
# 2015-01-02 E.Lapouyade : Creation
#
########################################################################################
import json
from lxml import objectify
from datetime import datetime
from random import randint
import dicttoxml

NB_ROW=10240

dummy_data = [ { 'dummy_key_A_%s' % i: i, 'dummy_key_B_%s' % i: i } for i in xrange(NB_ROW) ]

import lxml.etree as et

def data2xml(d, name='data'):
    r = et.Element(name)
    return et.tostring(buildxml(r, d))

def buildxml(r, d):
    if isinstance(d, dict):
        for k, v in d.iteritems():
            s = et.SubElement(r, k)
            buildxml(s, v)
    elif isinstance(d, tuple) or isinstance(d, list):
        for v in d:
            s = et.SubElement(r, 'i')
            buildxml(s, v)
    elif isinstance(d, basestring):
        r.text = d
    else:
        r.text = str(d)
    return r

with open('perf_json_xml.xml','w') as fh:
    t1 = datetime.now()
    dummy_data_xml = data2xml(dummy_data)
    fh.write(dummy_data_xml)
    t2 = datetime.now()
    dtx = (t2 - t1).total_seconds()
    print 'Dumping %s row into a xml file : %s' % (NB_ROW,dtx)

with open('perf_json_xml.json','w') as fh:
    t1 = datetime.now()
    json.dump(dummy_data,fh)
    t2 = datetime.now()
    dtj = (t2 - t1).total_seconds()
    print 'Dumping %s row into a json file : %s' % (NB_ROW,dtj)

print "json is %dx faster for dumping" % (dtx/dtj)

with open('perf_json_xml.xml') as fh:
    t1 = datetime.now()
    tree = objectify.parse(fh)
    root = tree.getroot()
    items = root.find('item')
    t2 = datetime.now()
    dtx = (t2 - t1).total_seconds()
    print 'Loading %s row from a xml file : %s' % (NB_ROW,dtx)

with open('perf_json_xml.json') as fh:
    t1 = datetime.now()
    data = json.load(fh)
    t2 = datetime.now()
    dtj = (t2 - t1).total_seconds()
    print 'Loading %s row into from json file : %s' % (NB_ROW,dtj)

print "json is %dx faster for loading" % (dtx/dtj)
