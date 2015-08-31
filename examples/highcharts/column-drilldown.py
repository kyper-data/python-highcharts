# -*- coding: utf-8 -*-
"""
Highcharts Demos
Column with drilldown: http://www.highcharts.com/demo/column-drilldown
"""

from highcharts import Highchart
H = Highchart(width=850, height=400)

"""
Drilldown chart can be created using add_drilldown_data_set method: 

add_drilldown_data_set(data, series_type, id, **kwargs):
id is the drilldown parameter in upperlevel dataset (Ex. drilldown parameters in data)
drilldown dataset is constructed similar to dataset for other chart
"""

data = [{
            'name': "Microsoft Internet Explorer",
            'y': 56.33,
            'drilldown': "Microsoft Internet Explorer"
        }, {
            'name': "Chrome",
            'y': 24.030000000000005,
            'drilldown': "Chrome"
        }, {
            'name': "Firefox",
            'y': 10.38,
            'drilldown': "Firefox"
        }, {
            'name': "Safari",
            'y': 4.77,
            'drilldown': "Safari"
        }, {
            'name': "Opera",
            'y': 0.9100000000000001,
            'drilldown': "Opera"
        }, {
            'name': "Proprietary or Undetectable",
            'y': 0.2,
            'drilldown': None
        }]

data_1 = [
    ["v11.0", 24.13],
    ["v8.0", 17.2],
    ["v9.0", 8.11],
    ["v10.0", 5.33],
    ["v6.0", 1.06],
    ["v7.0", 0.5]
]

data_2 = [
    ["v40.0", 5],
    ["v41.0", 4.32],
    ["v42.0", 3.68],
    ["v39.0", 2.96],
    ["v36.0", 2.53],
    ["v43.0", 1.45],
    ["v31.0", 1.24],
    ["v35.0", 0.85],
    ["v38.0", 0.6],
    ["v32.0", 0.55],
    ["v37.0", 0.38],
    ["v33.0", 0.19],
    ["v34.0", 0.14],
    ["v30.0", 0.14]      
]

data_3 = [
    ["v35", 2.76],
    ["v36", 2.32],
    ["v37", 2.31],
    ["v34", 1.27],
    ["v38", 1.02],
    ["v31", 0.33],
    ["v33", 0.22],
    ["v32", 0.15]
]

data_4 = [
    ["v8.0", 2.56],
    ["v7.1", 0.77],
    ["v5.1", 0.42],
    ["v5.0", 0.3],
    ["v6.1", 0.29],
    ["v7.0", 0.26],
    ["v6.2", 0.17]
]

data_5 = [
    ["v12.x", 0.34],
    ["v28", 0.24],
    ["v27", 0.17],
    ["v29", 0.16]
]

options = {
    'chart': {
        'type': 'column'
    },
    'title': {
        'text': 'Browser market shares. January, 2015 to May, 2015'
    },
    'subtitle': {
        'text': 'Click the columns to view versions. Source: <a href="http://netmarketshare.com">netmarketshare.com</a>.'
    },
    'xAxis': {
        'type': 'category'
    },
    'yAxis': {
        'title': {
            'text': 'Total percent market share'
        }

    },
    'legend': {
        'enabled': False
    },
    'plotOptions': {
        'series': {
            'borderWidth': 0,
            'dataLabels': {
                'enabled': True,
                'format': '{point.y:.1f}%'
            }
        }
    },

    'tooltip': {
        'headerFormat': '<span style="font-size:11px">{series.name}</span><br>',
        'pointFormat': '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
    }, 
    
}
   
H.set_dict_options(options)

H.add_data_set(data, 'column', "Brands", colorByPoint= True)
H.add_drilldown_data_set(data_1, 'column', 'Microsoft Internet Explorer', name='Microsoft Internet Explorer' )
H.add_drilldown_data_set(data_2, 'column', 'Chrome', name='Chrome')
H.add_drilldown_data_set(data_3, 'column', 'Firefox', name='Firefox')
H.add_drilldown_data_set(data_4, 'column', 'Safari', name='Safari')
H.add_drilldown_data_set(data_5, 'column', 'Opera', name='Opera')

H.htmlcontent