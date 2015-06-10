#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" Python-Highcharts common.py
Common Functions For Highcharts
"""

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

    def __init__(self, format_type=None, format_string=FORMATTER_TYPE_MAPPINGS['default_tooltip']):
        self.__dict__.update({'formatter': FORMATTER_TYPE_MAPPINGS.get(format_type, format_string)})


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


class Event(object):

    def __init__(self, event_type, event_method):
        self.event_type = event_type
        self.event_method = event_method

if __name__ == '__main__':
    print path_to_array("M 4687 2398 L 4679 2402 4679 2398 Z")