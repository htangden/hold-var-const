import matplotlib.pyplot as plt
import numpy as np



def plot_data(values, points, titles, labels, function_types):
    plt.style.use('dark_background')
    number_of_plots = len(titles)

    for i in range(number_of_plots):
        k = values[i][0]
        m = values[i][1]

        s_x, b_x = find_point_bounds(points[i])
        x_axis = np.linspace(s_x, b_x, 500)

        plt.subplot(number_of_plots*100 + 11 + i)
        plot_function(function_types[i], [k, m], x_axis)

        points_x = []
        points_y = []
        for x, y in points[i]:
            points_x.append(x)
            points_y.append(y)
       
        plt.plot(points_x, points_y, color = 'red', marker = 'x', linewidth = 0)
        plt.title(titles[i])
        plt.xlabel(labels[i][0])
        plt.ylabel(labels[i][1])

    plt.subplots_adjust(left=0.15,
                        bottom=0.1, 
                        right=0.85, 
                        top=0.9, 
                        wspace=0.4, 
                        hspace=0.6)
    plt.show()




def find_point_bounds(points):
    smallest_x = points[0][0]
    biggest_x = points[0][0]
    for x, y in points:
        if x < smallest_x:
            smallest_x = x
        elif x > biggest_x:
            biggest_x = x

    
    return [smallest_x, biggest_x]


def plot_function(function_type, values, x_axis):
    if function_type == "lin":
        plt.plot(x_axis, values[0] * x_axis + values[1], color = 'blue')
    if function_type == "sqrt":
        plt.plot(x_axis, values[0] + values[1] * x_axis**(1/2), color = 'blue')