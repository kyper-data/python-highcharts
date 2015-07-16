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

sys.path.append('/Users/hankchu/Documents/python-highcharts/highmaps')
import highmaps
from highmap_helper import jsonp_loader, js_map_loader, geojson_handler


Drilldown_functions_dict = {
                    'US_States': """function (e) {
                
                                    if (!e.seriesOptions) {
                                        var chart = this,
                                            mapKey = 'countries/us/' + e.point.drilldown + '-all',
                                            fail = setTimeout(function () {
                                                if (!Highcharts.maps[mapKey]) {
                                                    chart.showLoading('<i class="icon-frown"></i> Failed loading ' + e.point.name);
                
                                                    fail = setTimeout(function () {
                                                        chart.hideLoading();
                                                    }, 1000);
                                                }
                                            }, 3000);
            
                                        chart.showLoading('<i class="icon-spinner icon-spin icon-3x"></i>');
                
                                        $.getScript('http://code.highcharts.com/mapdata/' + mapKey + '.js', function () {
                
                                            data = Highcharts.geojson(Highcharts.maps[mapKey]);
                
                                            $.each(data, function (i) {
                                                this.value = i;
                                            });
                
                                            chart.hideLoading();
                                            clearTimeout(fail);
                                            chart.addSeriesAsDrilldown(e.point, {
                                                name: e.point.name,
                                                data: data,
                                                dataLabels: {
                                                    enabled: true,
                                                    format: '{point.name}'
                                                }
                                            });
                                        });
                                    }
                
                                    this.setTitle(null, { text: e.point.name });
                                }""",
                    }



H = highmaps.Highmaps()
H.set_JSsource('http://code.highcharts.com/maps/modules/drilldown.js')
H.set_CSSsource('http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css')

map_url = 'http://code.highcharts.com/mapdata/countries/us/us-all.js'
geojson = js_map_loader(map_url)
data = geojson_handler(geojson)

for i, item in enumerate(data):
    item.update({'drilldown':item['properties']['hc-key']})
    item.update({'value': i}) # add bogus data

options = {
        'chart' : {
            'events': {
                'drilldown': Drilldown_functions_dict['US_States'],
                'drillup': "function () {\
                                this.setTitle(null, { text: 'USA' });\
                                                                }",
            }
        },

        'title' : {
            'text' : 'Highcharts Map Drilldown'
        },

        'subtitle': {
            'text': 'USA',
            'floating': True,
            'align': 'right',
            'y': 50,
            'style': {
                'fontSize': '16px'
            }
        },

        'legend': {} if H.options['chart'].__dict__.get('width', None) < 400 else {
            'layout': 'vertical',
            'align': 'right',
            'verticalAlign': 'middle'
        },

        'colorAxis': {
            'min': 0,
            'minColor': '#E6E7E8',
            'maxColor': '#005645'
        },

        'mapNavigation': {
            'enabled': True,
            'buttonOptions': {
                'verticalAlign': 'bottom'
            }
        },

        'plotOptions': {
            'map': {
                'states': {
                    'hover': {
                        'color': '#EEDD66'
                    }
                }
            }
        },
        'drilldown': {
            'activeDataLabelStyle': {
                'color': '#FFFFFF',
                'textDecoration': 'none',
                'textShadow': '0 0 3px #000000'
            },
            'drillUpButton': {
                'relativeTo': 'spacingBox',
                'position': {
                    'x': 0,
                    'y': 60
                }
            }
        }
    }
H.add_data_set(data,'map','USA',dataLabels = {
                'enabled': True,
                'format': '{point.properties.postal-code}'
            }) 

H.set_dict_optoins(options)

H.file()