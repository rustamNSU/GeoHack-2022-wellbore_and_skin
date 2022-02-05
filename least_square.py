from cmath import pi
# import pwd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, least_squares
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

        # pwf_exact = pwf(self.k, self.Skin, self.Cs, self.B, self.Ct, self.h, self.pi, self.phi, self.mu, self.rw, self.q, self.t)
        # rng = np.random.default_rng()
        # noise = np.array(0.0001*pi* rng.normal(size=self.t.size))
        # self.pdata = pwf_exact + noise
        



def get_optimization_coef(input_data, twf_data, q_data, tp_data=0):
    
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
    t = np.linspace(1, 100, 20)   #*3600*1
    Cs = 5*( 2*math.pi*Ct*h*rw**2 )
    k = 2.0e-15
    Skin = 0.0

    log_t = np.log(t)
    # log_pwf_exact = np.log(pwf_exact)

    # fig, ax = plt.subplots()   
    # ax.plot(log_t, log_pwf_exact)

    
    # ax.plot(log_t, log_pdata, color="green")
    pwf_exact = pwf(k, Skin, Cs, B, Ct, h, pi, phi, mu, rw, q, t)
    rng = np.random.default_rng()
    noise = np.array(0.0001*pi* rng.normal(size=t.size))
    pdata = pwf_exact + noise
    log_pdata = np.log(np.array(pdata))


    def F(vector):       # vector = [k, Skin, Cs]
        array_not_size = pwf(vector[0], vector[1], vector[2], B, Ct, h, pi, phi, mu, rw, q, t, tp=0, not_site = True)
        pwD = array_not_size[3]
        
        pdata_not_size = ( 2*math.pi*k*h*(pi - pdata) ) / (q*B*mu)
        difference = np.linalg.norm(pwD - pdata_not_size, ord=1)
        return difference

    x0_array = np.array([1.0e-15, 1.0, 1.0e-9])
    
    
    # print(np.isfinite(F(x0_array)))
    
    res = least_squares(F, x0_array, bounds=([1.0e-17, -10.0, 0.0], [1.0e-13, 10.0, 1.0e-6]))
    print(res.x)
    print("exacr: ", k, Skin, Cs)
    


    # ax.legend() 
    # plt.show()   
    return 1 #Skin_new, Cs_new   # , k_new

if __name__ == "__main__":
    input_data = InputData()
    twf_data = np.linspace(1, 100, 10)
    # q_data = 10
    get_optimization_coef(input_data, twf_data, 10)
