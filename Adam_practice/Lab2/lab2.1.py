import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import lagrange

xx = np.array([1,2,3,4,5,6,7])

matr = np.array([[6,7,15,15,13,18,17],
[8,8,14,17,7,13,17],
[5,6,10,14,10,17,22],
[10,10,13,16,9,13,25],
[9,9,11,12,7,19,24],
[5,10,12,15,6,19,22],
[8,9,12,14,7,16,16],
[7,8,11,16,7,18,19],
[6,10,15,17,8,13,24],
[5,6,12,17,6,19,21],
[10,10,11,14,7,15,15],
[9,7,15,14,6,13,21],
[7,8,11,14,10,16,16],
[5,9,9,15,8,17,23],
[7,7,12,14,8,19,19],
[9,6,14,15,9,18,23],
[6,8,11,12,7,20,20],
[8,6,10,17,7,17,16],
[8,7,10,13,9,17,22]])


def func(x,a,b):
    return a*np.log10(x)+b

def solve(x, matrix):
    y_means = np.mean(matrix, axis=0)
    stand_deviation = np.std(matrix, axis=0)
    popt, pcov = curve_fit(func, x, y_means)
    poly = lagrange(x, y_means)

    plt.figure(figsize=(8,6))
    plt.errorbar(x, y_means, yerr=stand_deviation, fmt='o', label='data')
    plt.plot(x, poly(x),'r-', label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
    plt.xlabel('Время на самостоятельную работу')
    plt.ylabel('Баллы успеваемости')
    plt.legend()
    plt.show()

    return [print(f'{poly[i]}x^{i+1} +', end=' ') for i in range(len(poly))]



solve(xx,matr)
