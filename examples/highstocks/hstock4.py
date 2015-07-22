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

data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=large-dataset.json&callback=?'
data = jsonp_loader(data_url, regex = r'(\/\*.*\*\/)')

H.add_data_set(data['data'], 'line', 'Temperature', pointStart = data['pointStart'],
                pointInterval = data['pointInterval'],
                tooltip = {
                    'valueDecimals': 1,
                    'valueSuffix': '°C'
                })

options = {
    'chart': {
        'zoomType': 'x'
    },

    'rangeSelector': {

        'buttons': [{
            'type': 'day',
            'count': 3,
            'text': '3d'
        }, {
            'type': 'week',
            'count': 1,
            'text': '1w'
        }, {
            'type': 'month',
            'count': 1,
            'text': '1m'
        }, {
            'type': 'month',
            'count': 6,
            'text': '6m'
        }, {
            'type': 'year',
            'count': 1,
            'text': '1y'
        }, {
            'type': 'all',
            'text': 'All'
        }],
        'selected': 3
    },

    'yAxis': {
        'title': {
            'text': 'Temperature (°C)'
        }
    },

    'title': {
        'text': 'Hourly temperatures in Vik i Sogn, Norway, 2009-2015'
    },

}

H.set_dict_options(options)

H.save_file('highstocks')


