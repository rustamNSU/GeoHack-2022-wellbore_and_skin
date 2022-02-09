import mpmath as mp
import math

tt = [0.001, 0.01, 0.1, 1, 10]
fp = lambda p: 1 / (p+1)**2
ft = lambda t: t*math.exp(-t)

print([[ft(t), ft(t) - mp.invertlaplace(fp, t, method='stehfest')] for t in tt])