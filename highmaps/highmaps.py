#!/usr/bin/python

"""
Python-Highcharts is a Python wrapper for Highcharts graph library.
highmaps.py is for highmaps library in highcharts

For Highcharts Licencing Visit:
http://shop.highsoft.com/highcharts.html
Project location : xxxxx
"""

from __future__ import unicode_literals
from optparse import OptionParser
from jinja2 import Environment, PackageLoader
# from slugify import slugify
import json

import datetime, random, webbrowser, os, inspect, codecs
from _abcoll import Iterable
from options import ChartOptions, \
    ColorsOptions, CreditsOptions, ExportingOptions, \
    GlobalOptions, LabelsOptions, LangOptions, \
    LegendOptions, LoadingOptions, NavigationOptions, PaneOptions, \
    PlotOptions, SeriesData, SubtitleOptions, TitleOptions, \
    TooltipOptions, xAxisOptions, yAxisOptions

from highchart_types import Series, SeriesOptions, HighchartsError, MultiAxis
from common import Formatter

CONTENT_FILENAME = "./content.html"
PAGE_FILENAME = "./page.html"

pl = PackageLoader('highcharts', 'templates')
jinja2_env = Environment(lstrip_blocks=True, trim_blocks=True, loader=pl)

template_content = jinja2_env.get_template(CONTENT_FILENAME)
template_page = jinja2_env.get_template(PAGE_FILENAME)
    
DEFAULT_POINT_INTERVAL = 86400000

FORMAT_SPECIAL_CASES = {
    "formatter": "formatter",
    "labelFormatter": "formatter",
    "pointStart": "skip_quotes",
    "events": "skip_quotes",
    "load": "skip_quotes",
    "multiaxis": "multiaxis"
}

bool_mapping = {
    False: u'false',
    True: u'true',
}


def stab(tab=1):
    """
    create space tabulation
    """
    return ' ' * 4 * tab


class Highcharts(object):
    """
    Highcharts Base class.
    """
    #: chart count
    count = 0
    #:  directory holding the assets (bower_components)
    assets_directory = './bower_components/'

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

        #: an Instance of Jinja2 template
        self.template_page_highcharts = template_page
        self.template_content_highcharts = template_content
        
        # set data
        self.data = []
        
        # accepted keywords

        self.div_style = kwargs.get('style', '')
        self.date_flag = kwargs.get('date_flag', False)

        # None keywords attribute that should be modified by methods
        # We should change all these to _attr

        self.htmlcontent = ''  #: written by buildhtml
        self.htmlheader = ''
        #: Place holder for the graph (the HTML div)
        #: Written by ``buildcontainer``
        self.container = u''
        #: Header for javascript code
        self.containerheader = u''
        
        # Highcharts lib/ needs to make sure it's up to
        # date
        self.header_css = [
            '<link href="%s" rel="stylesheet" />' % h for h in
            (
                'https://www.highcharts.com/highslide/highslide.css',
            )
        ]

        self.header_js = [
            '<script type="text/javascript" src="%s"></script>' % h for h in
            (
                'https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js',
                'https://code.highcharts.com/highcharts.js',
                'https://code.highcharts.com/highcharts-more.js',
                'https://code.highcharts.com/modules/exporting.js'
            )
        ]

        #: Javascript code as string
        self.jschart = None
        # self.custom_tooltip_flag = False
        # self.tooltip_condition_string = ''
        # self.charttooltip = ''
        self.serie_no = 1

        # Default Nulls // ?
        self.hold_point_start = None
        self.hold_point_interval = None
        self.start_date_set = None

        # Bind Base Classes to self
        self.options = {
            "chart": ChartOptions(),
            "colors": ColorsOptions(),
            "credits": CreditsOptions(),
            "exporting": ExportingOptions(),
            "global": GlobalOptions(),
            "labels": LabelsOptions(),
            "lang": LangOptions(),
            "legend": LegendOptions(),
            "loading": LoadingOptions(),
            "navigation": NavigationOptions(),
            "pane": PaneOptions(),
            "plotOptions": PlotOptions(),
            "series": SeriesData(),
            "subtitle": SubtitleOptions(),
            "title": TitleOptions(),
            "tooltip": TooltipOptions(),
            "xAxis": xAxisOptions(),
            "yAxis": yAxisOptions(),
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
                if keyword == 'events':
                    self.options['chart'].update_dict(**{'events':{kwargs['events'].event_type:kwargs['events'].event_method}})
                else:
                    self.options['chart'].update_dict(**{keyword:kwargs[keyword]})
        # Some Extra Vals to store:
        self.data_set_count = 0

    # def __render__(self, ret=False, template="base"):
        # if template == "base":
        #     TEMPLATE = BASE_TEMPLATE
        # elif template == "gecko":
        #     TEMPLATE = GECKO_TEMPLATE
        # with open(TEMPLATE,"rb") as template_file:
        #     tmp = unicode(template_file.read())
        # rendered = tmp.format(**self.__export_options__())
        # if ret:
        #     return rendered


    def __export_options__(self):
        bind = self.options.items()
        data = {k:chart_formatter(k, opClass) \
        #data = {k: opClass.__dict__ \
            for k, opClass in bind}
        return data

    def __load_defaults__(self):
        self.options["chart"].update_dict(renderTo='container')
        self.options["title"].update_dict(text='A New Highchart')
        #self.options["yAxis"].update_dict(title_text='units')
        self.options["credits"].update_dict(enabled=False)


    def title(self, title=None):
        """ Bind Title """
        if not title:
            return self.options["title"].text
        else:
            self.options["title"].update_dict(text=title)


    def colors(self, colors=None):
        """ Bind Color Array """
        if not colors:
            return self.options["colors"].__dict__.values() if self.options['colors'] is not None else []
        else:
            self.options["colors"].set_colors(colors)


    def chart_background(self, background=None):
        """ Apply Chart Background """
        if not background:
            return self.options["chart"].backgroundColor
        else:
            self.options["chart"].update_dict(backgroundColor=background)

    def set_x_axis(self, **kwargs):
        self.options["xAxis"].update_dict(**kwargs)

    def set_y_axis(self, **kwargs):
        self.options["yAxis"].update_dict(**kwargs)

    def set_start_date(self, date):
        """ Set Plot Start Date """
        if isinstance(date, (int, float)):
            date = datetime.datetime.fromtimestamp(date)
        elif not isinstance(date, datetime.datetime):
            error = "Start Date Format Currently Not Supported: %s" % date
            raise HighchartError(error)
        date_dict = {
            "year": date.year,
            "month": date.month - 1,
            "day": date.day,
            "hour": date.hour,
            "minute": date.minute,
            "second": date.second,
        }
        formatted_date = "Date.UTC({year}, {month}, {day}, {hour}, {minute}, {second})"
        formatted_date = formatted_date.format(**date_dict)
        if not self.options['plotOptions'].__dict__:
            self.hold_point_start = formatted_date
            self.hold_point_interval = DEFAULT_POINT_INTERVAL
        hold_iterable = self.options['plotOptions'].__dict__.items()
        for series_type, series_options in hold_iterable:
            series_options.process_kwargs({'pointStart':formatted_date},
                series_type=series_type)
            if not 'pointInterval' in series_options.__dict__:
                series_options.process_kwargs({
                    'pointInterval':DEFAULT_POINT_INTERVAL},
                    series_type=series_type,
                    supress_errors=True)
        self.options['tooltip'].update_dict(formatter=Formatter('date'))
        self.options['xAxis'].update_dict(type='datetime')
        self.start_date_set = True


    def set_interval(self, interval):
        """ Set Plot Step Interval """
        if not isinstance(interval, int):
            raise HighchartError("Interval Value Must Be An Integer")
        # Unset Any Held Values To Avoid Them Overwriting This Value
        if self.hold_point_interval:
            self.hold_point_interval = None
        if not self.options['plotOptions'].__dict__:
            self.hold_point_interval = interval
        for hold_item in self.options['plotOptions'].__dict__.items():
            series_type, series_options = hold_item
            series_options.process_kwargs({'pointInterval':interval},
                series_type=series_type)
        if not self.start_date_set:
            print "Set The Start Date With .set_start_date(date)"


    def add_data_set(self, data, series_type="line", name=None, **kwargs):
        """ Update Plot Options With Defaults If None Exist """
        self.data_set_count += 1
        if not name:
            name = "Series %d" % self.data_set_count
        kwargs.update({'name':name})
        if self.hold_point_start:
            kwargs.update({"pointStart":self.hold_point_start})
            self.hold_point_start = None
        if self.hold_point_interval:
            kwargs.update({"pointInterval":self.hold_point_interval})
            self.hold_point_interval = None
        if series_type not in self.options["plotOptions"].__dict__:
            to_update = {series_type:SeriesOptions(series_type=series_type,
                supress_errors=True, **kwargs)}
            self.options["plotOptions"].update_dict(**to_update)
        series_data = Series(data, series_type=series_type, \
            supress_errors=True, **kwargs)
        self.options["series"].data.append(series_data)

    def set_options(self, options, force_options=False):
        """ Set Plot Options """
        if force_options:
            for k, v in options.items():
                self.options.update({k:v})
        else:
            new_options = {}
            for key, option_data in options.items():
                data = {}
                for key2, val in option_data.items():
                    if isinstance(val, dict):
                        for key3, val2 in val.items():
                            data.update({key2+"_"+key3:val2})
                    else:
                        data.update({key2:val})
                new_options.update({key:data})
            for key, val in new_options.items():
                self.options[key].update_dict(**val)


    # def show(self):
        """ Show Function """
        handle = webbrowser.get()
        if not os.path.exists(TMP_DIR):
            os.mkdir(TMP_DIR)
        new_filename = "%x.html" % (random.randint(pow(16, 5), pow(16, 6)-1))
        temp_dir = globals()['TMP_DIR']
        if not temp_dir[-1] == "/":
            temp_dir += "/"
        new_fn = temp_dir + new_filename
        with codecs.open(SHOW_TEMPLATE, 'rb', encoding='utf-8') as file_open:
            tmp = file_open.read()
        html = tmp.format(chart_data=self.__render__(ret=True))
        with codecs.open(new_fn, 'w', encoding='utf-8') as file_open:
            file_open.write(html)
        handle.open("file://"+new_fn)

    # def generate(self):
        """ __render__ Wrapper """
        return self.__render__(ret=True)

    def set_yAxis(self, *axis):
        if all(map(lambda a: isinstance(a, yAxisOptions), axis)):
            self.options['yAxis'] = MultiAxis(axis)
        else:
            raise HighchartsError("All Axis Must Be Of Type: yAxisOptions")    


    # def _slugify_name(self, name):
        """Slufigy name with underscore"""
        self.name = slugify(name, separator='_')


    def set_containerheader(self, containerheader):
        """Set containerheader"""
        self.containerheader = containerheader

    # def set_date_flag(self, date_flag=False):
    #     """Set date flag"""
    #     self.date_flag = date_flag

    # def set_custom_tooltip_flag(self, custom_tooltip_flag):
    #     """Set custom_tooltip_flag & date_flag"""
    #     self.custom_tooltip_flag = custom_tooltip_flag

    def __str__(self):
        """return htmlcontent"""
        self.buildhtml()
        return self.htmlcontent

    def buildcontent(self):
        """Build HTML content only, no header or body tags. To be useful this
        will usually require the attribute `juqery_on_ready` to be set which
        will wrap the js in $(function(){<regular_js>};)
        """
        self.buildcontainer()
        # if the subclass has a method buildjs this method will be
        # called instead of the method defined here
        # when this subclass method is entered it does call
        # the method buildjschart defined here
        self.buildjschart()
        self.option = json.dumps(self.__export_options__())
        self.data = json.dumps(data_formatter(self.options['series']))
        self.htmlcontent = self.template_content_highcharts.render(chart=self)

    def buildhtml(self):
        """Build the HTML page
        Create the htmlheader with css / js
        Create html page
        Add Js code for highcharts
        """
        self.buildcontent()
        self.content = self.htmlcontent
        self.htmlcontent = self.template_page_highcharts.render(chart=self)

    def buildhtmlheader(self):
        """generate HTML header content"""
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
        # if self.div_style:
        #     self.div_style = 'style="%s"' % self.div_style

        self.container = self.containerheader + \
            '<div id="%s" style="%s"></div>\n' % (self.div_name, self.div_style)

    def buildjschart(self):
        """generate javascript code for the chart"""
        self.jschart = ''

        # add custom tooltip string in jschart
        # default condition (if build_custom_tooltip is not called explicitly with date_flag=True)

        # if self.tooltip_condition_string == '':
        #     self.tooltip_condition_string = 'var y = String(graph.point.y);\n'

        # Include data
        # self.series_js = json.dumps(self.series)


class TemplateMixin(object):
    """
    A mixin that override buildcontent. Instead of building the complex
    content template we exploit Jinja2 inheritance. Thus each chart class
    renders it's own chart template which inherits from content.html
    """
    def buildcontent(self):
        """Build HTML content only, no header or body tags. To be useful this
        will usually require the attribute `juqery_on_ready` to be set which
        will wrap the js in $(function(){<regular_js>};)
        """
        self.buildcontainer()
        # if the subclass has a method buildjs this method will be
        # called instead of the method defined here
        # when this subclass method is entered it does call
        # the method buildjschart defined here
        self.buildjschart()
        self.htmlcontent = self.template_chart_highcharts.render(chart=self)

def set_temp_dir(temp_dir):
    globals()['TMP_DIR'] = temp_dir

class HighchartError(Exception):
    """ Highcharts Error Class """
    def __init__(self, *args):
        Exception.__init__(self, *args)
        self.args = args

# def color_formatter2(data):
#     """ Nothing to see here """
#     return str(data['colors'])

def color_formatter(data):
    return data.colors

# def update_template(tmp, key, val, tab_depth=1):
    # """ Generate Json Dicts """
    # if key not in FORMAT_SPECIAL_CASES:
    #     # Value Checking
    #     if isinstance(val, dict):
    #         tmp += u"\t%s: {\n" % key
    #         for subkey, subval in val.items():
    #             tmp = update_template(tmp, subkey, subval, tab_depth=3)
    #         tmp += u"\t\t" + u"},\n"
    #         return tmp
    #     elif isinstance(val, Iterable) and not isinstance(val, basestring):
    #         new_vals = []
    #         for item in val:
    #             if isinstance(item, dict):
    #                 ntmp = u"{"
    #                 for k,v in item.items():
    #                     ntmp = update_template(ntmp, k, v, tab_depth=0)
    #                 ntmp += u"}"
    #                 new_vals.append(ntmp)
    #             elif isinstance(item, Iterable) and not isinstance(item, basestring):
    #                 new_items = []
    #                 for subitem in item:
    #                     if isinstance(subitem, datetime.datetime):
    #                         utc = subitem.utctimetuple()
    #                         new_items.append(u"Date.UTC({year},{month},{day},{hours},{minutes},{seconds},{millisec})"
    #                                     .format(year=utc[0], month=utc[1]-1, day=utc[2], hours=utc[3],
    #                                             minutes=utc[4], seconds=utc[5], millisec=subitem.microsecond/1000))
    #                     elif isinstance(subitem, bool):
    #                         # Convert Bool to js equiv.
    #                         new_items.append(bool_mapping[subitem])
    #                     elif isinstance(subitem, basestring):
    #                         # Need to keep string quotes
    #                         new_items.append(u"\'" + subitem + u"\'")
    #                     else:
    #                         new_items.append(unicode(subitem))
    #                 new_vals.append(u"[{}]".format(u",".join(new_items)))
    #             elif isinstance(item, datetime.datetime):
    #                 utc = item.utctimetuple()
    #                 new_vals.append(u"Date.UTC({year},{month},{day},{hours},{minutes},{seconds},{millisec})"
    #                        .format(year=utc[0], month=utc[1], day=utc[2], hours=utc[3],
    #                                minutes=utc[4], seconds=utc[5], millisec=item.microsecond/1000))
    #             elif isinstance(item, bool):
    #                 # Convert Bool to js equiv.
    #                 new_vals.append(bool_mapping[item])
    #             elif item == None:
    #                 new_vals.append(u'null')
    #             elif isinstance(item, basestring):
    #                 # Need to keep string quotes
    #                 new_vals.append(u"\'" + item + u"\'")
    #             else:
    #                 new_vals.append(unicode(item))
    #         return tmp + u"{tabs}{key}:[{vals}],\n".format(tabs=u"\t"*tab_depth, key=key, vals=u",".join(new_vals))
    #     elif isinstance(val, datetime.datetime):
    #         utc = val.utctimetuple()
    #         val = (u"Date.UTC({year},{month},{day},{hours},{minutes},{seconds},{millisec})"
    #                 .format(year=utc[0], month=utc[1], day=utc[2], hours=utc[3],
    #                         minutes=utc[4], seconds=utc[5], millisec=val.microsecond/1000))
    #     elif isinstance(val, bool):
    #         # Convert Bool to js equiv.
    #         val = bool_mapping[val]
    #     elif val == None:
    #         val = u'null'
    #     elif isinstance(val, basestring):
    #         # Need to keep string quotes
    #         val = u"\'" + val + u"\'"
    #     tmp += u"\t"*tab_depth + u"%s: %s,\n" % (key, val)
    # else:
    #     if FORMAT_SPECIAL_CASES[key] == "skip_quotes":
    #         tmp += u"\t"*tab_depth + u"%s: %s,\n" % (key, val)
    #     elif FORMAT_SPECIAL_CASES[key] == "formatter":
    #         tmp += u"\t"*tab_depth + u"%s: %s,\n" % (key, val.formatter)
    #     elif FORMAT_SPECIAL_CASES[key] == "multiaxis":
    #         st = u""
    #         for k, v in val.__dict__.iteritems():
    #             st = update_template(st, k, v, tab_depth=tab_depth+1)
    #         return st
    #     else:
    #         raise NotImplementedError
    # return tmp

# def series_formatter2(data):
    # """ Special Formatting For Series """
    # temp = ""
    # for data_set in data['data']:
    #     temp += u"{\n"
    #     for key, val in  data_set.__dict__.items():
    #         temp = update_template(temp, key, val, tab_depth=1)
    #     temp += u"\t},"
    # return 

def data_formatter(data):
    """ Special Formatting For data """
    return [ data_set.__dict__ for data_set in data.data ]

def series_formatter(data):
    """ create empty list for series, data will be input later """
    #return [ data_set.__dict__ for data_set in data.data ]
    return []

def plotOptions_formatter(data):
    """ Special Formatting For plotOptions """
    return {key: data_set.__dict__ for key, data_set in data.__dict__.items()}

# def chart_formatter2(option_type, data):
    # """ Formatter Function """
    # # Special Cases
    # special_cases = {
    #     "colors": color_formatter,
    #     "series": series_formatter,
    # }
    # tmp = u""
    # #print option_type, data
    # if option_type in special_cases:
    #     tmp += special_cases[option_type](data)
    # elif option_type == "yAxis" and data.get('axis'):
    #     tmp += u"[{\n"
    #     for i, ax in enumerate(data['axis'], 1):
    #         tmp += update_template(u"", u'multiaxis', ax, tab_depth=1)
    #         if not i == len(data['axis']):
    #             tmp += u"\t},{\n"
    #     tmp += u"\t}]"
    #     print tmp
    # else:
    #     tmp += u"{\n"
    #     for key, val in data.items():
    #         if isinstance(val, dict):
    #             tmp += u"\t%s: {\n" % key
    #             for subkey, subval in val.items():
    #                 tmp = update_template(tmp, subkey, subval, tab_depth=3)
    #             tmp += u"\t\t" + u"},\n"
    #         elif isinstance(val, SeriesOptions):
    #             tmp += u"\t%s: {\n" % key
    #             for subkey, subval in val.__dict__.items():
    #                 tmp = update_template(tmp, subkey, subval, tab_depth=3)
    #             tmp += u"\t\t" + u"},\n"
    #         else:
    #             tmp = update_template(tmp, key, val, tab_depth=2)
    #     tmp += u"\t}"
    # return tmp

def chart_formatter(option_type, data):
    """ Formatter Function """
    # Special Cases
    special_cases = {
        "colors": color_formatter,
        "series": series_formatter,
        "plotOptions": plotOptions_formatter
    }
    #print option_type, data
    if option_type in special_cases:
        tmp = special_cases[option_type](data)
    else:
        tmp = data.__dict__
    return tmp


def _main():
    """
    Parse options and process commands
    """
    # Parse arguments
    usage = "usage: highcharts.py [options]"
    parser = OptionParser(usage=usage, version="python-highcharts - Charts generator with Highcharts library")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print messages to stdout")

    (options, args) = parser.parse_args()


if __name__ == '__main__':
    _main()