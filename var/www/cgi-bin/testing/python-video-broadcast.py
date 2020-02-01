#!/usr/bin/env python3

import numpy as np
import cv2
from flask import Flask, app, request, render_template, Response

print ('''Content-Type: text/html''')
print
print ('''
<html>
<head>

  <meta name="viewport" content="width=device-width, user-scalable=yes, initial-scale=1, maximum-scale=1">
 
 <meta name="mobile-web-app-capable" content="yes">
'  <meta id="theme-color" name="theme-color" content="#ffffff">
  <base target="_blank">
  <title>getUserMedia</title>
  <link href="//fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet" type="text/css">
  <link rel="stylesheet" href="https://kylemcdonald.github.io/samples/src/css/main.css">
</head>

<body>
  <div id="container">
    <video id="gum-local" playsinline controls="true" autoplay></video>
    <div id="errorMsg"></div>
  </div>
  <script src="https://webrtc.github.io/adapter/adapter-latest.js"></script>
  <script src="https://kylemcdonald.github.io/samples/src/js/common.js"></script>
  <script src="https://kylemcdonald.github.io/samples/src/content/getusermedia/gum/js/main.js"></script>
</body>
</html>
''')

print ('''<html><body>''')
print ('''<script>function pass_values() {var pass_to_python = stream; $.ajax({type:'POST',contentType:'application/json;charset-utf-08',dataType:'json',url:'https://lftr.biz/cgi-bin/test.py/pass_val?value='+pass_to_python ,success:function (data) {var reply=data.reply; if (reply=="success"){return else {alert("some error ocured in session agent")}}});}</script>''')


app = Flask(__name__)

@app.route('/pass_val',methods=['POST'])
def pass_val():
    name=request.args.get('value')
    print('gumcap',name)
    return jsonify({'reply':'success'})
@app.route('/')
def index():
    return ('''<html>
  <head>
    <title>Video Streaming Demonstration</title>
  </head>
  <body>
    <h1>Video Streaming Demonstration</h1>
    <img src='video_feed'>
  </body>
</html>''')

cap = cv2.VideoCapture('/var/www/vidsint/1-0.mp4')
#cap = gumcap

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        cap.set(3, 1080)
        cap.set(4, 720)
        #canny edge detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    def gen():
        cv2.imwrite('t.jpg', hsv)
        yield (b'--hsv\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')
        print ('''<script>let videopython='{0}';</script>'''.format(hsv))
        print ('''var videopython = document.querySelector('videopython');''')
        print ('''<style>videopython {background: #222;margin: 0 0 20px 0;width: 100%;} videopython { object-fit: cover;} @media (min-width: 1000px) {videopython {height: 480px;}}</style><videopython autoplay playsinline></videopython></body></html>''')
        @app.route('/video_feed')
        def video_feed():
            return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=hsv')
        if __name__ == '__main__':
            app.run(host='0.0.0.0', debug=True, ssl_context=('/var/security/lftr.biz.crt', '/var/security/lftr.biz.key'), port=8080, threaded=True)
