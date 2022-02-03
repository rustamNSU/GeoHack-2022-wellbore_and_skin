from pressure import p_wd
import math
import numpy as np
import matplotlib.pyplot as plt

def pwf(k, Skin, Cs, B, Ct, h, pi, mu, rw, q, t):
    Cd = Cs / ( 2*math.pi*Ct*h*rw**2 )
    td = t*(k / (phi*mu*Ct*rw**2))
    pwD = p_wd(Skin, Cd, td)
    pwf = pi - pwD*q*B*mu / (2*math.pi*k*h)
    return pwf


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
    Skin = -5
    t = np.linspace(1, 24*3600*10, 100)
    Cs = 5*( 2*math.pi*Ct*h*rw**2 )
    fig, ax = plt.subplots()   
    # ax.plot(td, pwD)
    ax.plot(t, pwf(k, 0, 0, B, Ct, h, pi, mu, rw, q, t), label="Cs=0, Skin=0")
    ax.plot(t, pwf(k, 5, 0, B, Ct, h, pi, mu, rw, q, t), label="Cs=0, Skin=5")
    ax.plot(t, pwf(k, 0, Cs, B, Ct, h, pi, mu, rw, q, t), label="Cs={}, Skin=0".format(Cs))
    ax.plot(t, pwf(k, 5, Cs, B, Ct, h, pi, mu, rw, q, t), label="Cs={}, Skin=5".format(Cs))
    ax.plot(t, pwf(k, -5, Cs, B, Ct, h, pi, mu, rw, q, t), label="Cs={}, Skin=-5".format(Cs))
    ax.plot(t, pwf(k, -5, 0, B, Ct, h, pi, mu, rw, q, t), label="Cs=0, Skin=-5")
    ax.set_xscale('log') 
    ax.set_yscale('log')
    ax.legend()                                     # показывать условные обозначения
    plt.show()      
