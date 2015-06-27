# -*- coding: utf-8 -*-
import json, os, sys
import pandas as pd
import numpy as np
import datetime

sys.path.append('/Users/hankchu/Documents/python-highcharts/highcharts')

import highcharts
from common import JSfunction
H = highcharts.Highcharts(width = 750, height = 600)

data1 = [502, 635, 809, 947, 1402, 3634, 5268]
data2 = [106, 107, 111, 133, 221, 767, 1766]
data3 = [163, 203, 276, 408, 547, 729, 628]
data4 = [18, 31, 54, 156, 339, 818, 1201]
data5 = [2, 2, 2, 6, 13, 30, 46]


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
        },
    }

H.set_dict_optoins(options)

H.add_data_set(data1, 'area', 'Asia')
H.add_data_set(data2, 'area', 'Africa')
H.add_data_set(data3, 'area', 'Europe')
H.add_data_set(data4, 'area', 'America')
H.add_data_set(data5, 'area', 'Oceania')


H.file()
