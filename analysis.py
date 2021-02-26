import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    with open(filename,'r') as in_file:
        # trace = in_file.readline() #reads single line in file and saves to a variable
        traces = in_file.readlines() # makes a list, each element will be one line of data
    return traces


def convert_input_string_to_trace_data(trace_string):
    trace_no_return = trace_string.strip("\n")
    trace_ints = trace_no_return.split(",")
    trace = [int(x) for x in trace_ints]
    return trace


def plot_trace(trace, axis_name):
    time = np.arange(0, len(trace), 1) 
    plt.plot(time,trace)
    plt.ylabel(axis_name)
    plt.show()


def plot_traces(traces):
    time = np.arange(0,len(traces[0]), 1)
    plt.subplot(3, 1, 1)
    plt.plot(time, traces[0])
    plt.ylabel("Pulse Ox")
    plt.subplot(3, 1, 2)
    plt.plot(time, traces[1])
    plt.ylabel("Blood Pressure")
    plt.subplot(3, 1, 3)
    plt.plot(time, traces[2])
    plt.ylabel("ECG")
    plt.show()
    
    
def plot_traces_same_x(traces):
    time = np.arange(0, len(traces[0]), 1)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    ax1.plot(time, traces[0])
    ax2.plot(time, traces[1])
    ax3.plot(time, traces[2])
    ax1.set_ylabel("pulse ox")
    ax2.set_ylabel("blood pressure")
    ax3.set_ylabel("ecg")
    plt.show()
    

def plot_all_on_one(traces):
    time = np.arange(0, len(traces[0]), 1)
    plt.plot(time, traces[0])
    plt.plot(time, traces[1])
    plt.plot(time, traces[2])
    plt.show()
    


def main():
    filename = "overall_data.dat"
    traces = load_data(filename)
    pulse_ox = convert_input_string_to_trace_data(traces[0])
    blood_pressure = convert_input_string_to_trace_data(traces[1])
    ecg = convert_input_string_to_trace_data(traces[2])
    '''
    plot_trace(pulse_ox, "Plethysmograph")
    plot_trace(blood_pressure, "Blood Pressure")
    plot_trace(ecg, "ECG")
    '''
    new_traces = [pulse_ox, blood_pressure, ecg]
    # plot_traces(new_traces)
    # plot_traces_same_x(new_traces)
    plot_all_on_one(new_traces)


if __name__ == "__main__":
    main()
    


