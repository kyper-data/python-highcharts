from highmap_helper import jsonp_loader, js_map_loader, geojson_handler

H = highmaps.Highmaps()
options = {
        'chart': {
            'borderWidth': 1,
            'marginRight': 50 
        },

        'title': {
            'text': 'US Counties unemployment rates, April 2015'
        },

        'legend': {
            'title': {
                'text': 'Unemployment<br>rate',
                'style': {
                    'color': "(Highcharts.theme && Highcharts.theme.textColor) || 'black'"
                }
            },
            'layout': 'vertical',
            'align': 'right',
            'floating': True,
            'valueDecimals': 0,
            'valueSuffix': '%',
            'backgroundColor': "(Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255, 255, 255, 0.85)'",
            'symbolRadius': 0,
            'symbolHeight': 14
        },

        'mapNavigation': {
            'enabled': True
        },

        'colorAxis': {
            'dataClasses': [{
                'from': 0,
                'to': 2,
                'color': "#F1EEF6"
            }, {
                'from': 2,
                'to': 4,
                'color': "#D4B9DA"
            }, {
                'from': 4,
                'to': 6,
                'color': "#C994C7"
            }, {
                'from': 6,
                'to': 8,
                'color': "#DF65B0"
            }, {
                'from': 8,
                'to': 10,
                'color': "#DD1C77"
            }, {
                'from': 10,
                'color': "#980043"
            }]
        },

        'plotOptions': {
            'map':{
            'mapData': 'geojson'

            },
            'mapline': {
                'showInLegend': False,
                'enableMouseTracking': False
            }
        },
    } 

H.set_dict_optoins(options)

# read data and map directly from url
data_url = 'http://www.highcharts.com/samples/data/jsonp.php?filename=us-counties-unemployment.json&callback=?'
map_url = 'http://code.highcharts.com/mapdata/countries/us/us-all-all.js'

data = jsonp_loader(data_url)
geojson = js_map_loader(map_url)
mapdata = geojson_handler(geojson)
lines = geojson_handler(geojson, 'mapline')
for x in mapdata:
    x.update({'name':x['name']+', '+x['properties']['hc-key'].split('-')[1].upper()})

#map(lambda x: x['properties'].update({'name':x['properties']['name']+', '+x['properties']['hc-key'].split('-')[1]}), geojson['features'])

H.add_data_set(data, 'map', 'Unemployment rate', joinBy = ['hc-key', 'code'], 
     tooltip = {
                    'valueSuffix': '%'
                },
                borderWidth = 0.5,
                states = {
                    'hover': {
                        'color': '#bada55'
                    }
                }
                )
H.add_data_set([lines[0]], 'mapline', 'State borders', color = 'white')
H.add_data_set([lines[3]], 'mapline', 'Separator', color = 'gray')
H.add_map_data(mapdata)



H.file()