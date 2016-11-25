import numpy as np

HR_array = []
temp_array = []
new_array = []
delta_HR = []
trend_HR = []
flag = False
i =0

while True:
    data = np.genfromtxt('/Users/eadickison/Documents/Processing/HeatExaustionProcessing/test32.csv', delimiter = ',')
    print(data[i])
    print (i)
    i= i+1