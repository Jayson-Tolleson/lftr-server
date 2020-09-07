

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
cgitb.enable()

import cgi

import ee; ee.Initialize()
import folium
from folium import plugins
from ee import batch
from owslib.wms import WebMapService
import math
import datetime
import time
import calendar
import cv2
import numpy as np
import utm
import geehydro


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
        width: 1400px;
    height: 1000px;
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
    width:1400px;       /* set this to approximate width of entire page you're embedding */
    height:1200px;      /* determines where the bottom of the page cuts off */
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
      <div id="content">
    <h1>Google Earth Engine with Folium</h1>
<html>
      <head >
        <title>   </title>
       <script type="text/javascript" >
        function go() {
            var m1=document.getElementsByName("a");
            var m2=document.getElementsByName("b");
            var m3=document.getElementsByName("c");
            var m4=document.getElementsByName("d");
            var m5=document.getElementsByName("e");
            var m6=document.getElementsByName("f");
            var m7=document.getElementsByName("g");
            var m8=document.getElementsByName("h");
            var m9=document.getElementsByName("i");
            var m10=document.getElementsByName("j");
            var m11=document.getElementsByName("k");
            var m12=document.getElementsByName("l");
            var m13=document.getElementsByName("m");
            window.location.href = "https://lftr.biz/cgi-bin//foliumee.py" + m1(0).value + "+" + m2(0).value + "+" + m3(0).value + "+" + m4(0).value + "+" + m5(0).value + "+" + m6(0).value + "+" + m7(0).value + "+" + m8(0).value + "+" + m9(0).value + "+" + m10(0).value + "+" + m11(0).value+ "+" + m12(0).value+ "+" + m13(0).value;
        }
       </script>
     </head>
     <body>

<form action="https://lftr.biz/cgi-bin/foliumee.py" onsubmit="go();">
Latitude (xxx.xxxx/-xxx.xxxx): <input type="text" name="a" value= "033.606"><br>
Longitude (xxx.xxxx/-xxx.xxxx): <input type="text" name="b" value= "-117.926"><br>
Zoom(0-22):"22" is max zoom in, 0 is max zoom out: <input type="number" name="c" value="6"><br>

Start:
    Time(hh:mm): <input type="number" name="d" value="08"> : <input type="number" name="e" value="15"><br><br>

    Date:

    Day: <input type="number" name="f" value="01"><br> Month: <input type="number" name="g" value="01"><br> Year: <input type="number" name="h" value="2020"><br>

End:
        Time(hh:mm): <input type="number" name="i" value="22"> : <input type="number" name="j" value="15"><br><br>
        Date:
        Day: <input type="number" name="k" value="01"><br> Month: <input type="number" name="l" value="01"><br> Year: <input type="number" name="m" value="2020"><br>

<input type="submit" value="geoloc">
</form></body></html></div></div></div></body></html>''')
print ('currently:')
print (time.asctime( time.localtime(time.time())))

form = cgi.FieldStorage()
lat = float(form.getvalue("a"))
lng = float(form.getvalue("b"))
zoom = int(form.getvalue("c"))
starthour= int(form.getvalue("d"))
startminute = int(form.getvalue("e"))
finishhour= int(form.getvalue("i"))
finishminute = int(form.getvalue("j"))
day1 = int(form.getvalue("f"))
day2 = int(form.getvalue("k"))
month = int(form.getvalue("g"))
month2 = int(form.getvalue("l"))
year = int(form.getvalue("h"))
year2 = int(form.getvalue("m"))
time1=(str(year)+'-'+str(month).zfill(2) +'-'+str(day1).zfill(2) +'T'+str(starthour).zfill(2) +':'+str(startminute).zfill(2))
time2=(str(year2)+'-'+str(month2).zfill(2) +'-'+str(day2).zfill(2) +'T'+str(finishhour).zfill(2) +':'+str(finishminute).zfill(2))
d=int(zoom)*.001365

tend=time.strftime('%Y'+'-'+'%m'+'-'+'%d'+'T'+'%H'+':'+'%M'+':'+'%S')

m = folium.Map(location=[lat,lng], zoom_start=zoom, tiles=None, height=1000)
minimap = plugins.MiniMap()
m.add_child(minimap)
plugins.LocateControl(auto_start=True).add_to(m)
m.add_child(folium.LatLngPopup())


folium.raster_layers.TileLayer(
    tiles='http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
    attr='google',
    name='google street view',
    max_zoom=20,
    subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
    overlay=True,
    opacity=.66,
    transparent=True,
    control=True,
).add_to(m)

#########
#########
sentinel1 = ee.ImageCollection('COPERNICUS/S1_GRD') \
    .filterBounds(ee.Geometry.Point(lng,lat))
vh = sentinel1 \
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH')) \
  .filter(ee.Filter.eq('instrumentMode', 'IW'))
vhAscending = vh.filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))
vhDescending = vh.filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))
composite = ee.Image.cat([
  vhAscending.select('VH').mean(),
  ee.ImageCollection(vhAscending.select('VV').merge(vhDescending.select('VV'))).mean(),
  vhDescending.select('VH').mean()
]).focal_median()
m.setCenter(lng, lat, zoom)
m.addLayer(composite, {'min':[-25, -20, -25], 'max': [0, 10, 0]}, 'composite')
################
##################
#########





folium.raster_layers.TileLayer(
    tiles='http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='google',
    name='google maps',
    max_zoom=22,
    subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
    opacity = .5,
    transparent=True,
    overlay=True,
    control=True,
).add_to(m)

folium.raster_layers.WmsTileLayer(
    url='http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi',
    name='Weather-IEM Nexrad',
    fmt='image/png',
    layers='nexrad-n0r-900913',
    attr='Weather Nexrad',
    transparent=True,
    overlay=True,
    control=True,
).add_to(m)
folium.raster_layers.WmsTileLayer(
    url='https://mesonet.agron.iastate.edu/cgi-bin/wms/us/wwa.cgi?',
    name='Weather Warnings',
    fmt='image/png',
    layers='',
    attr='Weatherl',
    transparent=True,
    overlay=True,
    control=True,
).add_to(m)
folium.raster_layers.WmsTileLayer(
    url='https://mesonet.agron.iastate.edu/cgi-bin/wms/us/mrms_nn.cgi?',
    name='Weather - 72 hr rainfall',
    fmt='image/png',
    layers='mrms_p72h',
    attr='Weather Iowa State',
    transparent=True,
    overlay=True,
    control=True,
).add_to(m)
folium.raster_layers.WmsTileLayer(
    url='https://mesonet.agron.iastate.edu/cgi-bin/wms/goes_west.cgi?',
    name='Goes West',
    fmt='image/png',
    layers='sector_chchannel ie hawaii_ch02',
    attr='noaa',
    transparent=True,
    overlay=True,
    control=True,
).add_to(m)

#########
#########
#########
##################
dataset = ee.ImageCollection('COPERNICUS/S2').filterDate(time1,time2).filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
rgb = dataset.select(['B4','B3','B2']).median()
##################
##################
##################
def add_ee_layer(self, ee_image_object, vis_params, name):
  map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
  folium.raster_layers.TileLayer(
    tiles = map_id_dict['tile_fetcher'].url_format,
    attr = "Google Earth Engine",
    name = 'COPERNICUS/S2',
opacity=.8,
overlay=True,
    control = True,
transparent=True,
  ).add_to(self)
folium.Map.add_ee_layer = add_ee_layer
dem = ee.Image(rgb)
vis_params = {'bands':['B4','B3','B2'], 'min':0.0,'max':10000.0,}
m.add_ee_layer(dem.updateMask(dem.gt(0)), vis_params, 'DEM')
##################
##################
#########
#########
################
dataset = ee.ImageCollection('COPERNICUS/S3/OLCI').filterDate(time1,time2)
rgb = dataset.select(['Oa08_radiance', 'Oa06_radiance', 'Oa04_radiance']).median().multiply(ee.Image([0.00876539, 0.0123538, 0.0115198]))
###############
###############
def add_ee_layer(self, ee_image_object, vis_params, name):
  map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
  folium.raster_layers.TileLayer(
    tiles = map_id_dict['tile_fetcher'].url_format,
    attr = "Google Earth Engine",
    name = 'COPERNICUS/S3/OLCI',
    control = True,
    transparent=True,
   overlay=True,
opacity= .55,
  ).add_to(self)
folium.Map.add_ee_layer = add_ee_layer
dem = rgb
vis_params = {'min': 0, 'max': 6, 'gamma': 1.5,}
m.add_ee_layer(dem.updateMask(dem.gt(0)), vis_params, 'DEM')
##################




##################
##################
folium.LayerControl().add_to(m)

outHtml = '/var/www/map.html' # temporary file path, change if needed
m.save(outHtml)
print ('''<section>
<div id="container">
<iframe id="embed" scrolling="no" src="/map.html"></iframe>
</div>
</section>
</div></div></div>''')



