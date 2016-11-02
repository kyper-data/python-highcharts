# -*- coding: utf-8 -*-
"""
Highcharts Demos
Time data with irregular intervals: http://www.highcharts.com/demo/spline-irregular-time
"""
from datetime import datetime
from highcharts import Highchart
H = Highchart()

winter_12_13_data = [
    [datetime(1970, 10, 21), 0],
    [datetime(1970, 11, 4), 0.28],
    [datetime(1970, 11, 9), 0.25],
    [datetime(1970, 11, 27), 0.2],
    [datetime(1970, 12, 2), 0.28],
    [datetime(1970, 12, 26), 0.28],
    [datetime(1970, 12, 29), 0.47],
    [datetime(1971, 1, 11), 0.79],
    [datetime(1971, 1, 26), 0.72],
    [datetime(1971, 2, 3), 1.02],
    [datetime(1971, 2, 11), 1.12],
    [datetime(1971, 2, 25), 1.2],
    [datetime(1971, 3, 11), 1.18],
    [datetime(1971, 4, 11), 1.19],
    [datetime(1971, 5, 1), 1.85],
    [datetime(1971, 5, 5), 2.22],
    [datetime(1971, 5, 19), 1.15],
    [datetime(1971, 6, 3), 0]
]

winter_13_14_data = [
    [datetime(1970, 10, 29), 0],
    [datetime(1970, 11, 9), 0.4],
    [datetime(1970, 12, 1), 0.25],
    [datetime(1971, 1, 1), 1.66],
    [datetime(1971, 1, 10), 1.8],
    [datetime(1971, 2, 19), 1.76],
    [datetime(1971, 3, 25), 2.62],
    [datetime(1971, 4, 19), 2.41],
    [datetime(1971, 4, 30), 2.05],
    [datetime(1971, 5, 14), 1.7],
    [datetime(1971, 5, 24), 1.1],
    [datetime(1971, 6, 10), 0]
]

winter_14_15_data = [
    [datetime(1970, 11, 25), 0],
    [datetime(1970, 12, 6), 0.25],
    [datetime(1970, 12, 20), 1.41],
    [datetime(1970, 12, 25), 1.64],
    [datetime(1971, 1, 4), 1.6],
    [datetime(1971, 1, 17), 2.55],
    [datetime(1971, 1, 24), 2.62],
    [datetime(1971, 2, 4), 2.5],
    [datetime(1971, 2, 14), 2.42],
    [datetime(1971, 3, 6), 2.74],
    [datetime(1971, 3, 14), 2.62],
    [datetime(1971, 3, 24), 2.6],
    [datetime(1971, 4, 2), 2.81],
    [datetime(1971, 4, 12), 2.63],
    [datetime(1971, 4, 28), 2.77],
    [datetime(1971, 5, 5), 2.68],
    [datetime(1971, 5, 10), 2.56],
    [datetime(1971, 5, 15), 2.39],
    [datetime(1971, 5, 20), 2.3],
    [datetime(1971, 6, 5), 2],
    [datetime(1971, 6, 10), 1.85],
    [datetime(1971, 6, 15), 1.49],
    [datetime(1971, 6, 23), 1.08]
]

H.add_data_set(winter_12_13_data, series_type="spline", name="Winter 2012-2013")
H.add_data_set(winter_13_14_data, series_type="spline", name="Winter 2013-2014")
H.add_data_set(winter_14_15_data, series_type="spline", name="Winter 2014-2015")

H.set_options('chart', {
    'type': 'spline'
})

H.set_options('xAxis', {
    'type': 'datetime',
    'dateTimeLabelFormats': { # don't display the dummy year
        'month': '%e. %b',
        'year': '%b'
    },
    'title': {
        'text': 'Date'
    }
})

H.set_options('yAxis', {
    'title': {
        'text': 'Snow depth (m)'
    },
    'min': 0
})

H.set_options('title', {
    'text': "Snow depth at Vikjafjellet, Norway"
})

H.set_options('subtitle', {
    'text': "Irregular time data in Highcharts JS"
})

H.set_options('tooltip', {
    'headerFormat': '<b>{series.name}</b><br>',
    'pointFormat': '{point.x:%e. %b}: {point.y:.2f} m'
})

H.set_options('plotOptions', {
    'spline': {
        'marker': {
            'enabled': True
        }
    }
})

H.htmlcontent