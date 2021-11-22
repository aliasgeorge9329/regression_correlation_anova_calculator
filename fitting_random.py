import numpy as np
import matplotlib.pyplot as plt
from least_square import *
import math


def fitting_random(x, y):
    # logy = log(⍺) +x*log(β)

    new_x = [math.log(each, math.exp(1)) for each in x]
    new_y = [math.log(each, math.exp(1)) for each in y]
    print("Here x and y means your transformed one!!\n")
    s_xx, s_yy, s_xy, sum_x, sum_y, n = lst_square(new_x, new_y)

    slope = round((s_xy / s_xx), 7)
    intercept = round(((sum_y / n) - slope * (sum_x / n)), 7)

    print(f"⍺ = {intercept}")
    print(f"β = {slope}")
    print(f"y = ({intercept}) + ({slope})x\n")
