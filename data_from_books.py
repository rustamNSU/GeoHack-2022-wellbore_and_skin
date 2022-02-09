from pressure import p_wd
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
my_data = genfromtxt('data/data.csv', delimiter=' ')
plt.rc('text', usetex=True)

def read_csv(file_path='data/data.csv'):
    data = genfromtxt(file_path, delimiter=' ')
    return data



def pwf(k, Skin, Cs, B, Ct, h, pi, phi, mu, rw, q, t, tp=0):
    Cd = Cs / ( 2*math.pi*Ct*h*rw**2 )
    td = t*(k / (phi*mu*Ct*rw**2))
    tpd = tp*(k / (phi*mu*Ct*rw**2))
    pwD = p_wd(Skin, Cd, td, tpd)
    pwf = pi - pwD*q*B*mu / (2*math.pi*k*h)
    # print("tp={}".format(tp))
    # print(t<tp)
    pwf[t<tp]=pi
    return pwf

def pwf_pwD(k, Skin, Cs, B, Ct, h, pi, phi, mu, rw, q, t, tp=0):
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
    
    xd = t[d:len(s)-d]
    yd = s[d:len(s)-d]
    dyd = (dx2*dy1/dx1+dx1*dy2/dx2)/(dx1+dx2)
    
    return xd,yd, dyd


def compute_model_data(data, ax, k=1.0743875237657162e-14, Skin=7.7, Cs=2.3e-7):
    t = 3600*data[:, 0]
    delta_p = data[:, 1]*6894.76
    q = 1.84e-6 * 174
    Ct = 4.2e-6/6894.76
    mu = 2.5e-3
    rw = 0.088392
    h = 32.61
    phi = 0.25
    B = 1.06
    
    Cd = Cs / (2*math.pi*phi*Ct*h*rw**2)   
    td = t*(k / (phi*mu*Ct*rw**2))
    pwd = delta_p * (2*math.pi*k*h) / (q*B*mu)
    
    t_log, p_log, dp_log = ldiffb(td, pwd)
    
    pwd2 = p_wd(Skin, Cd, td, 0)
    t_log2, p_log2, dp_log2 = ldiffb(td, pwd2)
     
    ax.plot(t_log, dp_log, linestyle='dashed', color='black')
    ax.plot(t_log, p_log, linestyle='solid', color='black', label="Field data")
    
    ax.plot(t_log2, dp_log2, linestyle='dashed', color='r')
    ax.plot(t_log2, p_log2, linestyle='solid', color='r', label="Numerical")
    ax.set_title("$Skin = {}\qquad Cs = {:0.2E}\qquad k = {:0.2E}$".format(Skin, Cs, k))
    ax.set_xlabel('$t_D$')
    ax.set_ylabel('$pw_D$')
    ax.set_xscale('log') 
    ax.set_yscale('log')
    ax.legend() 
    plt.show()
    
    
if __name__ == "__main__":
    data = read_csv('data/data.csv')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    compute_model_data(data, ax)
    plt.show()
