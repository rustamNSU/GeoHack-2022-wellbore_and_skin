from pressure import p_wd
import math
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

def pwf(k, Skin, Cs, B, Ct, h, pi, phi, mu, rw, q, t, tp=0, not_site = False):
    Cd = Cs / ( 2*math.pi*Ct*h*rw**2 )
    td = t*(k / (phi*mu*Ct*rw**2))
    tpd = tp*(k / (phi*mu*Ct*rw**2))
    
    remove_time = td > tpd
    td2 = td[remove_time] - tpd + 0.1
    pwD = p_wd(Skin, Cd, td2)
    pwD2 = np.zeros(len(td))
    pwD2[remove_time] = pwD
    pwD = pwD2
    delta_p = pwD*q*B*mu / (2*math.pi*k*h)
    pwf = pi - delta_p
    # print("tp={}".format(tp))
    # print(t<tp)
    # if q < 0:
    #     pwf[pwf<0]=0
    #     pwf[t<tp-tp/100]=0
    if not_site == False:
        return np.array(pwf, dtype=float)
    else:
        return np.array(pwf, dtype=float), Cd, td, pwD
    


if __name__ == "__main__":
    h = 45
    phi = 0.02
    Ct = 2.03e-9
    pi = 15.0e6
    mu = 1.0e-3
    B = 1
    rw = 0.1
    q = 3.0/24/3600


    k = 2.0e-16
    Skin = 0
    t = np.linspace(0.01, 24*3600*1.5, 500)
    t = np.sort(np.append(t, np.linspace(30000.01, 30200, 100)))
    Cs = 10*( 2*math.pi*Ct*h*rw**2 )

    pwf1 = pwf(k, Skin, Cs, B, Ct, h, 0, phi, mu, rw, q, t)
    pwf2 = pwf(k, Skin, Cs, B, Ct, h, 0, phi, mu, rw, -q, t, 30000)
    pwf_sum = pwf2 + pwf1 + pi

    fig, ax = plt.subplots()   
    ax.plot(t/3600, pwf_sum/1e6, color='black')
    ax.set_xlim([0, 60000/3600])
    ax.set_xlabel("$t$, hour")
    ax.set_ylabel("$pwf$, $MPa$")
    ax.axhline(y=pi/1.0e6, color='r', ls='--', label='Initial pressure')
    ax.axvline(x=30000/3600, color='orange', ls='--', label="$tp = {:2.2f}h$".format(30000/3600))
    ax.legend() 
    ax.set_title("Superposition")
    plt.show()      
