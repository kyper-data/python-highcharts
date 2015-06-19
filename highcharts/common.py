#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" Python-Highcharts common.py
Common Functions For Highcharts
"""
import datetime

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

class Formatter(object):
    """ Base Formatter Class """

    def __init__(self, format):
        ### Choose either from default functions in FORMATTER_TYPE_MAPPINGS using format_type 
        ### or wriet a function in format_string
        if format in FORMATTER_TYPE_MAPPINGS:
            self.formatter = RawJavaScriptText(FORMATTER_TYPE_MAPPINGS[format])
        elif isinstance(format, basestring):
            self.formatter = RawJavaScriptText(format)
        else:
            raise OptionTypeError("Option Type Mismatch: Expected: %s" % basestring)

    def __options__(self):
        return self.formatter

class CSSObject(object):
    """ CSS style class """

    def __init__(self, **kwargs):
        self.css = kwargs
    
    def __options__(self):
        return self.css


class JSfunction(object):

    def __init__(self, function):
        if isinstance(function, basestring):
            self.function = RawJavaScriptText(function)
        elif isinstance(function, JSfunction):
            self.function = function
        else:
            raise OptionTypeError("Option Type Mismatch: Expected: %s" % basestring)


    def __options__(self):
        return self.function


class RawJavaScriptText:

    def __init__(self, jstext):
        self._jstext = jstext   
    def get_jstext(self):
        return self._jstext


class CommonObject(object):

    def __init__(self, **kwargs):
        self.process_kwargs(kwargs)

    def __validate_options__(self, k,v,ov):
        if ov == NotImplemented: 
            raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
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

    def process_kwargs(self,kwargs):
        IDV_OBJECT_LIST = [JSfunction, Formatter, CSSObject, Position]

        for k, v in kwargs.items():
            if k in self.ALLOWED_OPTIONS:
                if self.__validate_options__(k,v,self.ALLOWED_OPTIONS[k]):
                    if isinstance(self.ALLOWED_OPTIONS[k], tuple) and \
                        self.ALLOWED_OPTIONS[k][0] in IDV_OBJECT_LIST:

                        if isinstance(v, dict):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                        elif isinstance(v, CommonObject) or isinstance(v, ArrayObject):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v.__options__())})
                        elif isinstance(v, JSfunction) or isinstance(v, Formatter):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](v.__options__().get_jstext())})
                        elif isinstance(v, CSSObject):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v.__options__())})
                        else:
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](v)})
                    else:
                        self.__dict__.update({k:v})
                else: 
                    raise OptionTypeError("Option Type Mismatch: Expected: %s" % self.ALLOWED_OPTIONS[k])
            else: 
                raise OptionTypeError("Option: %s Not Allowed For Event Class:" % k)


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

    # def load_defaults(self,series_type):
    #     self.process_kwargs(DEFAULT_OPTIONS.get(series_type,{}),series_type)


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
    "symbolX": float,
    "symbolY": float,
    "text": basestring,
    "theme": NotImplemented,#ThemeObject
    "verticalAlign": basestring,
    "width": int,
    "x": int,
    "y": int, 
    }


class Options3d(CommonObject): 
    ALLOWED_OPTIONS = {
    "alpha": float,
    "beta": float,
    "depth": int,
    "enabled": bool,
    "frame": NotImplemented, # FrameObject
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
    "distance": int,
    "enabled": bool,
    "format": basestring,
    "formatter": (Formatter, JSfunction, basestring),
    "overflow": basestring,
    "rotation": int,
    "staggerLines": int,
    "step": int,
    "style": (CSSObject, dict),
    "useHTML": bool,
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
    "text": basestring,
    }

class ArrayObject(object):

    def __init__(self, **kwargs):
        self.process_kwargs(kwargs)

    def __validate_options__(self, k,v,ov):
        if ov == NotImplemented: 
            raise OptionTypeError("Option Type Currently Not Supported: %s" % k)
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
        return [self.__dict__]

    def process_kwargs(self,kwargs):
        IDV_OBJECT_LIST = [JSfunction, Formatter, CSSObject, Position]

        for k, v in kwargs.items():
            if k in self.ALLOWED_OPTIONS:
                if self.__validate_options__(k,v,self.ALLOWED_OPTIONS[k]):
                    if isinstance(self.ALLOWED_OPTIONS[k], tuple) and \
                        self.ALLOWED_OPTIONS[k][0] in IDV_OBJECT_LIST:

                        if isinstance(v, dict):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v)})
                        elif isinstance(v, CommonObject) or isinstance(v, ArrayObject):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v.__options__())})
                        elif isinstance(v, JSfunction) or isinstance(v, Formatter):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](v.__options__().get_jstext())})
                        elif isinstance(v, CSSObject):
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](**v.__options__())})
                        else:
                            self.__dict__.update({k:self.ALLOWED_OPTIONS[k][0](v)})
                    else:
                        self.__dict__.update({k:v})
                else: 
                    raise OptionTypeError("Option Type Mismatch: Expected: %s" % self.ALLOWED_OPTIONS[k])
            else: 
                raise OptionTypeError("Option: %s Not Allowed For Event Class:" % k)


class PlotBands(ArrayObject):
    ALLOWED_OPTIONS = {
    "borderColor": basestring,
    "borderWidth": int,
    "color": basestring,
    "events": (Events, dict),
    "from": (int, float, datetime.datetime),
    "id": basestring,
    }


class OptionTypeError(Exception):

    def __init__(self,*args):
        self.args = args


def path_to_array(path):
    print path
    path = path.replace(r'/([A-Za-z])/g', r' $1 ')
    path = path.replace(r'/^\s*/', "").replace(r'/\s*$/', "")
    path = path.split(" ");
    for i, v in enumerate(path):
        try:
            path[i] = float(v)
        except:
            pass
    return path

if __name__ == '__main__':
    print path_to_array("M 4687 2398 L 4679 2402 4679 2398 Z")