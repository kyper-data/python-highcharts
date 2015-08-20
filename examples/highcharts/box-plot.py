# -*- coding: utf-8 -*-
"""
Highcharts Demos
Box plot: http://www.highcharts.com/demo/box-plot
"""

from highcharts import Highchart
H = Highchart(width=550, height=400)

options = {
    'chart': {
        'type': 'boxplot'
    },
    'title': {
        'text': 'Highcharts Box Plot Example'
    },
    'legend': {
        'enabled': False
    },
    'xAxis': {
        'categories': ['1', '2', '3', '4', '5'],
        'title': {
            'text': 'Experiment No.'
        }
    },

    'yAxis': {
        'title': {
            'text': 'Observations'
        },
        'plotLines': [{
            'value': 932,
            'color': 'red',
            'width': 1,
            'label': {
                'text': 'Theoretical mean: 932',
                'align': 'center',
                'style': {
                    'color': 'gray'
                }
            }
        }]
    },
}

data =[
    [760, 801, 848, 895, 965],
    [733, 853, 939, 980, 1080],
    [714, 762, 817, 870, 918],
    [724, 802, 806, 871, 950],
    [834, 836, 864, 882, 910]
]
data_outline = [[0, 644],
                [4, 718],
                [4, 951],
                [4, 969]]

H.set_dict_options(options)
H.add_data_set(data, 'boxplot', 'Observations', tooltip = {
                'headerFormat': '<em>Experiment No {point.key}</em><br/>'})
H.add_data_set(data_outline, 'scatter', 'Outlier', marker = {
                'fillColor': 'white',
                'lineWidth': 1,
                'lineColor': 'Highcharts.getOptions().colors[0]'
            },
            tooltip = {
                'pointFormat': 'Observation: {point.y}'
            })

H.htmlcontent
