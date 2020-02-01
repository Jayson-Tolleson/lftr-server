

#!/usr/bin/env python3
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
vid='/var/www/movie/movie.mp4'
video = cv2.VideoCapture(vid)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():


    """Video streaming generator function."""
    while(video.isOpened()):
        rval, frame = video.read()
        if rval:
            video.set(3, 1080)
            video.set(4, 720)


            cv2.imwrite('t.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')
        else:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)





@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, ssl_context=('/var/security/lftr.biz.crt', '/var/security/lftr.biz.key'), port=8000, threaded=True)
