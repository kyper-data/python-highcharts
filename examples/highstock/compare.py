# -*- coding: utf-8 -*-
"""
Highstock Demos
Compare multiple series: http://www.highcharts.com/stock/demo/compare
"""

from highcharts import Highstock
from highcharts.highstock.highstock_helper import jsonp_loader
H = Highstock()

names = ['MSFT', 'AAPL', 'GOOG']

for name in names:
    data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=' + name.lower() + '-c.json&callback=?'
    data = jsonp_loader(data_url, sub_d = r'(\/\*.*\*\/)')

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

H.htmlcontent