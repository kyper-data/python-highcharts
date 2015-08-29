# -*- coding: utf-8 -*-
"""
Highstock Demos
Single line series: http://www.highcharts.com/stock/demo/basic-line
"""

"""
This example generates the same highstocks chart as Example1-basic-line.py, 
but use jsonp_loader from highstock_helper instead of add_data_from_jsonp

jsonp_loader(url, prefix_regex=r'^(.*\()', suffix_regex=r'(\);)$', sub_d=None, sub_by='')
jsonp_loader is to request (JSON) data from a server in a different domain (JSONP) 
and covert to python readable data. 
    1. url is the url (https) where data is located
    2. "prefix_regex" and "suffix_regex" are regex patterns used to 
        remove JSONP specific prefix and suffix, such as callback header: "callback(" and end: ");", 
    3. "sub_d" is regex patterns for any unwanted string in loaded json data (will be replaced by sub_by). 
    4. "sub_by" is the string to replace any unwanted string defined by sub_d
For function coverstion, such as Data.UTC to datetime.datetime, please check JSONPDecoder
"""

from highcharts import Highstock
from highcharts.highstock.highstock_helper import jsonp_loader
H = Highstock()

data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?'
data = jsonp_loader(data_url, sub_d = r'(\/\*.*\*\/)') # to remove the comment in json doc from the url

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

H.htmlcontent