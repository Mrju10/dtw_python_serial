import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

# x1 = np.fromfile('auxiliar1.dat', dtype=int)
# y1 = np.fromfile('auxiliar2.dat', dtype=int)
x1 = np.fromfile('test1.dat', dtype=int)
y1 = np.fromfile('test2.dat', dtype=int)
print(x1)
print(y1)


# #y1 is the data
plt.plot(x1, y1, 'g-o', linewidth = 1) #Graph with data
plt.xlabel("Valores x", fontsize = 20)
plt.ylabel("Valores y", fontsize = 24, color = 'blue')
plt.text(5, 7, "pos", fontsize = 12)
plt.title("Aceleracion", fontsize = 20)
plt.legend( ('Etiqueta1', 'Etiqueta2'), loc = 'upper left')
 
plt.grid(True)
plt.savefig('figura3.png', dpi = 300) #guarda la gráfica con 300dpi (puntos por pulgada)
plt.show()

