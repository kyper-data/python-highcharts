# -*- coding: utf-8 -*-
"""
Highstock Demos
OHLC: http://www.highcharts.com/stock/demo/ohlc
"""

from highcharts import Highstock
from highcharts.highstock.highstock_helper import jsonp_loader
H = Highstock()

data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-ohlc.json&callback=?'
data = jsonp_loader(data_url, sub_d = r'(\/\*.*\*\/)')

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

H.htmlcontent