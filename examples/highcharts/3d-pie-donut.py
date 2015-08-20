# -*- coding: utf-8 -*-
"""
Highcharts Demos
3D donut: http://www.highcharts.com/demo/3d-pie-donut
"""

from highcharts import Highchart
H = Highchart(width=550, height=400)

options = {
    'chart': {
        'type': 'pie',
        'options3d': {
            'enabled': True,
            'alpha': 45
        }
    },
    'title': {
        'text': "Contents of Highsoft\'s weekly fruit delivery"
    },
    'subtitle': {
        'text': '3D donut in Highcharts'
    },
    'plotOptions': {
        'pie': {
            'innerSize': 100,
            'depth': 45
        }
    },
}

data = [
    ['Bananas', 8],
    ['Kiwi', 3],
    ['Mixed nuts', 1],
    ['Oranges', 6],
    ['Apples', 8],
    ['Pears', 4],
    ['Clementines', 4],
    ['Reddish (bag)', 1],
    ['Grapes (bunch)', 1]
]

H.set_dict_options(options)
H.add_data_set(data, 'pie', 'Delivered amount')

H.htmlcontent