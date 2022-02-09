from preproccesing import FieldData
import numpy as np
import matplotlib.pyplot as plt




def  plot_field_pressure(fig, ax, field_data):
    
    Pa_to_MPa = 1e6
    sec_to_hour = 3600
    x = field_data.pTime/sec_to_hour
    y = field_data.pwf / Pa_to_MPa
    
    ax.set_title('Plot 1')
    ax.set_ylabel('Pressure(MPa)')
    ax.set_xlabel('Time(hour)', fontsize=10)
    ax.plot_date(x, y)
    
    
    

def  plot_field_debit(fig, ax, field_data):
    x = field_data.pTime
    sec_to_hour = 3600
    y = np.array(list(map(field_data.get_debit, x)))
    x = field_data.pTime/ sec_to_hour
    
    ax.set_title('Plot 3', fontsize=12)
    ax.set_ylabel('Debit (m^3/hour)',)
    ax.set_xlabel('Time(hour)')
    ax.plot_date(x, y)
    
   