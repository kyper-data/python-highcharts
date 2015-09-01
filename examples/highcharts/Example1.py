
# -*- coding: utf-8 -*-
"""
Basic example for python-highcharts

All datasets need to input using "add_data_set" method
Highchart options can be either set by "set_options" method as showing here or
construct a option dictionary object and input using "set_dict_options" method
"""

from highcharts import Highchart # import highchart library
H = Highchart() # setup highchart instance

data = list(range(1,20))
data2 = list(range(20,1,-1)) # generate some random datasets

"""
Each dataset needs to input using add_data_set and add_data_from_jsonp (not recommended) methods

1. add_data_set(data, series_type="line", name=None, **kwargs)
    1. data is the dataset for chart 
    2. series_type (default: "line") is the type of plot this dataset will be presented 
    3. name is the variable name of dateset(default: Series X) used in python
    4. kwargs are for parameters in series or plotOptions 
        (for detail please ref to highcharts API: http://api.highcharts.com/highcharts#)

2. add_data_from_jsonp(data_src, data_name='json_data', series_type="line", name=None, **kwargs)
    add dataset from the data_src using jsonp. It is converted to jquery function "$.getJSON" in javascript environment
    1. data_src is the url (https) for the dataset
    2. data_name is the variable name of dataset. This name is used for javascript environment (not in python)
    3. series_type( default: "line") is the type of plot this dataset will be presented
    4. kwargs are for parameters in series or plotOptions 
        (for detail please ref to highcharts API: http://api.highcharts.com/highcharts#)
"""
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

"""
Set up highchart options using 
1. set_options method:  
    set_options(option_type, option_dict)
    option_type is the keyword for highchart options
    option_dict is (python) dict for option settings
    (for option details please ref to highcharts API: http://api.highcharts.com/highcharts#)
"""
H.set_options('chart', {'resetZoomButton': {'relativeTo': 'plot', 'position': {'x': 0, 'y': -30}}})
H.set_options('xAxis', {'events': {'afterBreaks': 'function(e){return}'}})
H.set_options('tooltip', {'formatter': 'default_tooltip'})
H.set_options('xAxis', {'events': {'pointBreak': 'function(e){return}'}})
H.set_options('chart', {'style': {'fontFamily': 'Lucida Grande, sans-serif', "fontfontSize": '12px'}})
H.set_options('chart', {'style': {"fontfontSize": '22px'}})
H.set_options('chart', {'resetZoomButton': {'position': {'x': 10}}})
H.set_options('chart', {'resetZoomButton': {'relativeTo': 'chart'}})

"""
Set up highchart options using 
2. set_dict_options method: 
    set_dict_options(options)
    option is a (python) dict for options settings

The way to use this method is very similar to the options object as on highcharts docs:
http://www.highcharts.com/docs/getting-started/how-to-set-options
1. construct option (python) dict similar to the option object in javascript
2. input option dict using set_dict_options
(for all the option details please ref to highcharts API: http://api.highcharts.com/highcharts#)
"""
options = {
    'xAxis':{
        'plotBands': 
            [{'color': '#FCFFC5', 'from': 2, 'to': 4}, 
            {'color': '#FCFFC5', 'from': 6, 'to': 8},
            {'color': '#FCFFC5', 'from': 10, 'to': 12}]
        }
}
H.set_dict_options(options) # input option object using set_dict_options method

H # showing the chart on ipython 
H.save_file('highcharts') # save result as .html file with input name (and location path)