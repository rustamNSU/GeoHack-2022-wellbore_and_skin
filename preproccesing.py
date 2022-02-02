import pandas as pd

data = pd.ExcelFile("data/GDIS.xlsx")

data.sheet_names

pressure = pd.read_excel(data, '1')

pressure = pressure[['Date', 'Данные']]

pressure = pressure.drop(index=0)

pressure['Данные'] = pressure['Данные']/10.197

from datetime import timedelta
for i in range(31262):
    print(timedelta(seconds=i * 3))

print(pressure)