from Sem2324.Adam_practice.Lab3 import lab3
import numpy as np

x_val = np.array([1,16,13,46,61,76])
y_val = np.array([0.5, 4, 6.9, 8.8, 10.9, 12.1])


lab3.plot_regression(x_val, y_val, 'linear')
lab3.plot_all(x_val, y_val)

