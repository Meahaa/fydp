import serial

ser = serial.Serial('/dev/cu.usbmodem1421', 115200)
data = []
data_split = []
HR_array = []
HR_diff = []
trend_HR = []
temp_array = []
new_array = []
flag = False
i=0


while True:
    data = ser.readline()
    data_split=data.rsplit(",")
    HR_array.append(data_split[0])
    temp_array.append(data_split[1])
    temp_array = map(float, temp_array)
    HR_array = map(float, HR_array)
    heart = HR_array[i]
    body_temp = temp_array[i]
    print ("HR:", heart)
    print("Temperature:", body_temp)
    if body_temp > 39 and body_temp < 40.5:
        print("Warning: Heat Exhaustion due to high body temperature")
        flag = True
    if body_temp > 40.5:
        print ("Warning: Player in Critical Condition")
    if heart > 200:
        print("Warning: Heat Exhaustion due to high heart rate")
        flag = True
    if flag != True:
        print("Player stable")
    i=i+1