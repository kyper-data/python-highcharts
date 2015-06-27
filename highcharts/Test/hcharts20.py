# -*- coding: utf-8 -*-
import json, os, sys
import pandas as pd
import numpy as np
import datetime

sys.path.append('/Users/hankchu/Documents/python-highcharts/highcharts')

import highcharts
H = highcharts.Highcharts(width = 550, height = 400)

options = {'chart': {
            'type': 'pie',
            'options3d': {
                'enabled': True,
                'alpha': 45
            }
        },
        'title': {
            'text': "Contents of Highsoft\'s weekly fruit delivery"
        },
        'subtitle': {
            'text': '3D donut in Highcharts'
        },
        'plotOptions': {
            'pie': {
                'innerSize': 100,
                'depth': 45
            }
        },
    }

data = [
                ['Bananas', 8],
                ['Kiwi', 3],
                ['Mixed nuts', 1],
                ['Oranges', 6],
                ['Apples', 8],
                ['Pears', 4],
                ['Clementines', 4],
                ['Reddish (bag)', 1],
                ['Grapes (bunch)', 1]
            ]

H.set_dict_optoins(options)
H.add_data_set(data, 'pie', 'Delivered amount')
H.file()