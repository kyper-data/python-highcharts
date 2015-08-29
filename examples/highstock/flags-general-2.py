# -*- coding: utf-8 -*-
"""
Highstock Demos
Flags marking events: http://www.highcharts.com/stock/demo/flags-general
"""

"""
This example generates the same chart as flags-general.py
But instead of copying from the website, the dataset is queried direcly using jsonp_loader
The json doc from the url is not in the correct format (lack of quotes), so the sub_d and sub_by parameters
are used to fix the problem.
"""

import datetime
from highcharts import Highstock
from highcharts.highstock.highstock_helper import jsonp_loader
H = Highstock()

data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=usdeur.json&callback=?'
data = jsonp_loader(data_url, 
    sub_d = r'(Date\.UTC\(([0-9]+,[0-9]+,[0-9]+)(,[0-9]+,[0-9]+,[0-9]+)?(,[0-9]+)?\))', 
    sub_by = r'"\1"') # data from url is not in right json format

data2 = [{
        'x' : datetime.datetime(2015, 6, 8),
        'title' : 'C',
        'text' : 'Stocks fall on Greece, rate concerns; US dollar dips'
    }, {
        'x' : datetime.datetime(2015, 6, 12),
        'title' : 'D',
        'text' : 'Zimbabwe ditches \'worthless\' currency for the US dollar '
    }, {
        'x' : datetime.datetime(2015, 6, 19),
        'title' : 'E',
        'text' : 'US Dollar Declines Over the Week on Rate Timeline'
    }, {
        'x' : datetime.datetime(2015, 6, 26),
        'title' : 'F',
        'text' : 'Greek Negotiations Take Sharp Turn for Worse, US Dollar set to Rally '
    }, {
        'x' : datetime.datetime(2015, 6, 29),
        'title' : 'G',
        'text' : 'Euro records stunning reversal against dollar'
    }, {
        'x' : datetime.datetime(2015, 6, 30),
        'title' : 'H',
        'text' : 'Surging US dollar curbs global IT spend'
    }]

H.add_data_set(data, 'line', 'USD to EUR', id = 'dataseries')
H.add_data_set(data2, 'flags', onSeries = 'dataseries',
                shape = 'circlepin',
                width = 16)

options = {
    'rangeSelector' : {
        'selected' : 0
    },

    'title' : {
        'text' : 'USD to EUR exchange rate'
    },
    'tooltip': {
                'style': {
                    'width': '200px'
                },
                'valueDecimals': 4,
                'shared' : True
            },

    'yAxis' : {
        'title' : {
            'text' : 'Exchange rate'
        }
    },

}

H.set_dict_options(options)

H.htmlcontent