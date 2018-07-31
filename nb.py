import numpy as np
from MPU9250 import MPU9250
from BMP280 import BMP280

m = MPU9250()

b = BMP280()

avg_x_accel = lambda x: np.array([list(m.readAccel().values()) for _ in range(x)]).mean(axis=0)

x = np.sum(avg_x_accel(100) - avg_x_accel(100))
print(x)
