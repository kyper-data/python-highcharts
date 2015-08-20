# -*- coding: utf-8 -*-
"""
Highmaps Demos
Map point with lat/long: http://www.highcharts.com/maps/demo/mappoint-latlon
"""

from highcharts import Highmap
from highcharts.highmaps.highmap_helper import jsonp_loader, js_map_loader, geojson_handler

H = Highmap(height=750)
map_url = 'http://code.highcharts.com/mapdata/countries/gb/gb-all.js'
geojson = js_map_loader(map_url)
data = [{
                'name': 'London',
                'lat': 51.507222,
                'lon': -0.1275
            }, {
                'name': 'Birmingham',
                'lat': 52.483056,
                'lon': -1.893611
            }, {
                'name': 'Leeds',
                'lat': 53.799722,
                'lon': -1.549167
            }, {
                'name': 'Glasgow',
                'lat': 55.858,
                'lon': -4.259
            }, {
                'name': 'Sheffield',
                'lat': 53.383611,
                'lon': -1.466944
            }, {
                'name': 'Liverpool',
                'lat': 53.4,
                'lon': -3
            }, {
                'name': 'Bristol',
                'lat': 51.45,
                'lon': -2.583333
            }, {
                'name': 'Belfast',
                'lat': 54.597,
                'lon': -5.93
            }, {
                'name': 'Lerwick',
                'lat': 60.155,
                'lon': -1.145,
                'dataLabels': {
                    'align': 'left',
                    'x': 5,
                    'verticalAlign': 'middle'
                }
            }]

fake_data = []
options = {
        'title': {
            'text': 'Highmaps basic lat/lon demo'
        },

        'mapNavigation': {
            'enabled': True
        },

        'tooltip': {
            'headerFormat': '',
            'pointFormat': '<b>{point.name}</b><br>Lat: {point.lat}, Lon: {point.lon}'
        },
        
    }
H.add_map_data(geojson, name = 'Basemap' ,borderColor = '#A0A0A0',
            nullColor = 'rgba(200, 200, 200, 0.3)',
            showInLegend = False)    
H.add_data_set(data,'mappoint','Cities',color = 'Highcharts.getOptions().colors[1]', is_coordinate = True)
H.add_data_set(geojson_handler(geojson, 'mapline'),
    'mapline','Separators',color = '#707070', showInLegend = False, enableMouseTracking = False)
H.set_dict_options(options)

H.htmlcontent