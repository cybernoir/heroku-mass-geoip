#!/usr/bin/python
import pygeoip
import re
import sys
import json
from flask import Flask
from flask import request
from flask import render_template

def get_info(ip_list):
    info = []
    if len(ip_list) > 500: return info
    for ip in ip_list:
        """Very basic validation check lol, need to be updated"""
        ip = ip.strip()
        try:
            country_name = country.country_name_by_addr(ip)
        except:
            country_name = "None"

        try:
            city_name = city.record_by_addr(ip)["city"]
        except:
            city_name = "None"

        try:
            asn_name = asn.org_by_addr(ip)
        except:
            asn_name = "None"

        if country_name == "": country_name = "None"

        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
            info.append({
                "addr": ip, 
                "country": country_name, 
                "city": city_name, 
                "asn": asn_name
            })
    return info

app = Flask(__name__)

country = pygeoip.GeoIP('data/GeoIP.dat')
city = pygeoip.GeoIP('data/GeoLiteCity.dat')
asn = pygeoip.GeoIP('data/GeoIPASNum.dat')

@app.route("/", methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':
        try:
            ip_list = request.form["ips"].split('\n')
            data = get_info(ip_list)
            return render_template("query_data.html", data=data)
        except:
            return "1"
    else:
        return render_template("index.html")

@app.route("/json/<ip>", methods=['GET'])
def return_json(ip):
    try:
        ip_list = [ip.encode("ascii")]
        data = get_info(ip_list)
        return json.dumps(data) + "\n"
        return u"IP: {0} || Location: {1}, {2} || ASN: {3}\n".format(data[0]["addr"], data[0]["country"], data[0]["city"], data[0]["asn"])
    except:
        return "1"

