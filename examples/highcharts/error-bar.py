# -*- coding: utf-8 -*-
"""
Highcharts Demos
Error bar: http://www.highcharts.com/demo/error-bar
"""

from highcharts import Highchart
H = Highchart(width=550, height=400)

options = {
	'chart': {
        'zoomType': 'xy'
    },
    'title': {
        'text': 'Temperature vs Rainfall'
    },
    'xAxis': [{
        'categories': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    }],
    'yAxis': [{ 
        'labels': {
            'format': '{value} °C',
            'style': {
                'color': 'Highcharts.getOptions().colors[1]'
            }
        },
        'title': {
            'text': 'Temperature',
            'style': {
                'color': 'Highcharts.getOptions().colors[1]'
            }
        }
    }, { 
        'title': {
            'text': 'Rainfall',
            'style': {
                'color': 'Highcharts.getOptions().colors[0]'
            }
        },
        'labels': {
            'format': '{value} mm',
            'style': {
                'color': 'Highcharts.getOptions().colors[0]'
            }
        },
        'max': 250,
        'opposite': True
    }],

    'tooltip': {
        'shared': True
    },
}

data1 = [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
data2 = [[48, 51], [68, 73], [92, 110], [128, 136], [140, 150], [171, 179], [135, 143], [142, 149], [204, 220], [189, 199], [95, 110], [52, 56]]
data3 = [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
data4 = [[6, 8], [5.9, 7.6], [9.4, 10.4], [14.1, 15.9], [18.0, 20.1], [21.0, 24.0], [23.2, 25.3], [26.1, 27.8], [23.2, 23.9], [18.0, 21.1], [12.9, 14.0], [7.6, 10.0]]

H.set_dict_options(options)
H.add_data_set(data1, 'column', 'Rainfall', yAxis = 1, tooltip = {
                'pointFormat': '<span style="font-weight: bold; color: {series.color}">{series.name}</span>: <b>{point.y:.1f} mm</b> '
            })
H.add_data_set(data2, 'errorbar', 'Rainfall error', yAxis = 1, tooltip = {
                'pointFormat': '(error range: {point.low}-{point.high} mm)<br/>'
            })
H.add_data_set(data3, 'spline', 'Temperature', tooltip = {
                'pointFormat': '<span style="font-weight: bold; color: {series.color}">{series.name}</span>: <b>{point.y:.1f}°C</b> '
            })
H.add_data_set(data4, 'errorbar', 'Temperature error', tooltip = {
                'pointFormat': '(error range: {point.low}-{point.high}°C)<br/>'
            })

H.htmlcontent

