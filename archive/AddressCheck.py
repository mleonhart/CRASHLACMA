from pygeocoder import Geocoder
from math import *

//Make sure to "pip install pygeocoder" prior to running this script.

results = Geocoder.geocode("7th and Figueroa")

if results.count == 1:
	print "The information entered gives the following address, please check if this is correct."
	latDif = results[0].latitude - 34.0522
	longDif = results[0].longitude + 118.2437
	if sqrt(latDif**2 + longDif**2) < 0.3 or results[0].city == "Los Angeles":
		print "The location: ", results[0], " is in the LA area"

if results.count > 1:
	print "There are multiple locations with this address, please enter additional information."
	print "The information entered gives the following addresses, please check this list and reenter your address."
	i = 0
	for i in range(0,results.count):
		latDif = results[i].latitude - 34.0522
		longDif = results[i].longitude + 118.2437
		print results[i].city
		if sqrt(latDif**2 + longDif**2) < 0.3  or results[0].city == "Los Angeles":
			print "The location: ", results[i], " is in the LA area"

if results.count < 1: print "No location matches this address, please enter a new address."
