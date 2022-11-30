# -*- coding: UTF-8 -*-
from past.builtins import basestring

import json, datetime
from .common import Formatter, Events, Position, ContextButton, Options3d, ResetZoomButton, DataGrouping, \
    Labels, Marker, Point, PlotBands, States, Tooltip, Title, Zones, Levels, Shadow, \
    JSfunction, ColorObject, CSSObject, SVGObject, \
    CommonObject, ArrayObject

PLOT_OPTION_ALLOWED_ARGS = {
  "common": {
    "allowPointSelect": bool,
    "animation": bool,
    "color": (ColorObject, basestring, dict),
    "cursor": basestring,
    "dataGrouping": (DataGrouping, dict),
    "dataLabels": (Labels, dict),
    "enableMouseTracking": bool,
    "events": (Events, dict),
    "id": basestring,
    "index": [float, int],
    "name": basestring,
    "point": (Point, dict),
    "selected": bool,
    "showCheckbox": bool,
    "showInLegend": bool,
    "states": (States, dict),
    "stickyTracking": bool,
    "tooltip": (Tooltip, dict),
    "visible": bool,
    "xAxis": [int, basestring],
    "yAxis": [int, basestring],
    "zIndex": int,
    "zoneAxis": basestring,
    "zones": (Zones, dict),
    },
  "area": {
    "compare": basestring,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "fillOpacity": float,
    "gapSize": [int, float],
    "keys": list,
    "legendIndex": [int, float],
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": (int,basestring, datetime.datetime),
    "shadow": [bool, dict],
    "stack": basestring,
    "stacking": basestring,
    "step": bool,
    "threshold": [int, type(None)],
    "trackByArea": bool,
    "turboThreshold": int,
  },
  "arearange": {
    "compare": basestring,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "fillOpacity": float,
    "gapSize": [int, float],
    "keys": list,
    "legendIndex": [int, float],
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "trackByArea": bool,
    "turboThreshold": int,
  },
  "areaspline": {
    "cropThreshold": int,
    "compare": basestring,
    "connectNulls": bool,
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "fillOpacity": float,
    "gapSize": [int, float],
    "keys": list,
    "legendIndex": [int, float],
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stack": basestring,
    "stacking": basestring,
    "threshold": [int, type(None)],
    "turboThreshold": int,
    "trackByArea": bool,
  },
  "areasplinerange": {
    "cropThreshold": int,
    "compare": basestring,
    "connectNulls": bool,
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "fillOpacity": float,
    "gapSize": [int, float],
    "keys": list,
    "legendIndex": [int, float],
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stack": basestring,
    "stacking": basestring,
    "threshold": [int, type(None)],
    "turboThreshold": int,
    "trackByArea": bool, 
  },
  "candlestick": {
    "colors": list,
    "cropThreshold": int,
    "connectNulls": bool,
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "fillOpacity": float,
    "groupPadding": [int, float],
    "grouping": bool,
    "keys": list,
    "legendIndex": [int, float],
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "minPointLength": [int, float],
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointRange": [int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "pointWidth": [int, float],
    "shadow": [bool, dict],
    "stack": basestring,
    "upColor": (ColorObject, basestring, dict),
    "upLineColor": (ColorObject, basestring, dict),
    "turboThreshold": int,
    "trackByArea": bool, 
  },
  "column": {
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": int,
    "borderWidth": [int, basestring],
    "colorByPoint": bool,
    "colors": list,
    "compare": basestring,
    "cropThreshold": int,
    "groupPadding": [float, int],
    "grouping": bool,
    "keys": list,
    "linkedTo": basestring,
    "minPointLength": int,
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPadding": [float, int],
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "pointWidth": [int, float],
    "shadow": [bool, dict],
    "stack": basestring,
    "stacking": basestring,
    "turboThreshold": int,
  },
  "columnrange": {
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": int,
    "borderWidth": [int, basestring],
    "colorByPoint": bool,
    "colors": list,
    "compare": basestring,
    "cropThreshold": int,
    "groupPadding": [float, int],
    "grouping": bool,
    "keys": list,
    "linkedTo": basestring,
    "minPointLength": int,
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPadding": [float, int],
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "pointWidth": [int, float],
    "shadow": [bool, dict],
    "stack": basestring,
    "stacking": basestring,
    "turboThreshold": int,
  },
  "flags": {
    "colors": list,
    "cropThreshold": int,
    "keys": list,
    "legendIndex": [int, float],
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "onSeries": basestring,
    "pointIntervalUnit": basestring,
    "shadow": [bool, dict],
    "shape": basestring,
    "stack": basestring,
    "stackDistance": [int, float],
    "style": (CSSObject, dict),
    "y": [int, float],
    "useHTML": bool,
  },
  "line": {
    "compare": basestring,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "gapSize": [int, float],
    "keys": list,
    "legendIndex": [int, float],
    "lineWidth": int,
    "linecap": basestring,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stack": basestring,
    "stacking": basestring,
    "step": basestring,
    "turboThreshold": int,
  },
  "ohlc": {
    "colorByPoint": bool,
    "colors": list,
    "compare": basestring,
    "cropThreshold": int,
    "groupPadding": [float, int],
    "grouping": bool,
    "keys": list,
    "legendIndex": [int, float],
    "lineWidth": int,
    "linkedTo": basestring,
    "minPointLength": int,
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPadding": [float, int],
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "pointWidth": [int, float],
    "shadow": [bool, dict],
    "stack": basestring,
    "stacking": basestring,
    "turboThreshold": int,
  },
   "polygon": {
    "compare": basestring,
    "cropThreshold": int,
    "dashStyle": basestring,
    "keys": list,
    "legendIndex": [int, float],
    "lineWidth": int,
    "linkedTo": basestring,
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stacking": basestring,
    "turboThreshold": int,
  },
    "scatter": {
    "compare": basestring,
    "cropThreshold": int,
    "dashStyle": basestring,
    "keys": list,
    "legendIndex": [int, float],
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "negativeColor": (ColorObject, basestring, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stacking": basestring,
    "turboThreshold": int,
  },
  "series": {
    "compare": basestring,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "gapSize": [int, float],
    "keys": list,
    "legendIndex": [int, float],
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stacking": basestring,
    "turboThreshold": int,
  },
  "spline": {
    "compare": basestring,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "gapSize": [int, float],
    "keys": list,
    "legendIndex": [int, float],
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stacking": basestring,
    "turboThreshold": int,
  },
}

DATA_SERIES_ALLOWED_OPTIONS = {
    "color": (ColorObject, basestring, dict),
    "connectEnds": bool,
    "connectNulls": bool,
    "dataLabels": (Labels, dict),
    "dataParser": NotImplemented,
    "dataURL": NotImplemented,
    "drilldown": basestring,
    "events": (Events, dict),
    "high": [int, float],
    "id": basestring,
    "index": int,
    "legendIndex": int,
    "name": basestring,
    "marker": (Marker, dict),
    "selected": bool,
    "sliced": bool,
    "showInLegend": bool,
    "type": basestring,
    "visible": bool,
    "x": [int, float, datetime.datetime],
    "xAxis": int,
    "yAxis": int,
}

DEFAULT_OPTIONS = {

}

class OptionTypeError(Exception):

    def __init__(self,*args):
        self.args = args


class SeriesOptions(object):
    """Class for plotOptions"""

    def __init__(self,series_type="line",supress_errors=False,**kwargs):
        self.load_defaults(series_type)
        self.process_kwargs(kwargs,series_type=series_type,supress_errors=supress_errors)

    @staticmethod
    def __validate_options__(k,v,ov):
        if isinstance(ov,list):
            if isinstance(v,tuple(ov)): return True
            else:
                raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
        else:
          if ov == NotImplemented: raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
          if isinstance(v,ov): return True
          else: return False

    def __options__(self):
        return self.__dict__

    def __jsonable__(self):
        return self.__dict__

    def update(self,series_type, **kwargs):
        allowed_args = PLOT_OPTION_ALLOWED_ARGS[series_type]
        allowed_args.update(PLOT_OPTION_ALLOWED_ARGS["common"])
        for k, v in kwargs.items():
            if k in allowed_args:
                if SeriesOptions.__validate_options__(k,v,allowed_args[k]):
                    if isinstance(allowed_args[k], tuple) and isinstance(allowed_args[k][0](), CommonObject):
                        # re-construct input dict with existing options in objects
                        if self.__getattr__(k):
                            if isinstance(v, dict):
                                self.__options__()[k].update(v)
                            else:
                                self.__options__()[k].__options__().update(v)
                        else:
                            self.__options__().update({k:allowed_args[k][0](**v)}) 

                    elif isinstance(allowed_args[k], tuple) and isinstance(allowed_args[k][0](), ArrayObject):
                        # update array 
                        if isinstance(v, dict):
                            self.__dict__[k].append(allowed_args[k][0](**v))
                        elif isinstance(v, list):
                            for item in v:
                                self.__dict__[k].append(allowed_args[k][0](**item))
                        else:
                            OptionTypeError("Not An Accepted Input Type: %s" % type(v))        

                    elif isinstance(allowed_args[k], tuple) and \
                        (isinstance(allowed_args[k][0](), CSSObject) or isinstance(allowed_args[k][0](), SVGObject)):
                        if self.__getattr__(k):
                            for key, value in v.items():
                                self.__dict__[k].__options__().update({key:value})
                        else:
                            self.__dict__.update({k:allowed_args[k][0](**v)})
                        
                        v = self.__dict__[k].__options__()
                        # upating object
                        if isinstance(v, dict):
                            self.__dict__.update({k:allowed_args[k][0](**v)})
                        else:
                            self.__dict__.update({k:allowed_args[k][0](v)})

                    elif isinstance(allowed_args[k], tuple) and (isinstance(allowed_args[k][0](), JSfunction) or
                        isinstance(allowed_args[k][0](), Formatter) or isinstance(allowed_args[k][0](), ColorObject)):
                        if isinstance(v, dict):
                            self.__dict__.update({k:allowed_args[k][0](**v)})
                        else:
                            self.__dict__.update({k:allowed_args[k][0](v)})
                    else:
                        self.__dict__.update({k:v})
            else: 
                print(k,v)
                if not supress_errors: raise OptionTypeError("Option Type Mismatch: Expected: %s" % allowed_args[k])
                

    def process_kwargs(self,kwargs,series_type,supress_errors=False):
        allowed_args = PLOT_OPTION_ALLOWED_ARGS[series_type]
        allowed_args.update(PLOT_OPTION_ALLOWED_ARGS["common"])

        for k, v in kwargs.items():
            if k in allowed_args:
                if SeriesOptions.__validate_options__(k,v,allowed_args[k]):
                    if isinstance(allowed_args[k], tuple):
                        if isinstance(v, dict):
                            self.__dict__.update({k:allowed_args[k][0](**v)})
                        elif isinstance(v, list):
                            if len(v) == 1:
                                self.__dict__.update({k:allowed_args[k][0](**v[0])})
                            else:
                                self.__dict__.update({k:allowed_args[k][0](**v[0])})
                                for item in v[1:]:
                                    self.__dict__[k].update(item)                          
                        elif isinstance(v, CommonObject) or isinstance(v, ArrayObject) or \
                            isinstance(v, CSSObject) or isinstance(v, SVGObject) or isinstance(v, ColorObject) or \
                            isinstance(v, JSfunction) or isinstance(v, Formatter) or isinstance(v, datetime.datetime):
                            self.__dict__.update({k:v})
                        else:
                            self.__dict__.update({k:allowed_args[k][0](v)})
                    else:
                        self.__dict__.update({k:v})          
                else: 
                    print(k,v)
                    if not supress_errors: raise OptionTypeError("Option Type Mismatch: Expected: %s" % allowed_args[k])
           

    def load_defaults(self,series_type): # not in use
        self.process_kwargs(DEFAULT_OPTIONS.get(series_type,{}),series_type)

    def __getattr__(self,item):
        if not item in self.__dict__:
            return None # Attribute Not Set
        else:
            return True
            

class Series(object):
    """Series class for input data """

    def __init__(self,data,series_type="line",supress_errors=False,**kwargs):

        # List of dictionaries. Each dict contains data and properties, 
        # which need to handle before construct the object for series 
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    for k, v in item.items():
                        if k in DATA_SERIES_ALLOWED_OPTIONS:
                            if SeriesOptions.__validate_options__(k,v,DATA_SERIES_ALLOWED_OPTIONS[k]):
                                if isinstance(DATA_SERIES_ALLOWED_OPTIONS[k], tuple):
                                    if isinstance(v, dict):
                                        item.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](**v)})
                                    elif isinstance(v, datetime.datetime):
                                        item.update({k:v})                            
                                    else:
                                        item.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](v)})
                                else:
                                    item.update({k:v})
                        
        self.__dict__.update({
          "data": data,
          "type": series_type,
          })

        # Series propertie can be input as kwargs, which is handled here 
        for k, v in kwargs.items():
            if k in DATA_SERIES_ALLOWED_OPTIONS:
                if SeriesOptions.__validate_options__(k,v,DATA_SERIES_ALLOWED_OPTIONS[k]):
                    if isinstance(DATA_SERIES_ALLOWED_OPTIONS[k], tuple):
                        if isinstance(v, dict):
                            self.__dict__.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](**v)})
                        elif isinstance(v, CommonObject) or isinstance(v, ArrayObject) or \
                            isinstance(v, CSSObject) or isinstance(v, SVGObject) or isinstance(v, ColorObject) or \
                            isinstance(v, JSfunction) or isinstance(v, Formatter) or isinstance(v, datetime.datetime):
                            self.__dict__.update({k:v})                           
                        else:
                            self.__dict__.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](v)})
                    else:
                        self.__dict__.update({k:v})
                else: 
                    if not supress_errors: raise OptionTypeError("Option Type Mismatch: Expected: %s" % DATA_SERIES_ALLOWED_OPTIONS[k])
            

    def __options__(self):
        return self.__dict__

    def __jsonable__(self):
        return self.__dict__
