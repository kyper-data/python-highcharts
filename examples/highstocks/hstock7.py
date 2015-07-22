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

data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-ohlc.json&callback=?'
data = jsonp_loader(data_url, regex = r'(\/\*.*\*\/)')

H.add_data_set(data, 'ohlc', 'AAPL Stock Price', dataGrouping = {
                    'units' : [[
                        'week', # unit name
                        [1] # allowed multiples
                    ], [
                        'month',
                        [1, 2, 3, 4, 6]
                    ]]
                })

options = {
    'rangeSelector' : {
        'selected' : 2
    },

    'title' : {
        'text' : 'AAPL Stock Price'
    },

}

H.set_dict_options(options)

H.save_file('highstocks')


