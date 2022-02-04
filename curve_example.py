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
    t = np.linspace(1, 24*3600*1, 100)   #
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
    
    

    # f = lambda k, Skin, Cs: pwf(k, Skin, Cs, B, Ct, h, pi, phi, mu, rw, q, t)


    # popt, pcov = curve_fit(pwf, t, pdata)
    # print("fit: a=%5.3f, b=%5.3f, c=%5.3f".format(popt))
    # ax.plot(t, pwf(t, *popt))



    ax.legend() 
    plt.show()   