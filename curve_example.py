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
    Skin = 0
    t = np.linspace(1, 40000, 40)   #*3600*1
    Cs = 0         # 5*( 2*math.pi*Ct*h*rw**2 )
    
    pwf0 = pwf(k, Skin, Cs, B, Ct, h, pi, phi, mu, rw, q, t)

    fig, ax = plt.subplots()   
    ax.plot(t, pwf0)

    #  шум начало

    rng = np.random.default_rng()
    noise = 0.001*pi* rng.normal(size=t.size)
    pdata = pwf0 + noise
    pdata = np.array(pdata)
    # # шум конец
    ax.plot(t, pdata, color="green")
    
    

    f = lambda x, k_new, Skin_new, Cs_new: pwf(k_new, Skin_new, Cs_new, B, Ct, h, pi, phi, mu, rw, q, x)


    popt, pcov = curve_fit(f, t, pdata, p0=[1e-15, 0, 0])
    k_new, Skin_new, Cs_new = popt
    print(k_new, Skin_new, Cs_new)
    ax.plot(t, f(t,k_new, Skin_new, Cs_new ))



    ax.legend() 
    plt.show()   