from datetime import datetime
import numpy as np
import pandas as pd

def read_field_data_xlsx(file_path):
    data = pd.ExcelFile(file_path)

    table = data.parse('1')

    pressure = table['Данные'].to_numpy()

    index = [0]
    new_pressure = np.delete(pressure, index)
    pressure = new_pressure / 10.197

    timedata = table['Date'].to_numpy()
    

    index = [0]
    new_timedata = np.delete(timedata, index)
    new_time_date = []

    start_time = new_timedata[0]
    for date in new_timedata:
        seconds = int(str(np.timedelta64(date - start_time, 's')).split(' ')[0])
        new_time_date.append(seconds)
    return pressure, new_time_date

if __name__ == "__main__":

    P, T = read_field_data_xlsx('data/GDIS.xlsx')

    print("pressure = {}, time = {}".format(P[0], T[0]))