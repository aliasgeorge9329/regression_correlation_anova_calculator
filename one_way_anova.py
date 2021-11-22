from prettytable import PrettyTable
from scipy.stats import f

table = PrettyTable()
table.field_names = ["Source of variation", "Degree of freedom", "Sum of square", "Mean square", "F"]


def one_way_anova():
    no_of_groups = int(input("\nEnter the No of Groups: "))
    alpha = float(input("Level of significance: "))
    print("\n")

    data = []
    ni = []
    _Ti = []
    xij_2 = []
    for i in range(0, no_of_groups):
        print(f"Enter the Group {i+1} samples")
        x = input().strip().split(" ")
        data.append([float(i) for i in x])
        ni.append(len(x))

    for x in data:
        ti_sum = 0
        xij_2_sum = 0
        for each in x:
            ti_sum += each
            xij_2_sum += each**2
        _Ti.append(round(ti_sum, 4))
        xij_2.append(xij_2_sum)

    _N = sum(ni)
    _T = sum(_Ti)
    xij_square_sum = sum(xij_2)
    _C = _T**2 / _N

    sst = xij_square_sum - _C
    ss_tr = 0
    for i in range(0, len(_Ti)):
        ss_tr += _Ti[i]**2 / ni[i]
    ss_tr -= _C
    sst = round(sst, 5)
    ss_tr = round(ss_tr, 5)
    _C = round(_C, 5)
    sse = round(sst - ss_tr, 5)
    ms_tr = round(ss_tr / (no_of_groups - 1), 5)
    mse = round(sse / (_N - no_of_groups), 5)
    _F = round(ms_tr / mse, 3)

    print(f"\nk (No of Groups) = {no_of_groups}")
    print(f"N (Total no of Samples in all Groups) = {_N}")
    print(f"ni (No of Samples in each Groups) = {ni}")
    print(f"\nTi (Sum of Samples in each Groups) = {_Ti}")
    print(f"T (Sum of Samples in all Groups) = {_T}")
    print(f"C (T^2 /N) = {_C}\n")
    print(f"\nSS(Tr) = {ss_tr}")
    print(f"SSE = {sse}")
    print(f"SST = {sst}\n")
    print(f"MS(Tr) (SS(Tr)/(k-1)) = {ms_tr}")
    print(f"MSE (SSE/(N-k)) = {mse}")
    print(f"\nF (MS(Tr)/MSE) = {_F}")
    print("\n")

    table.add_row(["Treatments", f"k-1 ={no_of_groups - 1}", f"SS(Tr) = {ss_tr}", f"MS(Tr) = {ms_tr}", f"{_F}"])
    table.add_row(["Error", f"N-k ={_N - no_of_groups}", f"SS(Tr) = {sse}", f"MS(Tr) = {mse}", ""])
    table.add_row(["-------------", "-------------", "-------------", "-------------", "-------------"])
    table.add_row(["Total", f"N-1 ={_N -1}", f"SST = {sst}", "", ""])

    print(table)
    print("\n")

    null_string = ""
    alternative_ = ""
    for i in range(1, no_of_groups+1):
        null_string += f"μ{i}="
        alternative_ += f"μ{i}≠"

    print(f"Testing {alternative_[:-1]} the alternative Hypothesis to test with null {null_string[:-1]}\n")
    test_statistics_value = _F
    critical_value = round(f.isf(alpha, dfn=no_of_groups - 1, dfd=_N - no_of_groups), 4)
    print(f"\nThe null must be rejected if F>{critical_value}\n")
    print("Calculations\n")
    print(f"F = {test_statistics_value}\n")
    print("Decision\n")
    if test_statistics_value > critical_value:
        print(f"Null {null_string[:-1]} must be Rejected at level of significance {alpha} and Accept {alternative_[:-1]}")
    else:
        print(f"Failure to reject Null {null_string[:-1]}")
