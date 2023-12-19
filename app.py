import numpy as np
from data_loader import *
from functions import *
from plot import *

data_path = "data/democracy-peace-gdp.xlsx"
#just for right now:
samples, x, y, z = data_loader(data_path)
regressions = [[z, x], [z, y]]

labels = [["GDP", "Democracy"], ["GDP", "Peace"], ["Democracy", "Peace"], ["Democracy", "Peace"]]
titles = ["Democracy vs GDP", "Peace vs GDP", "Peace vs Democracy (GDP Constant)", "Peace vs Democracy"]
values = [[0, 0], [0, 0], [0, 0], [0, 0]]
function_types = ["lin", "lin", "lin", "lin"]

#samples, x, y, z = data_loader(data_path)

for c, e in enumerate(regressions):
    data = np.vstack((e[0], e[1])).T
    if function_types[c] == "lin":
        values[c][0], values[c][1] = lin_reg(data)
    elif function_types[c] == "sqrt":
        values[c][0], values[c][1] = sqrt_reg(data)

differences = calculate_difference_points(values, function_types, regressions)
values[2][0], values[2][1] = lin_reg(differences)

if function_types[3] == "lin":
    values[3][0], values[3][1] = lin_reg(np.vstack((x, y)).T)
elif function_types[3] == "sqrt":
    values[3][0], values[3][1] = sqtr_reg(np.vstack((x, y)).T)




points = [np.vstack((z, x)).T, np.vstack((z, y)).T, np.array(differences), np.vstack((x, y)).T]





plot_data(values, points, titles, labels, function_types)
