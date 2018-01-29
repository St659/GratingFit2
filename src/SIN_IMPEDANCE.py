import numpy as np

import matplotlib.pylab as plt

x = np.linspace(-2*np.pi, 2*np.pi, 401)
plt.plot(x, 0.5*np.cos(x), 'r')
plt.ylim([-1,1])
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
#plt.axis('tight')
plt.show()