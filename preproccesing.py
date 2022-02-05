from dataclasses import field
from datetime import datetime
from matplotlib.pyplot import plot
import numpy as np
import pandas as pd
import time

class FieldData: 
    def __init__(self):
        self.pwf = []
        self.pTime = []
        self.q = []
        self.qTime = []
        self.rw = 0.108
        self.h = 43.8
        self.phi = 0.06
        self.B = 1.24
        self.mu = 1.64
        self.ct = 0.000225
        self.pi = 13386077.25

    def print_data(self, n=10):
        print("pressure = {}, time_in_seconds = {}, schedule_in_seconds = {}, debit = {}".format(\
        self.pwf[0:n], self.pTime[0:n], self.qTime[0:n], self.q[0:n]))

    def get_debit(self, t):
        indx = -1
        for qt in self.qTime:
            if t < qt:
                break
            else:
                indx = indx + 1
        return self.q[indx]


def read_field_data_xlsx(file_path):
    field_data = FieldData()

    data = pd.ExcelFile(file_path)
    table = data.parse('1')

    pressure = table['pressure'].to_numpy()

    pressure = pressure[1:]
    pressure = pressure * 98066.5

    timedata = table['date'].to_numpy()
    timedata = timedata[1:]

    time_in_seconds = np.zeros(len(timedata))
    start_time = timedata[0]
    for i, date in zip(range(len(timedata)), timedata):
        seconds = int(str(np.timedelta64(date - start_time, 's')).split(' ')[0])
        time_in_seconds[i] = seconds

    schedule = table['schedule'].to_numpy()
    removeNan = ~np.isnan(schedule)
    schedule = schedule[removeNan]

    schedule_in_seconds = np.zeros(len(schedule))


    for i, date in zip(range(len(schedule)), schedule):
        seconds = int(str(np.timedelta64(date-start_time, 's')).split(' ')[0])
        schedule_in_seconds[i] = seconds

    debit = table['q'].to_numpy()
    debit = debit[removeNan] / 86400.0

    field_data.pwf = pressure
    field_data.pTime = time_in_seconds
    field_data.q = debit
    field_data.qTime = schedule_in_seconds

    return field_data

if __name__ == "__main__":

    field_data = read_field_data_xlsx('data/GDIS.xlsx')
    field_data.print_data()

    import matplotlib.pyplot as plt 

    x = field_data.pTime

    y = np.array(list(map(field_data.get_debit, x)))

    plt.plot(x, y)
    plt.show()
