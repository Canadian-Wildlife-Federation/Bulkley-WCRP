#!/usr/bin/env python
# coding: utf-8

# This is a basic app using data called from the api as well as some interactivity.

# In[1]:


import dash
from dash import Dash, dcc, html, Input, Output, dash_table #pip install dash
import jupyter_dash #integrated in jupyter notebooks
from jupyter_dash import JupyterDash as JD
import dash_leaflet as dl
import dash_leaflet.express as dlx #pip install --upgrade protobuf==3.20.0 --user before importing and if necessarym, restart the kernel
import requests
import json
from dash_extensions.javascript import assign, arrow_function, Namespace
import pandas as pd
#import geopandas as gpd
import numpy as np
import random
from flask_caching import Cache
import os
import dash_bootstrap_components as dbc


# In[2]:


# #querying data from pg_featureserv API for bcfishpass
request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27HORS%27' #this query slows things down for some reason

request1 = 'https://tiles.hillcrestgeo.ca/bcfishpass/bcfishpass.streams.json'
query1 = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27HORS%27'

response_API = requests.get(request+query)
response_API1 = requests.get(request1+query1)

parse = response_API.text
stream = json.loads(parse)

# parse1 = response_API1.text
# gjson = json.loads(parse1)

# #api call function
# def apiCall(w):
#     request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
#     query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27' + w + '%27' #this query slows things down for some reason

#     request1 = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json'
#     query1 = '?properties=aggregated_crossings_id,pscis_status,barrier_status,access_model_ch_co_sk,all_spawningrearing_per_barrier,all_spawningrearing_km&filter=watershed_group_code%20=%20%27' + w + '%27%20AND%20all_spawningrearing_km%3e0'

#     response_API = requests.get(request+query)
#     response_API1 = requests.get(request1+query1)

#     parse = response_API.text
#     parse1 = response_API1.text

#     return parse, parse1


# prior_table = pd.read_csv('tables\priority_barriers.csv', index_col=False)
# inter_table = pd.read_csv('tables\inter_barriers.csv', index_col=False)


# In[3]:


#configuring the app
#useful resources include:
#https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Other/Dash_Introduction/intro.py
#https://dash-leaflet.herokuapp.com/
#https://github.com/plotly/jupyter-dash/blob/master/notebooks/getting_started.ipynb

from sre_constants import IN


app = JD(__name__)
server = app.server
cache = Cache()
cache.init_app(server, config={'CACHE_TYPE': 'SimpleCache'})
timeout = 20
#making dropdown option based on property in data table
id_list = []

ns = Namespace("myNamespace", "mySubNamespace")

#priority vs intermediate barrier list

prior_table = pd.read_csv('tables\\priority_barriers.csv', index_col=False)
inter_table = pd.read_csv('tables\\inter_barriers.csv', index_col=False)

#to imporve performance, this function should be CACHED
def priority(row):
    request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json?watershed_group_code=HORS&aggregated_crossings_id=' + str(row['aggregated_crossings_id'])
    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)
    features = result['features']
    hab_gain=0
    cost_benefit=0
    for i in range(len(features)):
        if features[i]['properties']['aggregated_crossings_id'] == row['aggregated_crossings_id']:
            hab_gain = features[i]['properties']['all_spawningrearing_belowupstrbarriers_km']
    
    if hab_gain != 0: cost_benefit = row['estimated_cost']/hab_gain
    
    return hab_gain,cost_benefit

prior_table['hab_gain'] = prior_table.apply(lambda row: priority(row)[0], axis=1)
prior_table['cost_benefit_ratio'] = prior_table.apply(lambda row: priority(row)[1], axis=1)


#seperate GeoJSOn for selected filtering

 
    #-----------------------------------------------------------------------------------------------------------------------------------

# #point to layer 
# point_to_layer = assign("function(feature, latlng, context){return L.circleMarker(latlng);}")
# ------------------------------------------------------------------------------
prior_drop =  dcc.Dropdown(
                    options=[
                        {'label': 'Priority Barrier List', 'value': 'priority'},
                        {'label': 'Intermediate Barrier List', 'value': 'intermediate'}
                    ],
                    placeholder='All Barriers',
                    id='dd',
                    style={'width': '500px'}
                )

barrtype_filter_drop = dcc.Dropdown(
                        options=[
                        {'label': 'TBD', 'value': 'TBD'},
                        {'label': 'DAM', 'value': 'Dam'},
                        {'label': 'PARTIAL', 'value': 'Partial'},
                        {'label': 'FULL', 'value': 'Full'},
                        {'label': 'PARTIAL-FULL', 'value': 'Partial-Full'},
                        {'label': 'POTENTIAL', 'value': 'Potential'}
                        ],
                        placeholder="Barrier Type",
                        id= 'barrtype',
                        disabled=True,
                        style={'width': '500px'}
                    )

nextstep_filter_drop = dcc.Dropdown(
                        options=[
                        {'label': 'Barrier Assessment', 'value': 'Barrier assessment'},
                        {'label': 'Design', 'value': 'Design'},
                        {'label': 'Follow up with Barrier Owner', 'value': 'Follow up with barrier owner'},
                        {'label': 'Habitat Investigations', 'value': 'Habitat investigations'},
                        {'label': 'Remediation', 'value': 'Remediation'}
                        ],
                        placeholder='Next Steps',
                        id= 'nextstep',
                        disabled=True,
                        style={'width': '500px'}
                    )

pcsis_filter_drop = dcc.Dropdown(
                        options=[
                        {'label': 'HABITAT CONFIRMATION', 'value': 'HABITAT CONFIRMATION'},
                        {'label': 'ASSESSED', 'value': 'ASSESSED'}
                        ],
                        placeholder='PCSIS Status',
                        id= 'PCSIS',
                        disabled=True,
                        style={'width': '500px'}
                    )

barrstat_filter_drop = dcc.Dropdown(
                        options=[
                        {'label': 'PASSABLE', 'value': 'PASSABLE'},
                        {'label': 'BARRIER', 'value': 'BARRIER'},
                        {'label': 'POTENTIAL', 'value': 'POTENTIAL'},
                        {'label': 'UNKNOWN', 'value': 'UNKNOWN'}
                        ],
                        placeholder='Barrier Status',
                        id= 'barrstat',
                        disabled=True,
                        style={'width': '500px'}
                    )

watershed_drop = dcc.Dropdown(
                    options=[
                        {'label': 'HORS', 'value': 'HORS'},
                        {'label': 'BULK', 'value': 'BULK'},
                        {'label': 'LNIC', 'value': 'LNIC'},
                        {'label': 'ELKR', 'value': 'ELKR'}
                    ],
                    value = 'HORS',
                    id='watershed',
                    style={'width': '500px'}
                )
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboard for Fish Passage BC", id = "title"),

    html.H3("Barrier List"),

    html.Div([
        html.Div([
            dbc.Col(prior_drop, width = 2),
            dbc.Col(watershed_drop, width = 2)
        ])
    ], id="dropdown"),

    html.H3("Priority Barrier List Filters"),
    
    html.Div([
        html.Div([
            dbc.Col(barrtype_filter_drop, width = 2),
            dbc.Col(nextstep_filter_drop, width = 2)
        ])
    ], id="extradropdown"),

    html.H3("Intermediate & All Barrier List Filters"),
    
    html.Div([
        html.Div([
            dbc.Col(pcsis_filter_drop, width = 2),
            dbc.Col(barrstat_filter_drop, width = 2)
        ])
    ], id="extradropdown2"),
    

    dl.Map(children=[
        
        
        dl.LayersControl(
        [dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    attribution='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'), name='ESRI Topographic', checked=False),
                    dl.BaseLayer(dl.TileLayer(), name='Base', checked=True), dl.BaseLayer(dl.Overlay(children = ns("pbf2dash")), name='test')] +
        [ dl.Overlay(children=[], checked=True, id='pass', name='Passable')]+
        [ dl.Overlay(children=[], checked=True, id='pot', name='Potential')]+
        [ dl.Overlay(children=[], checked=True, id='bar', name='Barrier')]+
        [ dl.Overlay(children=[], checked=True, id='other', name='Unknown')] +
        [dl.Overlay(dl.GeoJSON(data=stream, id="streams", zoomToBounds=True), name='Stream Network',checked=True)])
        ],
        id='map',
        style={'width': '1500px', 'height': '500px'}, #style is key as map will not show up without it
        center=[52.6,-120.5],
        zoom=8 
    ),

    html.Br(),


    dash_table.DataTable(
                        columns=[
                            {'name': 'Crossing ID', 'id': 'id', 'type': 'numeric'},
                            {'name': 'PSCIS status', 'id': 'pscis_status', 'type': 'text'},
                            {'name': 'Barrier Status', 'id': 'barrier_status', 'type': 'text'},
                            {'name': 'Acess Model', 'id': 'access_model_ch_co_sk', 'type': 'text'},
                            {'name': 'All habitat', 'id': 'all_spawningrearing_per_barrier', 'type': 'numeric'},
                            {'name': 'Latitude', 'id': 'lat', 'type': 'numeric'},
                            {'name': 'Longitude', 'id': 'lon', 'type': 'numeric'}
                        ],
                        data=[],
                        sort_action="native",
                        sort_mode="multi",
                        filter_action="native",
                        style_data={
                            'color': 'black',
                            'backgroundColor': 'white'
                        },
                        style_header={
                            'backgroundColor': '#00828d',
                            'fontWeight': 'bold'
                        },
                        id='table2',
                        active_cell= None
                        ),
    
    html.Br(),
    
    html.H2(id='test')

], id = 'app')



# ------------------------------------------------------------------------------
# Connect Leaflet Map to Dash Components
@cache.memoize(timeout=timeout)

#api call function
def apiCall(w):
    request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
    query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27' + w + '%27' #this query slows things down for some reason

    request1 = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json'
    query1 = '?properties=aggregated_crossings_id,pscis_status,barrier_status,access_model_ch_co_sk,all_spawningrearing_per_barrier,all_spawningrearing_km&filter=watershed_group_code%20=%20%27' + w + '%27%20AND%20all_spawningrearing_km%3e0'

    response_API = requests.get(request+query)
    response_API1 = requests.get(request1+query1)

    parse = response_API.text
    parse1 = response_API1.text

    return parse, parse1

# def apiCall_barrierType(w):
#     request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
#     query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27' + w + '%27' #this query slows things down for some reason

#     request1 = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json'
#     query1 = '?properties=aggregated_crossings_id,pscis_status,barrier_status,access_model_ch_co_sk,all_spawningrearing_per_barrier,all_spawningrearing_km&filter=watershed_group_code%20=%20%27' + w + '%27%20AND%20all_spawningrearing_km%3e0%20AND%20'

#     response_API = requests.get(request+query)
#     response_API1 = requests.get(request1+query1)

#     parse = response_API.text
#     parse1 = response_API1.text

#     return parse, parse1

def apiCall_prior(w,l,b,n):

    list1 = "("
    if l == 'intermediate':
        bar = inter_table

        for i in inter_table['intermediate'].values:
            if i == (inter_table['intermediate'].iat[-1]):
                list1 = list1 + str(i) + ")"
            else:
                list1 = list1 + str(i) + ","
    elif l == 'priority':

        if b is not None and n is None:
            bar = prior_table[prior_table['barrier_type']==b]
        elif b is None and n is not None:
            bar = prior_table[prior_table['next_steps']==n]
        else:
            bar = prior_table

        
        for i in bar['aggregated_crossings_id'].values:
            if i == (bar['aggregated_crossings_id'].iat[-1]):
                list1 = list1 + str(i) + ")"
            else:
                list1 = list1 + str(i) + ","


    request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
    query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27' + w + '%27' #this query slows things down for some reason

    request1 = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json'
    query1 = '?properties=aggregated_crossings_id,pscis_status,barrier_status,access_model_ch_co_sk,all_spawningrearing_per_barrier,all_spawningrearing_km&filter=watershed_group_code%20=%20%27' + w + '%27%20AND%20all_spawningrearing_km%3e0%20AND%20aggregated_crossings_id%20IN%20' + list1

    response_API = requests.get(request+query)
    response_API1 = requests.get(request1+query1)

    parse = response_API.text
    parse1 = response_API1.text

    return parse, parse1, bar

def get_data(features,p):
    Passable = []
    potential = []
    barrier = []
    other = []

    if p is not None:
        for i in range(len(features)):
            if features[i]['properties']['barrier_status'] == 'PASSABLE' and features[i]['properties']['pscis_status'] == p:
                Passable.append(
                    dl.CircleMarker(
                        id = str(features[i]['properties']['aggregated_crossings_id']),
                        color='white',
                        fillColor = '#32cd32',
                        fillOpacity = 1, 
                        center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                        children=[
                            dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                            dl.Popup(str(features[i]['properties']['aggregated_crossings_id'])),
                        ],
                    )
                )
            elif features[i]['properties']['barrier_status'] == 'POTENTIAL' and features[i]['properties']['pscis_status'] == p:
                potential.append(
                    dl.CircleMarker(
                        color='white',
                        fillColor = '#ffb400',
                        fillOpacity = 1, 
                        center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                        children=[
                            dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                            dl.Popup(str(features[i]['properties']['aggregated_crossings_id']) + "\n NEWS: idk whats going on!"),
                        ],
                    )
                )
            elif features[i]['properties']['barrier_status'] == 'BARRIER' and features[i]['properties']['pscis_status'] == p:
                barrier.append(
                    dl.CircleMarker(
                        id="marker",
                        color='white',
                        fillColor = '#d52a2a',
                        fillOpacity = 1, 
                        center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                        children=[
                            dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id']), id="tooltip"),
                            dl.Popup(str(features[i]['properties']['aggregated_crossings_id'])),
                        ],
                    )
                )
            elif features[i]['properties']['barrier_status'] == 'UNKNOWN' and features[i]['properties']['pscis_status'] == p:
                other.append(
                    dl.CircleMarker(
                        color = 'white',
                        fillColor = '#965ab3',
                        fillOpacity = 1,
                        center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                        children=[
                            dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                            dl.Popup()
                        ],
                    )
                )


    else:

        for i in range(len(features)):
            if features[i]['properties']['barrier_status'] == 'PASSABLE':
                Passable.append(
                    dl.CircleMarker(
                        id = str(features[i]['properties']['aggregated_crossings_id']),
                        color='white',
                        fillColor = '#32cd32',
                        fillOpacity = 1, 
                        center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                        children=[
                            dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                            dl.Popup(str(features[i]['properties']['aggregated_crossings_id'])),
                        ],
                    )
                )
            elif features[i]['properties']['barrier_status'] == 'POTENTIAL':
                potential.append(
                    dl.CircleMarker(
                        color='white',
                        fillColor = '#ffb400',
                        fillOpacity = 1, 
                        center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                        children=[
                            dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                            dl.Popup(str(features[i]['properties']['aggregated_crossings_id']) + "\n NEWS: idk whats going on!"),
                        ],
                    )
                )
            elif features[i]['properties']['barrier_status'] == 'BARRIER':
                barrier.append(
                    dl.CircleMarker(
                        id="marker",
                        color='white',
                        fillColor = '#d52a2a',
                        fillOpacity = 1, 
                        center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                        children=[
                            dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id']), id="tooltip"),
                            dl.Popup(str(features[i]['properties']['aggregated_crossings_id'])),
                        ],
                    )
                )
            else:
                other.append(
                    dl.CircleMarker(
                        color = 'white',
                        fillColor = '#965ab3',
                        fillOpacity = 1,
                        center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                        children=[
                            dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                            dl.Popup()
                        ],
                    )
                )

    pass_cluster = dl.MarkerClusterGroup(id='markers', children=Passable)
    pot_cluster = dl.MarkerClusterGroup(id='markers', children=potential)
    bar_cluster = dl.MarkerClusterGroup(id='barriers', children=barrier)
    other_cluster = dl.MarkerClusterGroup(id='markers1', children=other)
    return pass_cluster, pot_cluster, bar_cluster, other_cluster

def get_tabledata(features,p,b):
    id_list = []
#features[i]['properties']['barrier_status'] == 'PASSABLE
    if p is not None or b is not None:

        if p is not None and b is None:

            for i in range(len(features)):

                if features[i]['properties']['pscis_status'] == p:


                    pscis=features[i]['properties']['pscis_status']
                    barr=features[i]['properties']['barrier_status']
                    acc=features[i]['properties']['access_model_ch_co_sk']
                    all=features[i]['properties']['all_spawningrearing_per_barrier']
                    cross_id = str(features[i]['properties']['aggregated_crossings_id'])
                    lat = features[i]['geometry']['coordinates'][1]
                    lon = features[i]['geometry']['coordinates'][0]

                    temp = dict(id = cross_id, pscis_status=pscis, barrier_status=barr, access_model_ch_co_sk=acc, all_spawningrearing_per_barrier=all, lat = lat, lon = lon)

                    id_list = id_list + [temp,]

            return id_list
        
        elif b is not None and p is None:

            for i in range(len(features)):

                if features[i]['properties']['barrier_status'] == b:


                    pscis=features[i]['properties']['pscis_status']
                    barr=features[i]['properties']['barrier_status']
                    acc=features[i]['properties']['access_model_ch_co_sk']
                    all=features[i]['properties']['all_spawningrearing_per_barrier']
                    cross_id = str(features[i]['properties']['aggregated_crossings_id'])
                    lat = features[i]['geometry']['coordinates'][1]
                    lon = features[i]['geometry']['coordinates'][0]

                    temp = dict(id = cross_id, pscis_status=pscis, barrier_status=barr, access_model_ch_co_sk=acc, all_spawningrearing_per_barrier=all, lat = lat, lon = lon)

                    id_list = id_list + [temp,]
                    
            return id_list

    else: 
        
        for i in range(len(features)):
            pscis=features[i]['properties']['pscis_status']
            barr=features[i]['properties']['barrier_status']
            acc=features[i]['properties']['access_model_ch_co_sk']
            all=features[i]['properties']['all_spawningrearing_per_barrier']
            cross_id = str(features[i]['properties']['aggregated_crossings_id'])
            lat = features[i]['geometry']['coordinates'][1]
            lon = features[i]['geometry']['coordinates'][0]

            temp = dict(id = cross_id, pscis_status=pscis, barrier_status=barr, access_model_ch_co_sk=acc, all_spawningrearing_per_barrier=all, lat = lat, lon = lon)

            id_list = id_list + [temp,]
        return id_list

def get_latlon(features):
    id_list = []
    for i in range(len(features)):
        cross_id = str(features[i]['properties']['aggregated_crossings_id'])
        lat = features[i]['geometry']['coordinates'][1]
        lon = features[i]['geometry']['coordinates'][0]

        temp = dict(id = cross_id,lat = lat, lon = lon)

        id_list = id_list + [temp,]
    return id_list



@app.callback(
    [Output('pass', 'children'), Output('pot', 'children'), Output('bar', 'children'), Output('other', 'children'), Output('streams', 'data'), Output('table2','data')], [Input('watershed', 'value'), Input('dd', 'value'), Input('barrtype', 'value'), Input('nextstep', 'value'), Input('PCSIS', 'value'), Input('barrstat','value')]
)
def update_map(value, priority, barrtype, nextsteps, pcsis, barrstat):

    
    
    
    if value == 'BULK':
        parse, parse1 = apiCall('BULK')
        B_gjson = json.loads(parse1)
        B_stream = json.loads(parse)
        features = B_gjson['features']
        return get_data(features,pcsis)[0], get_data(features,pcsis)[1], get_data(features,pcsis)[2], get_data(features,pcsis)[3], B_stream, get_tabledata(features,pcsis,barrstat)
    elif value == 'LNIC':
        parse, parse1 = apiCall('LNIC')
        B_gjson = json.loads(parse1)
        B_stream = json.loads(parse)
        features = B_gjson['features']
        return get_data(features,pcsis)[0], get_data(features,pcsis)[1], get_data(features,pcsis)[2], get_data(features,pcsis)[3], B_stream, get_tabledata(features,pcsis,barrstat)
    elif value == 'ELKR':
        parse, parse1 = apiCall('ELKR')
        B_gjson = json.loads(parse1)
        B_stream = json.loads(parse)
        features = B_gjson['features']
        return get_data(features,pcsis)[0], get_data(features,pcsis)[1], get_data(features,pcsis)[2], get_data(features,pcsis)[3], B_stream, get_tabledata(features,pcsis,barrstat)
    elif value == 'HORS':
        parse, parse1 = apiCall('HORS')
        B_gjson = json.loads(parse1)
        B_stream = json.loads(parse)
        features = B_gjson['features']


        

        if priority == 'intermediate':
            parse, parse1 = apiCall_prior('HORS',priority,barrtype,nextsteps)[0],apiCall_prior('HORS',priority,barrtype,nextsteps)[1]
            B_gjson = json.loads(parse1)
            B_stream = json.loads(parse)
            features = B_gjson['features']
            data = []
            test = get_tabledata(features,pcsis,barrstat) #all that is needed to filter table data with new filtering structure (only for intermediate list)
            # for i in range(0, len(inter_table.iloc[:,0])):
            #     id_list = get_tabledata(features,pcsis,barrstat)
            #     id_index = dict((p['id'],j) for j,p in enumerate(id_list))
            #     index1 = id_index.get(str(inter_table.iloc[:,0][i]), -1)
            #     data = data + [id_list[index1],]
            #     #print(type(data))
            return get_data(features,pcsis)[0], get_data(features,pcsis)[1], get_data(features,pcsis)[2], get_data(features,pcsis)[3], B_stream, test
        elif priority == 'priority':
            parse, parse1 = apiCall_prior('HORS',priority,barrtype,nextsteps)[0],apiCall_prior('HORS',priority,barrtype,nextsteps)[1]
            B_gjson = json.loads(parse1)
            B_stream = json.loads(parse)
            features = B_gjson['features']
            bar = apiCall_prior('HORS',priority,barrtype,nextsteps)[2]
            bar.reset_index(drop=True, inplace=True)
            data=[]
            for i in range(0, len(bar.iloc[:,0])):
                id_list = get_latlon(features)
                id_index = dict((p['id'],j) for j,p in enumerate(id_list))
                index1 = id_index.get(str(bar.iloc[:,0][i]), -1)
                data = data + [id_list[index1],]
            data = pd.DataFrame(data)
            new = pd.concat([bar,data], axis=1, join="inner")#.drop_duplicates()#.reset_index(drop=True)
            data = new.set_index('aggregated_crossings_id', drop=False).to_dict(orient="records")#.drop('id',axis=1)

            return get_data(features,pcsis)[0], get_data(features,pcsis)[1], get_data(features,pcsis)[2], get_data(features,pcsis)[3], B_stream, data
            
        else:
           return get_data(features,pcsis)[0], get_data(features,pcsis)[1], get_data(features,pcsis)[2], get_data(features,pcsis)[3], B_stream, get_tabledata(features,pcsis,barrstat)
    
        
    
    else: 
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    
    
    
@app.callback(
    [Output('map', 'center'), Output('map', 'zoom')], [Input('table2', 'active_cell'), Input('watershed', 'value'), Input('PCSIS', 'value'), Input('barrstat','value')]
)
def marker(cell, value, pcsis, barrstat):
    if value == 'HORS':
        if cell['column_id'] == "id" or cell['column_id'] == "aggregated_crossings_id":
            parse1 = apiCall(value)[1]
            B_gjson = json.loads(parse1)
            features = B_gjson['features']
            id_list = get_tabledata(features,pcsis,barrstat)
            for i in id_list:
                if str(i['id']) == cell['row_id']:
                    lat = i['lat']
                    lon = i['lon']
                    center = [lat,lon]
            return center, 16 
    elif value == 'BULK':
        if cell['column_id'] == "id":
            parse1 = apiCall(value)[1]
            B_gjson = json.loads(parse1)
            features = B_gjson['features']
            id_list = get_tabledata(features,pcsis,barrstat)
            for i in id_list:
                if str(i['id']) == cell['row_id']:
                    lat = i['lat']
                    lon = i['lon']
                    center = [lat,lon]
            return center, 16

    elif value == 'LNIC':
        if cell['column_id'] == "id":
            parse1 = apiCall(value)[1]
            B_gjson = json.loads(parse1)
            features = B_gjson['features']
            id_list = get_tabledata(features,pcsis,barrstat)
            for i in id_list:
                if str(i['id']) == cell['row_id']:
                    lat = i['lat']
                    lon = i['lon']
                    center = [lat,lon]
            return center, 16

    elif value == 'ELKR':
        if cell['column_id'] == "id":
            parse1 = apiCall(value)[1]
            B_gjson = json.loads(parse1)
            features = B_gjson['features']
            id_list = get_tabledata(features,pcsis,barrstat)
            for i in id_list:
                if str(i['id']) == cell['row_id']:
                    lat = i['lat']
                    lon = i['lon']
                    center = [lat,lon]
            return center, 16           
    
    else:
        return dash.no_update, dash.no_update

# @app.callback(
#     [Output('table2', 'active_cell'), Output('test', 'children')], [Input('table2', 'active_cell'), Input('watershed', 'value'), Input('map', 'click_lat_lng')]
# )

# def click_marker(cell, value, click):
#     if value == 'HORS':
#         parse1 = apiCall(value)[1]
#         B_gjson = json.loads(parse1)
#         features = B_gjson['features']
#         id_list = get_tabledata(features,pcsis,barrstat)
#         for i in id_list:
#             if ((-0.001 <= (click[0] - i['lat'])) and ((click[0] - i['lat'])<= 0.001)) and ((-0.001 <= (click[0] - i['lon'])) and ((click[0] - i['lon'])<= 0.001)):
#                 return cell, (i['lat'])
#             else: return dash.no_update, dash.no_update

#app.clientside_callback("functions(x){return x;}", Output("test", "children"), Input(marker, "n_clicks"))

# @app.callback(
#     Output("test", "children"),[Input("barriers", "children")]
# )
# def click_marker(marker_id):
#     #print(marker_id[0])
#     return "KJFDHGLIDUGHIKGJC: {}".format(marker_id[0])

# @app.callback(
#     [Output('pass', 'children'), Output('pot', 'children'), Output('bar', 'children'), Output('other', 'children'), Output('streams', 'data'), Output('table2','data')], [Input('table2','derived_virtual_data'),Input('watershed', 'value'), Input('dd', 'value')]
# )
# def filter_trigger(rows, value, priority):

#     parse, parse1 = apiCall('HORS')
#     B_gjson = json.loads(parse1)
#     B_stream = json.loads(parse)
#     features = B_gjson['features']

#     if rows is not None:

#         dff = pd.DataFrame(rows) 
        
#         data = []
#         for i in range(0, len(dff.iloc[:,0])):
#             id_list = get_tabledata(features,pcsis,barrstat)
#             id_index = dict((p['id'],j) for j,p in enumerate(id_list))
#             index1 = id_index.get(str(dff.iloc[:,0][i]), -1)
#             data = data + [id_list[index1],]
#         return get_data(features,pcsis)[0], get_data(features,pcsis)[1], get_data(features,pcsis)[2], get_data(features,pcsis)[3], B_stream, data

    # else:

    #     return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

@app.callback(
    Output('table2', 'columns'), [Input('dd', 'value')]
)
def priority_filter(value):
    if value == 'priority':
        columns=[
                    {'name': 'Crossing ID', 'id': 'aggregated_crossings_id', 'type': 'numeric'},
                    {'name': 'Stream Name', 'id': 'stream_name', 'type': 'text'},
                    {'name': 'Road Name', 'id': 'road_name', 'type': 'text'},
                    {'name': 'Owner', 'id': 'owner', 'type': 'text'},
                    {'name': 'Proposed Fix', 'id': 'proposed_fix', 'type': 'text'},
                    {'name': 'Estimated Cost', 'id': 'estimated_cost', 'type': 'text'},
                    {'name': 'Upstream Habitat Quality', 'id': 'upstr_hab_quality', 'type': 'text'},
                    {'name': 'Barrier Type', 'id': 'barrier_type', 'type': 'text'},
                    {'name': 'Habitat Gain', 'id': 'hab_gain', 'type': 'numeric'},
                    {'name': 'Cost Benefit Ratio', 'id': 'cost_benefit_ratio', 'type': 'numeric'},
                    {'name': 'Upstream Habitat Quality', 'id': 'upstr_hab_quality', 'type': 'text'},
                    {'name': 'Priority', 'id': 'priority', 'type': 'text'},
                    {'name': 'Next Steps', 'id': 'next_steps', 'type': 'text'},
                    {'name': 'Reasoning', 'id': 'reason', 'type': 'text'},
                    {'name': 'Notes', 'id': 'notes', 'type': 'text'}
                    # {'name': 'Latitude', 'id': 'lat', 'type': 'numeric'},
                    # {'name': 'Longitude', 'id': 'lon', 'type': 'numeric'}
                ]
        return columns
    else:
        columns=[
                    {'name': 'Crossing ID', 'id': 'id', 'type': 'numeric'},
                    {'name': 'PSCIS status', 'id': 'pscis_status', 'type': 'text'},
                    {'name': 'Barrier Status', 'id': 'barrier_status', 'type': 'text'},
                    {'name': 'Acess Model', 'id': 'access_model_ch_co_sk', 'type': 'text'},
                    {'name': 'All habitat', 'id': 'all_spawningrearing_per_barrier', 'type': 'numeric'},
                    #{'name': 'Latitude', 'id': 'lat', 'type': 'numeric'},
                    #{'name': 'Longitude', 'id': 'lon', 'type': 'numeric'}
                ]
        return columns

@app.callback(
    [Output('barrtype','disabled'),Output('nextstep','disabled'),Output('PCSIS','disabled'),Output('barrstat','disabled')],[Input('dd', 'value')]
)

def extra_filter(value):
    if value == 'priority':
        return False, False, True, True
    else:
        return True, True, False, False

@app.callback(
    [Output('pass','checked'), Output('pot','checked'), Output('bar','checked'), Output('other','checked')],[Input('barrstat', 'value')]
)
def barrstat(value):
    if value == 'PASSABLE':
        return True, False, False, False
    elif value == 'POTENTIAL':
        return False, True, False, False
    elif value == 'BARRIER':
        return False, False, True, False
    elif value == 'UNKNOWN':
        return False, False, False, True
    else:
        return True, True, True, True       


        
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    #app.run_server()
    app.run_server(mode = 'inline', port = random.choice(range(2000, 10000)))
    #mode = 'inline' for JD

