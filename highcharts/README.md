# Project: Python-Highcharts

## License

Please be aware that highcharts is only free for non-commercial use: Pop over to [Highcharts](http://shop.highsoft.com/) for licencing information.

## Overview

Python-Highcharts is python API(s) for Highcharts projects (highcharts, highmaps, and highstocks). 

The frame was originated from PyHighcharts on Github but alienated from it since PyHighcharts is moving toward to more function-based wrapper

## Installation

 -need to work on this-

---------------------------------------------------------------------------------------------------------------
# Highcharts

## Design Overview

The usage is designed to close to it on Javascript. 

The main input is a python dictionary similart to options object, and the dictionary contains and handles most options listed in highcharts. 

Only the data_set(s) need to be input by separated function 

```python
from highcharts import Highcharts

# A chart is the container that your data will be rendered in, it can (obviously) support multiple data series within it.
chart = Highcharts()

# Adding a series requires a minimum of two arguments, the series type and an array of data points
data = range(1,20)
chart.add_data_set(data,'line','Example Series')

# This will generate and save a .html file at the location you assign
chart.file()
```

You can add chart option using set_options. Ex.
```python
chart.set_options('chart',{'resetZoomButton':{'relativeTo':'plot', 'position':{'x':0,'y':-30}}})
chart.set_options('xAxis',{'events':{'afterBreaks':'function(e){return}'}})
chart.set_options('tooltip',{'formatter':'default_tooltip'})

```

set_options function can update the options automatically if you input the same option_type. Ex. 
```python
chart.set_options('chart',{'style':{"fontfontSize": '22px'}})
chart.set_options('chart',{'resetZoomButton':{'position':{'x':10}}})
chart.set_options('chart',{'resetZoomButton':{'relativeTo':'chart'}})
chart.set_options('xAxis',{'plotBands':{'color': '#FCFFC5','from': 2, 'to':4}})
chart.set_options('xAxis',{'plotBands':{'color': '#FCFFC5','from': 6, 'to':8}})
chart.set_options('xAxis',{'plotBands':{'color': '#FCFFC5','from': 10, 'to':12}})

```

However, the better practice is to construct chart options by a dictionary (as highcharts suggests: http://www.highcharts.com/docs/getting-started/your-first-chart) and then input by set_dict_optoins function. Ex.

```python
options = {
        'title': {
            'text': 'Atmosphere Temperature by Altitude'
        },
        'subtitle': {
            'text': 'According to the Standard Atmosphere Model'
        },
        'xAxis': {
            'reversed': False,
            'title': {
                'enabled': True,
                'text': 'Altitude'
            },
            'labels': {
                'formatter': 'function () {\
                                    return this.value + "km";\
                                }'
            },
            'maxPadding': 0.05,
            'showLastLabel': True
        },
        'yAxis': {
            'title': {
                'text': 'Temperature'
            },
            'labels': {
                "formatter": "function () {\
                                                    return this.value + '°';\
                                                }"
            },
            'lineWidth': 2
        },
        'legend': {
            'enabled': False
        },
        'tooltip': {
            'headerFormat': '<b>{series.name}</b><br/>',
            'pointFormat': '{point.x} km: {point.y}°C'
        }
        }

chart.set_dict_optoins(options)

```
            
Only the series option in highchart needs to input by separated add_data_set (or/and add_drilldown_data_set) function, Ex.

```python
chart.add_data_set(data, 'scatter', 'Outlier', marker = {
                'fillColor': 'white',
                'lineWidth': 1,
                'lineColor': 'Highcharts.getOptions().colors[0]'
            },
            tooltip = {
                'pointFormat': 'Observation: {point.y}'
            })


chart.add_drilldown_data_set(data_2, 'column', 'Chrome', name = 'Chrome')

```


## Usage

```python
from highcharts import Highcharts
chart = Highcharts()

chart.set_options('chart', {'inverted': True})

options = {
        'title': {
            'text': 'Atmosphere Temperature by Altitude'
        },
        'subtitle': {
            'text': 'According to the Standard Atmosphere Model'
        },
        'xAxis': {
            'reversed': False,
            'title': {
                'enabled': True,
                'text': 'Altitude'
            },
            'labels': {
                'formatter': 'function () {\
                                    return this.value + "km";\
                                }'
            },
            'maxPadding': 0.05,
            'showLastLabel': True
        },
        'yAxis': {
            'title': {
                'text': 'Temperature'
            },
            'labels': {
                "formatter": "function () {\
                                                    return this.value + '°';\
                                                }"
            },
            'lineWidth': 2
        },
        'legend': {
            'enabled': False
        },
        'tooltip': {
            'headerFormat': '<b>{series.name}</b><br/>',
            'pointFormat': '{point.x} km: {point.y}°C'
        }
        }

chart.set_dict_optoins(options)
data =  [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1], 
        [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
chart.add_data_set(data, 'spline', 'Temperature', marker = {'enabled': False}) 

chart.file()

```

## Todo:

* More charts support
* Clean code and put more explanation
* Unittests

Reference: [Highcharts API](http://api.highcharts.com/highcharts)
