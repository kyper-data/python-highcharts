# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from future.standard_library import install_aliases
install_aliases()

from jinja2 import Environment, PackageLoader

import json, uuid
import re
import datetime
import html
from collections import Iterable
from .options import BaseOptions, ChartOptions, \
    ColorsOptions, CreditsOptions, ExportingOptions, \
    GlobalOptions, LabelsOptions, LangOptions, \
    LegendOptions, LoadingOptions, NavigatorOptions, NavigationOptions, \
    PlotOptions, RangeSelectorOptions, ScrollbarOptions, SeriesData, SubtitleOptions, TitleOptions, \
    TooltipOptions, xAxisOptions, yAxisOptions, MultiAxis

from .highstock_types import Series, SeriesOptions
from .common import Levels, Formatter, CSSObject, SVGObject, JSfunction, RawJavaScriptText, \
    CommonObject, ArrayObject, ColorObject

CONTENT_FILENAME = "./content.html"
PAGE_FILENAME = "./page.html"

pl = PackageLoader('highcharts.highstock', 'templates')
jinja2_env = Environment(lstrip_blocks=True, trim_blocks=True, loader=pl)

template_content = jinja2_env.get_template(CONTENT_FILENAME)
template_page = jinja2_env.get_template(PAGE_FILENAME)
    

class Highstock(object):
    """
    Highstock Base class.
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
        # set the model
        self.model = self.__class__.__name__  #: The chart model,
        self.div_name = kwargs.get("renderTo", "container")

        # an Instance of Jinja2 template
        self.template_page_highcharts = template_page
        self.template_content_highcharts = template_content
        
        # set Javascript src, Highcharts lib needs to make sure it's up to date
        self.JSsource = [
                'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                'https://code.highcharts.com/stock/6/highstock.js',
                'https://code.highcharts.com/stock/6/modules/exporting.js',
                'https://code.highcharts.com/6/highcharts-more.js',
            ]

        # set CSS src
        self.CSSsource = [
                'https://www.highcharts.com/highslide/highslide.css',

            ]
        # set data
        self.data = []
        self.data_temp = []

        # set navigator series
        self.navi_seri_flag = False
        self.navi_seri = {}
        self.navi_seri_temp = {}

        # Data from jsonp
        self.jsonp_data_flag = False
        self.jsonp_data_url_list = [] # DEM 2017/04/25: List of JSON data sources
        
        # javascript
        self.jscript_head_flag = False
        self.jscript_head = kwargs.get('jscript_head', None)
        self.jscript_end_flag = False
        self.jscript_end = kwargs.get('jscript_end', None)

        # accepted keywords
        self.div_style = kwargs.get('style', '')
        self.date_flag = kwargs.get('date_flag', False)

        # None keywords attribute that should be modified by methods
        # We should change all these to _attr

        self._htmlcontent = ''  #: written by buildhtml
        self.htmlheader = ''
        #: Place holder for the graph (the HTML div)
        #: Written by ``buildcontainer``
        self.container = u''
        #: Header for javascript code
        self.containerheader = u''
        # Loading message
        self.loading = 'Loading....'

        # Bind Base Classes to self
        self.options = {
            "chart": ChartOptions(),
            "colors": ColorsOptions(),
            "credits": CreditsOptions(),
            #"data": #NotImplemented
            "exporting": ExportingOptions(),
            "labels": LabelsOptions(),
            "legend": LegendOptions(),
            "loading": LoadingOptions(),
            "navigation": NavigationOptions(),
            "navigator": NavigatorOptions(),
            "plotOptions": PlotOptions(),
            "rangeSelector": RangeSelectorOptions(),
            "scrollbar": ScrollbarOptions(),
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


    def add_data_set(self, data, series_type="line", name=None, **kwargs):
        """set data for series option in highstocks"""

        self.data_set_count += 1
        if not name:
            name = "Series %d" % self.data_set_count
        kwargs.update({'name':name})

        series_data = Series(data, series_type=series_type, **kwargs)
        series_data.__options__().update(SeriesOptions(series_type=series_type, **kwargs).__options__())
        self.data_temp.append(series_data)


    def add_data_from_jsonp(self, data_src, data_name='json_data', series_type="line", name=None, **kwargs):
        """set map data directly from a https source
        the data_src is the https link for data
        and it must be in jsonp format
        """
        if not self.jsonp_data_flag:
            self.jsonp_data_flag = True
            
            if data_name == 'data':
                data_name = 'json_'+ data_name
            
            self.jsonp_data = data_name
        self.add_data_set(RawJavaScriptText(self.jsonp_data), series_type, name=name, **kwargs)
        # DEM 2017/04/25: Append new JSON data source to a list instead of
        #                 replacing whatever already exists
        self.jsonp_data_url_list.append(json.dumps(data_src))


    def add_navi_series(self, data, series_type="line", **kwargs):
        """set series for navigator option in highstocks"""

        self.navi_seri_flag = True
        series_data = Series(data, series_type=series_type, **kwargs)
        series_data.__options__().update(SeriesOptions(series_type=series_type, **kwargs).__options__())           
        self.navi_seri_temp = series_data

    def add_navi_series_from_jsonp(self, data_src=None, data_name='json_data', series_type="line", **kwargs):
        """set series for navigator option in highstocks"""

        if not self.jsonp_data_flag:
            self.jsonp_data_flag = True
            self.jsonp_data_url = json.dumps(data_src) 
            
            if data_name == 'data':
                data_name = 'json_'+ data_name
            
            self.jsonp_data = data_name
        
        self.add_navi_series(RawJavaScriptText(self.jsonp_data), series_type, **kwargs)


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


    def set_options(self, option_type, option_dict, force_options=False):
        """set plot options """
        if force_options:
            self.options[option_type].update(option_dict)
        elif (option_type == 'yAxis' or option_type == 'xAxis') and isinstance(option_dict, list):
            # For multi-Axis
            self.options[option_type] = MultiAxis(option_type)
            for each_dict in option_dict:
                self.options[option_type].update(**each_dict)
        elif option_type == 'colors':
            self.options["colors"].set_colors(option_dict) # option_dict should be a list
        elif option_type in ["global" , "lang"]: #Highcharts.setOptions: 
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


    def buildcontent(self):
        """build HTML content only, no header or body tags"""

        self.buildcontainer()
        self.option = json.dumps(self.options, cls = HighchartsEncoder)
        self.setoption = json.dumps(self.setOptions, cls = HighchartsEncoder) 
        self.data = json.dumps(self.data_temp, cls = HighchartsEncoder)

        # DEM 2017/04/25: Make 'data' available as an array
        # ... this permits jinja2 array access to each data definition
        # ... which is useful for looping over multiple data sources
        self.data_list = [json.dumps(x, cls = HighchartsEncoder) for x in self.data_temp]
        
        if self.navi_seri_flag:        
            self.navi_seri = json.dumps(self.navi_seri_temp, cls = HighchartsEncoder)

        self._htmlcontent = self.template_content_highcharts.render(chart=self).encode('utf-8')


    def buildhtml(self):
        """build the HTML page
        create the htmlheader with css / js
        create html page
        """
        self.buildcontent()
        self.buildhtmlheader()
        self.content = self._htmlcontent.decode('utf-8') # need to ensure unicode
        self._htmlcontent = self.template_page_highcharts.render(chart=self)
        return self._htmlcontent
        

    def buildhtmlheader(self):
        """generate HTML header content"""

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

    def save_file(self, filename = 'StockChart'):
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
        elif isinstance(obj, BaseOptions) or isinstance(obj, MultiAxis):
            return obj.__jsonable__()
        elif isinstance(obj, CSSObject) or isinstance(obj, Formatter) or isinstance(obj, JSfunction): 
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
