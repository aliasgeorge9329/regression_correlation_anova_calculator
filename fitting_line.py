import numpy as np
import matplotlib.pyplot as plt
from least_square import *


def fitting_line(x, y):
    s_xx, s_yy, s_xy, sum_x, sum_y, n = lst_square(x, y)

    slope = round((s_xy / s_xx), 7)
    intercept = round(((sum_y / n) - slope * (sum_x / n)), 7)

    print(f"⍺ = {intercept}")
    print(f"β = {slope}")
    print(f"y = ({intercept}) + ({slope})x")

    a = np.linspace(min(x), max(x), 100)

    plt.plot(x, y, 'o', label='original data')
    plt.plot(a, intercept + slope*a, 'r', label='fitted line')
    plt.legend()
    plt.show()
