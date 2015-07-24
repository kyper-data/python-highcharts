# -*- coding: utf-8 -*-
from future.standard_library import install_aliases
install_aliases()
from urllib.request import urlopen
import urllib

import json, os, sys
import pandas as pd
import numpy as np
import datetime
import re

sys.path.append('/Users/hankchu/Documents/python-highcharts/highcharts/highstocks')

import highstocks
from highstock_helper import jsonp_loader
H = highstocks.Highstock()

data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-ohlcv.json&callback=?'
data = jsonp_loader(data_url, re_d = r'(\/\*.*\*\/)')


ohlc = []
volume = []
groupingUnits = [
['week', [1]], 
['month', [1, 2, 3, 4, 6]]
]

for i in xrange(len(data)):
    ohlc.append(
        [
        data[i][0],
        data[i][1],
        data[i][2],
        data[i][3],
        data[i][4]
        ]
        )
    volume.append(
        [
        data[i][0],
        data[i][5]
        ]
        )


options = {
    'rangeSelector': {
                'selected': 1
            },

    'title': {
        'text': 'AAPL Historical'
    },

    'yAxis': [{
        'labels': {
            'align': 'right',
            'x': -3
        },
        'title': {
            'text': 'OHLC'
        },
        'height': '60%',
        'lineWidth': 2
    }, {
        'labels': {
            'align': 'right',
            'x': -3
        },
        'title': {
            'text': 'Volume'
        },
        'top': '65%',
        'height': '35%',
        'offset': 0,
        'lineWidth': 2
    }],
}

H.add_data_set(ohlc, 'candlestick', 'AAPL', dataGrouping = {
                    'units': groupingUnits
                }
)
H.add_data_set(volume, 'column', 'Volume', yAxis = 1, dataGrouping = {
                    'units': groupingUnits
                }
)

H.set_dict_options(options)


H.save_file('highstocks')





