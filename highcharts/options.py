# -*- coding: UTF-8 -*-

from highchart_types import OptionTypeError, Series, SeriesOptions
from common import Formatter, Event

import json

# Base Option Class

class BaseOptions(object):

    def __init__(self,**kwargs):
        self.update_dict(**kwargs)

    def __display_options__(self):
        print json.dumps(self.__dict__,indent=4,sort_keys=True)

    def __to_dict__(self):
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
        for k, v in kwargs.items(): 
            k = k.split("_")
            if k[0] in self.ALLOWED_OPTIONS:
                if isinstance(self.ALLOWED_OPTIONS[k[0]],dict):
                    if len(k) > 2:  
                        raise NotImplementedError
                    else:
                        if self.__validate_options__(k[1],v,self.ALLOWED_OPTIONS[k[0]][k[1]]) or not v:
                            if not k[0] in self.__dict__:
                                self.__dict__.update({k[0]:{}})
                            self.__dict__[k[0]].update({k[1]:v})
                        else: 
                            print k, v
                            raise OptionTypeError("Option Type Mismatch: Expected: %s" % self.ALLOWED_OPTIONS[k[0]][k[1]]) 
                else:
                    if self.__validate_options__(k[0],v,self.ALLOWED_OPTIONS[k[0]]) or not v:
                        if isinstance(v,dict) and isinstance(self.ALLOWED_OPTIONS[k[0]],dict):
                            self.__dict__.update({k[0]:{v[v.keys()[0]]:v.values()[0]}})
                        else:
                            self.__dict__.update({k[0]:v})
                    else:
                        print k, v, self.ALLOWED_OPTIONS
                        raise OptionTypeError("Option Type Mismatch: Expected: %s" % self.ALLOWED_OPTIONS[k[0]])
            else:
                print self.ALLOWED_OPTIONS
                print self.__name__
                print k, v
                raise OptionTypeError("Not An Accepted Option Type: %s" % k[0])

    def __getattr__(self,item):
        if not item in self.__dict__:
            return None # Attribute Not Set


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
        "events": (Event, dict),
        "height": (int,basestring),
        "ignoreHiddenSeries": bool,
        "inverted": bool,
        "margin": list,
        "marginBottom": int,
        "marginLeft": int,
        "marginRight": int,
        "marginTop": int,
        "plotBackgroundColor": basestring,
        "plotBackgroundImage": basestring,
        "plotBorderColor": basestring,
        "plotBorderWidth": int,
        "plotShadow": bool,
        "polar": bool,
        "reflow": bool,
        "renderTo": basestring,
        "resetZoomButton": NotImplemented,
        "selectionMarkerFill": basestring,
        "shadow": bool,
        "showAxes": bool,
        "spacingBottom": int,
        "spacingLeft": int,
        "spacingRight": int,
        "spacingTop": int,
        "style": dict, # StyleObject
        "type": basestring,
        "width": (int,basestring),
        "zoomType": basestring,
    }


class ColorsOptions(BaseOptions):
    """ Special Case, this is simply just an array of colours """
    def __init__(self):
        # Predefined Colors
        self.__dict__.update({"colors":[
           '#2f7ed8', 
           '#0d233a', 
           '#8bbc21', 
           '#910000', 
           '#1aadce', 
           '#492970',
           '#f28f43', 
           '#77a1e5', 
           '#c42525', 
           '#a6c96a'
        ]})

    def set_colors(self,colors):
        self.__dict__.update({"colors":colors})


class CreditsOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "enabled": bool,
        "href": basestring,
        "position": NotImplemented, # Need Position Class
        "style": NotImplemented,
        "text": basestring,
    }


class ExportingOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "buttons": NotImplemented,
        "chartOptions": NotImplemented,
        "enabled": bool,
        "filename": basestring,
        "type": basestring,
        "url": basestring,
        "width": int,
    }


class GlobalOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "VMLRadialGradientURL": basestring,
        "canvasToolsURL": basestring,
        "useUTC": bool,
    }


class LabelsOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "items": NotImplemented,
        "style": NotImplemented,
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
        "itemHiddenStyle": NotImplemented,
        "itemHoverStyle": NotImplemented,
        "itemMarginBottom": int,
        "itemMarginTop": int,
        "itemStyle": {
            "color": basestring,   
        },
        "itemWidth": int,
        "labelFormatter": Formatter,
        "layout": basestring,
        "lineHeight": int,
        "margin": int,
        "maxHeight": int,
        "navigation": NotImplemented,
        "padding": int,
        "reversed": bool,
        "rtl": bool,
        "shadow": bool,
        "style": NotImplemented,
        "symbolPadding": int,
        "symbolWidth": int,
        "useHTML": bool,
        "verticalAlign": basestring,
        "width": int,
        "x": int,
        "y": int,

    }


class LoadingOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "hideDuration": int,
        "labelStyle": NotImplemented,
        "showDuration": int,
        "style": NotImplemented,
    }


class NavigationOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "buttonOptions": NotImplemented,
        "menuItemHoverStyle": NotImplemented,
        "menuItemStyle": NotImplemented,
        "menuStyle": NotImplemented,
    }


class PaneOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "background": list,
        "center": list,
        "endAngle": int,
        "startAngle": int,
    }


class PlotOptions(BaseOptions):
    """ Another Special Case: Interface With all the different Highchart Plot Types Here """
    ALLOWED_OPTIONS = {
        "area": SeriesOptions,
        "arearange": SeriesOptions,
        "areaspline": SeriesOptions,
        "areasplinerange": SeriesOptions,
        "bar": SeriesOptions,
        "column": SeriesOptions,
        "columnrange": SeriesOptions,
        "gauge": SeriesOptions,
        "line": SeriesOptions,
        "pie": SeriesOptions,
        "scatter": SeriesOptions,
        "series": SeriesOptions,
        "spline": SeriesOptions,
        "boxplot": SeriesOptions,
    }


class SeriesData(BaseOptions):
    """ Another Special Case: Stores Data Series in an array for returning to the chart object """
    def __init__(self):
        self.__dict__.update({"data":[]})

class SubtitleOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "align": basestring,
        "floating": bool,
        "style": dict,
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
        "style": {
            "color": basestring,
        },
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
        "crosshairs": NotImplemented,
        "enabled": bool,
        "footerFormat": basestring,
        "formatter": Formatter, 
        "pointFormat": basestring,
        "positioner": NotImplemented,
        "shadow": bool,
        "shared": bool,
        "snap": int,
        "style": NotImplemented,
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
        "dateTimeLabelFormats": NotImplemented,
        "endOnTick": bool,
        "events": NotImplemented,
        "gridLineColor": basestring,
        "gridLineDashStyle": basestring,
        "gridLineWidth": int,
        "id": basestring,
        "labels":   {
            "align": "basestring",
            "enabled": bool,
            "formatter": Formatter,
            "overflow": basestring,
            "rotation": int,
            "staggerLines": int,
            "step": int,
            "style": {
                "color": basestring,
                "fontSize": int,
                "fontWeight": basestring,
            },
            "useHTML": bool,
            "x": int,
            "y": int,
            "zIndex": int,
        },
        "lineColor": basestring,
        "lineWidth": int,
        "linkedTo": int,
        "max": float,
        "maxPadding": float,
        "maxZoom": int,
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
        "plotBands": NotImplemented,
        "plotLines": NotImplemented,
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
        "tickPositioner": NotImplemented,
        "tickPositions": list,
        "tickWidth": int,
        "tickmarkPlacement": basestring,
        "title": {
            "align": basestring,
            "enabled": bool,
            "margin": int,
            "offset": int,
            "rotation": int,
            "style": {
                "color": basestring,
            },
            "text": basestring,
        },
        "type": basestring,
    }


class yAxisOptions(BaseOptions):
    ALLOWED_OPTIONS = {
        "allowDecimals": bool,
        "alternateGridColor": basestring,
        "categories": list,
        "dateTimeLabelFormats": NotImplemented,
        "endOnTick": bool,
        "events": NotImplemented,
        "gridLineColor": basestring,
        "gridLineDashStyle": basestring,
        "gridLineWidth": int,
        "id": basestring,
        "labels":   {
            "align": "basestring",
            "enabled": bool,
            "formatter": Formatter,
            "overflow": basestring,
            "rotation": int,
            "staggerLines": int,
            "step": int,
            "style": dict,
            "useHTML": bool,
            "x": int,
            "y": int,
            "zIndex": int,
        },
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
        "plotBands": NotImplemented,
        "plotLines": NotImplemented,
        "reversed": bool,
        "showEmpty": bool,
        "showFirstLabel": bool,
        "showLastLabel": bool,
        "stackLabels": NotImplemented,
        "startOfWeek": int,
        "startOnTick": bool,
        "tickColor": basestring,
        "tickInterval": int,
        "tickLength": int,
        "tickPixelInterval": int,
        "tickPosition": basestring,
        "tickPositioner": NotImplemented,
        "tickPositions": list,
        "tickWidth": int,
        "tickmarkPlacement": basestring,
        "title": {
            "align": basestring,
            "enabled": bool,
            "margin": int,
            "offset": int,
            "rotation": int,
            "style": {
                "color": basestring,
            },
            "text": (basestring, bool),
        },
        "type": basestring,    
    }




if __name__ == '__main__':
    C = ChartOptions(type="pie")
    C.__display_options__()