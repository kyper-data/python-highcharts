# -*- coding: utf-8 -*-
"""
Basic example for highmaps module in python-highcharts

As in highcharts, datasets need to input using "add_data_set" method.
Options can be either set by the "set_options" method as shown here or
by constructing a option dictionary object and input using "set_dict_options" method (recommended)

In highmaps, the map data can be input in multiple ways:

1. add_map_data method: (recommended)
    add_map_data(geojson, **kwargs)
    set map directly to the input (geojson) data 
    geojson is the map data in geojson format

2. set_map_source method:
    set_map_source(map_src, jsonp_map = False)
    map_src is the url (https) where map data is located,
    it is recommended to get map data from highcharts' map collection: 
    https://code.highcharts.com/mapdata/
    jsonp_map is boolean parameter if mapdata is loaded from jsonp
    geojson (from jsonp) or .js are accepted formats. 
    default is javascript (.js) format (from highcharts)

The following example is from Highmaps Demos
GeoJSON areas: http://www.highcharts.com/maps/demo/geojson
"""

from highcharts import Highmap
H = Highmap(width = 650, height = 500)

options = { # construct option dict
                                   
    'chart' :{ 'renderTo' : 'container'
    },
                           
    'title' : {
        'text' : 'GeoJSON in Highmaps'
    },

    'mapNavigation': {
        'enabled': True,
        'buttonOptions': {
            'verticalAlign': 'bottom'
        }
    },

    'colorAxis': {
    },
} 

data = [ # input dataset 
    {
        "code": "DE.SH",
        "value": 728
    },
    {
        "code": "DE.BE",
        "value": 710
    },
    {
        "code": "DE.MV",
        "value": 963
    },
    {
        "code": "DE.HB",
        "value": 541
    },
    {
        "code": "DE.HH",
        "value": 622
    },
    {
        "code": "DE.RP",
        "value": 866
    },
    {
        "code": "DE.SL",
        "value": 398
    },
    {
        "code": "DE.BY",
        "value": 785
    },
    {
        "code": "DE.SN",
        "value": 223
    },
    {
        "code": "DE.ST",
        "value": 605
    },
    {
        "code": "DE.",
        "value": 361
    },
    {
        "code": "DE.NW",
        "value": 237
    },
    {
        "code": "DE.BW",
        "value": 157
    },
    {
        "code": "DE.HE",
        "value": 134
    },
    {
        "code": "DE.NI",
        "value": 136
    },
    {
        "code": "DE.TH",
        "value": 704
    }
]
H.set_dict_options(options) # set options
H.add_data_set(data, 'map', 'Random data', joinBy=['code_hasc', 'code'], # set dataset
                states={
                    'hover': {
                        'color': '#BADA55'
                    }
                },
                dataLabels={
                    'enabled': True,
                    'format': '{point.properties.postal}'
                })

H.set_map_source('http://www.highcharts.com/samples/data/jsonp.php?filename=germany.geo.json&callback=?', True) # set map data from the src (jsonp)

H.htmlcontent