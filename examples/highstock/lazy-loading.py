# -*- coding: utf-8 -*-
"""
Highstock Demos
1.7 million points with async loading: http://www.highcharts.com/stock/demo/lazy-loading
"""

"""
This example generates a candlestick chart, which updates (async loading) when a different time period is selected
by the navigation bar due to the large dataset.

Due to the update, this chart requires JS function in the beginning and xAxis.events options.
"""

from highcharts import Highstock
H = Highstock()

data_url = 'http://www.highcharts.com/samples/data/from-sql.php?callback=?'
H.add_data_from_jsonp(data_url, 'json_data', 'candlestick', dataGrouping = {'enabled': False})

script = """json_data = [].concat(json_data, [[Date.UTC(2011, 9, 14, 19, 59), null, null, null, null]]);"""
H.add_JSscript(script, 'head')

H.add_navi_series_from_jsonp() # not really useful, but it shows in highstock demo

options = {
    'chart' : {
        'zoomType': 'x'
    },

    'navigator' : {
        'adaptToUpdatedData': False,
    },

    'scrollbar': {
        'liveRedraw': False
    },

    'title': {
        'text': 'AAPL history by the minute from 1998 to 2011'
    },

    'subtitle': {
        'text': 'Displaying 1.7 million data points in Highcharts Stock by async server loading'
    },

    'rangeSelector' : {
        'buttons': [{
            'type': 'hour',
            'count': 1,
            'text': '1h'
        }, {
            'type': 'day',
            'count': 1,
            'text': '1d'
        }, {
            'type': 'month',
            'count': 1,
            'text': '1m'
        }, {
            'type': 'year',
            'count': 1,
            'text': '1y'
        }, {
            'type': 'all',
            'text': 'All'
        }],
        'inputEnabled': False, # it supports only days
        'selected' : 4 # all
    },

    'xAxis' : {
        'events' : {
            'afterSetExtremes' : """function afterSetExtremes(e) {

        var chart = $('#container').highcharts();

        chart.showLoading('Loading data from server...');
        $.getJSON('http://www.highcharts.com/samples/data/from-sql.php?start=' + Math.round(e.min) +
                '&end=' + Math.round(e.max) + '&callback=?', function (data) {

                chart.series[0].setData(data);
                chart.hideLoading();
            });
    }"""
        },
        'minRange': 3600 * 1000 # one hour
    },

    'yAxis': {
        'floor': 0
    },

}

H.set_dict_options(options)

H.htmlcontent