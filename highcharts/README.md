# Project: Python-Highcharts

## License

Please be aware that highcharts is only free for non-commercial use: Pop over to [Highcharts](http://shop.highsoft.com/) for licencing information.

## Overview

Python-Highcharts is python API(s) for Highcharts projects (highcharts, highmaps, and highstocks). 

The frame was originated from PyHighcharts on Github but alienated from it since PyHighcharts is moving toward to more function-based wrapper

## Installation

 -need to work on this-

---------------------------------------------------------------------------------------------------------------
# Highmaps

## Design Overview

The usage is designed to close to it on Javascript. 

The main input is a python dictionary similart to options object, and the dictionary contains and handles most options listed in highcharts. 

Only the data_set(s) need to be input by separated function 

```python
from highmaps import Highmaps

# A chart is the container that your data will be rendered in, it can (obviously) support multiple data series within it.
chart = Highmaps()

# Adding a series requires a minimum of one argument, an array of data points
chart.add_data_set(data,'map','Example Series')

# This will generate and save a .html file at the location you assign
chart.file()
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

chart.set_dict_optoins(options)

```

The map data is set by set_map_source function. It is recommended to use the map collection on highcharts: http://code.highcharts.com/mapdata/

For the map properties: http://www.highcharts.com/docs/maps/map-collection

The default setting is to use highchart javascript map

```python

# Set map requires a least one argument: the map data url
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

# Reconstructure a GeoJSON object in preparation to be read directly. 
# geojson_handler function is similar to Highcharts.geojson in highchart: http://api.highcharts.com/highmaps#Highcharts.geojson
mapdata = geojson_handler(geojson)

chart.add_map_data(mapdata)

```

The series option in highmap needs to input separately using add_data_set (or/and add_drilldown_data_set) function, Ex.

```python
chart.add_data_set(data, 'map', 'Unemployment rate', joinBy = ['hc-key', 'code'], 
     tooltip = {
                    'valueSuffix': '%'
                },
                borderWidth = 0.5,
                states = {
                    'hover': {
                        'color': '#bada55'
                    }
                }
                )
chart.add_drilldown_data_set(sub_data, 'map', id = mapkey, name = item['name'], 
                dataLabels = {
                    'enabled': True,
                    'format': '{point.name}'
                }
            )
```

The data set can be loaded directly with url (jsonp format), but it is not recommended:
```python
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-counties-unemployment.json&callback=?'
chart.add_data_from_jsonp(data_url, 'json_data', 'map', 'Unemployment rate', joinBy = ['hc-key', 'code'], 
     tooltip = {
                    'valueSuffix': '%'
                },
                borderWidth = 0.5,
                states = {
                    'hover': {
                        'color': '#bada55'
                    }
                }
                )

```

Furthermore, API has function to add Javascript in the beginning or the end of jquery body: $(function(){},
but, again, it is not recommended unless it is really necessary 

```python
# Function requires at least two arguments: script (javascript) and location ('head' or 'end')
chart.add_JSscript("var lines = Highcharts.geojson(Highcharts.maps['countries/us/us-all-all'], 'mapline');", 'head')
```

## Usage

Bad practice: 
1) load data directionly and handle in javascript 2) has javascript at front and in the end 3) require unquote function: RawJavaScriptText 
```python
from highmaps import Highmaps
from common import RawJavaScriptText

chart = Highmaps()

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
        },
    } 

chart.set_dict_optoins(options)
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-counties-unemployment.json&callback=?'
chart.add_data_from_jsonp(data_url, 'json_data', 'map', 'Unemployment rate', joinBy = ['hc-key', 'code'], 
     tooltip = {
                    'valueSuffix': '%'
                },
                borderWidth = 0.5,
                states = {
                    'hover': {
                        'color': '#bada55'
                    }
                }
                )
chart.add_data_set(RawJavaScriptText('[lines[0]]'), 'mapline', 'State borders', color = 'white')
chart.add_data_set(RawJavaScriptText('[lines[1]]'), 'mapline', 'Separator', color = 'gray')
chart.set_map_source('http://code.highcharts.com/mapdata/countries/us/us-all-all.js', jsonp_map = False)
chart.add_JSscript("var lines = Highcharts.geojson(Highcharts.maps['countries/us/us-all-all'], 'mapline');", 'head')
chart.add_JSscript("Highcharts.each(geojson, function (mapPoint) {\
            mapPoint.name = mapPoint.name + ', ' + mapPoint.properties['hc-key'].substr(3, 2);\
        });", 'head')


chart.file()
```

Better practice: 
```python

from highmaps import Highmaps
from highmap_helper import jsonp_loader, js_map_loader, geojson_handler

chart = Highmaps()
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

chart.set_dict_optoins(options)

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
     tooltip = {
                    'valueSuffix': '%'
                },
                borderWidth = 0.5,
                states = {
                    'hover': {
                        'color': '#bada55'
                    }
                }
                )
chart.add_data_set([lines[0]], 'mapline', 'State borders', color = 'white')
chart.add_data_set([lines[3]], 'mapline', 'Separator', color = 'gray')
chart.add_map_data(mapdata)

chart.file()

```

## Todo:

* More examples
* Clean code and put more explanation
* Unittests

Reference: [Highcharts API](http://api.highcharts.com/highcharts)