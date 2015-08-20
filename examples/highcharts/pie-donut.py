# -*- coding: utf-8 -*-
"""
Highcharts Demos
Donut chart: http://www.highcharts.com/demo/pie-donut
"""

from highcharts import Highchart
H = Highchart(width = 850, height = 400)

data = [{
            'y': 55.11,
            'color': 'Highcharts.getOptions().colors[0]',
            'drilldown': {
                'name': 'MSIE versions',
                'categories': ['MSIE 6.0', 'MSIE 7.0', 'MSIE 8.0', 'MSIE 9.0'],
                'data': [10.85, 7.35, 33.06, 2.81],
                'color': 'Highcharts.getOptions().colors[0]'
            }
        }, {
            'y': 21.63,
            'color': 'Highcharts.getOptions().colors[1]',
            'drilldown': {
                'name': 'Firefox versions',
                'categories': ['Firefox 2.0', 'Firefox 3.0', 'Firefox 3.5', 'Firefox 3.6', 'Firefox 4.0'],
                'data': [0.20, 0.83, 1.58, 13.12, 5.43],
                'color': 'Highcharts.getOptions().colors[1]'
            }
        }, {
            'y': 11.94,
            'color': 'Highcharts.getOptions().colors[2]',
            'drilldown': {
                'name': 'Chrome versions',
                'categories': ['Chrome 5.0', 'Chrome 6.0', 'Chrome 7.0', 'Chrome 8.0', 'Chrome 9.0',
                    'Chrome 10.0', 'Chrome 11.0', 'Chrome 12.0'],
                'data': [0.12, 0.19, 0.12, 0.36, 0.32, 9.91, 0.50, 0.22],
                'color': 'Highcharts.getOptions().colors[2]'
            }
        }, {
            'y': 7.15,
            'color': 'Highcharts.getOptions().colors[3]',
            'drilldown': {
                'name': 'Safari versions',
                'categories': ['Safari 5.0', 'Safari 4.0', 'Safari Win 5.0', 'Safari 4.1', 'Safari/Maxthon',
                    'Safari 3.1', 'Safari 4.1'],
                'data': [4.55, 1.42, 0.23, 0.21, 0.20, 0.19, 0.14],
                'color': 'Highcharts.getOptions().colors[3]'
            }
        }, {
            'y': 2.14,
            'color': 'Highcharts.getOptions().colors[4]',
            'drilldown': {
                'name': 'Opera versions',
                'categories': ['Opera 9.x', 'Opera 10.x', 'Opera 11.x'],
                'data': [ 0.12, 0.37, 1.65],
                'color': 'Highcharts.getOptions().colors[4]'
            }
        }]

options = {
	'chart': {
        'type': 'pie'
    },
    'title': {
        'text': 'Browser market share, April, 2011'
    },
    'yAxis': {
        'title': {
            'text': 'Total percent market share'
        }
    },
    'plotOptions': {
        'pie': {
            'shadow': False,
            'center': ['50%', '50%']
        }
    },
    'tooltip': {
        'valueSuffix': '%'
    },
}


categories = ['MSIE', 'Firefox', 'Chrome', 'Safari', 'Opera']
browserData = []
versionsData = []

for i in range(len(data)):

    browserData.append({
        'name': categories[i],
        'y': data[i]['y'],
        'color': data[i]['color']
        })

    drillDataLen = len(data[i]['drilldown']['data'])
    for j in range(drillDataLen): 

        brightness = 0.2 - (j / drillDataLen) / 5;
        versionsData.append({
            'name': data[i]['drilldown']['categories'][j],
            'y': data[i]['drilldown']['data'][j],
            'color': 'Highcharts.Color(' + data[i]['color'] + ').brighten(' + str(brightness) + ').get()'
        })
        
H.set_dict_options(options)

H.add_data_set(browserData, 'pie', 'Browsers', size='60%',
            dataLabels={
                'formatter': 'function () { \
                                    return this.y > 5 ? this.point.name : null;\
                                }',
                'color': 'white',
                'distance': -30
            })

H.add_data_set(versionsData, 'pie', 'Versions', size='80%',
            innerSize='60%',
            dataLabels={
                'formatter': "function () {\
                                    return this.y > 1 ? '<b>' + this.point.name + ':</b> ' + this.y + '%'  : null;\
                                }"
            })

H.htmlcontent