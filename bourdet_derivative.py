from pressure import p_wd
import math
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

def pwf(k, Skin, Cs, B, Ct, h, pi, mu, rw, q, t, tp=0):
    Cd = Cs / ( 2*math.pi*Ct*h*rw**2 )
    td = t*(k / (phi*mu*Ct*rw**2))
    tpd = tp*(k / (phi*mu*Ct*rw**2))
    pwD = p_wd(Skin, Cd, td, tpd)
    pwf = pi - pwD*q*B*mu / (2*math.pi*k*h)
    # print("tp={}".format(tp))
    # print(t<tp)
    pwf[t<tp]=pi
    return pwf

def pwf_pwD(k, Skin, Cs, B, Ct, h, pi, mu, rw, q, t, tp=0):
    Cd = Cs / ( 2*math.pi*Ct*h*rw**2 )
    td = t*(k / (phi*mu*Ct*rw**2))
    tpd = tp*(k / (phi*mu*Ct*rw**2))
    pwD = p_wd(Skin, Cd, td, tpd)
    pwf = pi - pwD*q*B*mu / (2*math.pi*k*h)
    # print("tp={}".format(tp))
    # print(t<tp)
    pwf[t<tp]=pi
    return pwf, pwD, td


def ldiffb(t, s, d=2):
    '''#LDIFFB - Approximate logarithmic derivative with Bourdet's formula
    Syntax: xd,yd = hp.ldiffb(x,y[,d])
    d = optional argument allowing to adjust the distance between 
        successive points to calculate the derivative.
    See also: ldf, ldiff, ldiffs, ldiffh'''
    ###transform the value of the array X into logarithms 
    logx = []

    for i in range(0, len(t)):
        logx.append(math.log(t[i]))


    dx = np.diff(logx)
    dx1 = dx[0:len(dx)-2*d+1]
    dx2 = dx[2*d-1:len(dx)] 

    dy = np.diff(s)
    dy1 = dy[0:len(dx)-2*d+1]
    dy2 = dy[2*d-1:len(dy)]
    
    xd = t[2:len(s)-2]
    yd = s[2:len(s)-2]
    dyd = (dx2*dy1/dx1+dx1*dy2/dx2)/(dx1+dx2)
    
    return xd,yd, dyd


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
    Skin = 1
    Tend = 24*3600*5
    Tend_log = np.log(Tend)
    tLog = np.linspace(0, Tend_log, 200)
    t = np.exp(tLog)
    Cs = 1*( 2*math.pi*Ct*h*rw**2 )

    pwf, pwD, td = pwf_pwD(k, Skin, Cs, B, Ct, h, pi, mu, rw, q, t)
    t_log, p_log, dp_log = ldiffb(td, pwD)
    
    pwf2, pwD2, td2 = pwf_pwD(k, 10*Skin, Cs, B, Ct, h, pi, mu, rw, q, t)
    t_log2, p_log2, dp_log2 = ldiffb(td, pwD2)
    
    pwf3, pwD3, td3 = pwf_pwD(k, Skin, 10*Cs, B, Ct, h, pi, mu, rw, q, t)
    t_log3, p_log3, dp_log3 = ldiffb(td, pwD3)
    
    pwf4, pwD4, td4 = pwf_pwD(k, 10*Skin, 10*Cs, B, Ct, h, pi, mu, rw, q, t)
    t_log4, p_log4, dp_log4 = ldiffb(td, pwD4)

    fig, ax = plt.subplots()   
    ax.plot(t_log, dp_log, linestyle='dashed', color='b', label="$Skin = {},\;\, Cs = {:0.2E}$".format(Skin, Cs))
    ax.plot(t_log, p_log, linestyle='solid', color='b')
    
    ax.plot(t_log2, dp_log2, linestyle='dashed', color='g', label="$Skin = {}, Cs = {:0.2E}$".format(10*Skin, Cs))
    ax.plot(t_log2, p_log2, linestyle='solid', color='g')
    
    ax.plot(t_log3, dp_log3, linestyle='dashed', color='r', label="$Skin = {}, \;\, Cs = {:0.2E}$".format(Skin, 10*Cs))
    ax.plot(t_log3, p_log3, linestyle='solid', color='r')
    
    ax.plot(t_log4, dp_log4, linestyle='dashed', color='orange', label="$Skin = {}, Cs = {:0.2E}$".format(10*Skin, 10*Cs))
    ax.plot(t_log4, p_log4, linestyle='solid', color='orange')
    
    ax.set_xscale('log') 
    ax.set_yscale('log')
    ax.set_xlabel('$t_D$')
    ax.set_ylabel('$pw_D$')
    ax.set_title('Model sensitivity')
    ax.legend()                                     # показывать условные обозначения
    plt.show()      
