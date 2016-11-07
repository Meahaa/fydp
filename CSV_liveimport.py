import pandas as pd

HR_array = []
temp_array = []
new_array = []
delta_HR = []
trend_HR = []
flag = False

heartrate = pd.read_csv('/Users/eadickison/Documents/Processing/HeatExaustionProcessing/test2.csv')
#sensor_data = heartrate['sensor1']
#split_data = sensor_data.apply(lambda x: pd.Series(x.split(',')))
HR_array = heartrate['sensor1']
temp_array = heartrate['sensor2']
i = 0
print(HR_array)
for heart in HR_array:
    HR1 = HR_array[i]
    HR2 = HR_array[i+1]
    delta_HR = HR2-HR1
    print (delta_HR)
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
        if (i>=1):
            if trend_HR[i]>trend_HR[i-1] and trend_HR[i]>0:
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
