from correlation_normal_population import *
from sample_correlation import *


def correlation():
    print("\n")
    print("1.Sample Correlation (finding r)")
    print("2.Testing ⍴ =0(Fisher Transformation) of Normal Populations")
    print("3.Confidence Interval for ⍴(Population correlation coefficient of Normal Populations")

    choice = int(input())
    print("\n")
    if choice == 1:
        print("1.Sample Correlation (finding r)")
        sample_correlation()
    elif choice == 2:
        print("2.Testing ⍴ =0(Fisher Transformation) of Normal Populations")
        correlation_normal_population()
    elif choice == 3:
        print("3.Confidence Interval for ⍴(Population correlation coefficient of Normal Populations")
        population_interval_for_correlation()
    else:
        print("Invalid!")