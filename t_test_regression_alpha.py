import math
from least_square import *
from scipy.stats import t
from color import *


def t_test_regression_alpha(x, y):
    s_xx, s_yy, s_xy, sum_x, sum_y, n = lst_square(x, y)
    se = math.sqrt(((s_yy - (s_xy ** 2 / s_xx)) / (n - 2)))

    slope = round((s_xy / s_xx), 7)
    intercept = round(((sum_y / n) - slope * (sum_x / n)), 7)

    claim_alpha_bar = float(input("Claim_alpha_bar: "))

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

    test_statistics_value = ((intercept - claim_alpha_bar) / se) * math.sqrt(((n*s_xx) / (s_xx + n*((sum_x / n)**2))))

    print(f"\n{bcolors.OKCYAN}Select the alternative Hypothesis to test with null ᾶ = {claim_alpha_bar}{bcolors.FAIL}")
    print(f"1. ᾶ < {claim_alpha_bar} ")
    print(f"2. ᾶ > {claim_alpha_bar} ")
    print(f"3. ᾶ ≠ {claim_alpha_bar} {bcolors.ENDC}")

    selection = int(input())

    if selection == 1:
        critical_value = -1*round(t.isf(alpha, df=n-1), 4)
        print(f"The null must be rejected if t<{critical_value}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value < critical_value:
            print(f"Null ᾶ = {claim_alpha_bar} must be Rejected at level of significance {alpha} and Accept ᾶ < {claim_alpha_bar}")
        else:
            print(f"Failure to reject Null ᾶ = {claim_alpha_bar} ")

    if selection == 2:
        critical_value = round(t.isf(alpha, df=n-1), 4)
        print(f"The null must be rejected if t>{critical_value}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null ᾶ = {claim_alpha_bar} must be Rejected at level of significance {alpha} and Accept ᾶ > {claim_alpha_bar}")
        else:
            print(f"Failure to reject Null ᾶ = {claim_alpha_bar}  ")

    if selection == 3:
        critical_value_lower = -1*round(t.isf(alpha / 2, df=n-1), 4)
        critical_value_upper = round(t.isf(alpha / 2, df=n-1), 4)
        print(f" The null must be rejected if t<{critical_value_lower} or t>{critical_value_upper}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value_upper or test_statistics_value < critical_value_lower:
            print(f"Null ᾶ = {claim_alpha_bar} must be Rejected at level of significance {alpha} and Accept ᾶ != {claim_alpha_bar}")
        else:
            print(f"Failure to reject Null ᾶ = {claim_alpha_bar} ")



