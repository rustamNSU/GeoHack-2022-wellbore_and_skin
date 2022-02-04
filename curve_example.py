from cmath import pi
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import math
import matplotlib.pyplot as plt
from superposition import pwf

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

        pwf_exact = pwf(self.k, self.Skin, self.Cs, self.B, self.Ct, self.h, self.pi, self.phi, self.mu, self.rw, self.q, self.t)
        rng = np.random.default_rng()
        noise = np.array(0.0001*pi* rng.normal(size=self.t.size))
        self.pdata = pwf_exact + noise
        



def get_optimization_coef(input_data, twf_data, q_data, tp_data=0):
    
    h = input_data.h
    phi = input_data.phi
    Ct = input_data.Ct
    pi = input_data.pi
    mu = input_data.mu
    B = input_data.B
    rw = input_data.rw
    q = input_data.q
    k = input_data.k
    Skin = input_data.Skin  
    pdata = input_data.pdata
    t = np.linspace(1, 100, 20)   #*3600*1
    Cs = 5*( 2*math.pi*Ct*h*rw**2 )
    log_pdata = np.log(np.array(pdata))

    log_t = np.log(t)
    # log_pwf_exact = np.log(pwf_exact)

    fig, ax = plt.subplots()   
    # ax.plot(log_t, log_pwf_exact)

    
    ax.plot(log_t, log_pdata, color="green")
    
    

    # f = lambda x, k_new, Skin_new, Cs_new: np.log(pwf(k_new, Skin_new, Cs_new, B, Ct, h, pi, phi, mu, rw, q, x))
    f = lambda x, Skin_new, Cs_new: np.log(pwf(k, Skin_new, Cs_new, B, Ct, h, pi, phi, mu, rw, q, x))

    # ax.plot(t, f(t, 2e-15, 0, 0))

    # popt, pcov = curve_fit(f, t, log_pdata, bounds=([1.0e-17, -10.0, 0.0],[1.0e-13, 10.0, 1.0e-6]), p0=[1.5e-15, 0.0, 1.0e-9], method='trf')
      # k_new, Skin_new, Cs_new = popt
    # print(k_new, Skin_new, Cs_new)
    # print("exact: ", k, Skin, Cs)
    # ax.plot(log_t, f(t,k_new, Skin_new, Cs_new ))
    # print(pcov)
    popt, pcov = curve_fit(f, t, log_pdata, bounds=([-10.0, 0.0],[10.0, 1.0e-6]), p0=[0.0, 1.0e-9], method='trf')
    Skin_new, Cs_new = popt
    print(Skin_new, Cs_new)
    print("exact: ", Skin, Cs)
    ax.plot(log_t, f(t, Skin_new, Cs_new ))
    print(pcov)


    ax.legend() 
    plt.show()   
    return k, Skin, Cs
