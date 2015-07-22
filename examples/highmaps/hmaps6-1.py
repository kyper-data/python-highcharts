# -*- coding: utf-8 -*-
from future.standard_library import install_aliases
install_aliases()
from urllib.request import urlopen
import urllib

import json, os, sys
import pandas as pd
import numpy as np
import datetime
import re

sys.path.append('/Users/hankchu/Documents/python-highcharts/highcharts/highmaps')
import highmaps
from highmap_helper import jsonp_loader, js_map_loader, geojson_handler

H = highmaps.Highmap()
H.add_CSSsource('http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css')

map_url = 'http://code.highcharts.com/mapdata/countries/us/us-all.js'
geojson = js_map_loader(map_url)
data = geojson_handler(geojson)

for i, item in enumerate(data):
    item.update({'drilldown':item['properties']['hc-key']})
    item.update({'value': i}) # add bogus data

options = {
    'chart' : {
        'events': {
            'drilldown': "function(e){\
                            this.setTitle({ text: e.point.name }, null)\
                                    }",
            'drillup': "function () {\
                            this.setTitle({ text: 'USA' }, null);\
                                    }",
        }
    },

    'title' : {
        'text' : 'USA'
    },

    'legend': {} if H.options['chart'].__dict__.get('width', None) < 400 else {
        'layout': 'vertical',
        'align': 'right',
        'verticalAlign': 'middle'
    },

    'colorAxis': {
        'min': 0,
        'minColor': '#E6E7E8',
        'maxColor': '#006089'
    },

    'mapNavigation': {
        'enabled': True,
        'buttonOptions': {
            'verticalAlign': 'bottom'
        }
    },

    'plotOptions': {
        'map': {
            'states': {
                'hover': {
                    'color': '#EEDD66'
                }
            }
        }
    },
    'drilldown': {
        'activeDataLabelStyle': {
            'color': '#FFFFFF',
            'textDecoration': 'none',
            'textShadow': '0 0 3px #000000'
        },
        'drillUpButton': {
            'relativeTo': 'spacingBox',
            'position': {
                'x': 0,
                'y': 60
            }
        }
    }
    
}

H.add_data_set(data,'map','USA',dataLabels = {
                'enabled': True,
                'format': '{point.properties.postal-code}'
            }) 
H.set_dict_options(options)

for item in data:
    mapkey = item['drilldown']
    url = 'http://code.highcharts.com/mapdata/countries/us/' + mapkey + '-all.js'
    sub_geojson = js_map_loader(url)
    sub_data = geojson_handler(sub_geojson)
    for i, d in enumerate(sub_data):
        d.update({'value': i}) # add bogus data
    
    H.add_drilldown_data_set(sub_data, 'map', id = mapkey, name = item['name'], 
                dataLabels = {
                    'enabled': True,
                    'format': '{point.name}'
                }
            )

H.save_file('highmaps')
