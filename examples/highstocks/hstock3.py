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

names = ['MSFT', 'AAPL', 'GOOG']

for name in names:
    data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=' + name.lower() + '-c.json&callback=?'
    data = jsonp_loader(data_url, regex = r'(\/\*.*\*\/)')

    H.add_data_set(data, 'line', name)


options = {
    'rangeSelector': {
                    'selected': 4
                },
    'yAxis': {
        'labels': {
            'formatter': "function () {\
                            return (this.value > 0 ? ' + ' : '') + this.value + '%';\
                        }"
        },
        'plotLines': [{
            'value': 0,
            'width': 2,
            'color': 'silver'
        }]
    },

    'plotOptions': {
        'series': {
            'compare': 'percent'
        }
    },

    'tooltip': {
        'pointFormat': '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
        'valueDecimals': 2
    },
}

H.set_dict_options(options)

H.save_file('highstocks')


