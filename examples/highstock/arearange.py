# -*- coding: utf-8 -*-
"""
Highstock Demos
Area range: http://www.highcharts.com/stock/demo/arearange
"""
from highcharts import Highstock
from highcharts.highstock.highstock_helper import json_loader
H = Highstock()

data_url = 'http://www.highcharts.com/samples/data/range.json'
data = json_loader(data_url)

H.add_data_set(data, 'arearange', 'Temperatures')

options = {
    'rangeSelector' : {
        'selected' : 2
    },

    'title' : {
        'text' : 'Temperature variation by day'
    },

}

H.set_dict_options(options)

H.htmlcontent
