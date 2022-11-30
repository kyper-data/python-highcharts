#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" Python-Highcharts common.py
Common Functions For Highcharts
"""
from past.builtins import basestring
import datetime, re

FORMATTER_TYPE_MAPPINGS = {
    "default": "function() { return this.value }",
    "date": "function() { return''+Highcharts.dateFormat('%e. %b %Y %H:%M:%S',this.x) + ': '+ this.y; }",
    "pie": "function() { return '<b>'+ this.point.name +'</b>: '+ \
    this.percentage +' %'; }",
    "pound_yAxis": "function() { '&#163' + return this.value }",
    "pound_tooltip": "function() { return''+ this.x + ': '+ '&#163' +this.y; }",
    "percent": "function() { return this.value + ' %' }",
    "default_tooltip": "function () { return'<b>'+ this.series.name + '</b>: ' + this.y; }",
    "percent_tooltip": "function () { return'<b>'+ this.series.name + '</b>: ' + this.y + ' %'; }",
    "date_percent_tooltip": "function () { return''+Highcharts.dateFormat('%e. %b %Y',this.x) + '<br/><b>'+ this.series.name + '</b>: ' + this.y + ' %'; }",
    'filesize': """
function() {
    fileSizeInBytes = this.value;
    var i = -1;
    var byteUnits = [' kB', ' MB', ' GB', ' TB', 'PB', 'EB', 'ZB', 'YB'];
    do {
        fileSizeInBytes = fileSizeInBytes / 1024;
        i++;
    } while (fileSizeInBytes > 1024);

    return Math.max(fileSizeInBytes, 0.1).toFixed(1) + byteUnits[i];
}
""",
    'date_filesize_tooltip': """
function() {
    fileSizeInBytes = this.y;
    var i = -1;
    var byteUnits = [' kB', ' MB', ' GB', ' TB', 'PB', 'EB', 'ZB', 'YB'];
    do {
        fileSizeInBytes = fileSizeInBytes / 1024;
        i++;
    } while (fileSizeInBytes > 1024);

    return ''+Highcharts.dateFormat('%e. %b %Y %H:%M:%S',this.x) + '<br/><b>' + this.series.name + '</b>: ' + Math.max(fileSizeInBytes, 0.1).toFixed(1) + byteUnits[i];
}
""",
    'filesize_tooltip': """
function() {
    fileSizeInBytes = this.y;
    var i = -1;
    var byteUnits = [' kB', ' MB', ' GB', ' TB', 'PB', 'EB', 'ZB', 'YB'];
    do {
        fileSizeInBytes = fileSizeInBytes / 1024;
        i++;
    } while (fileSizeInBytes > 1024);

    return '<b>' + this.series.name + '</b>: ' + Math.max(fileSizeInBytes, 0.1).toFixed(1) + byteUnits[i];
}
""",
    'duration': """
function() {
    seconds = this.value;

    days = Math.floor(seconds / 86400);
    seconds = seconds - (days * 86400);

    hours = Math.floor(seconds / 3600);
    seconds = seconds - (hours * 3600);

    mins = Math.floor(seconds / 60);
    seconds = seconds - (mins * 60);

    res = "";
    if(days > 0){
        res += days + " d ";
    }
    if(hours > 0){
        res += hours + ' hr ';
    }
    if(mins > 0){
        res += mins + ' m ';
    }
    if(seconds > 0){
        res += seconds + ' s ';
    }
    return res;
}
""",
    'date_duration_tooltip': """
function() {
    seconds = this.y;

    days = Math.floor(seconds / 86400);
    seconds = seconds - (days * 86400);

    hours = Math.floor(seconds / 3600);
    seconds = seconds - (hours * 3600);

    mins = Math.floor(seconds / 60);
    seconds = seconds - (mins * 60);

    res = "";
    if(days > 0){
        res += days + " d ";
    }
    if(hours > 0){
        res += hours + ' hr ';
    }
    if(mins > 0){
        res += mins + ' m ';
    }
    if(seconds > 0){
        res += seconds + ' s ';
    }
    return ''+Highcharts.dateFormat('%e. %b %Y %H:%M:%S',this.x) + '<br/><b>'+ this.series.name + '</b>: ' + res;
}
""",
}

REGEX_LIST = {
    "re_funct" : re.compile(r'.*function\(.*\)\{.*\}', re.I), #for inputs such as function(xxx){xxx}
    "re_hcharts" : re.compile(r'.*Highcharts.*', re.I), #for inputs such as highcharts.xxxxx
}


class Formatter(object):
    """ Base Formatter Class """

    def __init__(self, format=None):
        ### Choose either from default functions in FORMATTER_TYPE_MAPPINGS using format_type 
        ### or wriet a function in format_string
        if format:
            if format in FORMATTER_TYPE_MAPPINGS:
                self.formatter = RawJavaScriptText(FORMATTER_TYPE_MAPPINGS[format])
            elif isinstance(format, basestring):
                self.formatter = RawJavaScriptText(format)
            else:
                raise OptionTypeError("Option Type Mismatch: Expected: %s" % basestring)

    def __options__(self):
        return self.formatter

    def __jsonable__(self):
        return self.formatter

class ColorObject(object):
    """ color object """
    
    def __init__(self, color = None, **kwargs):
        if not color:
            color = kwargs
        
        if color:
            if isinstance(color, dict):
                tmp = []            
                for i, item in enumerate(color['stops']):
                    tmp.append([RawJavaScriptText(x) if isinstance(x, basestring) and any([REGEX_LIST[key].search(x) for key in REGEX_LIST.keys()]) 
                                else x for x in item ])
                color['stops'] = tmp
                self.color = color
            elif any([REGEX_LIST[key].search(color) for key in REGEX_LIST.keys()]):
                self.color = RawJavaScriptText(color)
            elif isinstance(color, basestring):
                self.color = color
            else:
                raise OptionTypeError("Option Type Mismatch: Expected: %s" % (basestring or dict))
        else:
            self.color = None

    def __options__(self):
        return self.color

    def __jsonable__(self):
        return self.color


class CSSObject(object):
    """ CSS style class """
    ALLOWED_OPTIONS = {}
    def __init__(self, **kwargs):
        self.css = kwargs

        for k, v in self.css.items():
            if isinstance(v, basestring) and any([REGEX_LIST[key].search(v) for key in REGEX_LIST.keys()]):
                v = RawJavaScriptText(v)
                self.css.update({k:v})

    def __options__(self):
        return self.css

    def __jsonable__(self):
        return self.css


class SVGObject(object):
    """ SVG style class """

    def __init__(self, **kwargs):
        self.svg = kwargs

        for k, v in self.svg.items():
            if isinstance(v, basestring) and any([REGEX_LIST[key].search(v) for key in REGEX_LIST.keys()]):
                v = RawJavaScriptText(v)
                self.svg.update({k:v})
    
    def __options__(self):
        return self.svg

    def __jsonable__(self):
        return self.svg


class JSfunction(object):

    def __init__(self, function = None):
        if function:
            if isinstance(function, basestring):
                self.function = RawJavaScriptText(function)
            elif isinstance(function, JSfunction):
                self.function = function
            else:
                raise OptionTypeError("Option Type Mismatch: Expected: %s" % basestring)


    def __options__(self):
        return self.function

    def __jsonable__(self):
        return self.function


class RawJavaScriptText:

    def __init__(self, jstext):
        self._jstext = jstext   
    def get_jstext(self):
        return self._jstext


class CommonObject(object):

    def __init__(self, **kwargs):
        self.process_kwargs(kwargs)

    def __validate_options__(self, k, v, ov):

        if ov == NotImplemented: 
            raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
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

    def update(self, kwargs):
        for k, v in kwargs.items(): 
            if k in self.ALLOWED_OPTIONS:
                if isinstance(self.ALLOWED_OPTIONS[k], tuple) and isinstance(self.ALLOWED_OPTIONS[k][0](), CommonObject):
                    # re-construct input dict with existing options in objects
                    if self.__getattr__(k):
                        if isinstance(v, dict):
                            self.__options__()[k].update(v)
                        else:
                            self.__options__()[k].__options__().update(v)
                    else:
                        self.__options__().update({k:allowed_args[k][0](**v)}) 

                elif isinstance(self.ALLOWED_OPTIONS[k], tuple) and isinstance(self.ALLOWED_OPTIONS[k][0](), ArrayObject):
                    # update array 
                    if isinstance(v, dict):
                        self.__dict__[k].append(self.ALLOWED_OPTIONS[k][0](**v))
                    elif isinstance(v, list):
                        for item in v:
                            self.__dict__[k].append(self.ALLOWED_OPTIONS[k][0](**item))
                    else:
                        OptionTypeError("Not An Accepted Input Type: %s" % type(v))        

                elif isinstance(self.ALLOWED_OPTIONS[k], tuple) and \
                    (isinstance(self.ALLOWED_OPTIONS[k][0](), CSSObject) or isinstance(self.ALLOWED_OPTIONS[k][0](), SVGObject)):
                    if self.__getattr__(k):
                        for key, value in v.items():
                            self.__dict__[k].__options__().update({key:value})
                    else:
                        self.__dict__.update({k:allowed_args[k][0](**v)})
                    
                    v = self.__dict__[k].__options__()
                    # upating object
                    if isinstance(v, dict):
                        self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                    else:
                        self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](v)})

                elif isinstance(self.ALLOWED_OPTIONS[k], tuple) and (isinstance(self.ALLOWED_OPTIONS[k][0](), JSfunction) or
                    isinstance(self.ALLOWED_OPTIONS[k][0](), Formatter) or isinstance(self.ALLOWED_OPTIONS[k][0](), ColorObject)):
                    if isinstance(v, dict):
                        self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                    else:
                        self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](v)})
                else:
                    self.__dict__.update({k:v})

            else:
                raise OptionTypeError("Not An Accepted Option Type: %s" % k)

    def process_kwargs(self, kwargs):
        
        for k, v in kwargs.items():
            if k in self.ALLOWED_OPTIONS:
                if self.__validate_options__(k,v,self.ALLOWED_OPTIONS[k]):
                    if isinstance(self.ALLOWED_OPTIONS[k], tuple) and \
                        self.ALLOWED_OPTIONS[k][0] in IDV_OBJECT_LIST:
                        if isinstance(v, dict):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                        elif isinstance(v, CommonObject) or isinstance(v, ArrayObject) or \
                            isinstance(v, CSSObject) or isinstance(v, SVGObject) or isinstance(v, ColorObject) or \
                            isinstance(v, JSfunction) or isinstance(v, Formatter) or isinstance(v, datetime.datetime):
                            self.__dict__.update({k:v})
                        else:
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](v)})
                    else:
                        self.__dict__.update({k:v})
                else:
                    raise OptionTypeError("Option Type Mismatch: Expected: %s" % self.ALLOWED_OPTIONS[k])
            else:
                raise OptionTypeError("Option: %s Not Allowed For Event Class:" % k)

    def __getattr__(self, item):
        if not item in self.__dict__:
            return None # Attribute Not Set
        else:
            return True


class Events(CommonObject):
    """ Class for event listener """

    ALLOWED_OPTIONS = {
    "addSeries": (JSfunction, basestring),
    "afterPrint": (JSfunction, basestring),
    "beforePrint": (JSfunction, basestring),
    "click": (JSfunction, basestring),
    "drilldown": (JSfunction, basestring),
    "drillup": (JSfunction, basestring),
    "load": (JSfunction, basestring),
    "redraw": (JSfunction, basestring),
    "selection": (JSfunction, basestring),
    "afterAnimate": (JSfunction, basestring),
    "checkboxClick": (JSfunction, basestring),
    "hide": (JSfunction, basestring),
    "legendItemClick": (JSfunction, basestring),
    "mouseOut": (JSfunction, basestring),
    "mouseOver": (JSfunction, basestring),
    "show": (JSfunction, basestring),
    "remove": (JSfunction, basestring),
    "select": (JSfunction, basestring),
    "unselect": (JSfunction, basestring),
    "update": (JSfunction, basestring),
    "afterBreaks": (JSfunction, basestring),
    "afterSetExtremes": (JSfunction, basestring),
    "pointBreak": (JSfunction, basestring),
    "setExtremes": (JSfunction, basestring)  
    }

class Point(CommonObject):
    ALLOWED_OPTIONS = {
    "events": (Events, dict)
    }

class Position(CommonObject):
    ALLOWED_OPTIONS = {
    "align": basestring,
    "verticalAlign": basestring,
    "x": int,
    "y": int, 
    }

class ContextButton(CommonObject):
    """ Option class for the export button """
    ALLOWED_OPTIONS = {
    "align": basestring,
    "enabled": bool,
    "height": int,
    "menuItems": NotImplemented,
    "onclick": (JSfunction, basestring),
    "symbol": basestring,
    "symbolFill": basestring,
    "symbolSize": int,
    "symbolStroke": basestring,
    "symbolStrokeWidth": int,
    "symbolX": [float, int],
    "symbolY": [float, int],
    "text": basestring,
    "theme": NotImplemented,#ThemeObject
    "verticalAlign": basestring,
    "width": int,
    "x": int,
    "y": int, 
    }

class Back(CommonObject):
    ALLOWED_OPTIONS = {
    "color": (ColorObject, basestring, dict),
    "size": [int, float]
    }

class Bottom(CommonObject):
    ALLOWED_OPTIONS = {
    "color": (ColorObject, basestring, dict),
    "size": [int, float]
    }

class Side(CommonObject):
    ALLOWED_OPTIONS = {
    "color": (ColorObject, basestring, dict),
    "size": [int, float]
    }

class Frame(CommonObject):
    ALLOWED_OPTIONS = {
    "back": (Back, dict),
    "bottom": (Bottom, dict),
    "side": (Side, dict),
    }

class Options3d(CommonObject): 
    ALLOWED_OPTIONS = {
    "alpha": [float, int],
    "beta": [float, int],
    "depth": int,
    "enabled": bool,
    "frame": (Frame, dict), 
    "viewDistance": int
    }

class ResetZoomButton(CommonObject): 
    ALLOWED_OPTIONS = {
    "position": (Position, dict),
    "relativeTo": basestring,
    "theme": NotImplemented #ThemeObject
    }

class DrillUpButton(CommonObject): 
    ALLOWED_OPTIONS = {
    "position": (Position, dict),
    "relativeTo": basestring,
    "theme": NotImplemented #ThemeObject
    },

class Labels(CommonObject):   
    ALLOWED_OPTIONS = {
    "align": basestring,
    "backgroundColor": (ColorObject, basestring, dict),
    "borderColor": (ColorObject, basestring, dict),
    "borderRadius": [float, int],
    "borderWidth": [int, basestring],
    "color": (ColorObject, basestring, dict),
    "connectorColor": (ColorObject, basestring, dict),
    "connectorPadding": [float, int],
    "connectorWidth": [float, int],
    "crop": bool,
    "defer": bool,
    "distance": int,
    "enabled": bool,
    "format": basestring,
    "formatter": (Formatter, JSfunction, basestring),
    "inside": bool,
    "overflow": basestring,
    "padding": [float, int],
    "rotation": int, 
    "shadow": [bool, dict], #shadow object
    "shape": basestring,
    "softConnector": bool,
    "staggerLines": int,
    "step": int,
    "style": (CSSObject, dict),
    "text": basestring,
    "textAlign": basestring,
    "useHTML": bool,
    "verticalAlign": basestring,
    "x": int,
    "y": int,
    "zIndex": int,
    }

class Title(CommonObject): 
    ALLOWED_OPTIONS = {
    "align": basestring,
    "enabled": bool,
    "margin": int,
    "offset": int,
    "rotation": int,
    "style": (CSSObject, dict),
    "text": [basestring, type(None)]
    }

class Navigation(CommonObject): 
    ALLOWED_OPTIONS = {
    "activeColor": (ColorObject, basestring, dict),
    "animation": NotImplemented,
    "arrowSize": int,
    "inactiveColor": (ColorObject, basestring, dict),
    "style": (CSSObject, dict),
    }

class DateTimeLabelFormats(CommonObject):
    ALLOWED_OPTIONS = {
    "millisecond": basestring,
    "second": basestring,
    "minute": basestring,
    "hour": basestring,
    "day": basestring,
    "week": basestring,
    "month": basestring,
    "year": basestring,
    }

class Select(CommonObject):
    ALLOWED_OPTIONS = {
    "enabled": bool,
    "fillColor": (ColorObject, basestring, dict),
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "radius": int,
    }

class States(CommonObject):
    ALLOWED_OPTIONS = {
    "hover": dict,
    "select": dict,
    }

class Marker(CommonObject):
    ALLOWED_OPTIONS = {
    "enabled": bool,
    "fillColor": (ColorObject, basestring, dict),
    "height": int,
    "lineWidth": int,
    "lineColor": (ColorObject, basestring, dict),
    "radius": int,
    "states": (States, dict),
    "symbol": basestring,
    "width": int
    }

class Halo(CommonObject):
    ALLOWED_OPTIONS = {
    "attributes": (SVGObject, dict),
    "opacity": float,
    "size": int
    }

class Hover(CommonObject):
    ALLOWED_OPTIONS = {
    "enabled": bool,
    "fillColor": (ColorObject, basestring, dict),
    "halo": (Halo, dict),
    "lineColor": (ColorObject, basestring, dict),
    "lineWidth": int,
    "lineWidthPlus": int,
    "marker": (Marker, dict),
    "radius": int,
    "radiusPlus": int,
    "color": (ColorObject, basestring, dict),
    }

class States(CommonObject):
    ALLOWED_OPTIONS = {
    "hover": (Hover, dict),
    "select": (Select, dict)
    }

class Tooltip(CommonObject):
    ALLOWED_OPTIONS = {
    "dateTimeLabelFormats": (DateTimeLabelFormats, dict),
    "followPointer": bool,
    "followTouchMove": bool,
    "footerFormat": basestring,
    "headerFormat": basestring,
    "hideDelay": int,
    "pointFormat": basestring,
    "pointFormatter": (Formatter, JSfunction, basestring),
    "shape": basestring,
    "valueDecimals": int,
    "valuePrefix": basestring,
    "valueSuffix": basestring,
    "xDateFormat": basestring
    }


class ArrayObject(object):

    def __init__(self, **kwargs):
        self.data =[]
        self.process_kwargs(kwargs)

    def __validate_options__(self, k,v,ov):
 
        if ov == NotImplemented: 
            raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
        if isinstance(ov,list):
            if isinstance(v,tuple(ov)): return True
            else:
                raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
        else:
            if ov == NotImplemented: raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
            if isinstance(v,ov): return True
            else: return False

    def __options__(self):
        return self.data

    def __jsonable__(self):
        return self.data

    def update(self, kwargs):
        self.process_kwargs(kwargs)

    def process_kwargs(self, kwargs):
        temp = {}
        for k, v in kwargs.items():
            if k in self.ALLOWED_OPTIONS:
                if self.__validate_options__(k,v,self.ALLOWED_OPTIONS[k]):
                    if isinstance(self.ALLOWED_OPTIONS[k], tuple) and \
                        self.ALLOWED_OPTIONS[k][0] in IDV_OBJECT_LIST:
                        if isinstance(v, dict):
                            temp.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                        elif isinstance(v, CommonObject) or isinstance(v, ArrayObject) or \
                            isinstance(v, CSSObject) or isinstance(v, SVGObject) or isinstance(v, ColorObject) or \
                            isinstance(v, JSfunction) or isinstance(v, Formatter) or isinstance(v, datetime.datetime):
                            temp.update({k:v})
                        else:
                            temp.update({k:self.ALLOWED_OPTIONS[k][0](v)})
                    else:
                        temp.update({k:v})   
                else: 
                    raise OptionTypeError("Option Type Mismatch: Expected: %s" % self.ALLOWED_OPTIONS[k])
            else: 
                raise OptionTypeError("Option: %s Not Allowed For Event Class:" % k)
        self.data.append(temp)

class PlotBands(ArrayObject):
    ALLOWED_OPTIONS = {
    "borderColor": (ColorObject, basestring, dict),
    "borderWidth": [int, basestring],
    "color": (ColorObject, basestring, dict),
    "events": (Events, dict),
    "from": [int, float, datetime.datetime],
    "id": basestring,
    "label": (Labels, dict),
    "to": [int, float, datetime.datetime],
    "zIndex": int
    }

class PlotLines(ArrayObject):
    ALLOWED_OPTIONS = {
    "color": (ColorObject, basestring, dict),
    "dashStyle": basestring,
    "events": (Events, dict),
    "id": basestring,
    "label": (Labels, dict),
    "value": [int, float],
    "width": int,
    "zIndex": int
    }

class Items(ArrayObject):
    ALLOWED_OPTIONS = {
    "html": basestring,
    "style": (CSSObject, dict)
    }

class Background(ArrayObject):
    ALLOWED_OPTIONS = {
    "backgroundColor": (ColorObject, basestring, dict),
    "borderWidth": [int, basestring],
    "borderColor": (ColorObject, basestring, dict),
    "innerWidth": int,
    "outerWidth": int,
    "outerRadius": basestring,
    "shape": basestring,
    }

class Breaks(ArrayObject):
    ALLOWED_OPTIONS = {
    "breakSize": int,
    "from": [int, float],
    "repeat": int,
    "to": [int, float],
    }

class DataClasses(ArrayObject):
    ALLOWED_OPTIONS = {
    "color": (ColorObject, basestring, dict),
    "from": [int, float],
    "name": basestring,
    "to": [int, float],
    }

class Zones(ArrayObject):
    ALLOWED_OPTIONS = {
    "color": (ColorObject, basestring, dict),
    "dashStyle": basestring,
    "fillColor": (ColorObject, basestring, dict),
    "value": [int, float],
    }

class Levels(ArrayObject):
    ALLOWED_OPTIONS = {
    "borderColor": (ColorObject, basestring, dict),
    "borderDashStyle": basestring,
    "borderWidth": [int, basestring],
    "color": (ColorObject, basestring, dict),
    "dataLabels": (Labels, dict),
    "layoutAlgorithm": basestring,
    "layoutStartingDirection": basestring,
    "level": int,
    }    


IDV_OBJECT_LIST = [JSfunction, Formatter, Halo, Marker, Labels,
                    Position, Hover, Select, Events, States, ContextButton,
                    CSSObject, SVGObject, ColorObject,
                    RawJavaScriptText, DateTimeLabelFormats]


class OptionTypeError(Exception):

    def __init__(self, *args):
        self.args = args
