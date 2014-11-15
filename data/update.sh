#!/bin/bash
rm *.dat
wget -q http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
wget -q http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
wget -q http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz

gunzip *.gz

echo "Databases updated successfully!"
