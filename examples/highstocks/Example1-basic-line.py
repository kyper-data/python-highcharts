# -*- coding: utf-8 -*-
"""
Basic example for highstocks module in python-highcharts

As highcharts, datasets need to input using "add_data_set" method
options can be either set by "set_options" method as showing here or
construct a option dictionary object and input using "set_dict_options" method (recommended)

In most examples, add_data_from_jsonp method is used to show a similar practice in Highstock Demos 

The following example is from Highstock Demos
Single line series: http://www.highcharts.com/stock/demo/basic-line
"""

import highstocks
H = highstocks.Highstock()

data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?'
H.add_data_from_jsonp(data_url, 'json_data', 'line', 'AAPL', tooltip = {
    'valueDecimals': 2
    }
)

options = {
    'rangeSelector' : {
            'selected' : 1
        },

    'title' : {
        'text' : 'AAPL Stock Price'
    },
}
H.set_dict_options(options)

H
H.save_file('highstocks')