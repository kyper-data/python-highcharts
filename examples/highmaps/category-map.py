# -*- coding: utf-8 -*-
"""
Highmaps Demos
Categorized areas: http://www.highcharts.com/maps/demo/category-map
"""

from highcharts import Highmap
H = Highmap(width=650, height=500)

options = {
    'chart': {
        'spacingBottom': 20
    },
    'title' : {
        'text' : 'Europe time zones'
    },

    'legend': {
        'enabled': True
    },

    'plotOptions': {
        'map': {
            'allAreas': False,
            'joinBy': ['iso-a2', 'code'],
            'dataLabels': {
                'enabled': True,
                'color': 'white',
                'formatter': "function () {\
                                        if (this.point.properties && this.point.properties.labelrank.toString() < 5) {\
                                            return this.point.properties['iso-a2'];\
                                        }\
                }",
                'format': None,
                'style': {
                    'fontWeight': 'bold'
                }
            },
            'mapData': "Highcharts.maps['custom/europe']",
            'tooltip': {
                'headerFormat': '',
                'pointFormat': '{point.name}: <b>{series.name}</b>'
            }

        }
    }
} 



data1 = [{'code': x} for x in ['IE','IS', 'GB', 'PT']]
data2 = [{'code': x} for x in ['NO', 'SE', 'DK', 'DE', 'NL', 'BE', 'LU', 'ES', 'FR', 'PL', 'CZ', 'AT', 'CH', 'LI', 'SK', 'HU',\
                    'SI', 'IT', 'SM', 'HR', 'BA', 'YF', 'ME', 'AL', 'MK']]
data3 = [{'code': x} for x in ['FI', 'EE', 'LV', 'LT', 'BY', 'UA', 'MD', 'RO', 'BG', 'GR', 'TR', 'CY']]
data4 = [{'code': x} for x in ['RU']]

H.set_dict_options(options)
H.add_data_set(data1, 'map', 'UTC')
H.add_data_set(data2, 'map', 'UTC + 1')
H.add_data_set(data3, 'map', 'UTC + 2')
H.add_data_set(data4, 'map', 'UTC + 3')

H.set_map_source('http://code.highcharts.com/mapdata/custom/europe.js', jsonp_map=False) # set map data from src. data is in .js format

H.htmlcontent