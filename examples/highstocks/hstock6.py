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
from datetime import datetime
H = highstocks.Highstock()


data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=new-intraday.json&callback=?'
data = jsonp_loader(data_url, regex = r'(\/\*.*\*\/)')

H.add_data_set(data, 'area', 'AAPL', gapSize = 5,
                tooltip = {
                    'valueDecimals': 2
                },
                fillColor = {
                    'linearGradient' : {
                        'x1': 0,
                        'y1': 0,
                        'x2': 0,
                        'y2': 1
                    },
                    'stops' : [
                        [0, 'Highcharts.getOptions().colors[0]'],
                        [1, 'Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get("rgba")']
                    ]
                },
                threshold =  None)

options = {
    'title': {
        'text': 'AAPL stock price by minute'
    },

    'subtitle': {
        'text': 'Using explicit breaks for nights and weekends'
    },

    'xAxis': {
        'breaks': [{ # Nights
            'from': datetime(2011, 10, 6, 16),
            'to': datetime(2011, 10, 7, 8),
            'repeat': 24 * 36 * 10**5
        }, { # Weekends
            'from': datetime(2011, 10, 7, 16),
            'to': datetime(2011, 10, 10, 8),
            'repeat': 7 * 24 * 36 * 10**5
        }]
    },

    'rangeSelector' : {
        'buttons' : [{
            'type' : 'hour',
            'count' : 1,
            'text' : '1h'
        }, {
            'type' : 'day',
            'count' : 1,
            'text' : '1D'
        }, {
            'type' : 'all',
            'count' : 1,
            'text' : 'All'
        }],
        'selected' : 1,
        'inputEnabled' : False
    },

}

H.set_dict_options(options)

H.save_file('highstocks')


