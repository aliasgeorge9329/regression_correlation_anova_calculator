import numpy as np
from prettytable import PrettyTable
from scipy.stats import f

table = PrettyTable()
table.field_names = ["Source of variation", "Degree of freedom", "Sum of square", "Mean square", "F"]


def two_way_anova():
    a = int(input("Enter the no of Treatments: "))
    b = int(input("Enter the no of Blocks: "))
    alpha = float(input("Level of significance: "))
    data_each = []
    print("\nEnter the Data\n")
    for i in range(0, a):
        t_ = input().strip().split(" ")
        t = [float(x) for x in t_]
        data_each.append(t)

    data = np.array(data_each)

    _Tab = np.sum(data)
    _Tab2 = np.sum(data**2)
    _Ta = data.sum(axis=1)
    _Ta2 = data.sum(axis=1)**2
    _Tb = data.sum(axis=0)
    _Tb2 = data.sum(axis=0)**2
    _C = round(_Tab**2 / (a*b), 5)

    sst = round(_Tab2 - _C, 5)
    ss_tr = round(np.sum(_Ta2)/b-_C, 5)
    ss_bl = round(np.sum(_Tb2)/a-_C, 5)
    sse = round(sst - ss_tr - ss_bl, 5)

    ms_tr = round(ss_tr / (a - 1), 5)
    ms_bl = round(ss_bl / (b - 1), 5)
    mse = round(sse / ((a-1)*(b-1)), 5)

    _Ftr = round(ms_tr / mse, 3)
    _Fbl = round(ms_bl / mse, 3)

    print(f"\na (No of Treatments) = {a}")
    print(f"b (No of Blocks) = {b}")
    print(f"a*b (Total no of Samples) = {a*b}")

    print(f"\nTi. = {_Ta}")
    print(f"T.j = {_Tb}")
    print(f"ΣΣ yij^2 = {_Tab2}")
    print(f"C (T..^2 / a*b) = {_C}\n")
    print(f"\nSS(Tr) = {ss_tr}")
    print(f"SS(Bl) = {ss_bl}")
    print(f"SSE = {sse}")
    print(f"SST = {sst}\n")
    print(f"MS(Tr) (SS(Tr)/(a-1)) = {ms_tr}")
    print(f"MS(Bl) (SS(Bl)/(b-1)) = {ms_bl}")
    print(f"MSE (SSE/(a-1)*(b-1)) = {mse}")
    print(f"\nF_Tr (MS(Tr)/MSE) = {_Ftr}")
    print(f"F_Bl (MS(Bl)/MSE) = {_Fbl}")
    print("\n")

    table.add_row(["Treatments", f"a-1 = {a - 1}", f"SS(Tr) = {ss_tr}", f"MS(Tr) = {ms_tr}", f"{_Ftr}"])
    table.add_row(["Blocks", f"b-1 = {b - 1}", f"SS(Tr) = {ss_bl}", f"MS(Tr) = {ms_bl}", f"{_Fbl}"])
    table.add_row(["Error", f"(a-1)(b-1) = {((a-1)*(b-1))}", f"SSE = {sse}", f"MSE = {mse}", ""])
    table.add_row(["-------------", "-------------", "-------------", "-------------", "-------------"])
    table.add_row(["Total", f"ab-1 = {a*b - 1}", f"SST = {sst}", "", ""])

    print(table)
    print("\n")

    null_string_tr = ""
    alternative_tr = ""
    for i in range(1, a + 1):
        null_string_tr += f"⍺{i}="
        alternative_tr += f"⍺{i}≠"
    null_string_tr = null_string_tr[:-1] + "=0"
    alternative_tr = alternative_tr[:-1] + "≠0"

    null_string_bl = ""
    alternative_bl = ""
    for i in range(1, b + 1):
        null_string_bl += f"β{i}="
        alternative_bl += f"β{i}≠"
    null_string_bl = null_string_bl[:-1] + "=0"
    alternative_bl = alternative_bl[:-1] + "≠0"

    print("\nTreatments Testing")
    print(f"Testing {alternative_tr} the alternative Hypothesis to test with null {null_string_tr}")

    test_statistics_value_tr = _Ftr
    critical_value_tr = round(f.isf(alpha, dfn=(a - 1), dfd=((a-1)*(b-1))), 4)

    print(f"The null {null_string_tr} must be rejected if F>{critical_value_tr}\n")
    print("Calculations\n")
    print(f"F(Tr) = {test_statistics_value_tr}\n")
    print("Decision\n")
    if test_statistics_value_tr > critical_value_tr:
        print(f"Null {null_string_tr} must be Rejected at level of significance {alpha} and Accept {alternative_tr}")
    else:
        print(f"Failure to reject Null {null_string_tr}")

    print("\n\nBlocks Testing")
    print(f"Testing {alternative_bl}  the alternative Hypothesis to test with null {null_string_bl}")
    test_statistics_value_bl = _Fbl
    critical_value_bl = round(f.isf(alpha, dfn=(b - 1), dfd=((a-1)*(b-1))), 4)

    print(f"The null {null_string_bl} must be rejected if F>{critical_value_bl}\n")
    print("Calculations\n")
    print(f"F(Bl) = {test_statistics_value_bl}\n")
    print("Decision\n")
    if test_statistics_value_bl > critical_value_bl:
        print(
            f"Null {null_string_bl} must be Rejected at level of significance {alpha} and Accept {alternative_bl}")
    else:
        print(f"Failure to reject Null {null_string_bl}")
