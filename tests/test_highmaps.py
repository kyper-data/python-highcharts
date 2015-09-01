import unittest
import os

import sys
if sys.version_info >= (3, 0):
    def execfile(filepath):
        with open(filepath) as f:
            code = compile(f.read(), filepath, 'exec')
            exec(code)

class TestHighmaps(unittest.TestCase):
    """Very simple test cases that run through examples and check for exceptions."""

    PATH_ROOT = "examples/highmaps"

    def test_category_map(self):
        execfile(os.path.join(self.PATH_ROOT, 'category-map.py'))
        
    def test_color_axis(self):
        execfile(os.path.join(self.PATH_ROOT, 'color-axis.py'))

    def test_Example1_geojson(self):
        execfile(os.path.join(self.PATH_ROOT, 'Example1_geojson.py'))
    
    def test_geojson_multiple_types(self):
        execfile(os.path.join(self.PATH_ROOT, 'geojson-multiple-types.py'))

    def test_latlon_advanced(self):
        execfile(os.path.join(self.PATH_ROOT, 'latlon-advanced.py'))
    
    def test_map_drilldown_2(self):
        execfile(os.path.join(self.PATH_ROOT, 'map-drilldown-2.py'))

    def test_map_drilldown(self):
        execfile(os.path.join(self.PATH_ROOT, 'map-drilldown.py'))

    def test_mappoint_latlon(self):
        execfile(os.path.join(self.PATH_ROOT, 'mappoint-latlon.py'))
    
    def test_us_counties_2(self):
        execfile(os.path.join(self.PATH_ROOT, 'us-counties-2.py'))

    def test_us_counties(self):
        execfile(os.path.join(self.PATH_ROOT, 'us-counties.py'))