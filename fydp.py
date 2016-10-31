import json
import random
import pyowm
import math
from pprint import pprint
owm = pyowm.OWM('e6bfa133d68b3b9cf9547e4b7bf7f35d')

def round_up_to_even(f):
    return math.ceil(f / 2.) * 2

def round_up_to_five(x):
    return int(math.ceil(x / 5.0)) * 5

with open('data.json') as datafile:
  data = json.load(datafile)
  height = data["height"]
  weight = data["weight"]
  gender = data["gender"]
  bmi = float(weight) / (float(height)*float(height))

  observation = owm.weather_at_place('Waterloo,CA')
  w = observation.get_weather()

  h = w.get_humidity()
  t = w.get_temperature('fahrenheit')

  print "humdity: ", h

  humidity = round_up_to_five(h)
  print "rounded humidity: ", humidity

  air_temp = t['temp']
  print "air temperature: ", air_temp

  air_temp = round_up_to_even(air_temp)
  print "rounded aid temperature: ", air_temp

  body_temp = random.uniform(36.5, 41)
  print "body temperature: ", body_temp
  heart_rate = random.randint(80, 220)
  print "heart rate: ", heart_rate

  dehyd = 0
  dehyd_heart_rate = 0
  dehyd_body_temp = 0

  d = {}
  # temp: {humidity: Heat index}
  d = {110 : {40:136}, 108 : { 40:130, 45:137 }, 106 : { 40:124, 45:130, 50:137}, 104 : { 40:119, 45:124, 50:131, 55:137}, 102 : { 40:114, 45:114, 50:124, 55:130, 60:137}, 100 : { 40:109, 45:114, 50:118, 55:124, 60:129, 65:136 }, 98 : { 40:105, 45:109, 50:113, 55:117, 60:123, 65:128, 70:134} }
  
  print d[110][40]


  if body_temp > 40.5:
    print "warning: Heat stroke. Cease activity immediately."

  #low BMI
  if bmi < 25: 
    print "Normal BMI level"

    if body_temp > 39: 
      print "warning: Heat Exhaustion due to high body temperature"

    if heart_rate > 200:
      print "Warning: Heat Exhaustion due to high heart rate"

  #Medium BMI
  if bmi > 25 and bmi < 30:
    print "Overweight BMI level"

    if body_temp > 38.5: 
      print "warning: Heat Exhaustion due to high body temperature"

    if heart_rate > 190:
      print "Warning: Heat Exhaustion due to high heart rate"

  #High BMI
  if bmi > 29.9:
    print "Obese BMI level"

    if body_temp > 37: 
      print "warning: Heat Exhaustion due to high body temperature"

    if heart_rate > 180:
      print "Warning: Heat Exhaustion due to high heart rate"