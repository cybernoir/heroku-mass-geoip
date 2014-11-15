heroku-mass-geoip
=================

GeoIP lookup utility for heroku. Powered by Flask and Jinja.

![Screenshot](https://i.imgur.com/HeZLL5V.png)

**Installation:**

- git clone
- cd to data folder and run update.sh
- install pip requirements 
- run "gunicorn lookup:app"

Have one API function - /json/<ip>. You can get info about some address by running something like "curl http://your-site.com/json/127.0.0.1".
