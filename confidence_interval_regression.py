import math
from least_square import *
from scipy.stats import t


def confidence_regression(x, y):
    s_xx, s_yy, s_xy, sum_x, sum_y, n = lst_square(x, y)
    se = math.sqrt(((s_yy-(s_xy**2 / s_xx)) / (n - 2)))

    slope = round((s_xy / s_xx), 7)
    intercept = round(((sum_y / n) - slope * (sum_x / n)), 7)

    print("\n1. Confidence Intervals for Regression Coefficients ⍺_bar")
    print("2. Confidence Intervals for Regression Coefficients β_bar\n")

    choice = int(input())
    print("\n")
    if choice == 1:
        alpha_bar = intercept
        print("\n1.Confidence interval in Percentage")
        print("2.Level of significance given")
        choice = int(input())
        print("\n")
        alpha = 0
        if choice == 1:
            p = float(input("1.Confidence interval in Percentage: "))
            alpha = 1 - p / 100
        else:
            alpha = float(input("Level of significance: "))
        t_alpha_2 = round(t.isf(alpha / 2, df=n - 2), 4)

        alpha_l = round(alpha_bar - (t_alpha_2 * se * (math.sqrt(1 / n + ((sum_x / n) ** 2 / s_xx)))), 5)
        alpha_h = round(alpha_bar + (t_alpha_2 * se * (math.sqrt(1 / n + ((sum_x / n) ** 2 / s_xx)))), 5)

        print(f"\nt_(alpha/2) = {t_alpha_2}")
        print(f"se = {se}")
        print(f"\n{alpha_l} < ᾶ < {alpha_h}")

    elif choice == 2:
        beta_bar = slope
        print("\n1.Confidence interval in Percentage")
        print("2.Level of significance given")
        choice = int(input())
        print("\n")
        alpha = 0
        if choice == 1:
            p = float(input("1.Confidence interval in Percentage: "))
            alpha = 1 - p / 100
        else:
            alpha = float(input("Level of significance: "))
        t_alpha_2 = round(t.isf(alpha / 2, df=n - 2), 4)

        beta_l = round(beta_bar - (t_alpha_2 * se * (math.sqrt(1 / s_xx))), 5)
        beta_h = round(beta_bar + (t_alpha_2 * se * (math.sqrt(1 / s_xx))), 5)

        print(f"\nt_(alpha/2) = {t_alpha_2}")
        print(f"se = {se}")
        print(f"\n{beta_l} < β_bar < {beta_h}")

    else:
        print("Invalid!")










