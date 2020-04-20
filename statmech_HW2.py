import numpy as np
import math
import matplotlib.pyplot as plt

v = np.arange(0.62, 2.6, 0.001)  # Set range manually
p = np.zeros(len(v))
t = 1.00  # Set this value 0.95, 1.00, 1.05
f = np.zeros(len(v))    # Helmholtz free energy 
g = np.zeros(len(v))   # Gibbs free energy

for i in range(len(v)) :
    p[i] = (8/3)*(t/(v[i]-(1/3))) - 3/(v[i]*v[i])         # Van der Walls equation
    f[i] = -(8/3)*t*(math.log(v[i]-1/3)) - (3/v[i])    
    g[i] = f[i] + p[i]*v[i]   

plt.plot(p, g, 'b')
plt.grid()
plt.title('Relation of $p\'$ and $g$ at $t = 1.00$')
plt.xlabel('p\'')
plt.ylabel('g = f + p\'v')
plt.show()
