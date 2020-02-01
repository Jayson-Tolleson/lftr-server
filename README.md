# lftr-server : webrtc-broadcast and cgi development(python3)
my current python cgi devel environment
filesystem in var

## obtain a copy:

cd

sudo git clone https://github.com/Jayson-Tolleson/lftr-server.git

cd lftr-server/www && sudo cp -r security /var && sudo cp -r www /var

## start server

cd

sudo nohup python3 /var/www/webserver3.py &

sudo nohup python3 /var/www/opencvvideostreamer.py &

## filesystem
var

--security

----key

----cert

--www

----webserver3.py #port 443

----index.html

----record.html

----index2.html (space)

----js (space js)

----vids (for archivemovie.py)

----vidsint (for archivemovie.py)

----movie (for archivemovie.py and opencvvideostreamer)

----opencvvideosrtreamer #port 8000

------index.html

------server.py

------templates

--------index.html

----cgi-bin

------broadcast-record.py

------broadcast-record2.py

------maps.py

------archivemovie.py

------hello.py

------screen.py

--------testing

----------android-gps-tracker-map.py (gps server)

----------android-gps-signalling.py (gps client for android phone)

----------opencvbroadcast.py
