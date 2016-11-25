import json
import pyowm
import math
import serial
import colorama as c
from colorama import Fore, Back, Style

#API Key fro Weather Data
ser = serial.Serial('/dev/cu.usbmodem1411', 115200)
owm = pyowm.OWM('e6bfa133d68b3b9cf9547e4b7bf7f35d')
data = []
data_split = []
HR_array = []
temp_array = []
new_array = []
delta_temp = []
delta_HR = []
core_temp = []
new_HR = []

c.init()

#flag to indicate yes or no heat exhaustion
flag = False

#counter to advance index of HR and temp arrays
i=0
k=0

#used to round the temperature so it can be found in table
def round_up_to_even(f):
    return math.ceil(f / 2.) * 2

#used to round the humidity so it can be found in table
def round_up_to_five(x):
    return int(math.ceil(x / 5.0)) * 5

#reading in file for user supplied variables
with open('data.json') as datafile:
  data = json.load(datafile)
  height = data["height"]
  weight = data["weight"]
  gender = data["gender"]
  bmi = (float(weight) / (float(height)*float(height)))

  #set location for weather data and request data
  observation = owm.weather_at_place('Waterloo,CA')
  w = observation.get_weather()

  #identify humidity and temperature values
  h = w.get_humidity()
  t = w.get_temperature('fahrenheit')
  air_temp = t['temp']

  #found humidity so it can be found in the table
  humidity = round_up_to_five(h)
  print Style.BRIGHT + "rounded humidity: "+ Style.RESET_ALL + Fore.BLUE + str(humidity) + Style.RESET_ALL

  #round air temperature so it can be found in table
  air_temp = round_up_to_even(air_temp)
  print Style.BRIGHT + "rounded air temperature: "+ Style.RESET_ALL + Fore.BLUE + str(air_temp)+ Style.RESET_ALL

  d = {}
  # temp: {humidity: Heat index}
  d = {
        110 : {40:136}, 
        108 : { 40:130, 45:137},
        106 : { 40:124, 45:130, 50:137}, 
        104 : { 40:119, 45:124, 50:131, 55:137}, 
        102 : { 40:114, 45:114, 50:124, 55:130, 60:137}, 
        100 : { 40:109, 45:114, 50:118, 55:124, 60:129, 65:136 }, 
        98 : { 40:105, 45:109, 50:113, 55:117, 60:123, 65:128, 70:134}, 
        96 : { 40:101, 45:104, 50:108, 55:112, 60:116, 64:121, 70:128, 75:132 },
        94 : {40:97, 45:100, 50:102, 55:106, 60:110, 65:114, 70:119, 75:124, 80:129, 85:135},
        92 : { 40:94, 45:96, 50:99, 55:101, 60:105, 65:108, 70:112, 75:116, 80:121, 85:126, 90: 131},
        90 : { 40:91, 45:93, 50:95, 55:97, 60:100, 65:103, 70:106, 75:109, 80:113, 85:117, 90:122, 95:127, 100:132},
        88 : { 40:88, 45:89, 50:91, 55:93, 60:95, 65:98, 70:100, 75:100, 80:106, 85:110, 90:113, 95:117, 100:121},
        86 : { 40:85, 45:87, 50:88, 55:89, 60:91, 65:93, 70:95, 75:97, 80:100, 85:102, 90:105, 95:108, 100:12},
        84 : { 40:83, 45:84, 50:85, 55:86, 60:88, 65:89, 70:90, 75:92, 80:94, 85:96, 90:98, 95:100, 100:103 },
        82 : { 40:81, 45:82, 50:85, 55:84, 60:84, 65:85, 70:86, 75:88, 80:89, 85:90, 90:91, 95:93, 100:95},
      }

  if air_temp in d and humidity in d[air_temp]:
    heat_index = d[air_temp][humidity]

    #critical heat index
    if heat_index >= 130:
      print Style.BRIGHT + Fore.RED + "Extreme Danger: Heat Stroke and heat exhaustion very likely" + Style.RESET_ALL
    elif heat_index < 130 and heat_index >= 104:
      print "Danger: Heat Exhaustion likely"
    elif heat_index < 104 and heat_index >= 93:
      print "Extreme Caution: Heat Exhaustion possible"
    elif heat_index < 93:
      print "Caution: No critical danger due to heat"

  else:
    print 'Caution: No critical danger due to heat'

  while True:
    data = ser.readline()
    data_split=data.rsplit(",")
    HR_array.append(data_split[0])
    temp_array.append(data_split[1])
    temp_array = map(float, temp_array)
    HR_array = map(float, HR_array)
    heart = HR_array[i]
    body_temp = temp_array[i]
    core_temp.append(body_temp+2)
    core = core_temp[i]
    if (i>0):
        j = i-1
        temp_minus = core_temp[j]
        delta_temp.append(core-temp_minus)
        if (heart != 0):
            new_HR.append(heart)
            if(k>0):
                HR_minus = new_HR[k-1]
                delta_HR.append(new_HR[k]-HR_minus)
                print("HR Delta:"+ str(delta_HR[k-1]))
                if (delta_HR[k-1]>0):
                    print(Style.BRIGHT + Fore.MAGENTA + "INCREASING" + Style.RESET_ALL)
            k = k+1
        print "Temperature Delta:", delta_temp[j]
    print "HR:", heart
    print "Core Temperature:", core
    if bmi <25:
        print("Normal BMI level")
        if (i >0):
            if (heart != 0):
                over_HR = new_HR[k-1]-new_HR[0]
                over_temp = delta_temp[i-1]-delta_temp[0]
                dehydration = ((1/3)*over_HR)+(5*over_temp)
                print Style.BRIGHT + "Dehydration:"+ str(round(dehydration,3))+ Style.RESET_ALL
        if (i < 1):
            dehydration=0
        if body_temp > 39 and body_temp < 40.5:
            print(Style.BRIGHT + Fore.YELLOW + "Warning: Heat Exhaustion due to high body temperature"+ Style.RESET_ALL)
            flag = True
        if heart > 200:
            print(Style.BRIGHT + Fore.YELLOW + "Warning: Heat Exhaustion due to high heart rate"+ Style.RESET_ALL)
            flag = True
        if dehydration >6:
            print(Style.BRIGHT + Fore.YELLOW + "Warning: Heat Exhaustion due to dehydration"+ Style.RESET_ALL)
    if bmi > 25 and bmi < 30:
            print("Overweight BMI level")
            if body_temp > 38.5 and body_temp < 40.5:
                print(Style.BRIGHT + Fore.YELLOW + "Warning: Heat Exhaustion due to high body temperature"+ Style.RESET_ALL)
                flag = True
            if heart > 190:
                print(Style.BRIGHT + Fore.YELLOW + "Warning: Heat Exhaustion due to high heart rate"+ Style.RESET_ALL)
                flag = True
    if bmi >= 30:
            print("Obese BMI level")
            if body_temp > 37 and body_temp < 40.5:
                print(Style.BRIGHT + Fore.YELLOW + "Warning: Heat Exhaustion due to high body temperature"+ Style.RESET_ALL)
                flag = True
            if heart > 180:
                print(Style.BRIGHT + Fore.YELLOW + "Warning: Heat Exhaustion due to high heart rate"+ Style.RESET_ALL)
                flag = True
    if flag != True:
               print(Style.BRIGHT + Fore.GREEN + "Player stable" + Style.RESET_ALL)
    if body_temp >= 40.5:
            print (Style.BRIGHT + Fore.RED +"Warning: Heat Stroke. Cease activity immediately."+ Style.RESET_ALL)
    i = i+1








