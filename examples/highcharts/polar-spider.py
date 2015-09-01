# -*- coding: utf-8 -*-
"""
Highcharts Demos
Spiderweb: http://www.highcharts.com/demo/polar-spider
"""

from highcharts import Highchart
H = Highchart(width=550, height=400)

options = {
    'chart': {
        'polar': True,
        'type': 'line',
        'renderTo': 'test'
    },

    'title': {
        'text': 'Budget vs spending',
        'x': -80
    },

    'pane': {
        'size': '80%'
    },

    'xAxis': {
        'categories': ['Sales', 'Marketing', 'Development', 'Customer Support',
                'Information Technology', 'Administration'],
        'tickmarkPlacement': 'on',
        'lineWidth': 0
    },

    'yAxis': {
        'gridLineInterpolation': 'polygon',
        'lineWidth': 0,
        'min': 0
    },

    'tooltip': {
        'shared': True,
        'pointFormat': '<span style="color:{series.color}">{series.name}: <b>${point.y:,.0f}</b><br/>'
    },

    'legend': {
        'align': 'right',
        'verticalAlign': 'top',
        'y': 70,
        'layout': 'vertical'
    },
}

data1 = [43000, 19000, 60000, 35000, 17000, 10000]
data2 = [50000, 39000, 42000, 31000, 26000, 14000]

H.set_dict_options(options)
H.add_data_set(data1, name='Allocated Budget', pointPlacement='on')
H.add_data_set(data2, name='Actual Spending',  pointPlacement='on')

H.htmlcontent