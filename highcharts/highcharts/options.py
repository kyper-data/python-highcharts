# -*- coding: UTF-8 -*-
from past.builtins import basestring

from .highchart_types import OptionTypeError, Series, SeriesOptions
from .common import Formatter, Events, Position, ContextButton, Options3d, ResetZoomButton, \
    DrillUpButton, Labels, PlotBands, PlotLines, Title, Items, Navigation, Background, Breaks, \
    DataClasses, DateTimeLabelFormats, Zones, Levels, Marker, \
    JSfunction, ColorObject, CSSObject, SVGObject, CommonObject, ArrayObject

import json, datetime

# Base Option Class
class BaseOptions(object):

    def __init__(self,**kwargs):
        self.update_dict(**kwargs)

    def __display_options__(self):
        print(json.dumps(self.__dict__, indent=4, sort_keys=True))

    def __jsonable__(self):
        return self.__dict__

    def __validate_options__(self, k, v, ov):
        if ov == NotImplemented: 
            raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
        if isinstance(v,dict) and isinstance(ov,dict):
            keys = v.keys()
            if len(keys) > 1: 
                raise NotImplementedError
            return isinstance(v[keys[0]],ov[keys[0]])
        return isinstance(v, ov) 

    def update_dict(self, **kwargs):
        for k, v in kwargs.items(): 
            if k in self.ALLOWED_OPTIONS:
                # if isinstance(self.ALLOWED_OPTIONS[k], tuple) and isinstance(self.ALLOWED_OPTIONS[k][0](), SeriesOptions):
                if k in PlotOptions.ALLOWED_OPTIONS.keys():
                    if self.__getattr__(k):
                        self.__dict__[k].update(series_type=k, **v)
                    else:
                        v = SeriesOptions(series_type=k, **v)
                        self.__dict__.update({k:v})

                elif isinstance(self.ALLOWED_OPTIONS[k], tuple) and isinstance(self.ALLOWED_OPTIONS[k][0](), CommonObject):
                    if isinstance(v, dict): 
                        if self.__getattr__(k): 
                            self.__dict__[k].update(v) #update dict
                        else: # first
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                    else:
                        OptionTypeError("Not An Accepted Input Type: %s, must be dictionary" % type(v))

                elif isinstance(self.ALLOWED_OPTIONS[k], tuple) and isinstance(self.ALLOWED_OPTIONS[k][0](), ArrayObject):
                    if self.__getattr__(k): #existing attr
                        if isinstance(v, dict):
                            self.__dict__[k].update(v) # update array
                        elif isinstance(v, list):
                            for item in v:
                                self.__dict__[k].update(item) # update array
                        else:
                            OptionTypeError("Not An Accepted Input Type: %s, must be list or dictionary" 
                                            % type(v))          
                    else: #first 
                        if isinstance(v, dict):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                        elif isinstance(v, list):
                            if len(v) == 1:
                                self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v[0])})
                            else:
                                self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v[0])})
                                for item in v[1:]:
                                    self.__dict__[k].update(item)
                        else:
                            OptionTypeError("Not An Accepted Input Type: %s, must be list or dictionary"
                                            % type(v))

                elif isinstance(self.ALLOWED_OPTIONS[k], tuple) and \
                    (isinstance(self.ALLOWED_OPTIONS[k][0](), CSSObject) or isinstance(self.ALLOWED_OPTIONS[k][0](), SVGObject)):
                    if self.__getattr__(k): 
                        for key, value in v.items(): # check if v has object input 
                            self.__dict__[k].__options__().update({key:value})
                        
                        v = self.__dict__[k].__options__()
                    # upating object
                    if isinstance(v, dict):
                        self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                    else:
                        self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](v)})

                elif isinstance(self.ALLOWED_OPTIONS[k], tuple) and (isinstance(self.ALLOWED_OPTIONS[k][0](), JSfunction) or \
                    isinstance(self.ALLOWED_OPTIONS[k][0](), Formatter) or isinstance(self.ALLOWED_OPTIONS[k][0](), ColorObject)):
                    if isinstance(v, dict):
                        self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                    else:
                        self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](v)})
                else:
                    self.__dict__.update({k:v})

            else:
                print(self.ALLOWED_OPTIONS)
                print(k, v)
                raise OptionTypeError("Not An Accepted Option Type: %s" % k)


    def __getattr__(self, item):
        if not item in self.__dict__:
            return None # Attribute Not Set
        else:
            return True


class ChartOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "alignTicks": bool,
        "animation": [bool, dict, basestring],
        "backgroundColor": (ColorObject, basestring, dict),
        "borderColor": (ColorObject, basestring, dict),
        "borderRadius": int,
        "borderWidth": int,
        "className": basestring,
        "defaultSeriesType": basestring,
        "events": (Events, dict),
        "height": [int,basestring],
        "ignoreHiddenSeries": bool,
        "inverted": bool,
        "margin": list,
        "marginBottom": int,
        "marginLeft": int,
        "marginRight": int,
        "marginTop": int,
        "options3d": (Options3d, dict), 
        "plotBackgroundColor": (ColorObject, basestring, dict),
        "plotBackgroundImage": basestring,
        "plotBorderColor": (ColorObject, basestring, dict),
        "plotBorderWidth": int,
        "plotShadow": bool,
        "polar": bool,
        "reflow": bool,
        "renderTo": basestring,
        "resetZoomButton": (ResetZoomButton, dict),
        "selectionMarkerFill": basestring,
        "shadow": bool,
        "showAxes": bool,
        "spacingBottom": int,
        "spacingLeft": int,
        "spacingRight": int,
        "spacingTop": int,
        "style": (CSSObject, dict),
        "type": basestring,
        "width": [int,basestring],
        "zoomType": basestring,
    }


class ColorAxisOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "dataClassColor": basestring,
        "dataClasses": (DataClasses, dict),
        "endOnTick": bool,
        "events": (Events, dict),
        "gridLineColor": (ColorObject, basestring, dict),
        "gridLineDashStyle": basestring,
        "gridLineWidth": [float, int],
        "id": basestring,
        "labels": (Labels, dict),
        "lineColor": (ColorObject, basestring, dict),
        "lineWidth": [float, int],
        "marker": (Marker, dict),
        "max": [float, int],
        "maxColor": (ColorObject, basestring, dict),
        "maxPadding": [float, int],
        "min": [float, int],
        "minColor": (ColorObject, basestring, dict),
        "minPadding": [float, int],
        "minorGridLineColor": (ColorObject, basestring, dict),
        "minorGridLineDashStyle": basestring,
        "minorGridLineWidth": int,
        "minorTickColor": (ColorObject, basestring, dict),
        "minorTickInterval": int,
        "minorTickLength": int,
        "minorTickPosition": basestring,
        "minorTickWidth": int,
        "reversed": bool,
        "showFirstLabel": bool,
        "showLastLabel": bool,
        "startOfWeek": int,
        "startOnTick": bool,
        "stops": list,
        "tickColor": (ColorObject, basestring, dict),
        "tickInterval": int,
        "tickLength": int,
        "tickPixelInterval": int,
        "tickPosition": basestring,
        "tickPositioner": JSfunction,
        "tickPositions": list,
        "tickWidth": int,
        "type": basestring,
}


class ColorsOptions(BaseOptions):
    """ Special Case, this is simply just an array of colours """
    def __init__(self):
        self.colors = {}

    def set_colors(self, colors):
        if isinstance(colors, basestring):
            self.colors = ColorObject(colors)
        elif isinstance(colors, list) or isinstance(colors, dict):
            self.colors  = colors
        else:
            OptionTypeError("Not An Accepted Input Type: %s" % type(colors))


    def __jsonable__(self):
        return self.colors


class CreditsOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "enabled": bool,
        "href": basestring,
        "position": (Position, dict), 
        "style": (CSSObject, dict),
        "text": basestring,
    }


class DrilldownOptions(BaseOptions): #not implement yet, need work in jinjia
    ALLOWED_OPTIONS = {
        "activeAxisLabelStyle": (CSSObject, dict),
        "activeDataLabelStyle": (CSSObject, dict),
        "animation": NotImplemented, #(bool, dict), #not sure how to implement 
        "drillUpButton": (DrillUpButton, dict),
        "series": (SeriesOptions, dict),
    }


class ExportingOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "buttons": (ContextButton, dict),
        "chartOptions": (ChartOptions, dict), 
        "enabled": bool,
        "filename": basestring,
        "formAttributes": NotImplemented,
        "scale": int,
        "sourceHeight": int,
        "sourceWidth": int,
        "type": basestring,
        "url": basestring,
        "width": int,
    }


class GlobalOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "Date": NotImplemented,
        "VMLRadialGradientURL": basestring,
        "canvasToolsURL": basestring,
        "getTimezoneOffset": (JSfunction, basestring),
        "timezoneOffset": int,
        "useUTC": bool,
    }


class LabelsOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "items": (Items, dict),
        "style": (CSSObject, dict),
    }


class LangOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "decimalPoint": basestring,
        "downloadJPEG": basestring,
        "downloadPDF": basestring,
        "downloadPNG": basestring,
        "donwloadSVG": basestring,
        "exportButtonTitle": basestring,
        "loading": basestring,
        "months": list,
        "noData": basestring,
        "numericSymbols": list,
        "printButtonTitle": basestring,
        "resetZoom": basestring,
        "resetZoomTitle": basestring,
        "shortMonths": list,
        "thousandsSep": basestring,
        "weekdays": list,
    }


class LegendOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "align": basestring,
        "backgroundColor": (ColorObject, basestring, dict),
        "borderColor": (ColorObject, basestring, dict),
        "borderRadius": int,
        "borderWidth": int,
        "enabled": bool,
        "floating": bool,
        "itemDistance": int,
        "itemHiddenStyle": (CSSObject, dict),
        "itemHoverStyle": (CSSObject, dict),
        "itemMarginBottom": int,
        "itemMarginTop": int,
        "itemStyle": (CSSObject, dict),
        "itemWidth": int,
        "labelFormat": basestring,
        "labelFormatter": (Formatter, JSfunction),
        "layout": basestring,
        "lineHeight": int,
        "margin": int,
        "maxHeight": int,
        "navigation": (Navigation, dict),
        "padding": int,
        "reversed": bool,
        "rtl": bool,
        "shadow": bool,
        "style": (CSSObject, dict),
        "symbolHeight": int,
        "symbolPadding": int,
        "symbolRadius": int,
        "symbolWidth": int,
        "title": (Title, dict),
        "useHTML": bool,
        "verticalAlign": basestring,
        "width": int,
        "x": int,
        "y": int,
    }


class LoadingOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "hideDuration": int,
        "labelStyle": (CSSObject, dict),
        "showDuration": int,
        "style": (CSSObject, dict),
    }


class NavigationOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "buttonOptions": (ContextButton, dict),
        "menuItemHoverStyle": (CSSObject, dict),
        "menuItemStyle": (CSSObject, dict),
        "menuStyle": (CSSObject, dict),
    }


class PaneOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "background": (Background, list), #arrayObject
        "center": list,
        "endAngle": int,
        "size": int,
        "startAngle": int,
    }


class PlotOptions(BaseOptions):
    """ Another Special Case: Interface With all the different Highchart Plot Types Here """
    ALLOWED_OPTIONS = {
        "area": (SeriesOptions, dict),
        "arearange": (SeriesOptions, dict),
        "areaspline": (SeriesOptions, dict),
        "areasplinerange": (SeriesOptions, dict),
        "bar": (SeriesOptions, dict),
        "boxplot": (SeriesOptions, dict),
        "bubble": (SeriesOptions, dict),
        "column": (SeriesOptions, dict),
        "columnrange": (SeriesOptions, dict),
        "errorbar": (SeriesOptions, dict),
        "gauge": (SeriesOptions, dict),
        "heatmap": (SeriesOptions, dict),
        "line": (SeriesOptions, dict),
        "pie": (SeriesOptions, dict),
        "scatter": (SeriesOptions, dict),
        "series": (SeriesOptions, dict),
        "spline": (SeriesOptions, dict),
        "treemap": (SeriesOptions, dict),
    }


class SeriesData(BaseOptions):
    """ Another Special Case: Stores Data Series in an array for returning to the chart object """
    def __init__(self):
        #self.__dict__.update([])
        self = []


class SubtitleOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "align": basestring,
        "floating": bool,
        "style": (CSSObject, dict),
        "text": basestring,
        "useHTML": bool,
        "verticalAlign": basestring,
        "x": int,
        "y": int,
    }


class TitleOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "align": basestring,
        "floating": bool,
        "margin": int,
        "style": (CSSObject, dict),
        "text": basestring,
        "useHTML": bool,
        "verticalAlign": basestring,
        "x": int,
        "y": int,
    }


class TooltipOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "animation": bool,
        "backgroundColor": (ColorObject, basestring, dict),
        "borderColor": (ColorObject, basestring, dict),
        "borderRadius": int,
        "borderWidth": int,
        "crosshairs": [bool, list, dict],
        "dateTimeLabelFormats": (DateTimeLabelFormats, dict),
        "enabled": bool,
        "followPointer": bool,
        "followTouchMove": bool,
        "footerFormat": basestring,
        "formatter": (Formatter, JSfunction),
        "headerFormat": basestring,
        "pointFormat": basestring,
        "pointFormatter": (Formatter, JSfunction),
        "positioner": (JSfunction, basestring),
        "shadow": bool,
        "shared": bool,
        "snap": int,
        "style": (CSSObject, dict),
        "useHTML": bool,
        "valueDecimals": int,
        "valuePrefix": basestring,
        "valueSuffix": basestring,
        "xDateFormat": basestring,
    }


class xAxisOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "allowDecimals": bool,
        "alternateGridColor": (ColorObject, basestring, dict),
        "categories": list,
        'crosshair': bool,
        "dateTimeLabelFormats": (DateTimeLabelFormats, dict),
        "endOnTick": bool, 
        "events": (Events, dict),
        "gridLineColor": (ColorObject, basestring, dict),
        "gridLineDashStyle": basestring,
        "gridLineWidth": int,
        "id": basestring,
        "labels": (Labels, dict),
        "lineColor": (ColorObject, basestring, dict),
        "lineWidth": int,
        "linkedTo": int,
        "max": [float, int],
        "maxPadding": [float, int],
        "maxZoom": NotImplemented,
        "min": [float, int],
        "minPadding": [float, int],
        "minRange": int,
        "minTickInterval": int,
        "minorGridLineColor": (ColorObject, basestring, dict),
        "minorGridLineDashStyle": basestring,
        "minorGridLineWidth": int,
        "minorTickColor": (ColorObject, basestring, dict),
        "minorTickInterval": int,
        "minorTickLength": int,
        "minorTickPosition": basestring,
        "minorTickWidth": int,
        "offset": bool,
        "opposite": bool,
        "plotBands": (PlotBands, list),
        "plotLines": (PlotLines, list),
        "reversed": bool,
        "showEmpty": bool,
        "showFirstLabel": bool,
        "showLastLabel": bool,
        "startOfWeek": int,
        "startOnTick": bool,
        "tickColor": (ColorObject, basestring, dict),
        "tickInterval": int,
        "tickLength": int,
        "tickPixelInterval": int,
        "tickPosition": basestring,
        "tickPositioner": JSfunction,
        "tickPositions": list,
        "tickWidth": int,
        "tickmarkPlacement": basestring,
        "title": (Title, dict),
        "type": basestring,
        "units": list
    }


class yAxisOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "allowDecimals": bool,
        "alternateGridColor": (ColorObject, basestring, dict),
        "breaks": (Breaks, dict),
        "categories": list,
        "ceiling": (int, float),
        "dateTimeLabelFormats": (DateTimeLabelFormats, dict),
        "endOnTick": bool,
        "events": (Events, dict),
        "floor": (int, float),
        "gridLineColor": (ColorObject, basestring, dict),
        "gridLineDashStyle": basestring,
        "gridLineInterpolation": basestring,
        "gridLineWidth": int,
        "gridZIndex": int,
        "id": basestring,
        "labels": (Labels, dict),
        "lineColor": (ColorObject, basestring, dict),
        "lineWidth": int,
        "linkedTo": int,
        "max": [float, int],
        "maxColor": (ColorObject, basestring, dict),
        "maxPadding": [float, int],
        "maxZoom": NotImplemented,
        "min": [float, int],
        "minColor": (ColorObject, basestring, dict),
        "minPadding": [float, int],
        "minRange": int,
        "minTickInterval": int,
        "minorGridLineColor": (ColorObject, basestring, dict),
        "minorGridLineDashStyle": basestring,
        "minorGridLineWidth": int,
        "minorTickColor": (ColorObject, basestring, dict),
        "minorTickInterval": int,
        "minorTickLength": int,
        "minorTickPosition": basestring,
        "minorTickWidth": int,
        "offset": bool,
        "opposite": bool,
        "plotBands": (PlotBands, list),
        "plotLines": (PlotLines, list),
        "reversed": bool,
        "reversedStacks": bool,
        "showEmpty": bool,
        "showFirstLabel": bool,
        "showLastLabel": bool,
        "stackLabels": (Labels, dict),
        "startOfWeek": int,
        "startOnTick": bool,
        "stops": list,
        "tickAmount": int,
        "tickColor": (ColorObject, basestring, dict),
        "tickInterval": int,
        "tickLength": int,
        "tickPixelInterval": int,
        "tickPosition": basestring,
        "tickPositioner": (JSfunction, basestring),
        "tickPositions": list,
        "tickWidth": int,
        "tickmarkPlacement": basestring,
        "title": (Title, dict),
        "type": basestring,
        "units": list    
    }

class zAxisOptions(BaseOptions): #only for 3D plots
    ALLOWED_OPTIONS = {
        "allowDecimals": bool,
        "alternateGridColor": (ColorObject, basestring, dict),
        "breaks": (Breaks, dict),
        "categories": list,
        "ceiling": (int, float),
        "dateTimeLabelFormats": (DateTimeLabelFormats, dict),
        "endOnTick": bool,
        "events": (Events, dict),
        "floor": (int, float),
        "gridLineColor": (ColorObject, basestring, dict),
        "gridLineDashStyle": basestring,
        "gridLineInterpolation": basestring,
        "gridLineWidth": int,
        "gridZIndex": int,
        "id": basestring,
        "labels": (Labels, dict),
        "lineColor": (ColorObject, basestring, dict),
        "lineWidth": int,
        "linkedTo": int,
        "max": [float, int],
        "maxColor": (ColorObject, basestring, dict),
        "maxPadding": [float, int],
        "maxZoom": NotImplemented,
        "min": [float, int],
        "minColor": (ColorObject, basestring, dict),
        "minPadding": [float, int],
        "minRange": int,
        "minTickInterval": int,
        "minorGridLineColor": (ColorObject, basestring, dict),
        "minorGridLineDashStyle": basestring,
        "minorGridLineWidth": int,
        "minorTickColor": (ColorObject, basestring, dict),
        "minorTickInterval": int,
        "minorTickLength": int,
        "minorTickPosition": basestring,
        "minorTickWidth": int,
        "offset": bool,
        "opposite": bool,
        "plotBands": (PlotBands, list),
        "plotLines": (PlotLines, list),
        "reversed": bool,
        "reversedStacks": bool,
        "showEmpty": bool,
        "showFirstLabel": bool,
        "showLastLabel": bool,
        "stackLabels": (Labels, dict),
        "startOfWeek": int,
        "startOnTick": bool,
        "stops": list,
        "tickAmount": int,
        "tickColor": (ColorObject, basestring, dict),
        "tickInterval": int,
        "tickLength": int,
        "tickPixelInterval": int,
        "tickPosition": basestring,
        "tickPositioner": (JSfunction, basestring),
        "tickPositions": list,
        "tickWidth": int,
        "tickmarkPlacement": basestring,
        "title": (Title, dict),
        "type": basestring,
        "units": list    
    }


class MultiAxis(object):

    def __init__(self, axis):
        AXIS_LIST = {
            "xAxis": xAxisOptions,
            "yAxis": yAxisOptions
            }
        self.axis = []
        self.AxisObj = AXIS_LIST[axis]

    def update(self, **kwargs):
        self.axis.append(self.AxisObj(**kwargs))
        
    def __jsonable__(self):
        return self.axis

