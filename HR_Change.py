import serial
import numpy as np

ser = serial.Serial('/dev/cu.usbmodem1421', 115200)
PS_array = []
PS_split = []
HR_array = []
HR_diff = []
trend_HR = []
temp_array = np.array([])
new_array = []
flag = False
i = 0


while True:
    PS_array = ser.readline()
    print(PS_array)
    PS_split=PS_array.rsplit(",")
    print(PS_split)
    for item in PS_split:
        new_array.append(item)
        HR_array = new_array[::2]
        temp_array = new_array[1::2]
        temp_array = [x.replace("\r\n","")for x in temp_array]
        temp_array = map(float, temp_array)
        HR_array = map(float, HR_array)
        heart = HR_array[i]
        body_temp = temp_array[i]
        HR1 = HR_array[i-1]
        HR2 = HR_array[i]
        delta_HR = HR2-HR1
        trend_HR.append(delta_HR)
        if trend_HR[i]>trend_HR[i-1] and trend_HR[i]>0:
            print ("Delta HR is:", delta_HR)
            print ("Warning: Heart Rate Increasing by", delta_HR)
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


