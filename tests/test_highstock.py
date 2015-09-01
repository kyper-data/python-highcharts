import unittest
import os

import sys
if sys.version_info >= (3, 0):
    def execfile(filepath):
        with open(filepath) as f:
            code = compile(f.read(), filepath, 'exec')
            exec(code)

class TestHighstock(unittest.TestCase):
    """Very simple test cases that run through examples and check for exceptions."""

    PATH_ROOT = "examples/highstock"

    def test_arearange(self):
            execfile(os.path.join(self.PATH_ROOT, 'arearange.py'))

    def test_basic_line_2(self):
        execfile(os.path.join(self.PATH_ROOT, 'basic-line-2.py'))

    def test_candlestick_and_volume(self):
        execfile(os.path.join(self.PATH_ROOT, 'candlestick-and-volume.py'))

    def test_compare(self):
        execfile(os.path.join(self.PATH_ROOT, 'compare.py'))

    def test_data_grouping(self):
        execfile(os.path.join(self.PATH_ROOT, 'data-grouping.py'))

    def test_Example1_basic_line(self):
        execfile(os.path.join(self.PATH_ROOT, 'Example1-basic-line.py'))

    def test_flags_general(self):
        execfile(os.path.join(self.PATH_ROOT, 'flags-general.py'))

    def test_flags_general_2(self):
        execfile(os.path.join(self.PATH_ROOT, 'flags-general-2.py'))

    def test_intraday_area(self):
        execfile(os.path.join(self.PATH_ROOT, 'intraday-area.py'))

    def test_lazy_loading(self):
        execfile(os.path.join(self.PATH_ROOT, 'lazy-loading.py'))

    def test_ohlc(self):
        execfile(os.path.join(self.PATH_ROOT, 'ohlc.py'))

    def test_yaxis_plotbands(self):
        execfile(os.path.join(self.PATH_ROOT, 'yaxis-plotbands.py'))