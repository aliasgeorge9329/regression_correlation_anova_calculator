from fitting_line import *
from fitting_exponential import *
from fitting_polynomial import *
from fitting_random import *
from confidence_interval_regression import *
from t_test_regression_alpha import *
from t_test_regression_beta import *


def regression():
    print("Enter x and y\n")
    x = input()
    x = x.strip().split(" ")
    x = [float(i) for i in x]

    y = input()
    y = y.strip().split(" ")
    y = [float(i) for i in y]

    print("\n1.Fitting to a line ( y = ⍺ + βx)")
    print("2.Fitting to a exponential ( y= ⍺β^x)")
    print("3.Fitting to a Polynomial ( β0 + β1*x + β2*x^2+ ......... +βp*x^p)")
    print("4.Fitting to a Random function")
    print("5.Confidence Intervals for Regression Coefficients ⍺ and β")
    print("6.T test for Regression Coefficients ⍺_bar ")
    print("7.T test for Regression Coefficients β_bar ")
    print("\n")
    choice = int(input())
    print("\n")
    if choice == 1:
        print("1.Fitting to a line ( y = ⍺ + βx)")
        fitting_line(x, y)
    elif choice == 2:
        print("2.Fitting to a exponential ( y= ⍺β^x)")
        fitting_exponential(x, y)
    elif choice == 3:
        print("3.Fitting to a Polynomial ( β0 + β1*x + β2*x^2+ ......... +βp*x^p)")
        fitting_poly(x, y)
    elif choice == 4:
        print("4.Fitting to a Random function. U need to edit the py file")
        fitting_random(x, y)
    elif choice == 5:
        print("5.Confidence Intervals for Regression Coefficients ⍺ and β")
        confidence_regression(x, y)
    elif choice == 6:
        print("6.T test for Regression Coefficients ⍺_bar ")
        t_test_regression_alpha(x, y)
    elif choice == 7:
        print("7.T test for Regression Coefficients β_bar ")
        t_test_regression_beta(x, y)
    else:
        print("Invalid!")