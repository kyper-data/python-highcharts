# -*- coding: utf-8 -*-
import json, os, sys
import pandas as pd
import numpy as np
import datetime

sys.path.append('/Users/hankchu/Documents/python-highcharts/highmaps')

import highmaps

H = highmaps.Highmaps(width = 650, height = 550)

options = {
        'chart' : {
            'borderWidth' : 1
        },

        'title' : {
            'text' : 'US population density (/km²)'
        },

        'legend': {
            'layout': 'horizontal',
            'borderWidth': 0,
            'backgroundColor': 'rgba(255,255,255,0.85)',
            'floating': True,
            'verticalAlign': 'top',
            'y': 25
        },

        'mapNavigation': {
            'enabled': True
        },

        'colorAxis': {
            'min': 1,
            'type': 'logarithmic',
            'minColor': '#EEEEFF',
            'maxColor': '#000022',
            'stops': [
                [0, '#EFEFFF'],
                [0.67, '#4444FF'],
                [1, '#000022']
            ]
        },
    } 

H.set_dict_optoins(options)
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-population-density.json&callback=?'
H.add_data_from_jsonp(data_url, 'json_data', 'map', 'Population density', joinBy = ['postal-code', 'code'], 
     dataLabels = {
                    'enabled': True,
                    'color': 'white',
                    'format': '{point.code}'
                },
                tooltip = {
                    'pointFormat': '{point.code}: {point.value}/km²'
                }
                )

H.set_map_source('http://code.highcharts.com/mapdata/countries/us/us-all.js', jsonp_map = False)
H.add_jscript("$.each(json_data, function () {\
            this.code = this.code.toUpperCase();\
        });", 'head')
H.file()