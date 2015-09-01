# -*- coding: utf-8 -*-
from future.standard_library import install_aliases
install_aliases()
from past.builtins import basestring

from urllib.request import urlopen
import urllib

import json, os, sys
import datetime, re
from datetime import tzinfo

def jsonp_loader(url, prefix_regex=r'^(.*\()', suffix_regex=r'(\);)$', sub_d=None, sub_by=''):
    """Request (JSON) data from a server in a different domain (JSONP) 
    and covert to python readable data. 
    1. url is the url (https) where data is located
    2. "prefix_regex" and "suffix_regex" are regex patterns used to 
        remove JSONP specific prefix and suffix, such as callback header: "callback(" and end: ");", 
    3. "sub_d" is regex patterns for any unwanted string in loaded json data (will be replaced by sub_by). 
    4. "sub_by" is the string to replace any unwanted string defined by sub_d
    For function coverstion, such as Data.UTC to datetime.datetime, please check JSONPDecoder
    """

    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
    req = urllib.request.Request(url, headers=hdr)
    page = urlopen(req)
    result = page.read().decode('utf-8')
    # replace all the redundant info with sub_by 
    if sub_d:
        result = re.sub(sub_d, sub_by, result)

    prefix = re.search(prefix_regex, result).group()
    suffix = re.search(suffix_regex, result).group()
    if result.startswith(prefix) and result.endswith(suffix):
        result = result[len(prefix):-len(suffix)]
    return json.loads(result, encoding='utf8', cls=JSONPDecoder)

def js_map_loader(url):
    """Load map data from a .js source. It is designed for using highcharts' map collection:
    https://code.highcharts.com/mapdata/. Map data from other sources are not guaranteed
    """

    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
    req = urllib.request.Request(url, headers=hdr)
    page = urlopen(req)
    result = page.read().decode('utf-8')
    result = result[len(re.search(r'^.* = ', result).group()):]

    return json.loads(result)

def geojson_handler(geojson, hType='map'):
    """Restructure a GeoJSON object in preparation to be added directly by add_map_data or add_data_set methods. 
    The geojson will be broken down to fit a specific Highcharts (highmaps) type, either map, mapline or mappoint. 
    Meta data in GeoJSON's properties object will be copied directly over to object['properties']
    1. geojson is the map data (GeoJSON) to be converted
    2. hType is the type of highmap types. "map" will return GeoJSON polygons and multipolygons. 
        "mapline" will return GeoJSON linestrings and multilinestrings. 
        "mappoint" will return GeoJSON points and multipoints.
        default: "map"
    """

    hType_dict = {
    'map': ['polygon', 'multipolygon'],
    'mapline': ['linestring', 'multilinestring'],
    'mappoint': ['point', 'multipoint'],    
    }


    oldlist = [x for x in geojson['features'] if x['geometry']['type'].lower() in hType_dict[hType]]
    newlist = []
    for each_dict in oldlist:
        geojson_type = each_dict['geometry']['type'].lower()

        if hType == 'mapline':
            newlist.append(
            {'name': each_dict['properties'].get('name', None), 
             'path': _coordinates_to_path(each_dict['geometry']['coordinates'], hType, geojson_type),
             'properties': each_dict['properties'],
             }
            )
        elif hType == 'map':
            newlist.append(
            {'name': each_dict['properties']['name'], 
             'path': _coordinates_to_path(each_dict['geometry']['coordinates'], hType, geojson_type),
             'properties': each_dict['properties'],
             }
            )
        elif hType == 'mappoint':
            newlist.append(
            {'name': each_dict['properties']['name'], 
             'x': each_dict['geometry']['coordinates'][0],
             'y': -each_dict['geometry']['coordinates'][1],
             'properties': each_dict['properties'],
             }
            )
        
    return newlist

def interpolateRGB(lowRGB, highRGB, fraction):
    color = []

    for i in range(3):
        color.append((highRGB[i] - lowRGB[i]) * fraction + lowRGB[i])

    return 'rgb(' + str(int(round(color[0],0))) + ',' + str(int(round(color[1],0))) + ',' + \
        str(int(round(color[2],0))) + ')'

def _coordinates_to_path(coordinates_array, hType, geojson_type):
    new_array = []

    def _svglabel(alist):
        newlist = []
        for i, item in enumerate(alist):
            if i == 0:
                item = ['M']+[item[0], -item[1]]
            elif i == 1:
                item = ['L']+[item[0], -item[1]]
            else:
                item = [item[0], -item[1]]
            newlist += item
        return newlist
    
    if geojson_type == 'multipolygon':
        coordinates_array = [item for sublist in coordinates_array for item in sublist]
        
    if geojson_type in ['polygon', 'multipolygon', 'multilinestring']:
        for item in coordinates_array:
            new_array += _svglabel(item)
    else:
        new_array += _svglabel(coordinates_array)

    if hType == 'map':
        new_array+=['z']
    
    return new_array


def _path_to_array(path):
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
    print(path_to_array("M 4687 2398 L 4679 2402 4679 2398 Z"))

class JSONPDecoder(json.JSONDecoder):
    """Customized JSON decoder. It is used to convert everything 
    that is python non-compatible (usually Javascript functions)
    to one that can be read by python. It needs to coordinate with 
    customized JSON encoder in main library, such as highcharts.py, 
    to convert back to Javascript-compatiable functions.
    For example: in _iterdecode, it checks if queried JSON has Data.UTC 
    and (if yes)converts it to datetime.datetime
    """

    def decode(self, json_string):
        """
        json_string is basicly string that you give to json.loads method
        """

        default_obj = super(JSONPDecoder, self).decode(json_string)
        
        return list(self._iterdecode(default_obj))[0]

    def _iterdecode_list(self, lst):
        new_lst = []
        for item in lst:
            for chunk in self._iterdecode(item):
                new_lst.append(chunk)
        yield new_lst

    def _iterdecode_dict(self, dct):
        new_dct = {}
        for key, value in dct.items():
            for chunk in self._iterdecode(value):
                new_dct[key] = chunk
        yield new_dct

    def _iterdecode(self, obj):
        if isinstance(obj, (list, tuple)):
            for chunk in self._iterdecode_list(obj):
                yield chunk

        elif isinstance(obj, dict):
            for chunk in self._iterdecode_dict(obj): 
                yield chunk

        elif isinstance(obj, basestring) and JSONPDecoder.is_js_date_utc(obj):
            m = JSONPDecoder.is_js_date_utc(obj)
            yield JSONPDecoder.json2datetime(m)

        else:
            yield obj

    @staticmethod
    def is_js_date_utc(json):
        """Check if the string contains Date.UTC function 
        and return match group(s) if there is
        """
        
        JS_date_utc_pattern = r'Date\.UTC\(([0-9]+,[0-9]+,[0-9]+)(,[0-9]+,[0-9]+,[0-9]+)?(,[0-9]+)?\)'
        re_date = re.compile(JS_date_utc_pattern, re.M)

        if re_date.search(json):
            return re_date.search(json).group(0)
        else:
            return False

    @staticmethod
    def json2datetime(json):
        """Convert JSON representation to date or datetime object depending on
        the argument count. Requires UTC datetime representation.
        Raises ValueError if the string cannot be parsed.
        """
        
        json_m = re.search(r'([0-9]+,[0-9]+,[0-9]+)(,[0-9]+,[0-9]+,[0-9]+)?(,[0-9]+)?', json)
        args=json_m.group(0).split(',')
        
        try:
            args=map(int, args)
        except ValueError:
            raise ValueError('Invalid arguments: %s'%json)

        if len(args)==3: 
            return datetime.datetime(args[0], args[1]+1, args[2])
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
                