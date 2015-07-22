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

H = highstocks.Highstock()


def jsonp_loader(url, prefix_regex = r'^(.*\()', suffix_regex = r'(\);)$', regex = None):

    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
    req = urllib.request.Request(url, headers=hdr)
    page = urlopen(req)
    result = page.read()
    
    # replace all the redundant info with none 
    if regex:
    	result = re.sub(regex, '', result)

    prefix = re.search(prefix_regex, result).group()
    suffix = re.search(suffix_regex, result).group()
    if result.startswith(prefix) and result.endswith(suffix):
        result = result[len(prefix):-len(suffix)]
    return json.loads(result)


data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?'
data = jsonp_loader(data_url, regex = r'(\/\*.*\*\/)')


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





