# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from future.standard_library import install_aliases
install_aliases()

from past.builtins import basestring

from urllib.request import urlopen
from jinja2 import Environment, PackageLoader

import json, uuid
import re
import datetime
import html
from collections import Iterable
from .options import BaseOptions, ChartOptions, \
    ColorsOptions, ColorAxisOptions, CreditsOptions, DrilldownOptions, ExportingOptions, \
    GlobalOptions, LabelsOptions, LangOptions, \
    LegendOptions, LoadingOptions, MapNavigationOptions, NavigationOptions, PaneOptions, \
    PlotOptions, SeriesData, SubtitleOptions, TitleOptions, \
    TooltipOptions, xAxisOptions, yAxisOptions

from .highmap_types import Series, SeriesOptions
from .common import Formatter, CSSObject, SVGObject, MapObject, JSfunction, RawJavaScriptText, \
    CommonObject, ArrayObject, ColorObject



CONTENT_FILENAME = "./content.html"
PAGE_FILENAME = "./page.html"

pl = PackageLoader('highcharts.highmaps', 'templates')
jinja2_env = Environment(lstrip_blocks=True, trim_blocks=True, loader=pl)

template_content = jinja2_env.get_template(CONTENT_FILENAME)
template_page = jinja2_env.get_template(PAGE_FILENAME)
    
class Highmap(object):
    """
    Highcharts Base class.
    """
    #: chart count
    count = 0

    # this attribute is overriden by children of this
    # class
    CHART_FILENAME = None
    template_environment = Environment(lstrip_blocks=True, trim_blocks=True,
                                       loader=pl)

    def __init__(self, **kwargs):
        """
        This is the base class for all the charts. The following keywords are
        accepted:
        :keyword: **display_container** - default: ``True``
        """
        # Set the model
        self.model = self.__class__.__name__  #: The chart model,
        self.div_name = kwargs.get("renderTo", "container")

        # An Instance of Jinja2 template
        self.template_page_highcharts = template_page
        self.template_content_highcharts = template_content
        
        # Set Javascript src
        self.JSsource = [
                'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                'https://code.highcharts.com/maps/6/highmaps.js',
                'https://code.highcharts.com/6/highcharts.js',
                'https://code.highcharts.com/maps/6/modules/map.js',
                'https://code.highcharts.com/maps/6/modules/data.js',
                'https://code.highcharts.com/maps/6/modules/exporting.js'
            ]

        # set CSS src
        self.CSSsource = [
                'https://www.highcharts.com/highslide/highslide.css',
            ]
        # Set data
        self.data = []
        self.data_temp = []
        self.data_is_coordinate = False
        # Data from jsonp
        self.jsonp_data_flag = False

        # Set drilldown data
        self.drilldown_data = []
        self.drilldown_data_temp = []

        # Map
        self.mapdata_flag = False
        self.map = None

        # Jsonp map
        self.jsonp_map_flag = kwargs.get('jsonp_map_flag', False)

        # Javascript
        self.jscript_head_flag = False
        self.jscript_head = kwargs.get('jscript_head', None)
        self.jscript_end_flag = False
        self.jscript_end = kwargs.get('jscript_end', None)

        # Accepted keywords
        self.div_style = kwargs.get('style', '')
        self.drilldown_flag = kwargs.get('drilldown_flag', False)

        # None keywords attribute that should be modified by methods
        # We should change all these to _attr

        self._htmlcontent = ''  #: written by buildhtml
        self.htmlheader = ''
        # Place holder for the graph (the HTML div)
        # Written by ``buildcontainer``
        self.container = u''
        # Header for javascript code
        self.containerheader = u''
        # Loading message
        self.loading = 'Loading....'
        

        # Bind Base Classes to self
        self.options = {
            "chart": ChartOptions(),
            #"colorAxis": # cannot input until there is data, do it later
            "colors": ColorsOptions(),
            "credits": CreditsOptions(),
            #"data": #NotImplemented
            "drilldown": DrilldownOptions(),
            "exporting": ExportingOptions(),
            "labels": LabelsOptions(),
            "legend": LegendOptions(),
            "loading": LoadingOptions(),
            "mapNavigation": MapNavigationOptions(),
            "navigation": NavigationOptions(),
            "plotOptions": PlotOptions(),
            "series": SeriesData(),
            "subtitle": SubtitleOptions(),
            "title": TitleOptions(),
            "tooltip": TooltipOptions(),
            "xAxis": xAxisOptions(),
            "yAxis": yAxisOptions(),
        }

        self.setOptions = {
            "global": GlobalOptions(),
            "lang": LangOptions(),
        }

        self.__load_defaults__()

        # Process kwargs
        allowed_kwargs = [
            "width",
            "height",
            "renderTo",
            "backgroundColor",
            "events",
            "marginBottom",
            "marginTop",
            "marginRight",
            "marginLeft"
        ]

        for keyword in allowed_kwargs:
            if keyword in kwargs:
                self.options['chart'].update_dict(**{keyword:kwargs[keyword]})
        # Some Extra Vals to store:
        self.data_set_count = 0
        self.drilldown_data_set_count = 0


    def __load_defaults__(self):
        self.options["chart"].update_dict(renderTo='container')
        self.options["title"].update_dict(text='A New Highchart')
        self.options["credits"].update_dict(enabled=False)


    def add_JSsource(self, new_src):
        """add additional js script source(s)"""
        if isinstance(new_src, list):
            for h in new_src:
                self.JSsource.append(h)
        elif isinstance(new_src, basestring):
            self.JSsource.append(new_src)
        else:
            raise OptionTypeError("Option: %s Not Allowed For Series Type: %s" % type(new_src))


    def add_CSSsource(self, new_src):
        """add additional css source(s)"""
        if isinstance(new_src, list):
            for h in new_src:
                self.CSSsource.append(h)
        elif isinstance(new_src, basestring):
            self.CSSsource.append(new_src)
        else:
            raise OptionTypeError("Option: %s Not Allowed For Series Type: %s" % type(new_src))


    def add_data_set(self, data, series_type="map", name=None, is_coordinate = False, **kwargs):
        """set data for series option in highmaps """
        
        self.data_set_count += 1
        if not name:
            name = "Series %d" % self.data_set_count
        kwargs.update({'name':name})

        if is_coordinate:
            self.data_is_coordinate = True
            self.add_JSsource('https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.3.6/proj4.js')
            if self.map and not self.data_temp:
                series_data = Series([], series_type='map', **{'mapData': self.map})
                series_data.__options__().update(SeriesOptions(series_type='map', **{'mapData': self.map}).__options__())
                self.data_temp.append(series_data)

        if self.map and 'mapData' in kwargs.keys():
            kwargs.update({'mapData': self.map})

        series_data = Series(data, series_type=series_type, **kwargs)
       
        series_data.__options__().update(SeriesOptions(series_type=series_type, **kwargs).__options__())
        self.data_temp.append(series_data)


    def add_drilldown_data_set(self, data, series_type, id, **kwargs):
        """set data for drilldown option in highmaps 
        id must be input and corresponding to drilldown arguments in data series 
        """
        self.drilldown_data_set_count += 1
        if self.drilldown_flag == False:
            self.drilldown_flag = True
        
        kwargs.update({'id':id})
        series_data = Series(data, series_type=series_type, **kwargs)
        series_data.__options__().update(SeriesOptions(series_type=series_type, **kwargs).__options__())
        self.drilldown_data_temp.append(series_data)


    def add_data_from_jsonp(self, data_src, data_name = 'json_data', series_type="map", name=None, **kwargs):
        """add data directly from a https source
        the data_src is the https link for data using jsonp
        """
        self.jsonp_data_flag = True
        self.jsonp_data_url = json.dumps(data_src)
        if data_name == 'data':
            data_name = 'json_'+ data_name
        self.jsonp_data = data_name
        self.add_data_set(RawJavaScriptText(data_name), series_type, name=name, **kwargs)


    def add_JSscript(self, js_script, js_loc):
        """add (highcharts) javascript in the beginning or at the end of script
        use only if necessary
        """
        if js_loc == 'head':
            self.jscript_head_flag = True
            if self.jscript_head:
                self.jscript_head = self.jscript_head + '\n' +  js_script
            else:
                self.jscript_head = js_script
        elif js_loc == 'end':
            self.jscript_end_flag = True
            if self.jscript_end:
                self.jscript_end = self.jscript_end + '\n' +  js_script
            else:
                self.jscript_end = js_script
        else:
            raise OptionTypeError("Not An Accepted script location: %s, either 'head' or 'end'" 
                                % js_loc)


    def add_map_data(self, geojson, **kwargs):
        self.mapdata_flag = True
        self.map = 'geojson'
        self.mapdata = json.dumps(geojson)

        if self.data_is_coordinate:
            kwargs.update({'mapData': self.map})
            series_data = Series([], 'map')
            series_data.__options__().update(SeriesOptions('map', **kwargs).__options__())
            self.data_temp.append(series_data)
        elif kwargs:
            kwargs.update({'mapData': self.map})
            series_data = Series([], 'map')
            series_data.__options__().update(SeriesOptions('map', **kwargs).__options__())
            self.data_temp.append(series_data)
        elif self.data_temp:
            self.data_temp[0].__options__().update({'mapData': MapObject(self.map)})


    def set_map_source(self, map_src, jsonp_map = False):
        """set map data 
        use if the mapData is loaded directly from a https source
        the map_src is the https link for the mapData
        geojson (from jsonp) or .js formates are acceptable
        default is js script from highcharts' map collection: https://code.highcharts.com/mapdata/
        """

        if not map_src:
            raise OptionTypeError("No map source input, please refer to: https://code.highcharts.com/mapdata/")
        
        if  jsonp_map:
            self.jsonp_map_flag = True
            self.map = 'geojson'
            self.jsonp_map_url = json.dumps(map_src)
        else:
            self.add_JSsource(map_src)
            map_name = self._get_jsmap_name(map_src)
            self.map = 'geojson'
            self.jsmap = self.map + ' = Highcharts.geojson(' + map_name + ');'
            self.add_JSscript('var ' + self.jsmap, 'head')

        if self.data_temp:
            self.data_temp[0].__options__().update({'mapData': MapObject(self.map)})

    def set_options(self, option_type, option_dict, force_options=False):
        """set plot options"""

        if force_options: # not to use unless it is really needed
            self.options[option_type].update(option_dict)
        elif (option_type == 'yAxis' or option_type == 'xAxis') and isinstance(option_dict, list):
            self.options[option_type] = MultiAxis(option_type)
            for each_dict in option_dict:
                self.options[option_type].update(**each_dict)
        elif option_type == 'colors':
            self.options["colors"].set_colors(option_dict) # option_dict should be a list
        elif option_type == 'colorAxis':
            self.options.update({'colorAxis': self.options.get('colorAxis', ColorAxisOptions())})
            self.options[option_type].update_dict(**option_dict)
        elif option_type in ["global" , "lang"]:
            self.setOptions[option_type].update_dict(**option_dict)
        else:
            self.options[option_type].update_dict(**option_dict)

    def set_dict_options(self, options):
        """for dictionary-like inputs (as object in Javascript)
        options must be in python dictionary format
        """
        if isinstance(options, dict):
            for key, option_data in options.items():
                self.set_options(key, option_data)
        else:
            raise OptionTypeError("Not An Accepted Input Format: %s. Must be Dictionary" %type(options))


    def _get_jsmap_name(self, url):
        """return 'name' of the map in .js format"""
        
        ret = urlopen(url)
        return ret.read().decode('utf-8').split('=')[0].replace(" ", "") #return the name of map file, Ex. 'Highcharts.maps["xxx/xxx"]'


    def buildcontent(self):
        """build HTML content only, no header or body tags"""

        self.buildcontainer()
        self.option = json.dumps(self.options, cls = HighchartsEncoder)
        self.setoption = json.dumps(self.setOptions, cls = HighchartsEncoder) 
        self.data = json.dumps(self.data_temp, cls = HighchartsEncoder)
        
        if self.drilldown_flag: 
            self.drilldown_data = json.dumps(self.drilldown_data_temp, cls = HighchartsEncoder)
        self._htmlcontent = self.template_content_highcharts.render(chart=self).encode('utf-8')


    def buildhtml(self):
        """Build the HTML page
        Create the htmlheader with css / js
        Create html page
        """
        self.buildcontent()
        self.buildhtmlheader()
        self.content = self._htmlcontent.decode('utf-8') # need to ensure unicode
        self._htmlcontent = self.template_page_highcharts.render(chart=self)
        return self._htmlcontent

    def buildhtmlheader(self):
        """generate HTML header content"""
        #Highcharts lib/ needs to make sure it's up to date
        
        if self.drilldown_flag:
            self.add_JSsource('https://code.highcharts.com/maps/modules/drilldown.js')

        self.header_css = [
            '<link href="%s" rel="stylesheet" />' % h for h in self.CSSsource
        ]

        self.header_js = [
            '<script type="text/javascript" src="%s"></script>' % h for h in self.JSsource
        ]

        self.htmlheader = ''
        for css in self.header_css:
            self.htmlheader += css
        for js in self.header_js:
            self.htmlheader += js


    def buildcontainer(self):
        """generate HTML div"""
        if self.container:
            return
        # Create HTML div with style
        if self.options['chart'].width:
            if str(self.options['chart'].width)[-1] != '%':
                self.div_style += 'width:%spx;' % self.options['chart'].width
            else:
                self.div_style += 'width:%s;' % self.options['chart'].width
        if self.options['chart'].height:
            if str(self.options['chart'].height)[-1] != '%':
                self.div_style += 'height:%spx;' % self.options['chart'].height
            else:
                self.div_style += 'height:%s;' % self.options['chart'].height

        self.div_name = self.options['chart'].__dict__['renderTo'] # recheck div name
        self.container = self.containerheader + \
            '<div id="%s" style="%s">%s</div>\n' % (self.div_name, self.div_style, self.loading)

    @property
    def htmlcontent(self):
        return self.buildhtml()

    @property
    def iframe(self):
        htmlsrcdoc = html.escape(self.htmlcontent)
        htmlsrcdoc = re.sub('\\n', ' ', htmlsrcdoc)
        htmlsrcdoc = re.sub(' +', ' ', htmlsrcdoc)
        width = int(self.options['chart'].__dict__['width']) if self.options['chart'].__dict__.get('width') else 820
        height = int(self.options['chart'].__dict__['height']) if self.options['chart'].__dict__.get('height') else 520
        
        if self.options['chart'].__dict__.get('options3d'):
            if len(htmlsrcdoc) < 99965000 :
                return '<iframe style="border:0;outline:none;overflow:hidden" src="data:text/html,'+ htmlsrcdoc + '" height=' + str(height) + \
                        ' width=' + str(width) + '></iframe>'
            else:
                return '<iframe style="border:0;outline:none;overflow:hidden" srcdoc="'+ htmlsrcdoc + '" height='+ str(height) + ' width=' + str(width) + '></iframe>'
        else:
            return '<iframe style="border:0;outline:none;overflow:hidden" srcdoc="'+ htmlsrcdoc + '" height='+ str(height) + ' width=' + str(width) + '></iframe>'
    
    def __str__(self):
        """return htmlcontent"""
        #self.buildhtml()
        return self.htmlcontent

    def save_file(self, filename = 'Map'):
        """ save htmlcontent as .html file """
        filename = filename + '.html'
        
        with open(filename, 'w') as f:
            #self.buildhtml()
            f.write(self.htmlcontent)
        
        f.closed

class HighchartsEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        json.JSONEncoder.__init__(self, *args, **kwargs)
        self._replacement_map = {}

    def default(self, obj):
        if isinstance(obj, RawJavaScriptText):
            key = uuid.uuid4().hex
            self._replacement_map[key] = obj.get_jstext()
            return key
        elif isinstance(obj, datetime.datetime):
            utc = obj.utctimetuple()
            obj = (u"Date.UTC({year},{month},{day},{hours},{minutes},{seconds},{millisec})"
                    .format(year=utc[0], month=utc[1]-1, day=utc[2], hours=utc[3],
                            minutes=utc[4], seconds=utc[5], millisec=obj.microsecond/1000))
            return RawJavaScriptText(obj)
        elif isinstance(obj, BaseOptions):
            return obj.__jsonable__()
        elif isinstance(obj, CSSObject) or isinstance(obj, Formatter) or isinstance(obj, JSfunction) \
            or isinstance(obj, MapObject): 
            return obj.__jsonable__()
        elif isinstance(obj, SeriesOptions) or isinstance(obj, Series):
            return obj.__jsonable__()
        elif isinstance(obj, CommonObject) or isinstance(obj, ArrayObject) or isinstance(obj, ColorObject):
            return obj.__jsonable__()
        else:
            return json.JSONEncoder.default(self, obj)

    def encode(self, obj):
        result = json.JSONEncoder.encode(self, obj)
        for k, v in self._replacement_map.items():
            result = result.replace('"%s"' % (k,), v)
        return result


class OptionTypeError(Exception):

    def __init__(self,*args):
        self.args = args
