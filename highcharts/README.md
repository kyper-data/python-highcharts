# Project: Python-Highcharts

## License

Please be aware that highcharts is only free for non-commercial use: Pop over to [Highcharts](http://shop.highsoft.com/) for licencing information.

## Overview

PyHighcharts has changed!

The older version of the code is still available at: [PyHighcharts v1.0](https://github.com/fidyeates/PyHighcharts/tree/branch1.0)

This overhaul is intended to make the invocation of the PyHighcharts wrapper more pythonesque and allow for more modular functionality and better integration with web frameworks.

## Installation

The easiest way to get pyhighcharts would be via PyPi

    sudo pip install PyHighcharts

    Alternatively you can clone this repo and install from setup.py

        git clone https://github.com/fidyeates/PyHighcharts.git
            cd PyHighcharts
                git checkout dev
                    sudo python setup.py install

                    ## Whats New?

                    There are quite a few new features in PyHighcharts v2.0, we're attempting to bring stocks and maps into the forefront and allow customisation of charts in a less painful manner than previously.

                    These changes will be very breaking with the previous version of the code, so an upgrade will be in order.


                    ## Design Overview

                    We wanted to make it as easy as possible to integrate highcharts with web-frameworks. We went back to the drawing board as to the best, pythonic, method of invoking this and came up with the following design pattern.

                    ```python
                    from PyHighcharts import Chart, ChartTypes
                    
                    # A chart is the container that your data will be rendered in, it can (obviously) support multiple data series within it.
                    chart = Chart()
                    
                    # Adding a series requires a minimum of two arguments, the series type and an array of data points
                    chart.add_data_series(ChartTypes.Spline, [1, 2, 5, 4, 3], "Example Series")
                    
                    # This will open up a browser window and display the chart on the page
                    chart.show()
                    ```
                    
                    We've also implemented the concept of templates, we've found while using the older version of PyHighcharts, we call the same code over and over again.
                    
                    ```python
                    for chart_data in lots_of_charts:
                        chart = Chart()
                            chart.set_options(...)
                                chart.add_data_series(chart_data)
                                    # Do something with the chart here
                                    ```
                                    
                                    In PyHighcharts v2.0 this can be reduced to:
                                    
                                    ```python
                                    chart_template = Chart()
                                    chart_template.set_options(...)
                                    for chart_data in lots_of_charts:
                                        chart = chart_template.new()
                                            chart.add_data_series(chart_data)
                                                # Do something with the chart here
                                                ```
                                                
                                                While the output would be identical with both invocations, the ability to create duplicates of charts with a single function call allows for pre-templating of charts and makes the maintenance of the visual side of the library much easier.
                                                
                                                And you can always use the set options method:
                                                
                                                ```python
                                                chart.set_options(yAxis={"title": {"text": "Quantity"}})
                                                ```
                                                
                                                ## Usage
                                                
                                                ```python
                                                template = """
                                                <body>
                                                <div id="container"></div>
                                                <script>
                                                {}
                                                </script>
                                                </body>
                                                """
                                                from pyhighcharts import Chart, ChartTypes
                                                chart = Chart()
                                                data = [1,2,3,4,5,6,7,8,9,10]
                                                chart.add_data_series(ChartTypes.line, data, name="Test")
                                                template.format(chart.script())
                                                ```
                                                
                                                ## Todo:
                                                
                                                * More Maps & Stocks work
                                                * Cleaner code and some more helpful hooks
                                                * Unittests
                                                
                                                Reference: [Highcharts API](http://api.highcharts.com/highcharts)`""`````````
