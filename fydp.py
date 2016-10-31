import json
import random
from pprint import pprint

with open('data.json') as datafile:
  data = json.load(datafile)
  pprint(data)
  height = data["height"]
  weight = data["weight"]
  gender = data["gender"]
  bmi = float(weight) / (float(height)*float(height))

  body_temp = random.uniform(36.5, 41)
  print "body temperature: ", body_temp
  heart_rate = random.randint(80, 220)
  print "heart rate: ", heart_rate

  dehyd = 0
  dehyd_heart_rate = 0
  dehyd_body_temp = 0

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