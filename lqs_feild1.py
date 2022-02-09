from cProfile import label
from cmath import pi
# import pwd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, least_squares
from scipy.interpolate import make_interp_spline, make_lsq_spline, UnivariateSpline, LSQUnivariateSpline

import numpy as np
import math
import matplotlib.pyplot as plt
from superposition import pwf
from preproccesing import FieldData, read_field_data_xlsx
from bourdet_derivative import ldiffb




class InputData:
    def __init__(self):
        self.h = 45
        self.phi = 0.2
        self.Ct = 2.3e-9
        self.pi = 20.0e6
        self.mu = 1.0e-3
        self.B = 1
        self.rw = 0.15
        self.q = 3.0/24/3600

        # pwf_exact = pwf(self.k, self.Skin, self.Cs, self.B, self.Ct, self.h, self.pi, self.phi, self.mu, self.rw, self.q, self.t)
        # rng = np.random.default_rng()
        # noise = np.array(0.0001*pi* rng.normal(size=self.t.size))
        # self.pdata = pwf_exact + noise
        
def get_log_delta_t(pTime):    # новый массив времени
    t_start = float(np.log(pTime[0] + 1))
    t_end = float(np.log(pTime[-1]))
    log_delta_t = np.linspace(t_start, t_end, 100)
    delta_t = np.exp(log_delta_t)
    return delta_t


def get_optimization_coef(input_data, twf_data, q_data, tp_data=0):   # pdata

    field_data = read_field_data_xlsx('data/GDIS.xlsx', '1')
    h = field_data.h
    phi = field_data.phi
    Ct = field_data.ct
    pi = field_data.pi
    mu = field_data.mu
    B = field_data.B
    rw = field_data.rw
    q = field_data.q
    pdata = field_data.pwf
    t = field_data.pTime
    # hardcode
    q = q[-2]
    tp = field_data.qTime[-1]
    t = t - tp
    remove_negative = t>0
    t = t[remove_negative]
    pdata = pdata[remove_negative]
    # pi = pdata[0]

    t_delta_t = get_log_delta_t(t)
    # pressure_spline = UnivariateSpline(t, pdata, s = 3)                # сплайн
    # pdata = pressure_spline(t_delta_t)
    
    # log_pdata = np.log(np.array(pdata))
    # log_pwf_exact = np.log(pwf_exact)

    fig, ax = plt.subplots()   
    # ax.plot(t, pwf_exact, color="blue", label="k={}, Skin={}, Cs={}".format(k, Skin, Cs))
    # log_pdata = np.log(pdata)

    # x0_array = np.array([1.5e-15, 0.0, 1.0e-9])
    # # ax.plot(log_t, log_pdata, color="green",label="k0={}, Skin0={}, Cs0={}".format(x0_array[0], x0_array[1], x0_array[2]))

    # def F(vector):       # vector = [k, Skin, Cs]
    #     array_not_size = pwf(vector[0], vector[1], vector[2], B, Ct, h, pi, phi, mu, rw, q, t_delta_t, tp=0, not_site = True)
    #     # log_pwD = np.log(array_not_size[3])
    #     # log_pwD_field = np.log(( 2*math.pi*k*h*(pi - pdata) ) / (q*B*mu))
    #     log_pwD = array_not_size[3]
    #     log_pwD_field = ( 2*math.pi*vector[0]*h*(pi - pdata) ) / (q*B*mu)
    #     difference = np.linalg.norm(log_pwD - log_pwD_field, ord=2)
    #     return difference
    
    # # bounds=([1.0e-17, -10.0, 0.0], [1.0e-13, 10.0, 1.0e-6]), method='trf'
    # res = least_squares(F, x0_array, method='trf', x_scale=[1.0e-15, 1.0, 1.0e-8])
    # [k_new, Skin_new, Cs_new] = res.x
    # print("no exact: ", k_new, Skin_new, Cs_new)
    # pwf_new = pwf(k_new, Skin_new, Cs_new, B, Ct, h, pi, phi, mu, rw, q, t_delta_t)

    # ax.plot(t_delta_t, pwf_new, color="red", label="k={}, Skin={}, Cs={}".format(k_new, Skin_new, Cs_new))
    # log_pwf_new = np.log(pwf_new)
    # # ax.plot(log_t, log_pwf_new, color="red", label="k={}, Skin={}, Cs={}".format(k_new, Skin_new, Cs_new))


    # superposition start
    k = 2.0e-14
    Skin = -3
    Cs = 0*( 2*math.pi*Ct*h*rw**2 )
    pwf1, Cd, td1, pwD1 = pwf(k, Skin, Cs, B, Ct, h, 0, phi, mu, rw, -q, t_delta_t, not_site=True)

    # t2 = np.linspace(1, 80*tp, 10000)
    # log_t2 = get_log_delta_t(t2)
    # pwf2 = pwf(k, Skin, Cs, B, Ct, h, 0, phi, mu,  rw, q, log_t2)
    # spline = UnivariateSpline(log_t2, pwf2, s = 3)

    # pwf_sum = spline(log_t2[-1]-t_delta_t[-1]+t_delta_t)+pwf1 + pdata[0] - spline(log_t2[-1]-t_delta_t[-1]+t_delta_t[0])
    pwf_sum = pwf1 + pdata[0]

    # ax.plot(log_t2, pwf2, label="numerical")
    # ax.plot(t_delta_t, pwf1, label="numerical")
    ax.plot(t_delta_t/3600, pwf_sum/1e6, label="numerical, k = {:0.1E}, Skin = {}".format(k, Skin))
    ax.plot(t/3600, pdata/1e6, label="field data")
    ax.set_xlim(100/3600, t_delta_t[-1]/3600)
    ax.set_xlabel("t, hour")
    ax.set_ylabel("pwf, MPa")

    ax.set_xscale('log') 
    # ax.set_yscale('log') 
    ax.legend() 
    ax.set_title("Сравнение с полевыми данными (ГРП)") 
    
    
    fig2, ax2 = plt.subplots()    
    t_log, p_log, dp_log = ldiffb(td1, pwD1)
    td, pf, dpf = ldiffb(t[0:50:]*k / (phi*mu*Ct*rw**2), pdata[0:50:] / (q*B*mu / (2*math.pi*k*h)))
    ax2.plot(t_log, dp_log, linestyle='dashed', color='b', label="Skin = {}, Cs = {:0.2E}".format(Skin, Cs))
    ax2.plot(t_log, p_log, linestyle='solid', color='b')
    
    ax2.plot(td, dpf, linestyle='dashed', color='r', label="Skin = {}, Cs = {:0.2E}".format(Skin, 10*Cs))
    ax2.plot(td, pf, linestyle='solid', color='r')
    
    ax2.set_xscale('log') 
    ax2.set_yscale('log')
    
    plt.show()
    return 1 #Skin_new, Cs_new, k_new

if __name__ == "__main__":
    input_data = InputData()
    twf_data = np.linspace(1, 100, 10)
    # q_data = 10
    get_optimization_coef(input_data, twf_data, 10)