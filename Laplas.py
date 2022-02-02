import math
import numpy as np
from scipy.special import kv, expi
import matplotlib.pyplot as plt

def laplace_p_wd(Skin, CD, s): 
    pwd = ( (kv(0, np.sqrt(s)) + np.sqrt(s)*Skin*kv(1, np.sqrt(s)))/(np.sqrt(s)*kv(1, np.sqrt(s)) + CD*s*(kv(0,np.sqrt(s))+np.sqrt(s)*Skin*kv(1, np.sqrt(s)))) )/s
    return pwd 
    

def exact_solution(t,r):
    return 0.5*expi(r^2/(4*t))


s = np.linspace(0, 2, 100)  

fig, ax = plt.subplots()                        

ax.plot(s, laplace_p_wd(0, 0, s), color="blue")
ax.set_yscale('log') 
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                
