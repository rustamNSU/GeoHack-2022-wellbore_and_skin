from pressure import p_wd
import math
import numpy as np
import matplotlib.pyplot as plt


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
t = np.linspace(1, 1000, 50)

Cd = Cs / ( 2*math.pi*Ct*h*rw**2 )
td = t*(k / phi*mu*Ct*rw**2)
pwD = p_wd(Skin, Cd, td)
# pwf = pwD*q*B*mu / (2*math.pi*k*h) - pi
print (pwD)
# fig, ax = plt.subplots()   
# ax.plot(td, pwD)
# ax.legend()                                     # показывать условные обозначения
# plt.show()      