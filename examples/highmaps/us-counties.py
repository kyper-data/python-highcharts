# -*- coding: utf-8 -*-
"""
Highmaps Demos
Detailed map, US counties: http://www.highcharts.com/maps/demo/us-counties
"""
from highcharts import Highmap
from highcharts.highmaps.common import RawJavaScriptText

H = Highmap()

"""
This example shows how to make the map of US unemployment rates at county level in April 2015
as the highmaps demo: http://www.highcharts.com/maps/demo/us-counties

However, this example requires to do many things in javascript environment:
1. a JS function to get "mapline" data using highcharts geojson function:
 Highcharts.geojson(Highcharts.maps['countries/us/us-all-all'], 'mapline')
 where highcharts.maps is to get map data loaded from http://code.highcharts.com/mapdata/countries/us/us-all-all.js

2. a JS function to change names of each data set using Highcharts.each

3. need to add datasets for maplines. however, the datasets are not defined in python, therefore they need to add 
using "RawJavaScriptText('[lines[0]]')" which unquote the python string '[lines[0]]' in javascript environment
(from '[lines[0]]' to [lines[0]])

This is not a good way to generate this map with python-highcharts API but still use many javascript function
The example us-counties-2.py shows how to do this in pure python environment
"""
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

H.htmlcontent

