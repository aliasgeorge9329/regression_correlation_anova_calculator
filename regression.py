from fitting_line import *
from fitting_exponential import *
from fitting_polynomial import *
from fitting_random import *


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
    else:
        print("Invalid!")