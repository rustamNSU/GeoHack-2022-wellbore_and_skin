import math
import numpy as np
from scipy.special import kv, k0, k1, expi
import matplotlib.pyplot as plt
import mpmath as mp
  

def exact_solution(t, r):
    return -0.5*expi( -r**2 / (4*t) )

def laplace_p_wd(Skin, CDstor, s): 
    pwd = (k0(math.sqrt(s)) + math.sqrt(s)*Skin*k1(math.sqrt(s))) / ( ( math.sqrt(s)*k1(math.sqrt(s) ) + CDstor*s*( k0(math.sqrt(s)) + math.sqrt(s)*Skin*k1(math.sqrt(s)) ) ) * s)
    return pwd 
    


fp = lambda p: laplace_p_wd(0.0, 0.0, p)

tt = np.linspace(1, 1000, 50)

fig, ax = plt.subplots()   

ax.plot(tt, [mp.invertlaplace(fp, t, method='stehfest', degree = 20) for t in tt], color="blue")
ax.plot(tt, [exact_solution(t, 1.0) for t in tt], color="red")
# ax.set_yscale('log') 
# ax.set_xlabel("x")                              # подпись у горизонтальной оси х
# ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                
