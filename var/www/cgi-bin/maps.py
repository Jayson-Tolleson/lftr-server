#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
cgitb.enable()

import cgi

#html in python
print ('''Content-Type: text/html''') # HTML is following print 
print


print ('''<html><head>








  <title>J^2</title>
  <meta name="description" content="=100jay" />
  <meta name="keywords" content="Music, Art, Forum" />
  <meta http-equiv="content-type" content="text/html" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<style>
body {background: #1339de;}
</style>
<body>
  <div id="main">
    <div id="site_content">
      <div id="content">

<h1>hello map</h1>
<script></script>
<form>
input latitude: <input type = "number" name = "lat" value = "34">  <br />
input longitude: <input type = "number" name = "lng" value = "-118"> <br />
input zoom (0-22): <input type = "number" name = "zoom" value = "6"> <br />
input opacity (0-.5-1): <input type = "number" name = "opacity" value = ".5"> <br />
<button onclick="getLocation()">
<input type = "submit" value = "Submit" />
Try It</button>
</form>
''')


form = cgi.FieldStorage()
lat = form.getvalue("lat",34)
lng = form.getvalue("lng",-118)
zoom = form.getvalue("zoom",6)
opacity = form.getvalue("opacity",.44)

print (lat)
print (lng)
print (zoom)
print (opacity)
print
print (form)
print ('''
<html>

<head>
  <title>GIBS Google Example - Web Mercator (EPSG:3857)</title>

  <!-- Obtain your own API key at:
             https://code.google.com/apis/console -->
  <script type='text/javascript' src='https://maps.googleapis.com/maps/api/js?key=AIzaSyCEseay7iJ7jf8lnvZyz9rii6q4szW9Crk'>
  </script>''')


print ('''
  <script>
let lat='{0}';
let lng='{1}';
let zoom='{2}';
let opacity='{3}';
  </script>'''.format(lat,lng,zoom,opacity))

print ('''
  <script>
window.onload = function () {
  var mapOptions = {
    center:new google.maps.LatLng(lat,lng),
zoom: 6,
    maxZoom: 22
  };

  var map = new google.maps.Map(document.getElementById('map'), mapOptions);

  var getTileUrl = function (tile, zoom) {
    return '//gibs.earthdata.nasa.gov/wmts/epsg3857/best/' +
      'MODIS_Terra_Aerosol/default/Current/' +
      'GoogleMapsCompatible_Level16/' +
      zoom + '/' + tile.y + '/' +
      tile.x + '.png';

  };

  var layerOptions = {
    alt: 'MODIS_Terra_Aerosol',
    getTileUrl: getTileUrl,
    maxZoom: 16,
    minZoom: 1,
    name: 'MODIS_Terra_Aerosol',
    tileSize: new google.maps.Size(1024, 1024),
    opacity: opacity
  };

  var imageMapType = new google.maps.ImageMapType(layerOptions);
  map.overlayMapTypes.insertAt(0, imageMapType);
};
</script>
</head>
<style>
#map {
  background-color: #000;
  top: 150;
  left: 150;
  width: 80%;
  height: 80%;
}




</style>

<body>
  <div id='map'></div>
</body>

</html>


</body>
</div></div>
    <div id="content_footer"></div></html>''')

