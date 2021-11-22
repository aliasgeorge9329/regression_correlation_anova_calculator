from regression import *
from correlation import *
from one_way_anova import *

print("Welcome to Regression,Correlation, Anova Calculator")

print("\n1.Regression")
print("2.Correlation")
print("3.One Way Anova")
print("4.Two Way Anova")

choice = int(input())
print("\n")
if choice == 1:
    print("\n1.Regression")
    regression()
elif choice == 2:
    print("2.Correlation")
    correlation()
elif choice == 3:
    print("3.One Way Anova")
    one_way_anova()
elif choice == 4:
    print("4.Two Way Anova")
    pass
else:
    print("Invalid!")