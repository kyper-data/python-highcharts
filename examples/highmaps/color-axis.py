# -*- coding: utf-8 -*-
"""
Highmaps Demos
Color axis and data labels: http://www.highcharts.com/maps/demo/color-axis
"""

from highcharts import Highmap
H = Highmap(width = 650, height = 550)

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

H.set_dict_options(options)
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-population-density.json&callback=?' # set data_src
H.add_data_from_jsonp(data_url, 'json_data', 'map', 'Population density', joinBy = ['postal-code', 'code'], # add dataset from data_src using jsonp
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

"""
python-highcharts provides add_JSscript method:
add_JSscript(js_script, js_loc):
js_script is the javascript string 
js_loc is location of this javascript string, can be either head (at beginning of the script) or
end (in the end of the script)

The JS string here is a function to convert (state) codes in dateset to Upper case (from lower)
However, it is not recommended to do it this way. 
The better practice is to load data into python environment and handle in python. 
It can be done by writting a python script or using the functions in highmap_helper module
"""
H.add_JSscript("$.each(json_data, function () {\
            this.code = this.code.toUpperCase();\
        });", 'head')

H.htmlcontent