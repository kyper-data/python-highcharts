# -*- coding: utf-8 -*-
import json, os, sys
import pandas as pd
import numpy as np
import datetime

import highcharts

from common import JSfunction
H = highcharts.Highcharts(width=750, height=600)

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
        'series': {
            'stacking': 'normal'
        }
    }
}
H.set_dict_options(options)

H.add_data_set(data1, 'bar', 'Year 1800')
H.add_data_set(data2, 'bar', 'Year 1900')
H.add_data_set(data3, 'bar', 'Year 2008')
H.add_data_set(data4, 'bar', 'Year 2012')

H.file()