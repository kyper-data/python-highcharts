import sys, os
sys.path.append('Documents/python-highcharts/highcharts')

def main():

	import highcharts
	reload(highcharts)

	data = [1,2,3,4,5,6,7,8,9,10]
	H = highcharts.Highcharts(width=500, height=500, renderTo='container')
	H.add_data_set(data,type='line',name='test_data')
	H.buildhtml()
	H.htmlcontent



if __name__ == '__main__':
	main()