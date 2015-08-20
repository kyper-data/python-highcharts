# -*- coding: utf-8 -*-
"""
Highcharts Demos
Percentage area: http://www.highcharts.com/demo/area-stacked-percent
"""
from highcharts import Highchart
H = Highchart(width=750, height=600)

data1 = [502, 635, 809, 947, 1402, 3634, 5268] # data for Asia
data2 = [106, 107, 111, 133, 221, 767, 1766] # data for Africa
data3 = [163, 203, 276, 408, 547, 729, 628] # data for Europe
data4 = [18, 31, 54, 156, 339, 818, 1201] # data for America
data5 = [2, 2, 2, 6, 13, 30, 46] # data for Oceania


options = {
    'title': {
        'text': 'Historic and Estimated Worldwide Population Growth by Region'
    },
    'subtitle': {
        'text': 'Source: Wikipedia.org'
    },
    'xAxis': {
        'categories': ['1750', '1800', '1850', '1900', '1950', '1999', '2050'],
        'tickmarkPlacement': 'on',
        'title': {
            'enabled': False
        }
    },
    'yAxis': {
        'title': {
            'text': 'Billions'
        },
        'labels': {
            'formatter': 'function () {\
                                return this.value ;\
                            }'
        }
    },
    'tooltip': {
        'shared': True,
        'valueSuffix': ' millions'
    },
    'plotOptions': {
        'area': {
            'stacking': 'normal',
            'lineColor': '#666666',
            'lineWidth': 1,
            'marker': {
                'lineWidth': 1,
                'lineColor': '#666666'
            }
        }
    }
}

H.set_dict_options(options)

H.add_data_set(data1, 'area', 'Asia')
H.add_data_set(data2, 'area', 'Africa')
H.add_data_set(data3, 'area', 'Europe')
H.add_data_set(data4, 'area', 'America')
H.add_data_set(data5, 'area', 'Oceania')

H.htmlcontent