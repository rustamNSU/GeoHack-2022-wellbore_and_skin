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
    p_wd = [mp.invertlaplace(fp, t, method='stehfest', degree = 20) for t in tt]
    return p_wd





if __name__ == "__main__":
    fp = lambda p: laplace_p_wd(0, 0, p)

    tt = np.linspace(0.1, 10000, 50)

    fig, ax = plt.subplots()   

    # ax.plot(tt, [mp.invertlaplace(fp, t, method='stehfest', degree = 20) for t in tt], color="black")

    ax.plot(tt, p_wd(0 , 0, tt), label="CD=0, Skin=0")
    # print ( max( [mp.invertlaplace(fp, t, method='stehfest', degree = 20) - p_wd(0 , 0, tt) for t in tt] ) )     # max не работает!!!!
    ax.plot(tt, p_wd(0, 5, tt), label="CD=5, Skin=0")
    ax.plot(tt, p_wd(5, 0, tt), label="CD=0, Skin=5")
    ax.plot(tt, p_wd(5, 5, tt), label="CD=5, Skin=5")
    ax.set_xscale('log') 
    # ax.set_yscale('log') 
    ax.set_xlabel("t")                              # подпись у горизонтальной оси х
    ax.set_ylabel("pD")                              # подпись у вертикальной оси y
    ax.legend()                                     # показывать условные обозначения

    plt.show()                                