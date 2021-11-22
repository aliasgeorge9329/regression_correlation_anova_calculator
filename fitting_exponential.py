import numpy as np
import matplotlib.pyplot as plt
from least_square import *
import math


def fitting_exponential(x, y):
    # logy = log(⍺) +x*log(β)
    
    new_y = [math.log(each, math.exp(1)) for each in y]
    print("Here x and y means your transformed one!!\n")
    s_xx, s_yy, s_xy, sum_x, sum_y, n = lst_square(x, new_y)

    slope = round((s_xy / s_xx), 7)
    intercept = round(((sum_y / n) - slope * (sum_x / n)), 7)

    print(f"log(⍺) = {intercept}")
    print(f"log(β) = {slope}")
    print(f"logy = ({intercept}) + ({slope})x\n")
    print(f"y = {round(math.exp(1)**intercept, 5)}*e^({round(slope, 5)})x")

    a = np.linspace(min(x), max(x), 100)

    plt.plot(x, y, 'o', label='original data')
    plt.plot(a, (math.exp(1)**intercept)*(math.exp(slope))**a, 'r', label='fitted')
    plt.legend()
    plt.show()
