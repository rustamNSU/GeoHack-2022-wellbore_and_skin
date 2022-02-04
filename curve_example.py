from cmath import pi
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import math
import matplotlib.pyplot as plt
from superposition import pwf

if __name__ == "__main__":
    h = 45
    phi = 0.2
    Ct = 2.03e-9
    pi = 20.0e6
    mu = 1.0e-3
    B = 1
    rw = 0.15
    q = 3.0/24/3600
    

    k = 2.0e-15
    Skin = 3.0
    t = np.linspace(1, 100, 20)   #*3600*1
    Cs = 5*( 2*math.pi*Ct*h*rw**2 )
    
    pwf_exact = pwf(k, Skin, Cs, B, Ct, h, pi, phi, mu, rw, q, t)

    log_t = np.log(t)
    log_pwf_exact = np.log(pwf_exact)

    fig, ax = plt.subplots()   
    ax.plot(log_t, log_pwf_exact)

    #  шум начало

    rng = np.random.default_rng()
    noise = np.array(0.0001*pi* rng.normal(size=t.size))
    pdata = pwf_exact + noise
    log_pdata = np.log(np.array(pdata))
    # # шум конец
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