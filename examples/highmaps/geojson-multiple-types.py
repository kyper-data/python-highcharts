# -*- coding: utf-8 -*-
"""
Highmaps Demos
GeoJSON with rivers and cities: http://www.highcharts.com/maps/demo/geojson-multiple-types
"""
from highcharts import Highmap
from highcharts.highmaps.highmap_helper import jsonp_loader, js_map_loader, geojson_handler

H = Highmap()
options = {
        'title' : {
                'text' : 'Highmaps from geojson with multiple geometry types'
            },

        'mapNavigation': {
            'enabled': True,
            'buttonOptions': {
                'verticalAlign': 'bottom'
            }
            },
    } 

H.set_dict_options(options)

map_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=australia.geo.json&callback=?'

geojson = jsonp_loader(map_url)
states = geojson_handler(geojson, 'map')
rivers = geojson_handler(geojson, 'mapline')
cities = geojson_handler(geojson, 'mappoint')
specialCityLabels = {
    'Melbourne': {
        'align': 'right'
    },
    'Canberra': {
        'align': 'right',
        'y': -5
    },
    'Wollongong': {
        'y': 5
    },
    'Brisbane': {
        'y': -5
    }
}

"""
Use map function in python to handle the dataset operation
"""

def states_label(x):

    if x['properties']['code_hasc'] == 'AU.CT' or x['properties']['code_hasc'] == 'AU.JB':
        x.update({'dataLabels':{'enabled': False}
                })
    elif x['properties']['code_hasc'] == 'AU.SA':
        x.update({'middleY':0.3})
    elif x['properties']['code_hasc'] == 'AU.QL':
        x.update({'middleY':0.7})

def cities_label(x):
    global specialCityLabels
    if x['name'] in specialCityLabels.keys():
        x.update({'dataLabels': specialCityLabels[x['name']]});

map(states_label, states)
map(cities_label, cities)

H.add_data_set(states, 'map', 'States and territories', color = 'Highcharts.getOptions().colors[2]',
                states = {
                    'hover': {
                        'color': 'Highcharts.getOptions().colors[4]'
                    }
                },
                dataLabels = {
                    'enabled': True,
                    'format': '{point.name}',
                    'style': {
                        'width': '80px' 
                    }
                },
                tooltip = {
                    'pointFormat': '{point.name}'
                })
H.add_data_set(rivers, 'mapline', 'Rivers', color = 'Highcharts.getOptions().colors[0]',
                tooltip = {
                    'pointFormat': '{point.properties.NAME}'
                })
H.add_data_set(cities, 'mappoint', 'Cities', color = 'black',
                marker = {
                    'radius': 2
                },
                dataLabels = {
                    'align': 'left',
                    'verticalAlign': 'middle'
                },
                animation = False,
                tooltip = {
                    'pointFormat': '{point.name}'
                })

H.htmlcontent