from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["x", "y", "x^2", "y^2", "xy"]


def lst_square(x, y):
    data = []
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_2 = 0
    sum_y_2 = 0
    sum_xy = 0

    for i in range(0, n):
        d = {"x": x[i],
             "x^2": round(x[i]**2, 3),
             "y": y[i],
             "y^2": round(y[i]**2, 3),
             "xy": round(x[i]*y[i], 4)
             }
        table.add_row([d["x"], d["y"], d["x^2"], d["y^2"], d["xy"]])
        data.append(d)

    for each in data:
        sum_x_2 += each['x^2']
        sum_y_2 += each['y^2']
        sum_xy += each['xy']

    table.add_row(["------", "------", "------", "------", "------"])
    table.add_row([f"x̄ = {round(sum_x/n ,4)}", f"ȳ = {round(sum_y/n ,4)}", f"{round(sum_x_2,4)}", f"{round(sum_y_2,4)}", f"{round(sum_xy,4)}"])

    s_xx = round((sum_x_2 - sum_x**2 / n), 4)
    s_yy = round((sum_y_2 - sum_y**2 / n), 4)
    s_xy = round((sum_xy - sum_x*sum_y / n), 4)

    print(f"\n{table}")
    print(f"\nSxx = {sum_x_2} - ({sum_x})^2/{n} = {s_xx}")
    print(f"Syy = {sum_y_2} - ({sum_y})^2/{n} = {s_yy}")
    print(f"Sxy = {sum_xy} - ({sum_x})*({sum_y})/{n} = {s_xy}\n")

    return s_xx, s_yy, s_xy, sum_x, sum_y, n



