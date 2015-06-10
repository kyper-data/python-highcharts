# -*- coding: UTF-8 -*-
import json

PLOT_OPTION_ALLOWED_ARGS = {
  "common": {
    "animation": bool,
    "color": basestring,
    "cursor": basestring,
    "dataLabels": NotImplemented,
    "enableMouseTracking": bool,
    "events": NotImplemented,
    "id": basestring,
    "point": NotImplemented,
    "selected": bool,
    "showCheckbox": bool,
    "showInLegend": bool,
    "states": NotImplemented,
    "stickyTracking": bool,
    "tooltip": NotImplemented,
    "visible": bool,
    "zIndex": int,
    "marker": dict
  },
  "area": {
    "allowPointSelect": bool,
    "connectEnds": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "fillColor": basestring,
    "fillOpacity": float,
    "lineColor": basestring,
    "lineWidth": int,
    "marker": dict,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
    "shadow": bool,
    "stacking": basestring,
    "threshold": int,
    "turboThreshold": int,
    "trackByArea": bool,
  },
  "arearange": {
    "allowPointSelect": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "fillColor": basestring,
    "fillOpacity": float,
    "lineColor": basestring,
    "lineWidth": int,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
    "shadow": bool,
    "turboThreshold": int,
    "trackByArea": bool,
  },
  "areaspline": {
    "allowPointSelect": bool,
    "cropThreshold": int,
    "connectEnds": bool,
    "connectNulls": bool,
    "dashStyle": basestring,
    "fillColor": basestring,
    "fillOpacity": float,   
    "lineColor": basestring,
    "lineWidth": int,
    "marker": dict,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
    "shadow": bool,
    "stacking": basestring,
    "threshold": int,
    "turboThreshold": int,
    "trackByArea": bool,
  },
  "areasplinerange": {
    "allowPointSelect": bool,
    "connectNulls": bool,
    "cropThreshold": int,
    "dashStyle": basestring,
    "fillColor": basestring,
    "fillOpacity": float,
    "lineColor": basestring,
    "lineWidth": int,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
    "shadow": bool,
    "turboThreshold": int,
    "trackByArea": bool,  
  },
  "bar": {
    "allowPointSelect": bool,
    "borderColor": basestring,
    "borderRadius": int,
    "borderWidth": int,
    "colorByPoint": bool,
    "cropThreshold": int,
    "groupPadding": float,
    "grouping": bool,
    "lineColor": basestring,
    "lineWidth": int,
    "minPointLength": int,
    "pointPadding": float,
    "pointRange": int,
    "pointWidth": int,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
    "shadow": bool,
    "stacking": basestring,
    "turboThreshold": int,
  },
  "column": {
    "allowPointSelect": bool,
    "borderColor": basestring,
    "borderRadius": int,
    "borderWidth": int,
    "colorByPoint": bool,
    "cropThreshold": int,
    "groupPadding": (float, int),
    "grouping": bool,
    "lineColor": basestring,
    "lineWidth": int,
    "minPointLength": int,
    "pointPadding": float,
    "pointRange": int,
    "pointWidth": (int, float),
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
    "shadow": bool,
    "stacking": basestring,
    "turboThreshold": int,
  },
  "columnrange": {
    "allowPointSelect": bool,
    "borderColor": basestring,
    "borderRadius": int,
    "borderWidth": int,
    "colorByPoint": bool,
    "cropThreshold": int,
    "groupPadding": float,
    "grouping": bool,
    "lineColor": basestring,
    "lineWidth": int,
    "minPointLength": int,
    "pointPadding": float,
    "pointRange": int,
    "pointWidth": int,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
    "shadow": bool,
    "stacking": basestring,
    "turboThreshold": int,
    "showInLegend": bool,

  },
  "gauge": {
    "dial": NotImplemented,
    "animation": bool,
    "color": NotImplemented,
    "cursor": NotImplemented,
    "dataLabels": NotImplemented,
    "dial": NotImplemented,
    "enableMouseTracking": bool,
    "events": NotImplemented,
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
    "threshold": int,
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
    "marker": dict,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
    "shadow": NotImplemented,
    "stacking": basestring,
    "step": basestring,
    "turboThreshold": int,
  },
  "pie": {
    "allowPointSelect": bool,
    "borderColor": basestring,
    "borderWidth": int,
    "center": list,
    "ignoreHiddenPoint": bool,
    "innerSize": int,
    "lineWidth": int,
    "marker": dict,
    "pointPlacement": basestring,
    "shadow": bool,
    "size": (int,basestring),
    "slicedOffset": int,
    "startAngle": int,
    "dataLabels": dict,
    "showInLegend": bool
  },
  "boxplot": {
    "allowPointSelect": bool,
    "borderColor": basestring,
    "borderWidth": int,
    "center": list,
    "ignoreHiddenPoint": bool,
    "innerSize": int,
    "lineWidth": int,
    "marker": dict,
    "pointPlacement": basestring,
    "shadow": bool,
    "size": (int,basestring),
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
    "marker": dict,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
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
    "marker": dict,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
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
    "marker": dict,
    "pointInterval": int,
    "pointPlacement": basestring,
    "pointStart": (int,basestring),
    "shadow": bool,
    "stacking": basestring,
    "turboThreshold": int,
  },
}

DATA_SERIES_ALLOWED_OPTIONS = {
    'color': basestring,
  "dataParser": NotImplemented,
  "dataURL": NotImplemented,
  "index": int,
  "legendIndex": int,
  "name": basestring,
  "stack": basestring,
  "type": basestring,
  "xAxis": int,
  "yAxis": int,
  "marker": dict,
    'showInLegend': bool,
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
      for o in ov:
        if isinstance(v,o): return True
      else:
        raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
    else:
      if ov == NotImplemented: raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
      if isinstance(v,ov): return True
      else: return False

  def __options__(self):
    return self.__dict__

  def __display_options__(self):
    print json.dumps(self.__options__(),indent=4,sort_keys=True)

  def process_kwargs(self,kwargs,series_type,supress_errors=False):
    allowed_args = PLOT_OPTION_ALLOWED_ARGS[series_type]
    for k, v in kwargs.items():
      if k in allowed_args:
        if SeriesOptions.__validate_options__(k,v,allowed_args[k]):
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


class Series(object):

  def __init__(self,data,series_type="line",supress_errors=False,**kwargs):
    self.__dict__.update({
      "data": data,
      "type": series_type,
      })
    for k, v in kwargs.items():
      if k in DATA_SERIES_ALLOWED_OPTIONS:
        if SeriesOptions.__validate_options__(k,v,DATA_SERIES_ALLOWED_OPTIONS[k]):
          self.__dict__.update({k:v})
        else:
          if not supress_errors: raise OptionTypeError("Option Type Mismatch: Expected: %s" % DATA_SERIES_ALLOWED_OPTIONS[k])
      else:
        if not supress_errors: raise OptionTypeError("Option: %s Not Allowed For Data Series: %s" % (k, series_type))
