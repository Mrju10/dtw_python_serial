import numpy as np
from scipy.spatial.distance import euclidean
import pyttsx3
import time
engine = pyttsx3.init()
engine.setProperty("rate", 220)

from fastdtw import fastdtw

x1 = np.fromfile('test1.dat', dtype=int)
x2 = np.fromfile('auxiliar1.dat', dtype=int)
y1 = np.fromfile('test2.dat', dtype=int)
y2 = np.fromfile('auxiliar1.dat', dtype=int)
distance, path = fastdtw(x1, x2, dist=euclidean)
distance2, path = fastdtw(y1, y2, dist=euclidean)
print("Distance X", distance)
print("Distance Y", distance2)

if distance <= 30340.0:
    engine.say("Hola Mundo")
    engine.runAndWait()