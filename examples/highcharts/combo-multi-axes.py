# -*- coding: utf-8 -*-
"""
Highcharts Demos
Multiple axes: http://www.highcharts.com/demo/combo-multi-axes
"""

from highcharts import Highchart
H = Highchart(width=850, height=400)

data1 = [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
data2 = [1016, 1016, 1015.9, 1015.5, 1012.3, 1009.5, 1009.6, 1010.2, 1013.1, 1016.9, 1018.2, 1016.7]
data3 = [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]

options = {
	'chart': {
        'zoomType': 'xy'
    },
    'title': {
        'text': 'Average Monthly Weather Data for Tokyo'
    },
    'subtitle': {
        'text': 'Source: WorldClimate.com'
    },
    'xAxis': [{
        'categories': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'crosshair': True
    }],
    'yAxis': [{ 
        'labels': {
            'format': '{value}°C',
            'style': {
                'color': 'Highcharts.getOptions().colors[2]'
            }
        },
        'title': {
            'text': 'Temperature',
            'style': {
                'color': 'Highcharts.getOptions().colors[2]'
            }
        },
        'opposite': True

    }, { 
        'gridLineWidth': 0,
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
        }

    }, { 
        'gridLineWidth': 0,
        'title': {
            'text': 'Sea-Level Pressure',
            'style': {
                'color': 'Highcharts.getOptions().colors[1]'
            }
        },
        'labels': {
            'format': '{value} mb',
            'style': {
                'color': 'Highcharts.getOptions().colors[1]'
            }
        },
        'opposite': True
    }],
    'tooltip': {
        'shared': True,
        
    },
    'legend': {
        'layout': 'vertical',
        'align': 'left',
        'x': 80,
        'verticalAlign': 'top',
        'y': 55,
        'floating': True,
        'backgroundColor': "(Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'"
    },
}
H.set_dict_options(options)

H.add_data_set(data1, 'column', 'Rainfall', yAxis=1, tooltip={
                'valueSuffix': ' mm'})
H.add_data_set(data2, 'spline', 'Sea-Level Pressure', yAxis=2 ,marker={
                'enabled': False
            },
            dashStyle='shortdot',
            tooltip={
                'valueSuffix': ' mb'
            })
H.add_data_set(data3, 'spline', 'Temperature', tooltip={
                'valueSuffix': ' °C'
            })

H.htmlcontent