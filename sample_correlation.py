from least_square import *
import numpy as np
import matplotlib.pyplot as plt


def sample_correlation():
    print("Enter x and y\n")
    x = input()
    x = x.strip().split(" ")
    x = [float(i) for i in x]

    y = input()
    y = y.strip().split(" ")
    y = [float(i) for i in y]

    s_xx, s_yy, s_xy, sum_x, sum_y, n = lst_square(x, y)

    r = s_xy/(s_xx * s_yy)
    print(f"\nSample_correlation_coefficient (r) = {r}")

    plt.plot(x, y, 'o', label='original data')
    plt.legend()
    plt.show()
