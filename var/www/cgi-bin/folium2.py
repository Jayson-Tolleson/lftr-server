#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
cgitb.enable()

import cgi

import ee; ee.Initialize()



#html in python

print ('''Content-Type: text/html''') # HTML is following print 
print #12 returns in the next bracket

print ('''











<html><head>
  <title>J^2</title>
  <meta name="description" content="=100jay" />
  <meta name="keywords" content="Music, Art, Forum" />
  <meta http-equiv="content-type" content="text/html" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<style>
body {background: #1339de;}
div#container
{        background: black;
 width: 50%;
  margin: 100px auto;
        color: white;
        border-radius: 1em;
        width: 1200px;
    height: 500px;
    overflow:hidden;     /* if you don't want a scrollbar, set to hidden */
    overflow-x:hidden;   /* hides horizontal scrollbar on newer browsers */
    /* resize and min-height are optional, allows user to resize viewable area */
    -webkit-resize:vertical;
    -moz-resize:vertical;
    resize:vertical;
 //   min-height:1600px;
}
iframe#embed
{
    width:1200px;       /* set this to approximate width of entire page you're embedding */
    height:2400px;      /* determines where the bottom of the page cuts off */
    margin-left:0px; /* clipping left side of page */
    margin-top:0px;  /* clipping top of page */
    overflow:hidden;
    /* resize seems to inherit in at least Firefox */
    -webkit-resize:none;
    -moz-resize:none;
    resize:none;
}

</style>
<body>
  <div id="main">
    <div id="site_content">
      <div id="content">''')

import ee
import folium
from owslib.wms import WebMapService


url = 'http://oos.soest.hawaii.edu/thredds/wms/hioos/satellite/dhw_5km'

# Define a method for displaying Earth Engine image tiles to folium map.
def add_ee_layer(self, ee_image_object, vis_params, name):
  map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
  folium.raster_layers.TileLayer(
  #  tiles = url,
    tiles = map_id_dict['tile_fetcher'].url_format,
    attr = "Map Data © Google Earth Engine",
    name = name,
    overlay = True,
    control = True
  ).add_to(self)

# Add EE drawing method to folium.
folium.Map.add_ee_layer = add_ee_layer

# Fetch an elevation model.
dem = ee.Image('USGS/SRTMGL1_003')
# Set visualization parameters.
vis_params = {
  'min': 0,
  'max': 4000,
  'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

# Create a folium map object.
my_map = folium.Map(location=[34, -118], zoom_start=12, height=500, control_scale=True)

# Add the elevation model to the map object.
my_map.add_ee_layer(dem.updateMask(dem.gt(0)), vis_params, 'DEM')

#


# Add a layer control panel to the map.
my_map.add_child(folium.LayerControl())


outHtml = '/var/www/map.html' # temporary file path, change if needed
my_map.save(outHtml)
print ('''<section>
<div id="container">
<iframe id="embed" scrolling="no" src="/map.html"></iframe>
</div>
</section>''')

print ('''<div><h1>end of page</h1></div>''')




