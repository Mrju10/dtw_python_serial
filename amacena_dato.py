import matplotlib.pyplot as plt
import serial 
import time, json
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial()
ser.baudrate = 11500
ser.port = 'COM7'
ser.open()
i=0
j=1
y1 = []
y2 = []
y3 = []
m1 = []
m2 = []
cadenax=[]
cadenay=[]
string_list=[]

while j <= 51:
    microbitdata = str(ser.readline())
    data = microbitdata[2:]
    data = data.replace("  ", "")
    data = data.replace("'", "")
    data = data.replace("\\r\\n", "")
    data = data.replace("\\r", "")
    data = data.replace("\\n", "")
    data = data.replace("x", "")
    data = data.replace("y", " ")
    # print(data)
    y1.append(data)
    j +=1
ser.close()
y1.remove(y1[0])


for v in y1:
    # print (v)
    aux = str(v)
    aux = aux.split()
    # aux=list(map(int, aux))
    y2.append(aux)

for v in y2:
    aux1=list(map(int, v))
    y3.append(aux1)

for v in y3:
    for m in v:
        m1.append(m)
        print(m)
    

# y2 =np.array(y2).reshape(1,98)
# y2 = list(map(int, y2))

print(y1)
print(y2)
print(y3)
print(m1)

arr_length = len(m1)
print(arr_length)

par=0
impar=0
for i in range(arr_length):
    if(i%2==0):
        cadenax.append(m1[i])
    else:
        cadenay.append(m1[i])

print(cadenax)
print(cadenay)
cadenax=np.array(cadenax)
cadenay=np.array(cadenay)
cadenax.tofile('test1.dat')
cadenay.tofile('test2.dat')
# for v in y2:
#     m1 = m1.append(v[0])
#     for v2 in v:
#         print(v2)
#         # m1 = m1.append(v2[0])
#         # m2 = m2.append(v2[1])
        