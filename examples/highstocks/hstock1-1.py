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

data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?'
data = jsonp_loader(data_url, re_d = r'(\/\*.*\*\/)')


options = {
    'rangeSelector' : {
            'selected' : 1
        },

    'title' : {
        'text' : 'AAPL Stock Price'
    },
}

H.add_data_set(data, 'line', 'AAPL', tooltip = {
    'valueDecimals': 2
    }
)


H.set_dict_options(options)


H.save_file('highstocks')





