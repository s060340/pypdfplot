import pypdfplot as plt
import numpy as np

x = np.arange(-10,20,0.1)
y = x**2

plt.plot(x,y,'r')
plt.publish()
