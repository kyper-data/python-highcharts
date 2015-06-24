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
    "point": (Point, dict),
    "selected": bool,
    "showCheckbox": bool,
    "showInLegend": bool,
    "states": (States, dict),
    "stickyTracking": bool,
    "tooltip": (Tooltip, dict),
    "visible": bool,
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
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "linkedTo": basestring,
    "marker": (Marker, dict),
    "negativeColor": (ColorObject, basestring, dict),
    "negativeFillColor": (ColorObject, basestring, dict),
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring, datetime.datetime),
    "shadow": bool,
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
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": bool,
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
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": bool,
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
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": bool,
    "turboThreshold": int,
    "trackByArea": bool,  
  },
  "bar": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": int,
    "borderWidth": int,
    "colorByPoint": bool,
    "cropThreshold": int,
    "groupPadding": float,
    "grouping": bool,
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "minPointLength": int,
    "pointPadding": float,
    "pointRange": int,
    "pointWidth": int,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": bool,
    "stacking": basestring,
    "turboThreshold": int,
  },
  "column": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": int,
    "borderWidth": int,
    "colorByPoint": bool,
    "cropThreshold": int,
    "groupPadding": [float, int],
    "grouping": bool,
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "minPointLength": int,
    "pointPadding": float,
    "pointRange": int,
    "pointWidth": [int, float],
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": bool,
    "stacking": basestring,
    "turboThreshold": int,
  },
  "columnrange": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": int,
    "borderWidth": int,
    "colorByPoint": bool,
    "cropThreshold": int,
    "groupPadding": float,
    "grouping": bool,
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "minPointLength": int,
    "pointPadding": float,
    "pointRange": int,
    "pointWidth": int,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": bool,
    "stacking": basestring,
    "turboThreshold": int,
    "showInLegend": bool,

  },
  "gauge": {
    "dial": NotImplemented,
    "animation": bool,
    "color": (ColorObject, basestring, dict),
    "cursor": NotImplemented,
    "dataLabels": NotImplemented,
    "dial": NotImplemented,
    "enableMouseTracking": bool,
    "events": (Events, dict),
    "id": NotImplemented,
    "linkedTo": NotImplemented,
    "negativeColor": NotImplemented,
    "pivot": NotImplemented,
    "point": NotImplemented,
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
    "lineWidth": int,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": NotImplemented,
    "stacking": basestring,
    "step": basestring,
    "turboThreshold": int,
  },
  "pie": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderWidth": int,
    "center": list,
    "ignoreHiddenPoint": bool,
    "innerSize": int,
    "lineWidth": int,
    "marker": (Marker, dict),
    "pointPlacement": basestring,
    "shadow": bool,
    "size": [int,basestring],
    "slicedOffset": int,
    "startAngle": int,
    "dataLabels": dict,
    "showInLegend": bool
  },
  "boxplot": {
    "allowPointSelect": bool,
    "borderColor": (ColorObject, basestring, dict),
    "borderWidth": int,
    "center": list,
    "ignoreHiddenPoint": bool,
    "innerSize": int,
    "lineWidth": int,
    "marker": (Marker, dict),
    "pointPlacement": basestring,
    "shadow": bool,
    "size": [int,basestring],
    "slicedOffset": int,
    "startAngle": int,
    "dataLabels": dict,
    "showInLegend": bool
  },
  "scatter": {
    "allowPointSelect": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "lineWidth": int,
    "marker": (Marker, dict),
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": bool,
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
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": bool,
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
    "pointPlacement": basestring,
    "pointStart": [int,basestring,datetime.datetime],
    "shadow": bool,
    "stacking": basestring,
    "turboThreshold": int,
  },
}

DATA_SERIES_ALLOWED_OPTIONS = {
    "color": (ColorObject, basestring, dict),
    "dataParser": NotImplemented,
    "dataURL": NotImplemented,
    "index": int,
    "legendIndex": int,
    "name": basestring,
    "stack": basestring,
    "type": basestring,
    "xAxis": int,
    "yAxis": int,
    "marker": (Marker, dict),
    "showInLegend": bool,
    "visible": bool,
}

DEFAULT_OPTIONS = {

}

class OptionTypeError(Exception):

    def __init__(self,*args):
        self.args = args


class SeriesOptions(object):

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
                    if not supress_errors: raise OptionTypeError("Option Type Mismatch: Expected: %s" % allowed_args[k])
            else: 
                if not supress_errors: raise OptionTypeError("Option: %s Not Allowed For Series Type: %s" % (k,series_type))

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

    def __init__(self,data,series_type="line",supress_errors=False,**kwargs):
        self.__dict__.update({
          "data": data,
          "type": series_type,
          })

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
            else: 
                if not supress_errors: raise OptionTypeError("Option: %s Not Allowed For Series Type: %s" % (k,series_type))


    def __options__(self):
        return self.__dict__
