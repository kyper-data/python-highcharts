import unittest
import os

import sys
if sys.version_info >= (3, 0):
    def execfile(filepath):
        with open(filepath) as f:
            code = compile(f.read(), filepath, 'exec')
            exec(code)

class TestHighcharts(unittest.TestCase):
    """Very simple test cases that run through examples and checks for exceptions."""

    PATH_ROOT = "examples/highcharts"

    def test_3d_pie_donut(self):
        execfile(os.path.join(self.PATH_ROOT, '3d-pie-donut.py'))

    def test_3d_scatter_draggable(self):
        execfile(os.path.join(self.PATH_ROOT, '3d-scatter-draggable.py'))

    def test_area_basic(self):
        execfile(os.path.join(self.PATH_ROOT, 'area-basic.py'))

    def test_area_stacked_percent(self):
        execfile(os.path.join(self.PATH_ROOT, 'area-stacked-percent.py'))

    def test_arearange_line(self):
        execfile(os.path.join(self.PATH_ROOT, 'arearange-line.py'))

    def test_bar_basic(self):
        execfile(os.path.join(self.PATH_ROOT, 'bar-basic.py'))

    def test_box_plot(self):
        execfile(os.path.join(self.PATH_ROOT, 'box-plot.py'))

    def test_bubble(self):
        execfile(os.path.join(self.PATH_ROOT, 'bubble.py'))

    def test_column_drilldown(self):
        execfile(os.path.join(self.PATH_ROOT, 'column-drilldown.py'))

    def test_column_placement(self):
        execfile(os.path.join(self.PATH_ROOT, 'column-placement.py'))

    def test_column_stacked_and_grouped(self):
        execfile(os.path.join(self.PATH_ROOT, 'column-stacked-and-grouped.py'))

    def test_combo_multi_axes(self):
        execfile(os.path.join(self.PATH_ROOT, 'combo-multi-axes.py'))

    def test_error_bar(self):
        execfile(os.path.join(self.PATH_ROOT, 'error-bar.py'))

    def test_Example1(self):
        execfile(os.path.join(self.PATH_ROOT, 'Example1.py'))
        os.remove("highcharts.html")

    def test_error_bar(self):
        execfile(os.path.join(self.PATH_ROOT, 'heatmap.py'))

    def test_line_time_series(self):
        execfile(os.path.join(self.PATH_ROOT, 'line-time-series.py'))

    def test_line_basic(self):
        execfile(os.path.join(self.PATH_ROOT, 'line-basic.py'))

    def test_pie_basic(self):
        execfile(os.path.join(self.PATH_ROOT, 'pie-basic.py'))

    def test_pie_donut(self):
        execfile(os.path.join(self.PATH_ROOT, 'pie-donut.py'))

    def test_polar_spider(self):
        execfile(os.path.join(self.PATH_ROOT, 'polar-spider.py'))

    def test_scatter(self):
        execfile(os.path.join(self.PATH_ROOT, 'scatter.py'))

    def test_spline_inverted(self):
        execfile(os.path.join(self.PATH_ROOT, 'spline-inverted.py'))

    def test_spline_irregular_time(self):
        execfile(os.path.join(self.PATH_ROOT, 'spline-irregular-time.py'))

    def test_spline_symbols(self):
        execfile(os.path.join(self.PATH_ROOT, 'spline-symbols.py'))

    def test_treemap_levels(self):
        execfile(os.path.join(self.PATH_ROOT, 'treemap-levels.py'))
        
