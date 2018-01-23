import time
import json
import requests
import random

api_key = "ecf0dcdfc655c8033a567fc40a459a09"
google_key = "AIzaSyBkNN_dpfx2AYXHst_gGCImejSk5Y5AVbA"
seattle = 5809844
minneapolis = 5037649
seattle_data = ""
hottest = ""
coldest = ""
windiest = ""
closest = ""
closest_hottest = ""
origin = ""
cold_count = 0
most_common = {}

############################################################################################

def tempf(data):
	return data["main"]["temp"] * 1.8 - 459.67
def tempf_str(data):
	return str(data["main"]["temp"] * 1.8 - 459.67)
def name(data):
	return unicode(data["name"])
def weather(data):
	return data["weather"][0]["description"]

def cur_summary(data):
	print "You are currently located in " + name(data) + ". It is currently " + tempf_str(data) + " degrees in " + name(data) + "."
	time.sleep(1)
	print "The weather in " + name(data) + " is " + weather(data) + "."
	time.sleep(1)
	print "Lets find you somewhere warmer"

def print_summary(data):
	a = "In " + name(data) + " it is " + tempf_str(data) + " degrees. "
	#b = "The windspeed is " + str(data["wind"]["speed"]) + "."
	c = "The weather is " + weather(data)
	print a
	time.sleep(.75)
	print c
	time.sleep(.75)

def print_hottest(data):
	global hottest
	global cold_count
	if tempf(data) > tempf(origin):
		print name(data) + " is warmer than " + name(origin) + "!"
		time.sleep(.75)
		(d,t) = calculate_distance(origin,data)
		print name(data) + "is " + d + " away. It would take " + t + " to drive there."
		time.sleep(.75)
	else:
		cold_count += 1
	if tempf(data) > tempf(hottest):
		print name(data) + " is the warmest city! Warmer than " + name(hottest)
		time.sleep(.75)
		hottest = data
	else:
		print name(hottest) + " is still the warmest city so far at " + tempf_str(hottest) + " degrees."
		if cold_count > 5:
			print "Be grateful though; There are " + str(cold_count) + " cities colder than you!"

"""
def print_coldest(data):
	global coldest
	if data["main"]["temp"] < coldest["main"]["temp"]:
		print name(data) + " is the coldest city at " + str(convertF(coldest["main"]["temp"])) + " degrees! Colder than " + name(coldest)
		coldest = data
	else:
		print name(coldest) + " is the coldest city so far at " + str(convertF(coldest["main"]["temp"])) + " degrees."
"""

def print_windiest(data):
	pass
def print_most_common(data):
	pass

def calculate_distance(origin,destination):
	olat=str(origin["coord"]["lat"])
	olong=str(origin["coord"]["lon"])
	dlat=str(destination["coord"]["lat"])
	dlong=str(destination["coord"]["lon"])
	r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins="+olat+","+olong+"&destinations="+dlat+","+dlong+"&key="+google_key)
	r.text
	gdata = json.loads(r.text)
	#print gdata
	distance = gdata["rows"][0]["elements"][0]["distance"]["text"]
	time = gdata["rows"][0]["elements"][0]["duration"]["text"]

	return(distance,time)
############################################################################################
"""r = requests.get("http://api.openweathermap.org/data/2.5/weather?id="+str(seattle)+"&appid=" + api_key)
r.text
s = json.loads(r.text)
r = requests.get("http://api.openweathermap.org/data/2.5/weather?id="+str(minneapolis)+"&appid=" + api_key)
r.text
m = json.loads(r.text)
calculate_distance(s,m)"""


##################################
f = open("city.list.csv","r")

city_list=[]

for line in f:
	line = line[:len(line)-1]
	line = line.split(",")
	if line[0] == "US":
		city_list.append(line)

f.close

r = requests.get("http://api.openweathermap.org/data/2.5/weather?id="+str(seattle)+"&appid=" + api_key)
r.text
data = json.loads(r.text)
origin = data
hottest = data
coldest = data
windiest = data

cur_summary(data)
time.sleep(1)
while True:
	id = random.choice(city_list)[1]
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?id="+str(id)+"&appid=" + api_key)
	r.text
	data = json.loads(r.text)
	print_summary(data)
	print_hottest(data)
	time.sleep(.5)	
	#print_coldest(data)
	#time.sleep(.5)
