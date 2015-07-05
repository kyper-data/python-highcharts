# -*- coding: utf-8 -*-
import json, os, sys
import pandas as pd
import numpy as np
import datetime

sys.path.append('/Users/hankchu/Documents/python-highcharts/highmaps')

import highmaps
H = highmaps.Highmaps(width = 650, height = 500)

options = {
                                   
            'chart' :{ 'renderTo' : 'container'
            },
                                   
            'title' : {
                'text' : 'GeoJSON in Highmaps'
            },

            'mapNavigation': {
                'enabled': True,
                'buttonOptions': {
                    'verticalAlign': 'bottom'
                }
            },

            'colorAxis': {
            },
        } 

data = [
        {
            "code": "DE.SH",
            "value": 728
        },
        {
            "code": "DE.BE",
            "value": 710
        },
        {
            "code": "DE.MV",
            "value": 963
        },
        {
            "code": "DE.HB",
            "value": 541
        },
        {
            "code": "DE.HH",
            "value": 622
        },
        {
            "code": "DE.RP",
            "value": 866
        },
        {
            "code": "DE.SL",
            "value": 398
        },
        {
            "code": "DE.BY",
            "value": 785
        },
        {
            "code": "DE.SN",
            "value": 223
        },
        {
            "code": "DE.ST",
            "value": 605
        },
        {
            "code": "DE.",
            "value": 361
        },
        {
            "code": "DE.NW",
            "value": 237
        },
        {
            "code": "DE.BW",
            "value": 157
        },
        {
            "code": "DE.HE",
            "value": 134
        },
        {
            "code": "DE.NI",
            "value": 136
        },
        {
            "code": "DE.TH",
            "value": 704
        }
    ]
H.set_dict_optoins(options)
H.add_data_set(data, 'map', 'Random data', joinBy =  ['code_hasc', 'code'],
                states = {
                    'hover': {
                        'color': '#BADA55'
                    }
                },
                dataLabels =  {
                    'enabled': True,
                    'format': '{point.properties.postal}'
                })

H.set_map_source('http://www.highcharts.com/samples/data/jsonp.php?filename=germany.geo.json&callback=?', True)
H.file()