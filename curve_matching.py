import numpy as np
import matplotlib.pyplot as plt
import math


def load_data(filename):
    with open(filename,'r') as in_file:
        data = in_file.readlines() # makes a list, each element will be one line of data
    return data


def separate_input(input_data):
    data_no_return = input_data.strip("\n")
    data_floats = data_no_return.split(",")
    data = [float(x) for x in data_floats]
    return data


def sin_cos(time):
    amplitude1 = 1
    amplitude2 = 2
    frequency1 = 2
    frequency2 = 3
    curve1 = []
    curve2 = []
    my_curve = []
    for i in range(0, len(time)):
        x1 = amplitude1 * math.sin (frequency1 * time[i])
        curve1.append(x1)
        x2 = amplitude2 * math.cos (frequency2 * time[i])
        curve2.append(x2)
        x3 = x1 + x2
        my_curve.append(x3)
    return my_curve


def plot_signal(time, signal):
    plt.plot(time,signal)
    plt.show()


def plot_traces_same_x(time, signal, my_curve):
    # time = np.arange(0, len(time[0]), 1)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(time, my_curve)
    ax2.plot(time, signal)
    ax1.set_ylabel("mine")
    ax2.set_ylabel("given")
    plt.show()


def main():
    filename = "curve_to_match.dat"
    data = load_data(filename)
    time = separate_input(data[0])
    my_curve = sin_cos(time)
    signal = separate_input(data[1])
    # plot_signal(time, signal)
    plot_traces_same_x(time, signal, my_curve)


if __name__ == "__main__":
    main()