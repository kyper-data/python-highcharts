# -*- coding: utf-8 -*-
"""
Highcharts Demos
Stacked and grouped column: http://www.highcharts.com/demo/column-stacked-and-grouped
"""
from highcharts import Highchart

H = Highchart(width=750, height=600)

data1 = [5, 3, 4, 7, 2]
data2 = [3, 4, 4, 2, 5]
data3 = [2, 5, 6, 2, 1]
data4 = [3, 0, 4, 4, 3]

options = {
	'title': {
        'text': 'Total fruit consumtion, grouped by gender'
    },

    'xAxis': {
        'categories': ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
    },

    'yAxis': {
        'allowDecimals': False,
        'min': 0,
        'title': {
            'text': 'Number of fruits'
        }
    },

    'tooltip': {
        'formatter': "function () {\
                        return '<b>' + this.x + '</b><br/>' +\
                            this.series.name + ': ' + this.y + '<br/>' +\
                            'Total: ' + this.point.stackTotal;\
                    }"
    },
    'plotOptions': {
        'column': {
            'stacking': 'normal'
        }
    }
}
H.set_dict_options(options)

H.add_data_set(data1, 'column', 'John', stack='male' )
H.add_data_set(data2, 'column', 'Joe', stack='male')
H.add_data_set(data3, 'column', 'Jane', stack='female')
H.add_data_set(data4, 'column', 'Janet', stack='female')

H.htmlcontent