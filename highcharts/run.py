# Load the jinja library's namespace into the current module.
import os
from jinja2 import Environment, PackageLoader, FileSystemLoader


# Specify any input variables to the template as a dictionary.
templateVars = { "title" : "Test Example",
                 "description" : "A simple inquiry of function." }

class vars:
	def __init__():

		self.title = "Test Example"
		self.description = "A simple inquiry of function"


Vars = vars

print(Vars)

from jinja2 import Environment, FileSystemLoader
 
PATH = os.path.dirname(os.path.abspath(__file__))

#CONTENT_FILENAME = "./content.html"
#PAGE_FILENAME = "./page.html"
TEST_FILENAME = "test.html"


#pl = PackageLoader('highcharts', 'templates')
sl = FileSystemLoader(searchpath = os.path.join(PATH, 'templates'))
jinja2_env = Environment(lstrip_blocks=True, trim_blocks=True, loader=sl)

# template_content = jinja2_env.get_template(CONTENT_FILENAME)
# template_page = jinja2_env.get_template(PAGE_FILENAME)
template_test = jinja2_env.get_template(TEST_FILENAME)

htmlcontent = template_test.render(chart = Vars)

print(htmlcontent) 