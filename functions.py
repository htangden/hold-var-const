import numpy as np

def lin_reg(points): # f(x) = ax + b
    sumof = {
    "x**2": 0,
    "x": 0,
    "xy": 0,
    "y": 0
    }

    for x, y in points:
        sumof["x**2"] += x**2
        sumof["x"] += x
        sumof["xy"] += x*y
        sumof["y"] += y

    n = len(points)
    a = (sumof["xy"]-sumof["x"]*sumof["y"]/n)/(sumof["x**2"]-(sumof["x"]**2)/n)
    b = (sumof["y"] - ((sumof["x"])*(sumof["xy"]-sumof["x"]*sumof["y"]/n))/(sumof["x**2"]-(sumof["x"]**2)/n))/n

    return a, b


def sqrt_reg(points): #f(x) = a + b*sqrt(x)
    sumof = {
        "x": 0,
        "y": 0,
        "x**1/2": 0,
        "yx**1/2": 0
    }

    for x, y in points:
        sumof["x"] += x
        sumof["y"] += y
        sumof["x**1/2"] += x**(1/2)
        sumof["yx**1/2"] += y*(x**(1/2))
    
    n = len(points)
    a = (sumof["y"]*sumof["x"]-sumof["yx**1/2"]*sumof["x**1/2"])/(n*sumof["x"]-sumof["x**1/2"]**2)
    b = (sumof["yx**1/2"] - (sumof["y"]*sumof["x"]*sumof["x**1/2"]-sumof["yx**1/2"]*sumof["x**1/2"]**2)/(n*sumof["x"]-sumof["x**1/2"]**2))/sumof["x"]

    return a, b


def calculate_difference_points(values, function_types, regressions):
    differences = []
    for i in range(len(regressions[0][0])):
        x_diff = calculate_diff(values[0], function_types[0], [regressions[0][0][i], regressions[0][1][i]])
        y_diff = calculate_diff(values[1], function_types[1], [regressions[1][0][i], regressions[1][1][i]])
        differences.append([x_diff, y_diff])
    return differences

def calculate_diff(values, function_type, point):
    if function_type == "lin":
        return point[1] - (values[1] + values[0] * point[0])
    if function_type == "sqrt":
        return point[1] - (values[0] + values[1] * point[0]**(1/2))
