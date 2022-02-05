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
from preproccesing import FieldData



class InputData:
    def __init__(self):
        self.h = 45
        self.phi = 0.2
        self.Ct = 2.03e-9
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
    
    h = input_data.h
    phi = input_data.phi
    Ct = input_data.Ct
    pi = input_data.pi
    mu = input_data.mu
    B = input_data.B
    rw = input_data.rw
    q = input_data.q
    # k = input_data.k
    # Skin = input_data.Skin  
    # pdata = input_data.pdata
    t = np.linspace(1, 24*3600*5, 1000)   #*3600*1
    Cs = 5.0*( 2*math.pi*Ct*h*rw**2 )
    k = 2.0e-15
    Skin = 4.0 # 0.0

    # log_t = np.log(t)
    

    
    pwf_exact = pwf(k, Skin, Cs, B, Ct, h, pi, phi, mu, rw, q, t)
    rng = np.random.default_rng()
    noise = np.array(0.001*pi* rng.normal(size=t.size))
    pdata = pwf_exact + noise

    # pdata подаются на вход, а здесь генерятся выше
    t_delta_t = get_log_delta_t(t)
    # knots = np.r_[(t_delta_t[0],)*(k+1), t, (t_delta_t[-1],)*(k+1)]
    pressure_spline = UnivariateSpline(t, pdata, s = 3)                # сплайн
    pdata = pressure_spline(t_delta_t)
    

    
    # log_pdata = np.log(np.array(pdata))
    # log_pwf_exact = np.log(pwf_exact)

    fig, ax = plt.subplots()   
    # ax.plot(log_t, log_pwf_exact, color="blue", label="k={}, Skin={}, Cs={}".format(k, Skin, Cs))
    # ax.plot(t, pwf_exact, color="blue", label="k={}, Skin={}, Cs={}".format(k, Skin, Cs))
    # log_pdata = np.log(pdata)

    x0_array = np.array([1.5e-15, 0.0, 1.0e-9])
    # ax.plot(log_t, log_pdata, color="green",label="k0={}, Skin0={}, Cs0={}".format(x0_array[0], x0_array[1], x0_array[2]))

    def F(vector):       # vector = [k, Skin, Cs]
        array_not_size = pwf(vector[0], vector[1], vector[2], B, Ct, h, pi, phi, mu, rw, q, t_delta_t, tp=0, not_site = True)
        # log_pwD = np.log(array_not_size[3])
        # log_pwD_field = np.log(( 2*math.pi*k*h*(pi - pdata) ) / (q*B*mu))
        log_pwD = array_not_size[3]
        log_pwD_field = ( 2*math.pi*k*h*(pi - pdata) ) / (q*B*mu)
        difference = np.linalg.norm(log_pwD - log_pwD_field, ord=1)
        return difference


        
    res = least_squares(F, x0_array, bounds=([1.0e-17, -10.0, 0.0], [1.0e-13, 10.0, 1.0e-6]), method='dogbox')
    [k_new, Skin_new, Cs_new] = res.x
    print("no exact: ", k_new, Skin_new, Cs_new)
    print("exacr: ", k, Skin, Cs)
    pwf_new = pwf(k_new, Skin_new, Cs_new, B, Ct, h, pi, phi, mu, rw, q, t_delta_t)

    # ax.plot(t, pwf_new, color="red", label="k={}, Skin={}, Cs={}".format(k_new, Skin_new, Cs_new))
    # log_pwf_new = np.log(pwf_new)
    # ax.plot(log_t, log_pwf_new, color="red", label="k={}, Skin={}, Cs={}".format(k_new, Skin_new, Cs_new))
    # ax.set_xscale('log') 
    # ax.set_yscale('log') 

    # ax.legend() 
    # plt.show()   
    return 1 #Skin_new, Cs_new, k_new

if __name__ == "__main__":
    input_data = InputData()
    twf_data = np.linspace(1, 100, 10)
    # q_data = 10
    get_optimization_coef(input_data, twf_data, 10)



