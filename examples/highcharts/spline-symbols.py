# -*- coding: utf-8 -*-
"""
Highcharts Demos
Spline with symbols: http://www.highcharts.com/demo/spline-symbols
"""

from highcharts import Highchart
H = Highchart()


options = {
    'title': {
                'text': 'Monthly Average Temperature'
            },
    'subtitle': {
        'text': 'Source: WorldClimate.com'
    },
    'xAxis': {
        'categories': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    },
    'yAxis': {
        'title': {
            'text': 'Temperature'
        },
        'labels': {
            'formatter': u'function () {\
                            return this.value + "°";\
                        }'
        }
    },
    'tooltip': {
        'crosshairs': True,
        'shared': True,
        'pointFormat': '{series.name}: {point.y}°C <br>'
    }
}


H.set_dict_options(options) 

data1 =  [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, {
                'y': 26.5,
                'marker': {
                    'symbol': 'url(http://www.highcharts.com/demo/gfx/sun.png)'
                }
            }, 23.3, 18.3, 13.9, 9.6]
data2 = [{'y': 3.9,'marker': {
                    'symbol': 'url(http://www.highcharts.com/demo/gfx/snow.png)'
                }
            }, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]


H.add_data_set(data1, 'spline', 'Tokyo', marker={
                'symbol': 'square'
            })
H.add_data_set(data2, 'spline', 'London', marker={
                'symbol': 'diamond'
            }) 

H.htmlcontent