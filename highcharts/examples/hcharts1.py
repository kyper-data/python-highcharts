import json, os, sys
import pandas as pd
import numpy as np

import highcharts

H = highcharts.Highcharts()

data = range(1,20)
data2 = range(20,1,-1)
H.add_data_set(data2,'line')
H.add_data_set(data, 'line', 
    marker={
        'states': {
            'hover': {
                'enabled': True, 
                'fillColor': 'white', 
                'lineColor': 'red',
                'lineWidth': 2
            }
        }
    },
    events={
        'click': "function (event) { alert(this.name + ' clicked\\n' + 'Alt: ' + event.altKey + '\\n' + \
                 'Control: ' + event.ctrlKey + '\\n' + 'Shift: ' + event.shiftKey + '\\n');}"}, 
    dashStyle='ShortDash'
)


H.set_options('chart', {'resetZoomButton': {'relativeTo': 'plot', 'position': {'x': 0, 'y': -30}}})
H.set_options('xAxis', {'events': {'afterBreaks': 'function(e){return}'}})
H.set_options('tooltip', {'formatter': 'default_tooltip'})
H.set_options('xAxis', {'events': {'pointBreak': 'function(e){return}'}})
H.set_options('chart', {'style': {'fontFamily': 'Lucida Grande, sans-serif', "fontfontSize": '12px'}})
H.set_options('chart', {'style': {"fontfontSize": '22px'}})
H.set_options('chart', {'resetZoomButton': {'position': {'x': 10}}})
H.set_options('chart', {'resetZoomButton': {'relativeTo': 'chart'}})
H.set_options('xAxis', {'plotBands': {'color': '#FCFFC5', 'from': 2, 'to': 4}})
H.set_options('xAxis', {'plotBands': {'color': '#FCFFC5', 'from': 6, 'to': 8}})
H.set_options('xAxis', {'plotBands': {'color': '#FCFFC5', 'from': 10, 'to': 12}})

H.file()