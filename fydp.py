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
  print body_temp
  heart_rate = random.randint(80, 220)

  if body_temp > 37: #and bmi > 25: 
    print "warning: Heat Exhaustion!"

  if body_temp > 40.5:
    print "warning: Heat stroke. Cease activity immediately."

  if heart_rate > 200:
    print "hey"