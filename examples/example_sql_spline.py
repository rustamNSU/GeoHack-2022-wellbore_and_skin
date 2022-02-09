import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline, LSQUnivariateSpline
import numpy as np
#x and y array definition (initial set of data points)
x = np.linspace(0, 10, 30)
y = np.sin(0.5*x)*np.sin(x*np.random.randn(30))



#spline definition  
spline = UnivariateSpline(x, y, s = 3)

x_spline = np.linspace(0, 10, 1000)
y_spline = spline(x_spline)
#Plotting
fig = plt.figure()
ax = fig.subplots()
ax.scatter(x, y)
ax.plot(x_spline, y_spline, 'g')
plt.show()