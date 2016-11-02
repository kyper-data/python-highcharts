# python-highcharts [![CircleCI](https://circleci.com/gh/kyper-data/python-highcharts.svg?style=svg)](https://circleci.com/gh/kyper-data/python-highcharts)

## License

The python-highcharts wrapper is licensed under the [MIT license](http://opensource.org/licenses/MIT).

However, please be aware that the Highcharts project itself, as well as Highmaps and Highstock, are only free for non-commercial use under the Creative Commons Attribution-NonCommercial license. Commercial use requires the purchase of a separate license. Pop over to [Highcharts](http://shop.highsoft.com/) for more information.

## Overview

python-highcharts is a simple translation layer between Python and Javascript for Highcharts projects (highcharts, highmaps, and highstocks).

In addition, python-highcharts integrates with [Jupyter notebook](https://github.com/jupyter/notebook), which enables you to render Highcharts, Highmaps, and Highstock visualizations directly in notebooks. See examples [here](https://github.com/kyper-data/python-highcharts/tree/developer/examples/ipynb).

The original framework was inspired by [python-nvd3](https://github.com/areski/python-nvd3) and [PyHighcharts](https://github.com/fidyeates/PyHighcharts).

## Installation

python-highcharts supports Python 2.7/3.4+ and is available on PyPI. To install:
```
pip install python-highcharts
```

---------------------------------------------------------------------------------------------------------------
# Highcharts/Highstock

## Basic Usage

Usage of python-highcharts is very similar to usage of the original Javascript library. 

The main input is a python dictionary similar to Highcharts's 'options' object. The dictionary supports most options listed in the official [Highcharts documentation](http://api.highcharts.com/highcharts). 

However, the data_set(s) need to be input by a separate function.

```python
from highcharts import Highchart

# A chart is the container that your data will be rendered in, it can (obviously) support multiple data series within it.
chart = Highchart()

# Adding a series requires at minimum an array of data points. 
# You can also change the series type, the name, or other series options as kwargs.
data = range(1,20)
chart.add_data_set(data, series_type='line', name='Example Series')

# This will generate and save a .html file at the location you assign
chart.save_file()
```

You can add chart options using set_options. Ex:
```python
chart.set_options('chart', {'resetZoomButton': {'relativeTo': 'plot', 'position': {'x': 0,'y': -30}}})
chart.set_options('xAxis', {'events': {'afterBreaks': 'function(e){return}'}})
chart.set_options('tooltip', {'formatter': 'default_tooltip'})
```

The set_options function can update the options automatically if you input the same option_type. Ex:
```python
chart.set_options('chart', {'style': {"fontSize": '22px'}})
chart.set_options('chart', {'resetZoomButton': {'position': {'x': 10}}})
chart.set_options('chart', {'resetZoomButton': {'relativeTo': 'chart'}})
chart.set_options('xAxis', {'plotBands': {'color': '#FCFFC5', 'from': 2, 'to': 4}})
chart.set_options('xAxis', {'plotBands': {'color': '#FCFFC5', 'from': 6, 'to': 8}})
chart.set_options('xAxis', {'plotBands': {'color': '#FCFFC5', 'from': 10, 'to': 12}})
```

However, the better practice is to construct chart options by a dictionary (as Highcharts suggests: http://www.highcharts.com/docs/getting-started/your-first-chart) and then input by the set_dict_options function. Ex:
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
            'formatter': "function () {\
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

chart.set_dict_options(options)
```

Unlike Javascript Highcharts, the series option can't be included in the options dictionary. It needs to input by the add_data_set (and/or add_drilldown_data_set) function, Ex:
```python
chart.add_data_set(data, 'scatter', 'Outlier', 
    marker={
        'fillColor': 'white',
        'lineWidth': 1,
        'lineColor': 'Highcharts.getOptions().colors[0]'
    },
    tooltip={'pointFormat': 'Observation: {point.y}'}
)

chart.add_drilldown_data_set(data_2, 'column', 'Chrome', name='Chrome')
```


## Example Usage

```python
from highcharts import Highchart
chart = Highchart()

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
            'formatter': "function () {\
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

chart.set_dict_options(options)
data =  [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1], 
[50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
chart.add_data_set(data, 'spline', 'Temperature', marker={'enabled': False}) 

chart.save_file()

```

## Jupyter/IPython notebook

To render charts in Jupyter notebooks, simply put the chart object on the last line of a cell:

```python
chart.set_dict_options(options)
data =  [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1], 
[50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
chart.add_data_set(data, 'spline', 'Temperature', marker={'enabled': False}) 

chart
```

### Example notebooks:

* [Highcharts](http://nbviewer.ipython.org/github/kyper-data/python-highcharts/blob/master/examples/ipynb/highcharts/Example1.ipynb)
* [Highmaps](http://nbviewer.ipython.org/github/kyper-data/python-highcharts/blob/master/examples/ipynb/highmaps/Example1.ipynb)
* [Highstock](http://nbviewer.ipython.org/github/kyper-data/python-highcharts/blob/master/examples/ipynb/highstock/Example1-basic-line.ipynb)

## Todo:

* More charts support
* Clean code and put more explanation

Reference: [Highcharts API](http://api.highcharts.com/highcharts)

---------------------------------------------------------------------------------------------------------------
# Highmaps

## Basic Usage

Usage of python-highcharts is very similar to usage of the original Javascript library. 

The main input is a python dictionary similar to Highmaps's 'options' object. The dictionary supports most options listed in the official [Highmaps documentation](http://api.highcharts.com/highmaps). 

However, the data_set(s) need to be input by a separate function.

```python
from highcharts import Highmap

# A chart is the container that your data will be rendered in, it can (obviously) support multiple data series within it.
chart = Highmap()

# Adding a series requires a minimum of one argument, an array of data points
chart.add_data_set(data, series_type='map', name='Example Series')

# This will generate and save a .html file at the location you assign
chart.save_file()
```

Although you can add chart option using set_options, but
a better practice is to construct chart options by a dictionary (as highcharts suggests: http://www.highcharts.com/docs/getting-started/your-first-chart) and then input by set_dict_optoins function. Ex.

```python
options = {
    'chart': {
        'borderWidth': 1,
        'marginRight': 50 
    },

    'title': {
        'text': 'US Counties unemployment rates, April 2015'
    },

    'legend': {
        'title': {
            'text': 'Unemployment<br>rate',
            'style': {
                'color': "(Highcharts.theme && Highcharts.theme.textColor) || 'black'"
            }
        },
        'layout': 'vertical',
        'align': 'right',
        'floating': True,
        'valueDecimals': 0,
        'valueSuffix': '%',
        'backgroundColor': "(Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255, 255, 255, 0.85)'",
        'symbolRadius': 0,
        'symbolHeight': 14
    },

    'mapNavigation': {
        'enabled': True
    },

    'colorAxis': {
        'dataClasses': [{
            'from': 0,
            'to': 2,
            'color': "#F1EEF6"
        }, {
            'from': 2,
            'to': 4,
            'color': "#D4B9DA"
        }, {
            'from': 4,
            'to': 6,
            'color': "#C994C7"
        }, {
            'from': 6,
            'to': 8,
            'color': "#DF65B0"
        }, {
            'from': 8,
            'to': 10,
            'color': "#DD1C77"
        }, {
            'from': 10,
            'color': "#980043"
        }]
    },

    'plotOptions': {
        'map':{
        'mapData': 'geojson'

        },
        'mapline': {
            'showInLegend': False,
            'enableMouseTracking': False
        }
    },
} 

chart.set_dict_options(options)

```

The map data is set by set_map_source function. It is recommended to use the map collection on highcharts: http://code.highcharts.com/mapdata/

For the map properties visit: http://www.highcharts.com/docs/maps/map-collection

The default setting is to use the Highchart Javascript map.

```python

# set_map_source requires a least one argument: the map data url
chart.set_map_source('http://code.highcharts.com/mapdata/countries/us/us-all-all.js', jsonp_map = False)
```

However, the better practice is to load map data using function in highmap_helper library 
and convert it in preparation to be added directly by the add_map or add_data_set functions. 

```python
from highmap_helper import jsonp_loader, js_map_loader, geojson_handler

map_url = 'http://code.highcharts.com/mapdata/countries/us/us-all-all.js'

# Load .js format map data from the source and convert to GeoJSON object
geojson = js_map_loader(map_url)

# Similarly, json format (jsonp) map data can be loaded using:
geojson = jsonp_loader("a_jsonp_map_url")

# Reconstruct a GeoJSON object in preparation to be read directly. 
# geojson_handler function is similar to Highcharts.geojson in Highcharts: http://api.highcharts.com/highmaps#Highcharts.geojson
mapdata = geojson_handler(geojson)

chart.add_map_data(mapdata)

```

The series option in Highmaps needs to be input separately using add_data_set (and/or add_drilldown_data_set) function, Ex.

```python
chart.add_data_set(data, 'map', 'Unemployment rate', joinBy=['hc-key', 'code'], 
    tooltip={
        'valueSuffix': '%'
    },
    borderWidth = 0.5,
    states={
        'hover': {
            'color': '#bada55'
        }
    }
)
chart.add_drilldown_data_set(sub_data, 'map', id=mapkey, name=item['name'], 
    dataLabels={
        'enabled': True,
        'format': '{point.name}'
    }
)
```

The data set can be loaded directly from the url (jsonp format), but it is not recommended:
```python
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-counties-unemployment.json&callback=?'
chart.add_data_from_jsonp(data_url, 'json_data', 'map', 'Unemployment rate', joinBy=['hc-key', 'code'], 
    tooltip={
        'valueSuffix': '%'
    },
    borderWidth = 0.5,
    states={
        'hover': {
            'color': '#bada55'
        }
    }
)

```

Furthermore, python-highcharts has a function to add Javascript in the beginning or the end of JQuery body: $(function(){},
but, again, it is not recommended unless it is really necessary. 

```python
# function requires at least two arguments: script (javascript) and location ('head' or 'end')
chart.add_JSscript("var lines = Highcharts.geojson(Highcharts.maps['countries/us/us-all-all'], 'mapline');", 'head')
```

## Examples

Bad practice: 
1) load data directly and handle it in Javascript 2) insert javascript into thea head 3) use unquote function RawJavaScriptText to prepare Javascript:
```python
from highcharts import Highmap
from common import RawJavaScriptText

chart = Highmap()

options = {
    'chart': {
        'borderWidth': 1,
        'marginRight': 50 
    },
    'title': {
        'text': 'US Counties unemployment rates, April 2015'
    },
    'legend': {
        'title': {
            'text': 'Unemployment<br>rate',
            'style': {
                'color': "(Highcharts.theme && Highcharts.theme.textColor) || 'black'"
            }
        },
        'layout': 'vertical',
        'align': 'right',
        'floating': True,
        'valueDecimals': 0,
        'valueSuffix': '%',
        'backgroundColor': "(Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255, 255, 255, 0.85)'",
        'symbolRadius': 0,
        'symbolHeight': 14
    },
    'mapNavigation': {
        'enabled': True
    },
    'colorAxis': {
        'dataClasses': [{
            'from': 0,
            'to': 2,
            'color': "#F1EEF6"
        }, {
            'from': 2,
            'to': 4,
            'color': "#D4B9DA"
        }, {
            'from': 4,
            'to': 6,
            'color': "#C994C7"
        }, {
            'from': 6,
            'to': 8,
            'color': "#DF65B0"
        }, {
            'from': 8,
            'to': 10,
            'color': "#DD1C77"
        }, {
            'from': 10,
            'color': "#980043"
        }]
    },
    'plotOptions': {
        'mapline': {
            'showInLegend': False,
            'enableMouseTracking': False
        }
    }
} 

chart.set_dict_options(options)
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-counties-unemployment.json&callback=?'
chart.add_data_from_jsonp(data_url, 'json_data', 'map', 'Unemployment rate', 
    joinBy=['hc-key', 'code'], 
    tooltip={'valueSuffix': '%'},
    borderWidth=0.5,
    states={'hover': {'color': '#bada55'}}
)
chart.add_data_set(RawJavaScriptText('[lines[0]]'), 'mapline', 'State borders', color = 'white')
chart.add_data_set(RawJavaScriptText('[lines[1]]'), 'mapline', 'Separator', color = 'gray')
chart.set_map_source('http://code.highcharts.com/mapdata/countries/us/us-all-all.js', jsonp_map = False)
chart.add_JSscript("var lines = Highcharts.geojson(Highcharts.maps['countries/us/us-all-all'], 'mapline');", 'head')
chart.add_JSscript("Highcharts.each(geojson, function (mapPoint) {\
    mapPoint.name = mapPoint.name + ', ' + mapPoint.properties['hc-key'].substr(3, 2);\
});", 'head')

chart.save_file()
```

Better practice: 
```python

from highcharts import Highmap
from highmap_helper import jsonp_loader, js_map_loader, geojson_handler

chart = Highmap()
options = {
    'chart': {
        'borderWidth': 1,
        'marginRight': 50 
    },
    'title': {
        'text': 'US Counties unemployment rates, April 2015'
    },
    'legend': {
        'title': {
            'text': 'Unemployment<br>rate',
            'style': {
                'color': "(Highcharts.theme && Highcharts.theme.textColor) || 'black'"
            }
        },
        'layout': 'vertical',
        'align': 'right',
        'floating': True,
        'valueDecimals': 0,
        'valueSuffix': '%',
        'backgroundColor': "(Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255, 255, 255, 0.85)'",
        'symbolRadius': 0,
        'symbolHeight': 14
    },
    'mapNavigation': {
        'enabled': True
    },
    'colorAxis': {
        'dataClasses': [{
            'from': 0,
            'to': 2,
            'color': "#F1EEF6"
        }, {
            'from': 2,
            'to': 4,
            'color': "#D4B9DA"
        }, {
            'from': 4,
            'to': 6,
            'color': "#C994C7"
        }, {
            'from': 6,
            'to': 8,
            'color': "#DF65B0"
        }, {
            'from': 8,
            'to': 10,
            'color': "#DD1C77"
        }, {
            'from': 10,
            'color': "#980043"
        }]
    },
    'plotOptions': {
        'map':{
            'mapData': 'geojson'
        },
        'mapline': {
            'showInLegend': False,
            'enableMouseTracking': False
        }
    }
} 

chart.set_dict_options(options)

# read data and map directly from url
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-counties-unemployment.json&callback=?'
map_url = 'http://code.highcharts.com/mapdata/countries/us/us-all-all.js'

data = jsonp_loader(data_url)
geojson = js_map_loader(map_url)
mapdata = geojson_handler(geojson)
lines = geojson_handler(geojson, 'mapline')
for x in mapdata:
    x.update({'name':x['name']+', '+x['properties']['hc-key'].split('-')[1].upper()})

#map(lambda x: x['properties'].update({'name':x['properties']['name']+', '+x['properties']['hc-key'].split('-')[1]}), geojson['features'])

chart.add_data_set(data, 'map', 'Unemployment rate', joinBy = ['hc-key', 'code'], 
    tooltip={'valueSuffix': '%'},
    borderWidth=0.5,
    states={
        'hover': {
            'color': '#bada55'
        }
    }
)
chart.add_data_set([lines[0]], 'mapline', 'State borders', color = 'white')
chart.add_data_set([lines[3]], 'mapline', 'Separator', color = 'gray')
chart.add_map_data(mapdata)

chart.save_file()

```

## Todo:

* More examples
* Clean code and put more explanation

Reference: [Highcharts API](http://api.highcharts.com/highcharts)
