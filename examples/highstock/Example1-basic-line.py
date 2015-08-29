# -*- coding: utf-8 -*-
"""
Basic example for highstock module in python-highcharts

As in highcharts, datasets need to be input using the "add_data_set" or "add_data_from_jsonp" methods.
Options can be either set by "set_options" method as showing here or
construct a option dictionary object and input using "set_dict_options" method (recommended).

In highstock, the (new) feature "navigator" is automatically added into the bottom of the chart
based on the first dataset added into chart. But the dataset used in navigator can be changed using 
add_navi_series and add_navi_series_from_jsonp methods:

1. add_navi_series(data, series_type="line", **kwargs)
	1. data is the dataset added into the navigator
	2. series_type is the plot type for navigator
	3. kwargs are for parameters in series 
        (for detail please ref to highcharts API: http://api.highcharts.com/highcharts#)

2. add_navi_series_from_jsonp(data_src=None, data_name='json_data', series_type="line", **kwargs)
    add dataset from the data_src using jsonp. It is converted to jquery function "$.getJSON" in javascript environment
    1. data_src is the url (https) for the dataset
    2. data_name is the variable name of dataset. This name is used for javascript environment (not in python)
    3. series_type( default: "line") is the type of plot this dataset will be presented
    4. kwargs are for parameters in series or plotOptions 
        (for detail please ref to highcharts API: http://api.highcharts.com/highcharts#)

In most examples, add_data_from_jsonp method is used to show a similar practice in Highstock Demos 

The following example is from Highstock Demos
Single line series: http://www.highcharts.com/stock/demo/basic-line
"""

from highcharts import Highstock
from highcharts.highstock.highstock_helper import jsonp_loader
H = Highstock()

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

H.htmlcontent