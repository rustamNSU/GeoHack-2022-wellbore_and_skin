import math
import numpy as np
from scipy.special import kv, k0, k1, expi
import matplotlib.pyplot as plt
import mpmath as mp

# def laplace_p_wd(Skin, CD, s): 
#     pwd = ( (kv(0, np.sqrt(s)) + np.sqrt(s)*Skin*kv(1, np.sqrt(s)))/(np.sqrt(s)*kv(1, np.sqrt(s)) + CD*s*(kv(0,np.sqrt(s))+np.sqrt(s)*Skin*kv(1, np.sqrt(s)))) )/s
#     return pwd 
    

def exact_solution(t, r):
    return -expi(-r^2/(4*t))

def laplace_p_wd(Skin, CDstor, s): 
    pwd = ((k0(math.sqrt(s)) + math.sqrt(s)*Skin*k1(math.sqrt(s)))/(math.sqrt(s)*k1(math.sqrt(s)) + CDstor*s*(k0(math.sqrt(s))+math.sqrt(s)*Skin*k1(math.sqrt(s)))))/s
    return pwd 
    

s = np.linspace(0, 2, 100)  


fp = lambda p: laplace_p_wd(0.0, 0.0, p)

tt = [1.0, 10.0, 100.0]
print([mp.invertlaplace(fp, t, method='stehfest') for t in tt])
# print(mp.invertlaplace(fp, 1.0, method='stehfest'))

# fig, ax = plt.subplots()                        

# ax.plot(s, laplace_p_wd(0, 0, s), color="blue")
# ax.set_yscale('log') 
# ax.set_xlabel("x")                              # подпись у горизонтальной оси х
# ax.set_ylabel("y")                              # подпись у вертикальной оси y
# ax.legend()                                     # показывать условные обозначения

# plt.show()                                
