# -*- coding: UTF-8 -*-

from highchart_types import OptionTypeError, Series, SeriesOptions
from common import Formatter, Events, Position, ContextButton, Options3d, ResetZoomButton, \
    DrillUpButton, Labels, PlotBands, PlotLines, Title, Items, Navigation, Background, Breaks, \
    DateTimeLabelFormats, Zones, JSfunction, CSSObject, SVGObject, CommonObject, ArrayObject

import json, datetime

# Base Option Class
class BaseOptions(object):

    def __init__(self,**kwargs):
        self.update_dict(**kwargs)

    def __display_options__(self):
        print(json.dumps(self.__dict__,indent=4,sort_keys=True))

    def __jsonable__(self):
        return self.__dict__

    def __validate_options__(self,k,v,ov):
        if ov == NotImplemented: 
            raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
        if isinstance(v,dict) and isinstance(ov,dict):
            keys = v.keys()
            if len(keys) > 1: 
                raise NotImplementedError
            return isinstance(v[keys[0]],ov[keys[0]])
        return isinstance(v, ov) 

    def update_dict(self,**kwargs):

        DICTOBJECT_LIST = {
            "events": Events,
            "options3d": Options3d,
            "resetZoomButton": ResetZoomButton,
            "drillUpButton": DrillUpButton,
            "position": Position,
            "buttons": ContextButton,
            "labels": Labels,
            "title": Title,
            "formatter": Formatter,
            "labelFormatter": Formatter,
            "chartOptions": ChartOptions,
            "getTimezoneOffset": JSfunction,
            "positioner": JSfunction,
            "style": CSSObject,
        }

        ARRAYOBJECT_LIST = {
            "background": Background,
            "breaks": Breaks,
            "plotBands": PlotBands,
            "plotLines": PlotLines,
            "items": Items,
            "zones": Zones
        }

        for k, v in kwargs.items(): 
            if k in self.ALLOWED_OPTIONS:
                if k in DICTOBJECT_LIST: 
                    # re-construct input dict with existing options in objects
                    if self.__getattr__(k): 
                        if isinstance(v, dict): 
                            for key, value in v.items(): # check if v has object input 
                                if key in DICTOBJECT_LIST:
                                    self.__dict__[k].__options__()[key].__options__().update(value)
                                    #new_v =  self.__dict__[k].__options__()[key].__options__()
                                    #self.__dict__[k].__options__().update({key:new_v})
                                else:
                                    self.__dict__[k].__options__().update({key:value})
                        else:
                            self.__dict__[k].__options__().update(v)

                        v = self.__dict__[k].__options__()
                    # upating object
                    if isinstance(v, dict):
                        self.__dict__.update({k:DICTOBJECT_LIST[k](**v)})
                    else:
                        self.__dict__.update({k:DICTOBJECT_LIST[k](v)})

                elif k in ARRAYOBJECT_LIST:
                    if self.__getattr__(k): # update array 
                        if isinstance(v, dict):
                            self.__dict__[k].append(ARRAYOBJECT_LIST[k](**v))
                        elif isinstance(v, list):
                            for item in v:
                                self.__dict__[k].append(ARRAYOBJECT_LIST[k](**item))
                        else:
                            OptionTypeError("Not An Accepted Input Type: %s" % type(v))        
                    else: #first 
                        if isinstance(v, dict):
                            self.__dict__.update({k:[ARRAYOBJECT_LIST[k](**v)]})
                        elif isinstance(v, list):
                            if len(v) == 1:
                                self.__dict__.update({k:[ARRAYOBJECT_LIST[k](**v[0])]})
                            else:
                                self.__dict__.update({k:[ARRAYOBJECT_LIST[k](**v[0])]})
                                for item in v[1:]:
                                    self.__dict__[k].append(ARRAYOBJECT_LIST[k](**item))
                        else:
                            OptionTypeError("Not An Accepted Input Type: %s" % type(v))

                elif isinstance(v, SeriesOptions):
                    if self.__getattr__(k):
                        self.__dict__[k].__options__().update(v.__options__())
                        v = SeriesOptions(series_type=k, supress_errors=True, 
                            **self.__dict__[k].__options__())
                    self.__dict__.update({k:v})      

                else:
                    self.__dict__.update({k:v})

            else:
                print(self.ALLOWED_OPTIONS)
                print(self.__name__)
                print(k, v)
                raise OptionTypeError("Not An Accepted Option Type: %s" % k)


    def __getattr__(self,item):
        if not item in self.__dict__:
            return None # Attribute Not Set
        else:
            return True


class ChartOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "alignTicks": bool,
        "animation": bool,
        "backgroundColor": basestring,
        "borderColor": basestring,
        "borderRadius": int,
        "borderWidth": int,
        "className": basestring,
        "defaultSeriesType": basestring,
        "events": Events,
        "height": [int,basestring],
        "ignoreHiddenSeries": bool,
        "inverted": bool,
        "margin": list,
        "marginBottom": int,
        "marginLeft": int,
        "marginRight": int,
        "marginTop": int,
        "options3d": (Options3d, dict), 
        "plotBackgroundColor": basestring,
        "plotBackgroundImage": basestring,
        "plotBorderColor": basestring,
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


class ColorsOptions(BaseOptions):
    """ Special Case, this is simply just an array of colours """
    def __init__(self):
        # Predefined Colors
        self.colors = ['#2f7ed8', 
           '#0d233a', 
           '#8bbc21', 
           '#910000', 
           '#1aadce', 
           '#492970',
           '#f28f43', 
           '#77a1e5', 
           '#c42525', 
           '#a6c96a']

        #self.colors = []

    def set_colors(self,colors):
        #self.__dict__.update({"colors":colors})
        self.colors.append(colors)

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
        "series": SeriesOptions,
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
        "getTimezoneOffset": JSfunction,
        "timezoneOffset": int,
        "useUTC": bool,
    }


class LabelsOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "items": Items, 
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
        "backgroundColor": basestring,
        "borderColor": basestring,
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
        "column": (SeriesOptions, dict),
        "columnrange": (SeriesOptions, dict),
        "gauge": (SeriesOptions, dict),
        "line": (SeriesOptions, dict),
        "pie": (SeriesOptions, dict),
        "scatter": (SeriesOptions, dict),
        "series": (SeriesOptions, dict),
        "spline": (SeriesOptions, dict) ,
        "boxplot": (SeriesOptions, dict),
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
        "backgroundColor": basestring,
        "borderColor": basestring,
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
        "positioner": JSfunction,
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
        "alternateGridColor": basestring,
        "categories": list,
        "dateTimeLabelFormats": (DateTimeLabelFormats, dict),
        "endOnTick": bool, 
        "events": Events,
        "gridLineColor": basestring,
        "gridLineDashStyle": basestring,
        "gridLineWidth": int,
        "id": basestring,
        "labels": (Labels, dict),
        "lineColor": basestring,
        "lineWidth": int,
        "linkedTo": int,
        "max": float,
        "maxPadding": float,
        "maxZoom": NotImplemented,
        "min": float,
        "minPadding": float,
        "minRange": int,
        "minTickInterval": int,
        "minorGridLineColor": basestring,
        "minorGridLineDashStyle": basestring,
        "minorGridLineWidth": int,
        "minorTickColor": basestring,
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
        "tickColor": basestring,
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
        "alternateGridColor": basestring,
        "breaks": Breaks,
        "categories": list,
        "ceiling": (int, float),
        "dateTimeLabelFormats": (DateTimeLabelFormats, dict),
        "endOnTick": bool,
        "events": Events,
        "floor": (int, float),
        "gridLineColor": basestring,
        "gridLineDashStyle": basestring,
        "gridLineInterpolation": basestring,
        "gridLineWidth": int,
        "gridZIndex": int,
        "id": basestring,
        "labels": (Labels, dict),
        "lineColor": basestring,
        "lineWidth": int,
        "linkedTo": int,
        "max": float,
        "maxColor": basestring,
        "maxPadding": float,
        "maxZoom": NotImplemented,
        "min": float,
        "minColor": basestring,
        "minPadding": float,
        "minRange": int,
        "minTickInterval": int,
        "minorGridLineColor": basestring,
        "minorGridLineDashStyle": basestring,
        "minorGridLineWidth": int,
        "minorTickColor": basestring,
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
        "tickColor": basestring,
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




if __name__ == '__main__':
    C = ChartOptions(type="pie")
    C.__display_options__()