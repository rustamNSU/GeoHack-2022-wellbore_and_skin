from dataclasses import field
from datetime import datetime
import numpy as np
import pandas as pd
# import schedule 
# import time

# def definite_pressure():
#     print("q")

# schedule.every().seconds.at("t").do(definite_pressure)
# schedule.every()

# class FieldData: 
#     def __init__(self):
#         # self.pwf = 
#         # self.pTime = 
#         # self.q = 
#         # self.qTime = 
#         self.rw = 0.108
#         self.h = 43.8
#         self.phi = 0.06
#         self.B = 1.24
#         self.mu = 1.64
#         self.ct = 0.000225
#         self.pi = 13386077.25


def read_field_data_xlsx(file_path):

    # field_data = FieldData()

    data = pd.ExcelFile(file_path)

    table = data.parse('1')

    pressure = table['pressure'].to_numpy()

    index = [0]
    new_pressure = np.delete(pressure, index)
    pressure = new_pressure * 98066.5

    timedata = table['date'].to_numpy()

    index = [0]
    new_timedata = np.delete(timedata, index)
    new_time_date = []

    start_time = new_timedata[0]
    for date in new_timedata:
        seconds = int(str(np.timedelta64(date - start_time, 's')).split(' ')[0])
        new_time_date.append(seconds)

    schedule = table['schedule'].to_numpy()
    removeNan = ~np.isnan(schedule)
    schedule = schedule[removeNan]

    # index = [0]
    # new_schedule = np.delete(schedule, index)
    new_schedule = schedule
    new_time_date2 = []

    # start_time = new_schedule[0]
    for date in new_schedule:
        seconds = int(str(np.timedelta64(date-start_time, 's')).split(' ')[0])
        new_time_date2.append(seconds)

    expenditure = table['q'].to_numpy()

    # index = [0]
    # new_expenditure = np.delete(expenditure, index)
    expenditure = expenditure[removeNan] / 86400


    return pressure, new_time_date, new_time_date2, expenditure


if __name__ == "__main__":

    P, T, S, E = read_field_data_xlsx('data/GDIS.xlsx')

    print("pressure = {}, time = {}, schedule = {}, expenditure = {}".format(P[0:10], T[0:10], S[0:10], E[-10:-1]))
