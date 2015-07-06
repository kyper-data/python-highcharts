# -*- coding: utf-8 -*-
from future.standard_library import install_aliases
install_aliases()
from urllib.request import urlopen
import urllib

import json, os, sys
import pandas as pd
import numpy as np
import datetime
import re

def jsonp_loader(url):

    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
    req = urllib.request.Request(url, headers=hdr)
    page = urlopen(req)
    result = page.read()
    
    prefix = re.search(r'^(.*\()', result).group()
    suffix = re.search(r'(\);)$', result).group()
    if result.startswith(prefix) and result.endswith(suffix):
        result = result[len(prefix):-len(suffix)]
    
    return json.loads(result)

def js_map_loader(url):

    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
    req = urllib.request.Request(url,headers=hdr)
    page = urlopen(req)
    result = page.read()
    result = result[len(re.search(r'^.* = ', result).group()):]

    return json.loads(result)

def geojson_handler(geojson, hType = 'map'):
    """Restructure a GeoJSON object in preparation to be added directly by the add_map or add_data_set functions. 
    The GeoJSON will be broken down to fit a specific Highcharts type, either map, mapline or mappoint. 
    Meta data in GeoJSON's properties object will be copied directly over to object['properties']."""
    
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

                