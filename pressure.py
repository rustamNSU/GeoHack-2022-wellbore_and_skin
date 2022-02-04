import math
import numpy as np
from scipy.special import kv, k0, k1, expi
import matplotlib.pyplot as plt
import mpmath as mp
  

def exact_solution(t, r):
    return -0.5*expi( -r**2 / (4*t) )

def laplace_p_wd(Skin, CDstor, s):
    s = float(s)
    pwd = (k0(math.sqrt(s)) + math.sqrt(s)*Skin*k1(math.sqrt(s))) / ( ( math.sqrt(s)*k1(math.sqrt(s) ) + CDstor*s*( k0(math.sqrt(s)) + math.sqrt(s)*Skin*k1(math.sqrt(s)) ) ) * s)
    return pwd 

def p_wd(Skin, CDstor, tt):
    fp = lambda p: laplace_p_wd(Skin, CDstor, p)
    for t in tt:
        if t<0:
            print(t)
    p_wd = [mp.invertlaplace(fp, t, method='stehfest', degree = 20) for t in tt]
    return np.array(p_wd)



if __name__ == "__main__":

    h = 10
    phi = 0.1
    Ct = 1.0e-5
    pi = 6.0e6
    mu = 7.0e-3
    B = 1
    k = 2.0e-15
    Skin = 0
    Cs = 0
    rw = 1.0e-1
    q = 60.0/24/3600
    t = np.linspace(1, 24*3600*5, 100)

    Cd = Cs / ( 2*math.pi*Ct*h*rw**2 )
    td = t*(k / (phi*mu*Ct*rw**2))
    # pwD = p_wd(Skin, Cd, td)

    fp = lambda p: laplace_p_wd(0, 0, p)

    tt = td

    fig, ax = plt.subplots()   

    print(tt)
    ax.plot(tt, p_wd(0 , 0, tt), label="CD=0, Skin=0")
    # print ( max( [mp.invertlaplace(fp, t, method='stehfest', degree = 20) - p_wd(0 , 0, tt) for t in tt] ) )     # max не работает!!!!
    ax.plot(tt, p_wd(0, 5, tt), label="CD=5, Skin=0")
    ax.plot(tt, p_wd(5, 0, tt), label="CD=0, Skin=5")
    ax.plot(tt, p_wd(5, 5, tt), label="CD=5, Skin=5")
    ax.set_xscale('log') 
    ax.set_yscale('log') 
    ax.set_xlabel("t")                              # подпись у горизонтальной оси х
    ax.set_ylabel("pD")                              # подпись у вертикальной оси y
    ax.legend()                                     # показывать условные обозначения

    plt.show()                                