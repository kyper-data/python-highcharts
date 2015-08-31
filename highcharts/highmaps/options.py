# -*- coding: UTF-8 -*-
from past.builtins import basestring

from .highmap_types import OptionTypeError, Series, SeriesOptions
from .common import Formatter, Events, Position, ContextButton, Button, Options3d, ResetZoomButton, \
    DrillUpButton, Labels, DataClasses, Title, Items, Navigation, Background, Breaks, Marker, \
    DateTimeLabelFormats, JSfunction, ColorObject, CSSObject, SVGObject, CommonObject, ArrayObject

import json, datetime

# Base Option Class
class BaseOptions(object):

    def __init__(self, **kwargs):
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
        "animation": [bool, dict, basestring],
        "backgroundColor": (ColorObject, basestring, dict),
        "borderColor": (ColorObject, basestring, dict),
        "borderRadius": [int, float],
        "borderWidth": [int, float],
        "className": basestring,
        "events": (Events, dict),
        "height": [int,basestring],
        "margin": list,
        "marginBottom": int,
        "marginLeft": int,
        "marginRight": int,
        "marginTop": int,
        "plotBackgroundColor": (ColorObject, basestring, dict),
        "plotBackgroundImage": basestring,
        "plotBorderColor": (ColorObject, basestring, dict),
        "plotBorderWidth": [int, float],
        "plotShadow": bool,
        "reflow": bool,
        "renderTo": basestring,
        "resetZoomButton": (ResetZoomButton, dict),
        "selectionMarkerFill": basestring,
        "shadow": bool,
        "spacing": list,
        "spacingBottom": int,
        "spacingLeft": int,
        "spacingRight": int,
        "spacingTop": int,
        "style": (CSSObject, dict),
        "type": basestring,
        "width": [int,basestring],
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
        "series": (Series, dict),
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
        "borderRadius": [int, float],
        "borderWidth": [int, float],
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
        "valueDecimals": int,
        "valueSuffix": basestring,
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


class MapNavigationOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "buttonOptions": (ContextButton, dict),
        "buttons": (Button, dict),
        "enableButtons": bool,
        "enableDoubleClickZoom": bool,
        "enableDoubleClickZoomTo": bool,
        "enableMouseWheelZoom": bool,
        "enableTouchZoom": bool,
        "enabled": bool,
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
        "heatmap": (SeriesOptions, dict),
        "map": (SeriesOptions, dict),
        "mapbubble": (SeriesOptions, dict),
        "mapline": (SeriesOptions, dict),
        "mappoint": (SeriesOptions, dict),
        "series": (SeriesOptions, dict),
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
        "borderRadius": [int, float],
        "borderWidth": [int, float],
        "crosshairs": [bool, list, dict],
        "enabled": bool,
        "followPointer": bool,
        "followTouchMove": bool,
        "footerFormat": basestring,
        "formatter": (Formatter, JSfunction),
        "headerFormat": basestring,
        "pointFormat": basestring,
        "positioner": (JSfunction, basestring),
        "shadow": bool,
        "style": (CSSObject, dict),
        "useHTML": bool,
        "valueDecimals": int,
        "valuePrefix": basestring,
        "valueSuffix": basestring,
    }


class xAxisOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "allowDecimals": bool,
        "alternateGridColor": (ColorObject, basestring, dict),
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
        "reversed": bool,
        "showEmpty": bool,
        "showFirstLabel": bool,
        "showLastLabel": bool,
        "startOnTick": bool,
        "tickColor": (ColorObject, basestring, dict),
        "tickInterval": int,
        "tickLength": int,
        "tickPixelInterval": int,
        "tickPosition": basestring,
        "tickPositioner": JSfunction,
        "tickPositions": list,
        "tickWidth": int,
        "title": (Title, dict),
    }


class yAxisOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "allowDecimals": bool,
        "alternateGridColor": (ColorObject, basestring, dict),
        "endOnTick": bool,
        "events": (Events, dict),
        "floor": (int, float),
        "gridLineColor": (ColorObject, basestring, dict),
        "gridLineDashStyle": basestring,
        "gridLineWidth": int,
        "id": basestring,
        "labels": (Labels, dict),
        "lineColor": (ColorObject, basestring, dict),
        "lineWidth": int,
        "max": [float, int],
        "maxColor": (ColorObject, basestring, dict),
        "maxPadding": [float, int],
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
        "reversed": bool,
        "showEmpty": bool,
        "showFirstLabel": bool,
        "showLastLabel": bool,
        "startOnTick": bool,
        "tickColor": (ColorObject, basestring, dict),
        "tickInterval": int,
        "tickLength": int,
        "tickPixelInterval": int,
        "tickPosition": basestring,
        "tickPositioner": (JSfunction, basestring),
        "tickPositions": list,
        "tickWidth": int,
        "title": (Title, dict),  
    }
    