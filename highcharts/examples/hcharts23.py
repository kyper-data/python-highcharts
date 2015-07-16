# -*- coding: utf-8 -*-
import json, os, sys
import pandas as pd
import numpy as np
import datetime

import highcharts

H = highcharts.Highcharts(width=550, height=400)

options = {
	'title': {
        'text': 'Highcharts Treemap'
    }
}

data = [{
            'id': "id_1",
            'name': 'A'
        }, {
            'id': "id_2",
            'name': 'A1',
            'value': 2,
            'parent': 'id_1'
        }, {
            'id': "id_3",
            'name': 'A2',
            'value': 2,
            'parent': 'id_1'
        }, {
            'id': "id_4",
            'name': 'A3',
            'value': 2,
            'parent': 'id_1'
        }, {
            'name': 'B',
            'value': 6
        }, {
            'name': 'C',
            'value': 4
        }, {
            'name': 'D',
            'value': 3
        }, {
            'name': 'E',
            'value': 2
        }, {
            'name': 'F',
            'value': 2
        }, {
            'name': 'G',
            'value': 1
        }]

H.set_dict_options(options)
H.add_data_set(data, 'treemap', layoutAlgorithm='squarified',
            levels = [{
                'level': 1,
                'borderWidth': '3px',
                'dataLabels': {
                    'enabled': True,
                    'align': 'left',
                    'verticalAlign': 'top',
                    'color': 'white',
                    'style': {
                        'fontWeight': 'bold'
                    }
                }
            }, {
                'level': 2,
                'layoutAlgorithm': 'stripes'
            }])

H.file()