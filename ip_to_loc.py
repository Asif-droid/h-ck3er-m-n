import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
# from geopy.distance import distance
print("ok")

def ip_details(ip):
    try:
        response = DbIpCity.get(ip, api_key='free')
        print("ok")
        print("response", response)
        return response
    except Exception as e:
        return e

def url_to_Ip(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except Exception as e:
        return e

ip_details(url_to_Ip("www.timesofisrael.com"))