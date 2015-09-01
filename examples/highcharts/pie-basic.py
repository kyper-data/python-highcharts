# -*- coding: utf-8 -*-
"""
Highcharts Demos
Pie chart, line and column: http://www.highcharts.com/demo/pie-basic
"""
import datetime
from highcharts import Highchart

H = Highchart(width=850, height=400)

data = [{
        'name': "Microsoft Internet Explorer",
        'y': 56.33
    }, {
        'name': "Chrome",
        'y': 24.03,
        'sliced': True,
        'selected': True
    }, {
        'name': "Firefox",
        'y': 10.38
    }, {
        'name': "Safari",
        'y': 4.77
    }, {
        'name': "Opera",
        'y': 0.91
    }, {
        'name': "Proprietary or Undetectable",
        'y': 0.2
    }]
    
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

H.set_dict_options(options)

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

H.htmlcontent