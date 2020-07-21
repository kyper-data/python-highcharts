# -*- coding: utf-8 -*-
"""
Highstock Demos
52,000 points with data grouping: http://www.highcharts.com/stock/demo/data-grouping
"""

from highcharts import Highstock
from highcharts.highstock.highstock_helper import json_loader
H = Highstock()

data_url = 'http://www.highcharts.com/samples/data/large-dataset.json'
data = json_loader(data_url)

H.add_data_set(data['data'], 'line', 'Temperature', pointStart = data['pointStart'],
                pointInterval = data['pointInterval'],
                tooltip = {
                    'valueDecimals': 1,
                    'valueSuffix': u'°C'
                })

options = {
    'chart': {
        'zoomType': 'x'
    },

    'rangeSelector': {

        'buttons': [{
            'type': 'day',
            'count': 3,
            'text': '3d'
        }, {
            'type': 'week',
            'count': 1,
            'text': '1w'
        }, {
            'type': 'month',
            'count': 1,
            'text': '1m'
        }, {
            'type': 'month',
            'count': 6,
            'text': '6m'
        }, {
            'type': 'year',
            'count': 1,
            'text': '1y'
        }, {
            'type': 'all',
            'text': 'All'
        }],
        'selected': 3
    },

    'yAxis': {
        'title': {
            'text': u'Temperature (°C)'
        }
    },

    'title': {
        'text': 'Hourly temperatures in Vik i Sogn, Norway, 2009-2015'
    },

}

H.set_dict_options(options)

H.htmlcontent
