# -*- coding: utf-8 -*-
"""
Highstock Demos
Two panes, candlestick and volume: http://www.highcharts.com/stock/demo/candlestick-and-volume
"""
from highcharts import Highstock
from highcharts.highstock.highstock_helper import jsonp_loader
H = Highstock()

data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-ohlcv.json&callback=?'
data = jsonp_loader(data_url, sub_d = r'(\/\*.*\*\/)')

ohlc = []
volume = []
groupingUnits = [
['week', [1]], 
['month', [1, 2, 3, 4, 6]]
]

for i in range(len(data)):
    ohlc.append(
        [
        data[i][0], # the date
        data[i][1], # open
        data[i][2], # high
        data[i][3], # low
        data[i][4]  # close
        ]
        )
    volume.append(
        [
        data[i][0], # the date
        data[i][5]  # the volume 
        ]
    )


options = {
    'rangeSelector': {
                'selected': 1
            },

    'title': {
        'text': 'AAPL Historical'
    },

    'yAxis': [{
        'labels': {
            'align': 'right',
            'x': -3
        },
        'title': {
            'text': 'OHLC'
        },
        'height': '60%',
        'lineWidth': 2
    }, {
        'labels': {
            'align': 'right',
            'x': -3
        },
        'title': {
            'text': 'Volume'
        },
        'top': '65%',
        'height': '35%',
        'offset': 0,
        'lineWidth': 2
    }],
}

H.add_data_set(ohlc, 'candlestick', 'AAPL', dataGrouping = {
                    'units': groupingUnits
                }
)
H.add_data_set(volume, 'column', 'Volume', yAxis = 1, dataGrouping = {
                    'units': groupingUnits
                }
)

H.set_dict_options(options)

H.htmlcontent