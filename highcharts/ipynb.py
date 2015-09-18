# -*- coding: utf-8 -*-

'''
IPython notebook compatability module for highcharts-python

Adapted from python-nvd3: https://github.com/areski/python-nvd3/blob/develop/nvd3/ipynb.py
'''

try:
    _ip = get_ipython()
except:
    _ip = None
if _ip and (_ip.__module__.startswith('IPython') or _ip.__module__.startswith('ipykernel')):

    def _print_html(chart):
        '''Function to return the HTML code for the div container plus the javascript
        to generate the chart.  This function is bound to the ipython formatter so that
        charts are displayed inline.'''

        import html
        htmlsrcdoc = html.escape(chart.htmlcontent)
        width = int(chart.options['chart'].__dict__['width']) if chart.options['chart'].__dict__.get('width') else 820
        height = int(chart.options['chart'].__dict__['height']) if chart.options['chart'].__dict__.get('height') else 520

        if chart.options['chart'].__dict__.get('options3d'):
            if len(htmlsrcdoc) < 99965000 :
                return '<iframe style="border:0;outline:none;overflow:hidden" src="data:text/html,'+ htmlsrcdoc + ' "height= ' + str(height) +' \
                        width =' + str(width) + '></iframe>'
            else:
                return '<iframe style="border:0;outline:none;overflow:hidden" srcdoc="'+ htmlsrcdoc + ' "height= '+ str(height) + ' width = ' + str(width) + '></iframe>'
        else:
            return '<iframe style="border:0;outline:none;overflow:hidden" srcdoc="'+ htmlsrcdoc + ' "height= '+ str(height) + ' width = ' + str(width) + '></iframe>'


    def _setup_ipython_formatter(ip):
        ''' Set up the ipython formatter to display HTML formatted output inline'''
        from IPython import __version__ as IPython_version
        from .highcharts.highcharts import Highchart 
        from .highmaps.highmaps import Highmap
        from .highstock.highstock import Highstock

        if IPython_version >= '0.11':
            html_formatter = ip.display_formatter.formatters['text/html']
            
            for chart_type in [Highchart, Highmap, Highstock]:
                html_formatter.for_type(chart_type, _print_html)

    _setup_ipython_formatter(_ip)
