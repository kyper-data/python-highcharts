# -*- coding: utf-8 -*-
"""
Highcharts Demos
Spline with inverted axes: http://www.highcharts.com/demo/spline-inverted
"""
from highcharts import Highchart
H = Highchart()

# set option 
H.set_options('chart', {'inverted': True})

# highchart option can be also set as a dict object
# first construct the dict object for all the options:
options = {
    'title': {
        'text': 'Atmosphere Temperature by Altitude'
    },
    'subtitle': {
        'text': 'According to the Standard Atmosphere Model'
    },
    'xAxis': {
        'reversed': False,
        'title': {
            'enabled': True,
            'text': 'Altitude'
        },
        'labels': {
            'formatter': 'function () {\
                                return this.value + "km";\
                            }'
        },
        'maxPadding': 0.05,
        'showLastLabel': True
    },
    'yAxis': {
        'title': {
            'text': 'Temperature'
        },
        'labels': {
            "formatter": u"function () {\
                                                return this.value + '°';\
                                            }"
        },
        'lineWidth': 2
    },
    'legend': {
        'enabled': False
    },
    'tooltip': {
        'headerFormat': '<b>{series.name}</b><br/>',
        'pointFormat': '{point.x} km: {point.y}°C'
    }
}
# then input using set_dict_options method
H.set_dict_options(options)
data =  [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1], 
		[50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
H.add_data_set(data, 'spline', 'Temperature', marker={'enabled': False}) 

H.htmlcontent