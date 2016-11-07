import serial
import numpy as np
import csv

ser = serial.Serial("/dev/cu.usbmodem1411", 115200)
PS_array = []
PS_split = []
HR_array = []
HR_diff = []
temp_array = np.array([])
new_array = []

while True:
    PS_array = ser.readline()
    print(PS_array)
    PS_split=PS_array.rsplit(",")
    print(PS_split)
    for item in PS_split:
        new_array.append(item)
    HR_array = new_array[::2]
    temp_array = new_array[1::2] #list comprehension
    temp_array = [x.replace("\r\n","")for x in temp_array]
    fields = ['HR', 'Temp']
    with open(r'./HR.csv', 'a') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(HR_array, temp_array)


