# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np


if __name__ == '__main__':
    # Интервал изменения переменной по оси X
    xmin = -20.0
    xmax = 20.0
    count = 200

    # Создадим список координат по оиси X на отрезке [xmin; xmax]
    x = np.linspace(xmin, xmax, count)

    # Вычислим значение функции в заданных точках
    y = np.sinc(x / np.pi)

    plt.figure(figsize=(8, 8))

    # !!! Две строки, три столбца.
    # !!! Текущая ячейка - 1
    plt.subplot(2, 3, 1)
    plt.plot(x, y)
    plt.title("1")

    # !!! Текущая ячейка - 2
    plt.subplot(2, 3, 2)
    plt.plot(x, y)
    plt.title("2")

    # !!! Текущая ячейка - 3
    plt.subplot(2, 3, 3)
    plt.plot(x, y)
    plt.title("3")

    # !!! Текущая ячейка - 4
    plt.subplot(2, 3, 4)
    plt.plot(x, y)
    plt.title("4")

    # !!! Текущая ячейка - 5
    plt.subplot(2, 3, 5)
    plt.plot(x, y)
    plt.title("5")

    # !!! Текущая ячейка - 6
    plt.subplot(2, 3, 6)
    plt.plot(x, y)
    plt.title("6")

    # Покажем окно с нарисованным графиком
    plt.show()