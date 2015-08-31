# -*- coding: utf-8 -*-
"""
Highmaps Demos
Detailed map, US counties: http://www.highcharts.com/maps/demo/us-counties
"""

from highcharts import Highmap
from highcharts.highmaps.highmap_helper import jsonp_loader, js_map_loader, geojson_handler

H = Highmap()

"""
This example generates the same map as us-counties.py, but using functions in highmap_helper module to 
handle data in python environment completely
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
        'map':{
        'mapData': 'geojson'

        },
        'mapline': {
            'showInLegend': False,
            'enableMouseTracking': False
        }
    },
} 

H.set_dict_options(options)

"""
Load data and map data directly from url using jsonp_loader and js_map_loader
1. jsonp_loader(url, prefix_regex=r'^(.*\()', suffix_regex=r'(\);)$', sub_d=None, sub_by='')
    jsonp_loader is to request (JSON) data from a server in a different domain (JSONP) 
    and covert to python readable data. 
    1. url is the url (https) where data is located
    2. "prefix_regex" and "suffix_regex" are regex patterns used to 
        remove JSONP specific prefix and suffix, such as callback header: "callback(" and end: ");", 
    3. "sub_d" is regex patterns for any unwanted string in loaded json data (will be replaced by sub_by). 
    4. "sub_by" is the string to replace any unwanted string defined by sub_d
    For function coverstion, such as Data.UTC to datetime.datetime, please check JSONPDecoder

2. js_map_loader(url)
    js_map_loader is to load map data from a .js source. It is designed for using highcharts' map collection:
    https://code.highcharts.com/mapdata/. Map data from other sources are not guaranteed 
"""
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-counties-unemployment.json&callback=?'
map_url = 'http://code.highcharts.com/mapdata/countries/us/us-all-all.js'
data = jsonp_loader(data_url)
geojson = js_map_loader(map_url)

"""
Convert loaded mapadata into the format readable by highcharts using geojson_handler

geojson_handler(geojson, hType='map')
geojson_handler is similar to highcharts.geojson function, which is to 
restructure a geojson object to be add directly by add_map_data or add_data_set method. 
The geojson will be broken down to fit a specific Highcharts (highmaps) type, either map, mapline or mappoint. 
Meta data in GeoJSON's properties object will be copied directly over to object['properties']
1. geojson is the map data (GeoJSON) to be converted
2. hType is the type of highmap types. "map" will return GeoJSON polygons and multipolygons. 
    "mapline" will return GeoJSON linestrings and multilinestrings. 
    "mappoint" will return GeoJSON points and multipoints.
    default: "map"
"""

mapdata = geojson_handler(geojson)
lines = geojson_handler(geojson, 'mapline')

"""
Change the name property in map data. 
This is doing the same thing as the second JS function added in the example us-counties.py 
"""
for x in mapdata:
    x.update({'name':x['name']+', '+x['properties']['hc-key'].split('-')[1].upper()})


H.add_data_set(data, 'map', 'Unemployment rate', joinBy = ['hc-key', 'code'], 
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
H.add_data_set([lines[0]], 'mapline', 'State borders', color = 'white')
H.add_data_set([lines[3]], 'mapline', 'Separator', color = 'gray')
H.add_map_data(mapdata)

H.htmlcontent

