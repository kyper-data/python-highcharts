# Project: Python-Highcharts

## License

Please be aware that highcharts is only free for non-commercial use: Pop over to [Highcharts](http://shop.highsoft.com/) for licencing information.

## Overview

Python-Highcharts is python API(s) for Highcharts projects (highcharts, highmaps, and highstocks). 

The frame was originated from PyHighcharts on Github but alienated from it since PyHighcharts is moving toward to more function-based wrapper

## Installation

 -need to work on this-

## Design Overview

The way to use is designed to close to on Javascript. The main input is a python dictionary which contains and handles most options listed in highcharts. 

Only the data_set need to be input by separated function 

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
                    
We've also implemented the concept of templates, we've found while using the older version of PyHighcharts, we call the same code over and over again.