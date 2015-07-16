# -*- coding: utf-8 -*-

'''
ipython compatability module for highcharts-python
This adds simple ipython compatibility to the highcharts-python package, without making any
major modifications to how the main package is structured.  It utilizes the IPython
display-formatter functionality, as described at:
http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/notebooks/Custom%20Display%20Logic.ipynb
For additional examples, see:
https://github.com/sympy/sympy/blob/master/sympy/interactive/printing.py
'''

try:
    _ip = get_ipython()
except:
    _ip = None
if _ip and _ip.__module__.startswith('IPython'):

    def _print_html(chart):
        '''Function to return the HTML code for the div container plus the javascript
        to generate the chart.  This function is bound to the ipython formatter so that
        charts are displayed inline.'''

        import html
        htmlsrcdoc = html.escape(chart.htmlcontent)
        width = int(chart['options']['chart']['width']) if chart['options']['chart'].get('width') else 820
        height = int(chart['options']['chart']['height']) if chart['options']['chart'].get('height') else 520

        return '<iframe style="border:0;outline:none;overflow:hidden" srcdoc="'+ htmlsrcdoc + '" height='+ str(height) + ' width=' + str(width) + '></iframe>'

    def _setup_ipython_formatter(ip):
        ''' Set up the ipython formatter to display HTML formatted output inline'''
        from IPython import __version__ as IPython_version
        from highcharts import Highchart, Highmap#, Highstock

        if IPython_version >= '0.11':
            html_formatter = ip.display_formatter.formatters['text/html']
            for chart_type in [Highchart, Highmap]:
                html_formatter.for_type_by_name('highcharts', chart_type, _print_html)

    _setup_ipython_formatter(_ip)