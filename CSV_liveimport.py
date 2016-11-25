import pandas as pd
import time

HR_array = []
temp_array = []
new_array = []
delta_HR = []
trend_HR = []
flag = False
i =0

data = pd.read_csv('/Users/eadickison/Documents/Processing/HeatExaustionProcessing/test30.csv')
HR_array = data['sensor1']
temp_array = data['sensor2']
while True:
    time.sleep(5)
    body_temp = temp_array[i]
    heart = HR_array[i]
    print ("body temperature: ", temp_array[i])
    print ("i is:", i)
    bmi = 24
    if bmi < 25:
        print("Normal BMI level")
        if body_temp > 39 and body_temp < 40.5:
            print("Warning: Heat Exhaustion due to high body temperature")
            flag = True
        if heart > 200:
            print("Warning: Heat Exhaustion due to high heart rate")
            flag = True
        if flag != True:
            print("Player stable")
    if bmi > 25 and bmi < 30:
        print("Overweight BMI level")
        if body_temp > 38.5 and body_temp < 40.5:
            print("Warning: Heat Exhaustion due to high body temperature")
            flag = True
        if heart > 190:
            print("Warning: Heat Exhaustion due to high heart rate")
            flag = True
        if flag != True:
            print("Player stable")
    if bmi > 29.9:
        print("Obese BMI level")
        if body_temp > 37 and body_temp < 40.5:
            print("warning: Heat Exhaustion due to high body temperature")
            flag = True
        if heart > 180:
            print("Warning: Heat Exhaustion due to high heart rate")
            flag = True
        if flag != True:
            print("Player stable")
    i = i+1
    j = i+1
    test = HR_array.size
    print(test)
    if j >= test:
        print ("loading")
        time.sleep(5)