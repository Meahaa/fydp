import pandas as pd
import time

HR_array = []
temp_array = []
new_array = []
delta_HR = []
trend_HR = []
flag = False

data = pd.read_csv('/Users/eadickison/Documents/Processing/HeatExaustionProcessing/test24.csv')
#sensor_data = heartrate['sensor1']
#split_data = sensor_data.apply(lambda x: pd.Series(x.split(',')))
HR_array = data['sensor1']
temp_array = data['sensor2']
i = 1
k=0
j=0
for heart in HR_array:
    time.sleep(5)
    HR1 = HR_array[i-1]
    HR2 = HR_array[i]
    delta_HR = HR2-HR1
    trend_HR.append(delta_HR)
    body_temp = temp_array[i]
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
        if (k>=1):
            if trend_HR[k]>trend_HR[k-1] and trend_HR[k]>0:
                print ("Delta HR is:", delta_HR)
                print ("Warning: Heart Rate Increasing by", delta_HR)
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