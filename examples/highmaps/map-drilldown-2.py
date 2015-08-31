# -*- coding: utf-8 -*-
"""
Highmaps Demos
Drilldown: http://www.highcharts.com/maps/demo/map-drilldown
"""

from highcharts import Highmap
from highcharts.highmaps.highmap_helper  import jsonp_loader, js_map_loader, geojson_handler

H = Highmap()
H.add_CSSsource('http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css')

"""
This example is to show how to generate drilldown map with both state and county level data in the US 
without using the JS functions as shown in Highmaps Demos

The drilldown data can be added using add_drilldown_data_set method:
add_drilldown_data_set(data, series_type, id, **kwargs)
1. data is the dataset for drilldown level
2. series_type is the type of plot presented at the drilldown level
3. id is the identifier used for the drilldown parent point to identify its series. 
    This needs to be consistent with the drilldown property in dataset of parent level 
4. kwargs are for parameters in series or plotOptions 
    (for detail please ref to highcharts API: http://api.highcharts.com/highcharts#)

However, the tradeoff is that user needs to query and handle the whole dataset in python environment
and put the whole dataset into the .html file, which could make final file very big.
"""

map_url = 'http://code.highcharts.com/mapdata/countries/us/us-all.js'
geojson = js_map_loader(map_url)
data = geojson_handler(geojson)

for i, item in enumerate(data):
    item.update({'drilldown':item['properties']['hc-key']})
    item.update({'value': i}) # add bogus data

options = {
    'chart' : {
        'events': { # Here event option is only used to change the tittle when different level data is shown
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

    'legend': {} if H.options['chart'].__dict__.get('width', 0) < 400 else { 
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

for item in data: # add drilldown dataset
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

H.htmlcontent
