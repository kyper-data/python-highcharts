# -*- coding: UTF-8 -*-
import json, datetime
from common import Formatter, Events, Position, ContextButton, Options3d, ResetZoomButton, DrillUpButton, Labels, \
    Marker, Point, PlotBands, States, Tooltip, Title, Zones, JSfunction, ColorObject, CSSObject, SVGObject, \
    CommonObject, ArrayObject

from types import NoneType

PLOT_OPTION_ALLOWED_ARGS = {
  "common": {
    "animation": bool,
    "color": (ColorObject, basestring, dict),
    "cursor": basestring,
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
    "allowPointSelect": bool,
    "connectEnds": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "fillOpacity": float,
    "getExtremesFromAll": bool,
    "keys": list,
    "legendIndex": [int, float],
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "negativeColor": (ColorObject, basestring, dict),
    "negativeFillColor": (ColorObject, basestring, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": (int,basestring, datetime.datetime),
    "shadow": [bool, dict], #shadow object
    "stacking": basestring,
    "step": bool,
    "threshold": [int, NoneType],
    "trackByArea": bool,
    "turboThreshold": int,
  },
  "arearange": {
    "allowPointSelect": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "fillOpacity": float,
    "getExtremesFromAll": bool,
    "keys": list,
    "legendIndex": [int, float],
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "negativeColor": (ColorObject, basestring, dict),
    "negativeFillColor": (ColorObject, basestring, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "trackByArea": bool,
    "turboThreshold": int,
  },
  "areaspline": {
    "allowPointSelect": bool,
    "cropThreshold": int,
    "connectEnds": bool,
    "connectNulls": bool,
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "fillOpacity": float,
    "getExtremesFromAll": bool,  
    "keys": list,
    "legendIndex": [int, float],
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "negativeColor": (ColorObject, basestring, dict),
    "negativeFillColor": (ColorObject, basestring, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stack": basestring,
    "stacking": basestring,
    "threshold": [int, NoneType],
    "turboThreshold": int,
    "trackByArea": bool,
  },
  "areasplinerange": {
    "allowPointSelect": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "fillOpacity": float,
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "pointInterval": int,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "turboThreshold": int,
    "trackByArea": bool,  
  },
  "bar": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": int,
    "borderWidth": int,
    "colorByPoint": bool,
    "colors": list,
    "cropThreshold": int,
    "depth": [int, float],
    "edgeColor": (ColorObject, basestring, dict),
    "edgeWidth": int,
    "getExtremesFromAll": bool,
    "groupPadding": [float, int],
    "groupZPadding": [float, int],
    "grouping": bool,
    "keys": list,
    "linkedTo": basestring,
    "minPointLength": int,
    "negativeColor": (ColorObject, basestring, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPadding": [float, int],
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "pointWidth": int,
    "shadow": [bool, dict],
    "stacking": basestring,
    "threshold": [int, NoneType],
    "turboThreshold": int,
  },
  "boxplot": {
    "allowPointSelect": bool,
    "colorByPoint": bool,
    "colors": list,
    "depth": [int, float],
    "edgeColor": (ColorObject, basestring, dict),
    "edgeWidth": int,
    "fillColor": (ColorObject, basestring, dict),
    "getExtremesFromAll": bool,
    "groupPadding": [float, int],
    "groupZPadding": [float, int],
    "grouping": bool,
    "keys": list,
    "lineWidth": int,
    "linkedTo": basestring,
    "medianColor": (ColorObject, basestring, dict),
    "medianWidth": [int,float],
    "negativeColor": (ColorObject, basestring, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPadding": [float, int],
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "pointWidth": int,
    "shadow": [bool, dict],
    "size": [int,basestring],
    "slicedOffset": int,
    "startAngle": int,
    "showInLegend": bool
  },
  "bubble": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": int,
    "borderWidth": int,
    "colors": list,
    "colorByPoint": bool,
    "cropThreshold": int,
    "depth": [int, float],
    "edgeColor": (ColorObject, basestring, dict),
    "edgeWidth": int,
    "getExtremesFromAll": bool,
    "groupPadding": [float, int],
    "groupZPadding": [float, int],
    "grouping": bool,
    "keys": list,
    "linkedTo": basestring,
    "minPointLength": int,
    "negativeColor": (ColorObject, basestring, dict),
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPadding": [float, int],
    "pointPlacement": [basestring, int, float],
    "pointRange": int,
    "pointStart": [int,basestring,datetime.datetime],
    "pointWidth": int,
    "shadow": [bool, dict],
    "stacking": basestring,
    "threshold": [int, NoneType],
    "turboThreshold": int,
  },
  "column": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": int,
    "borderWidth": int,
    "colors": list,
    "colorByPoint": bool,
    "cropThreshold": int,
    "depth": [int, float],
    "edgeColor": (ColorObject, basestring, dict),
    "edgeWidth": int,
    "getExtremesFromAll": bool,
    "groupPadding": [float, int],
    "groupZPadding": [float, int],
    "grouping": bool,
    "keys": list,
    "linkedTo": basestring,
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "minPointLength": int,
    "negativeColor": (ColorObject, basestring, dict),
    "pointPadding": [float, int],
    "pointRange": int,
    "pointWidth": [int, float],
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stacking": basestring,
    "threshold": [int, NoneType],
    "turboThreshold": int,
  },
  "columnrange": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": int,
    "borderWidth": int,
    "colors": list,
    "colorByPoint": bool,
    "depth": [int, float],
    "edgeColor": (ColorObject, basestring, dict),
    "edgeWidth": int,
    "getExtremesFromAll": bool,
    "cropThreshold": int,
    "groupPadding": [float, int],
    "groupZPadding": [float, int],
    "grouping": bool,
    "keys": list,
    "linkedTo": basestring,
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "minPointLength": int,
    "negativeColor": (ColorObject, basestring, dict),
    "pointPadding": [float, int],
    "pointRange": int,
    "pointWidth": int,
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stacking": basestring,
    "threshold": [int, NoneType],
    "turboThreshold": int,
  },
  "errorbar": {
    "allowPointSelect": bool,
    "colors": list,
    "colorByPoint": bool,
    "cursor": basestring,
    "depth": [int, float],
    "edgeColor": (ColorObject, basestring, dict),
    "edgeWidth": int,
    "getExtremesFromAll": bool,
    "cropThreshold": int,
    "groupZPadding": [float, int],
    "keys": list,
    "linkedTo": basestring,
    "lineWidth": int,
    "negativeColor": (ColorObject, basestring, dict),
    "pointPadding": [float, int],
    "pointRange": int,
    "pointWidth": int,
    "pointInterval": int,
    "pointIntervalUnit": basestring,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "stemColor": (ColorObject, basestring, dict),
    "stemDashStyle": basestring,
    "stemWidth": [float, int],
    "stickyTracking": bool,
    "turboThreshold": int,
    "whiskerColor": (ColorObject, basestring, dict),
    "whiskerLength": [float, int, basestring],
    "whiskerWidth": [float, int]
  },
  "gauge": {
    "dial": NotImplemented,
    "animation": bool,
    "cursor": NotImplemented,
    "dial": NotImplemented,
    "id": NotImplemented,
    "linkedTo": NotImplemented,
    "negativeColor": NotImplemented,
    "pivot": NotImplemented,
    "selected": bool,
    "showCheckbox": bool,
    "showInLegend": NotImplemented,
    "states": NotImplemented,
    "stickyTracking": bool,
    "threshold": [int, NoneType],
    "tooltip": NotImplemented,
    "visible": bool,
    "wrap": bool,
    "zIndex": NotImplemented,
  },
  "line": {
    "allowPointSelect": bool,
    "connectEnds": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "getExtremesFromAll": bool,
    "keys": list,
    "legendIndex": [int, float],
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "negativeColor": (ColorObject, basestring, dict),
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
  "pie": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderWidth": int,
    "center": list,
    "colors": list,
    "depth": [int, float],
    "endAngle": [int, float],
    "ignoreHiddenPoint": bool,
    "innerSize": [int, basestring],
    "legendIndex": [int, basestring],
    "linkedTo": basestring,
    "minSize": [int, basestring],
    "shadow": [bool, dict],
    "showInLegend": bool,
    "size": [int,basestring],
    "slicedOffset": int,
    "startAngle": int,
  },
    "scatter": {
    "allowPointSelect": bool,
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
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "threshold": [int, float],
    "turboThreshold": int,
  },
  "series": {
    "allowPointSelect": bool,
    "connectEnds": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "lineWidth": int,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointPlacement": [basestring, int, float],
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": [bool, dict],
    "stacking": basestring,
    "turboThreshold": int,
  },
  "spline": {
    "allowPointSelect": bool,
    "connectEnds": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "lineWidth": int,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointPlacement": [basestring, int, float],
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
    "x": [int, float],
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

    def __display_options__(self):
        print(json.dumps(self.__options__(),indent=4,sort_keys=True))

    def process_kwargs(self,kwargs,series_type,supress_errors=False):
        allowed_args = PLOT_OPTION_ALLOWED_ARGS[series_type]
        allowed_args.update(PLOT_OPTION_ALLOWED_ARGS["common"])

        for k, v in kwargs.items():
            if k in allowed_args:
                if SeriesOptions.__validate_options__(k,v,allowed_args[k]):
                    if isinstance(allowed_args[k], tuple):
                        if isinstance(v, dict):
                            self.__dict__.update({k:allowed_args[k][0](**v)})
                        elif isinstance(v, CommonObject) or isinstance(v, ArrayObject):
                            self.__dict__.update({k:allowed_args[k][0](**v.__options__())})
                        elif isinstance(v, JSfunction) or isinstance(v, Formatter):
                            self.__dict__.update({k:allowed_args[k][0](v.__options__().get_jstext())})
                        elif isinstance(v, CSSObject) or isinstance(v, SVGObject):
                            self.__dict__.update({k:allowed_args[k][0](**v.__options__())})
                        elif isinstance(v, ColorObject):
                            if isinstance(v.__options__(), basestring):
                                self.__dict__.update({k:allowed_args[k][0](v.__options__())})
                            else:
                                self.__dict__.update({k:allowed_args[k][0](**v.__options__())})
                        elif isinstance(v, datetime.datetime):
                            self.__dict__.update({k:v})                            
                        else:
                            self.__dict__.update({k:allowed_args[k][0](v)})
                    else:
                        self.__dict__.update({k:v})
                else: 
                    print(k,v)
                    if not supress_errors: raise OptionTypeError("Option Type Mismatch: Expected: %s" % allowed_args[k])
            # else:
            #     if not supress_errors: raise OptionTypeError("Option: %s Not Allowed For Series Type: %s" % (k,series_type))

    def load_defaults(self,series_type):
        self.process_kwargs(DEFAULT_OPTIONS.get(series_type,{}),series_type)


class HighchartsError(Exception):

    def __init__(self, *args):
        self.args = args


class MultiAxis(object):

    def __init__(self, axis):
        self.axis = axis

    def __options__(self):
        return self.__dict__


class Series(object):
    """Series class for input data """

    def __init__(self,data,series_type="line",supress_errors=False,**kwargs):

        # List of dictionaries. Each dict contains data and properties, which need to handle before construct the object for series 
        for item in data:
            if isinstance(item, dict):
                for k, v in item.items():
                    if k in DATA_SERIES_ALLOWED_OPTIONS:
                        if SeriesOptions.__validate_options__(k,v,DATA_SERIES_ALLOWED_OPTIONS[k]):
                            if isinstance(DATA_SERIES_ALLOWED_OPTIONS[k], tuple):
                                if isinstance(v, dict):
                                    item.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](**v)})
                                elif isinstance(v, CommonObject) or isinstance(v, ArrayObject):
                                    item.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](**v.__options__())})
                                elif isinstance(v, JSfunction) or isinstance(v, Formatter):
                                    item.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](v.__options__().get_jstext())})
                                elif isinstance(v, CSSObject) or isinstance(v, SVGObject):
                                    item.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](**v.__options__())})
                                elif isinstance(v, ColorObject):
                                    if isinstance(v.__options__(), basestring):
                                        item.update({k:allowed_args[k][0](v.__options__())})
                                    else:
                                        item.update({k:allowed_args[k][0](**v.__options__())})
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
                        elif isinstance(v, CommonObject) or isinstance(v, ArrayObject):
                            self.__dict__.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](**v.__options__())})
                        elif isinstance(v, JSfunction) or isinstance(v, Formatter):
                            self.__dict__.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](v.__options__().get_jstext())})
                        elif isinstance(v, CSSObject) or isinstance(v, SVGObject):
                            self.__dict__.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](**v.__options__())})
                        elif isinstance(v, ColorObject):
                            if isinstance(v.__options__(), basestring):
                                self.__dict__.update({k:allowed_args[k][0](v.__options__())})
                            else:
                                self.__dict__.update({k:allowed_args[k][0](**v.__options__())})
                        elif isinstance(v, datetime.datetime):
                            self.__dict__.update({k:v})                            
                        else:
                            self.__dict__.update({k:DATA_SERIES_ALLOWED_OPTIONS[k][0](v)})
                    else:
                        self.__dict__.update({k:v})
                else: 
                    if not supress_errors: raise OptionTypeError("Option Type Mismatch: Expected: %s" % DATA_SERIES_ALLOWED_OPTIONS[k])
            


    def __options__(self):
        return self.__dict__
