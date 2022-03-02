import matplotlib.pyplot as plt
import serial 
import time, json
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial()
ser.baudrate = 11500
ser.port = 'COM6'
ser.open()
i=1
y1 = []
while i < 50:
    microbitdata = str(ser.readline())
    temperature = microbitdata[2:]
    temperature = temperature.replace("  ", "")
    temperature = temperature.replace("'", "")
    temperature = temperature.replace("\\r\\n", "")
    temperature = temperature.replace("\\r", "")
    temperature = temperature.replace("\\n", "")
    print(temperature)
    y1.append(temperature)
    i +=1

y1.remove(y1[0])
y1.insert(0, '0')

y1 = list(map(int, y1))
print(y1)
a = np.linspace(0,20,49)

# #y1 is the data
plt.plot(a, y1, 'g-o', linewidth = 1) #Graph with data
plt.xlabel("Tiempo (s)", fontsize = 20)
plt.ylabel("Movimiento", fontsize = 24, color = 'blue')
plt.text(5, 7, "Más texto", fontsize = 12)
plt.title("Aceleracion", fontsize = 20)
plt.legend( ('Etiqueta1', 'Etiqueta2', 'Etiqueta3'), loc = 'upper left')
 
plt.grid(True)
plt.savefig('figura3.png', dpi = 300) #guarda la gráfica con 300dpi (puntos por pulgada)
plt.show()

