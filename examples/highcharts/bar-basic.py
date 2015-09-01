# -*- coding: utf-8 -*-
"""
Highcharts Demos
Basic bar: http://www.highcharts.com/demo/bar-basic
"""

from highcharts import Highchart
H = Highchart(width=750, height=600)

data1 = [107, 31, 635, 203, 2]
data2 = [133, 156, 947, 408, 6]
data3 = [973, 914, 4054, 732, 34]
data4 = [1052, 954, 4250, 740, 38]

options = {
	'title': {
        'text': 'Stacked bar chart'
    },
    'subtitle': {
        'text': 'Source: <a href="https://en.wikipedia.org/wiki/World_population">Wikipedia.org</a>'
    },
    'xAxis': {
        'categories': ['Africa', 'America', 'Asia', 'Europe', 'Oceania'],
        'title': {
            'text': None
        }
    },
    'yAxis': {
        'min': 0,
        'title': {
            'text': 'Population (millions)',
            'align': 'high'
        },
        'labels': {
            'overflow': 'justify'
        }
    },
    'tooltip': {
        'valueSuffix': ' millions'
    },
    'legend': {
        'layout': 'vertical',
        'align': 'right',
        'verticalAlign': 'top',
        'x': -40,
        'y': 80,
        'floating': True,
        'borderWidth': 1,
        'backgroundColor': "((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF')",
        'shadow': True
    },
    'credits': {
        'enabled': False
    },
    'plotOptions': {
        'bar': {
            'dataLabels': {
                'enabled': True
            }
        }
    }
}

H.set_dict_options(options)

H.add_data_set(data1, 'bar', 'Year 1800')
H.add_data_set(data2, 'bar', 'Year 1900')
H.add_data_set(data3, 'bar', 'Year 2008')
H.add_data_set(data4, 'bar', 'Year 2012')

H.htmlcontent