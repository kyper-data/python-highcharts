# -*- coding: utf-8 -*-
import json, os, sys
import pandas as pd
import numpy as np
import datetime

import highcharts

H = highcharts.Highchart(width=850, height=400)

data = [
                ['Firefox',   45.0],
                ['IE',       26.8],
                {
                    'name': 'Chrome',
                    'y': 12.8,
                    'sliced': True,
                    'selected': True
                },
                ['Safari',    8.5],
                ['Opera',     6.2],
                ['Others',   0.7]
            ]

options = {
		'chart': {
            'plotBackgroundColor': None,
            'plotBorderWidth': None,
            'plotShadow': False
        },
        'title': {
            'text': 'Browser market shares at a specific website, 2014'
        },
        'tooltip': {
            'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
    }

H.set_dict_optoins(options)

H.add_data_set(data, 'pie', 'Browser share', allowPointSelect=True,
                cursor='pointer',
                showInLegend=True,
                dataLabels={
                    'enabled': False,
                    'format': '<b>{point.name}</b>: {point.percentage:.1f} %',
                    'style': {
                        'color': "(Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'"
                    }
                }
            )

H.save_file()