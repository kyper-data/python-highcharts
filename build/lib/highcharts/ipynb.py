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

        return chart.iframe

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
