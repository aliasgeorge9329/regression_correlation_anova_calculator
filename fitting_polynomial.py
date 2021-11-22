import numpy as np
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["l", "r"]


def fitting_poly(x, y):
    p = int(input("Enter the Highest Power of polynomial: "))
    n = len(x)
    data_x_power = []
    data_xy_x_power = []
    d_array = []
    print("\n")
    print(f"Σy = {sum(y)}")
    for i in range(1, 2*p+1):
        new_x = [each**i for each in x]
        data_x_power.append(sum(new_x))
        print(f"Σx{i} = {sum(new_x)}")

    for i in range(1, p+1):
        t = 0
        for j in range(0, n):
            t += (x[j] ** i) * y[j]
        data_xy_x_power.append(t)
        print(f"Σx{i}y = {t}")

    array_1 = [n]
    for i in range(0, p):
        array_1.append(data_x_power[i])
    d_array += [array_1]

    for i in range(0, p):
        array_t = []
        for j in range(i, p+i+1):
            array_t.append(data_x_power[j])
        d_array += [array_t]

    a_ = np.array(d_array)
    b_array = []
    b_array += [sum(y)]
    b_array += data_xy_x_power
    b_ = np.array([b_array])
    print("\n")
    table.add_row([np.transpose(b_), a_])
    print(table)
    print("\nThe coefficient ( β0, β1, β2... are following)\n")
    x = np.dot(np.linalg.inv(a_), np.transpose(b_))
    print(x)

