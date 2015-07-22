# -*- coding: utf-8 -*-
import json, os, sys
import pandas as pd
import numpy as np
import datetime

sys.path.append('/Users/hankchu/Documents/python-highcharts/highcharts/highmaps')

import highmaps
from common import RawJavaScriptText

H = highmaps.Highmap()

options = {
        'chart': {
            'borderWidth': 1,
            'marginRight': 50 
        },

        'title': {
            'text': 'US Counties unemployment rates, April 2015'
        },

        'legend': {
            'title': {
                'text': 'Unemployment<br>rate',
                'style': {
                    'color': "(Highcharts.theme && Highcharts.theme.textColor) || 'black'"
                }
            },
            'layout': 'vertical',
            'align': 'right',
            'floating': True,
            'valueDecimals': 0,
            'valueSuffix': '%',
            'backgroundColor': "(Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255, 255, 255, 0.85)'",
            'symbolRadius': 0,
            'symbolHeight': 14
        },

        'mapNavigation': {
            'enabled': True
        },

        'colorAxis': {
            'dataClasses': [{
                'from': 0,
                'to': 2,
                'color': "#F1EEF6"
            }, {
                'from': 2,
                'to': 4,
                'color': "#D4B9DA"
            }, {
                'from': 4,
                'to': 6,
                'color': "#C994C7"
            }, {
                'from': 6,
                'to': 8,
                'color': "#DF65B0"
            }, {
                'from': 8,
                'to': 10,
                'color': "#DD1C77"
            }, {
                'from': 10,
                'color': "#980043"
            }]
        },

        'plotOptions': {
            'mapline': {
                'showInLegend': False,
                'enableMouseTracking': False
            }
        },
    } 

H.set_dict_options(options)
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-counties-unemployment.json&callback=?'
H.add_data_from_jsonp(data_url, 'json_data', 'map', 'Unemployment rate', joinBy = ['hc-key', 'code'], 
     tooltip = {
                    'valueSuffix': '%'
                },
                borderWidth = 0.5,
                states = {
                    'hover': {
                        'color': '#bada55'
                    }
                }
                )
H.add_data_set(RawJavaScriptText('[lines[0]]'), 'mapline', 'State borders', color = 'white')
H.add_data_set(RawJavaScriptText('[lines[1]]'), 'mapline', 'Separator', color = 'gray')
H.set_map_source('http://code.highcharts.com/mapdata/countries/us/us-all-all.js', jsonp_map = False)
H.add_JSscript("var lines = Highcharts.geojson(Highcharts.maps['countries/us/us-all-all'], 'mapline');", 'head')
H.add_JSscript("Highcharts.each(geojson, function (mapPoint) {\
            mapPoint.name = mapPoint.name + ', ' + mapPoint.properties['hc-key'].substr(3, 2);\
        });", 'head')


H.save_file()

