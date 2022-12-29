#!/usr/bin/env python
# coding: utf-8

# # API practice

# This is where I will be practice producing API called maps.

# In[1]:


from urllib import response
from ipyleaflet import *
from ipywidgets import HTML
import requests
import json
import pandas
from pandas import json_normalize


#setting the map to center and zoom
m = Map(center=(52.6,-120.5), zoom=4)

#alternate basemap tile
dm_layer = basemap_to_tiles(basemaps.CartoDB.DarkMatter)
m.add_layer(dm_layer)

#caching
#querying data from pg_featureserv API for bcfishpass
request = 'https://cabd-web.azurewebsites.net/cabd-api/features/dams?filter=province_territory_code:eq:bc&filter=nhn_watershed_id:eq:08DA003'
response_api = requests.get(request)
parse = response_api.text
dams = json.loads(parse)

# geo = GeoJSON(data = dams,
#               name = "dams")
# m.add_layer(geo)

#popup & marker cluster
markers = ()

#style for marker https://fontawesome.com/v4/icons/
icon = AwesomeIcon(
  name='wrench',
  marker_color='blue',
  icon_color='blue'
)

#https://carpentries-incubator.github.io/jupyter_maps/03-vector/index.html

features = dams['features']
for i in range(len(features)):
    location=(features[i]['geometry']['coordinates'][1],features[i]['geometry']['coordinates'][0])
    instructors = (features[i]['properties']['cabd_id'])
    html = """
    <p>
      <h4>Table:        """ + " ".join(instructors) + """</h4>
    </p>
    """
    marker = Marker(icon = icon, location = location)

    # Popup associated to a layer
    marker.popup = HTML(html)
    #m.add_layer(marker)

    #marker cluster markers
    markers = markers + (marker,)

m.add_layer(MarkerCluster(markers = markers, name="DAMS"))

#display(m)

print(type(response_api))


# In[2]:


from ipyleaflet import *
from ipywidgets import HTML
import requests
import json
import pandas
from pandas import json_normalize


#setting the map to center and zoom
m = Map(center=(52.6,-120.5), zoom=8)

#alternate basemap tile
dm_layer = basemap_to_tiles(basemaps.CartoDB.DarkMatter)
m.add_layer(dm_layer)

#caching
#querying data from pg_featureserv API for bcfishpass
request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
query = '?properties=watershed_group_code&filter=watershed_group_code%20=%20%27HORS%27' #this query slows things down for some reason

request1 = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json'
query1 = '?filter=watershed_group_code%20=%20%27HORS%27%20AND%20all_spawningrearing_km%3e0'

response_API = requests.get(request+query)
response_API1 = requests.get(request1+query1)

parse = response_API.text
stream = json.loads(parse)

parse1 = response_API1.text
gjson = json.loads(parse1)
  


#converting json to geojson
geo = GeoJSON(data = stream,
              name = "stream")
m.add_layer(geo)

geo1 = GeoJSON(data=gjson,
               name="layer")

#m.add_layer(geo1)

#adding controls to map
control = LayersControl(position='topright')

#popup & marker cluster
markers = ()

#style for marker https://fontawesome.com/v4/icons/
icon = AwesomeIcon(
  name='wrench',
  marker_color='blue',
  icon_color='blue'
)

#https://carpentries-incubator.github.io/jupyter_maps/03-vector/index.html

features = gjson['features']
for i in range(len(features)):
    location=(features[i]['geometry']['coordinates'][1],features[i]['geometry']['coordinates'][0])
    instructors = (features[i]['id'])
    html = """
    <p>
      <h4>Table:        """ + " ".join(instructors) + """</h4>
    </p>
    """
    marker = Marker(icon = icon, location = location)

    # Popup associated to a layer
    marker.popup = HTML(html)
    #m.add_layer(marker)

    #marker cluster markers
    markers = markers + (marker,)

m.add_layer(MarkerCluster(markers = markers, name="Crossings"))
    




m.add_control(control)


#displaying map inline
display(m)

