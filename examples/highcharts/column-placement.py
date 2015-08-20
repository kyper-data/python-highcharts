# -*- coding: utf-8 -*-
"""
Highcharts Demos
Fixed placement columns: http://www.highcharts.com/demo/column-placement
"""
import datetime
from highcharts import Highchart

H = Highchart(width=850, height=400)

options = {
	'chart': {
        'type': 'column'
    },
    'title': {
        'text': 'Efficiency Optimization by Branch'
    },
    'xAxis': {
        'categories': [
            'Seattle HQ',
            'San Francisco',
            'Tokyo'
        ]
    },
    'yAxis': [{
        'min': 0,
        'title': {
            'text': 'Employees'
        }
    }, {
        'title': {
            'text': 'Profit (millions)'
        },
        'opposite': True
    }],
    'legend': {
        'shadow': False
    },
    'tooltip': {
        'shared': True
    },
    'plotOptions': {
        'column': {
            'grouping': False,
            'shadow': False,
            'borderWidth': 0
        }
    }
}

data1 = [150, 73, 20]
data2 = [140, 90, 40]
data3 = [183.6, 178.8, 198.5]
data4 = [203.6, 198.8, 208.5]

H.set_dict_options(options)

H.add_data_set(data1, 'column', 'Employees', color='rgba(165,170,217,1)',
				pointPadding=0.3, pointPlacement=-0.2 )
H.add_data_set(data2, 'column', 'Employees Optimized', color='rgba(126,86,134,.9)',
				pointPadding=0.4, pointPlacement=-0.2 )
H.add_data_set(data3, 'column', 'Profit', color='rgba(248,161,63,1)', tooltip={
                'valuePrefix': '$',
                'valueSuffix': ' M'
            },
            pointPadding=0.3,
            pointPlacement=0.2,
            yAxis=1)
H.add_data_set(data4, 'column', 'Profit Optimized', color='rgba(186,60,61,.9)',
			tooltip={
                'valuePrefix': '$',
                'valueSuffix': ' M'
            },
            pointPadding=0.4,
            pointPlacement=0.2,
            yAxis=1)

H.htmlcontent