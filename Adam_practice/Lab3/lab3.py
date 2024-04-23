import numpy as np
import matplotlib.pyplot as plt

def linear_regression(x, y):
    try:
        b = (len(x) * np.sum(x * y) - np.sum(x) * np.sum(y)) / (len(x) * np.sum(x ** 2) - (np.sum(x)) ** 2)
        a = (np.sum(y) - b * np.sum(x)) / len(x)
        return b, a
    except Exception as e:
        print(f"Shit happens:( , error: {e}")

def power_regression(x,y):
    try:
        matrix = np.array([[len(x), np.sum(np.log(x))], [np.sum(np.log(x)), np.sum(np.log(x)**2)]])
        vect = np.array([[np.sum(np.log(y))], [np.sum(np.log(x) * np.log(y))]])
        inv = np.linalg.inv(matrix)
        coef = np.dot(inv, vect)
        return np.e ** coef[0, 0], coef[1, 0]
    except Exception as e:
        print(f'Shit happens, your shit now is {e}')

def poly_regression(x,y):
    try:
        matrix1 = np.array([[np.sum(x ** 4), np.sum(x ** 3), np.sum(x ** 2)],
                            [np.sum(x ** 3), np.sum(x ** 2), np.sum(x)],
                            [np.sum(x ** 2), np.sum(x), len(x)]], dtype=np.float64)

        matrix2 = np.array([[np.sum(x ** 2 * y)], [np.sum(x * y)], [np.sum(y)]], dtype=np.float64)

        inv_mat = np.linalg.inv(matrix1)

        coef = np.dot(inv_mat, matrix2)
        return coef[0, 0], coef[1, 0], coef[2, 0]
    except Exception as e:
        print(f'Oh no, exception! Shit. Your error is {e}')

def exp_regression(x, y):
    try:
        matrix = np.array([[np.sum(x**2), np.sum(x)], [np.sum(x), len(x)]])
        vect = np.array([[np.sum(np.log(y) * x)], [np.sum(np.log(y))]])
        inv = np.linalg.inv(matrix)
        coef = np.dot(inv, vect)
        return coef[0, 0], np.e ** coef[1, 0]
    except Exception as e:
        print(f'Shit happens, your shit now is {e}')




def plot_regression(x, y, reg):
    x_plot = np.linspace(min(x), max(x), 1000)
    a = 0
    b = 0
    c = 0
    S = 0
    y_plot = 0
    if reg == 'linear':
        a, b = linear_regression(x, y)
        y_plot = a * x_plot + b
        S = np.sum((a * x + b - y) ** 2)
    elif reg == 'poly':
        a, b, c = poly_regression(x, y)
        y_plot = a * x_plot**2 + b * x_plot + c
        S = np.sum((a * x**2 + b*x + c - y) ** 2)
    elif reg == 'power':
        a, b = power_regression(x, y)
        y_plot = a * x_plot**b
        S = np.sum((a * x**b - y) ** 2)
    elif reg == 'exp':
        a, b = exp_regression(x, y)
        y_plot = b * (np.e)**(a * x_plot)
        S = np.sum((b * (np.e)**(a*x) - y) ** 2)



    plt.plot(x_plot, y_plot, label=f"{reg} regression")
    plt.scatter(x, y, color='red', marker='o', label='Точки')
    plt.title(f"{reg} reg for coefs {a:.3f}, {b:.3f}, {c:.3f}"
              f" square error: {S:.3f}.")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    return S


def plot_all(x,y):
    reg = ['linear', 'poly', 'exp', 'power']
    Smax = []
    for i in reg:
       Smax.append(plot_regression(x, y, i))
    print (f'{reg[Smax.index(max(Smax))]} is optimal regression')

