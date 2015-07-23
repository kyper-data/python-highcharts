# -*- coding: utf-8 -*-
from future.standard_library import install_aliases
install_aliases()
from urllib.request import urlopen
import urllib

import json, os, sys
import pandas as pd
import numpy as np
import datetime, re, string
from datetime import tzinfo


def jsonp_loader(url, prefix_regex = r'^(.*\()', suffix_regex = r'(\);)$', regex = None):

    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
    req = urllib.request.Request(url, headers=hdr)
    page = urlopen(req)
    result = page.read()
    # replace all the redundant info with none 
    if regex:
        result = re.sub(regex, '', result)

    prefix = re.search(prefix_regex, result).group()
    suffix = re.search(suffix_regex, result).group()
    if result.startswith(prefix) and result.endswith(suffix):
        result = result[len(prefix):-len(suffix)]

    return json.loads(result, encoding='utf8', cls=JSONPDecoder)


def interpolateRGB(lowRGB, highRGB, fraction):
    color = []

    for i in range(3):
        color.append((highRGB[i] - lowRGB[i]) * fraction + lowRGB[i])

    return 'rgb(' + str(int(round(color[0],0))) + ',' + str(int(round(color[1],0))) + ',' + \
        str(int(round(color[2],0))) + ')'


class JSONPDecoder(json.JSONDecoder):

    def decode(self, json_string):
        """
        json_string is basicly string that you give to json.loads method
        """
        JS_datetime = r'Date\.UTC\(([0-9]+,[0-9]+,[0-9]+)(,[0-9]+,[0-9]+,[0-9]+)?(,[0-9]+)?\)'
        re_date = re.compile(JS_datetime, re.M)
        
        if self.js_date_utc(json_string):
            m = self.js_date_utc(json_string)
            for i in m:
                json_string = json_string.replace(i.group(0), str(self.json2datetime(i.group(0)).utctimetuple()))
        
        print json_string

        default_obj = super(JSONPDecoder,self).decode(json_string)
        return default_obj

    def js_date_utc(self, json):
        
        JS_datetime = r'Date\.UTC\(([0-9]+,[0-9]+,[0-9]+)(,[0-9]+,[0-9]+,[0-9]+)?(,[0-9]+)?\)'
        re_date = re.compile(JS_datetime, re.M)
        if re_date.search(json):
            return re_date.finditer(json)
        else:
            return False

    def json2datetime(self, json):
        """Convert JSON representation to date or datetime object depending on
        the argument count. Requires UTC datetime representation.
        Raises ValueError if the string cannot be parsed."""
        
        json_m = re.search(r'([0-9]+,[0-9]+,[0-9]+)(,[0-9]+,[0-9]+,[0-9]+)?(,[0-9]+)?', json)
        args=json_m.group(0).split(',')
        
        try:
            args=map(int, args)
        except ValueError:
            raise ValueError('Invalid arguments: %s'%json)

        if len(args)==3: 
            return datetime.date(args[0], args[1]+1, args[2])
        elif len(args)==6: 
            return datetime.datetime(args[0], args[1]+1, args[2], 
                                    args[3], args[4], args[5], tzinfo=UTC())
        elif len(args)==7:
            args[6]*=1000
            return datetime.datetime(args[0], args[1]+1, args[2], 
                                    args[3], args[4], args[5], args[6], tzinfo=UTC())
        raise ValueError('Invalid number of arguments: %s'%json)


class UTC(tzinfo):
    """UTC"""

    ZERO=datetime.timedelta(0)
    
    def utcoffset(self, dt):
        return ZERO
    
    def tzname(self, dt):
        return "UTC"
    
    def dst(self, dt):
        return ZERO


