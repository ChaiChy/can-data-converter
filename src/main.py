from curses.ascii import CAN
import matplotlib.pyplot as plt
import csv
import struct


def process_capacitance(hex_value :str) :
    hex_val = bytes.fromhex(hex_value)
    capacitance = struct.unpack('<f', hex_val[:4])
    return capacitance


def get_raw_capcitance(converted_list, channel_id: str):
    index = 3
    raw_capacitance_measurement = []
    for element in converted_list:
        if channel_id in element[2]:
            raw_capacitance_measurement.append(element[2][index+1:])
    return raw_capacitance_measurement
            
def get_time(converted_list, channel_id: str):
    index = 3
    time = []
    for element in converted_list:
        if channel_id in element[2]:
            time.append(element[0])
    return time
    


if __name__ == "__main__":
    capacitance_list = []
    CAN_list = csv.reader(open('csv_data/candump-2022.csv'), delimiter=' ')
    CAN_list = list(CAN_list)
    raw_cap_list = get_raw_capcitance(CAN_list, "162")
    for i in range(0, len(raw_cap_list), 1):
        capacitance_list.append(process_capacitance(raw_cap_list[i])) 
    print(capacitance_list)
    time_list = get_time(CAN_list, "162")
    #print(time_list)

    # Data for plotting
    y = capacitance_list
    x = time_list

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='time (s)', ylabel='farad (fF)',
        title='kill me')
    ax.grid()

    fig.savefig("test.png")
    plt.show()

