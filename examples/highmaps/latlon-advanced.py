# -*- coding: utf-8 -*-
"""
Highmaps Demos
Advanced lat/long: http://www.highcharts.com/maps/demo/latlon-advanced
"""

from highcharts import Highmap
from highcharts.highmaps.highmap_helper import jsonp_loader, js_map_loader, geojson_handler, interpolateRGB

H = Highmap(height=550)
map_url = 'http://code.highcharts.com/mapdata/countries/us/us-all.js'
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-capitals.json&callback=?'
geojson = js_map_loader(map_url)
data = jsonp_loader(data_url)

options = {
    'title': {
            'text': 'Highmaps lat/lon demo'
        },

    'tooltip': {
        'formatter': "function () {\
                            return this.point.capital + ', ' + this.point.parentState + '<br>Lat: ' + this.point.lat + ' Lon: ' + this.point.lon + '<br>Population: ' + this.point.population;\
                        }",
        'crosshairs': [{
            'zIndex': 5,
            'dashStyle': 'dot',
            'snap': False,
            'color': 'gray'
        }, {
            'zIndex': 5,
            'dashStyle': 'dot',
            'snap': False,
            'color': 'gray'
        }]
    },
}

max_p = max([item['population'] for item in data])

for item in data:
    item.update({'z':item['population']})
    item.update({'color':interpolateRGB([255,0,10],[0,255,20],item['population']/max_p)})

H.add_map_data(geojson, name='Basemap' ,borderColor='#606060',
            nullColor='rgba(200, 200, 200, 0.2)',
            showInLegend=False) 
H.add_data_set(geojson_handler(geojson, 'mapline'),
    'mapline','Separators', showInLegend=False, enableMouseTracking=False)    
H.add_data_set(data,'mapbubble','Cities', dataLabels={
                    'enabled': True,
                    'format': '{point.capital}'
                }, maxSize='12%', is_coordinate=True)

H.set_dict_options(options)

H.htmlcontent