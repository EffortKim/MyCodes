#### Drawing p-v graph minimizing g

v = np.arange(0.62, 2.6, 0.001)
p = np.zeros(len(v))
t = 0.95
f = np.zeros(len(v))
g = np.zeros(len(v))
v_temp = np.zeros(len(v))
g_temp = np.zeros(len(v))
p_temp = np.zeros(len(v))
v_min = np.zeros(len(v))
p_min = np.zeros(len(v))
g_min = np.zeros(len(v))

for i in range(len(v)) : 
    p[i] = (8/3)*(t/(v[i]-(1/3))) - 3/(v[i]*v[i])  # Van der Walls equation
    f[i] = -(8/3)*t*(math.log(v[i]-1/3)) - (3/v[i])   # Helmholtz free energy  
    g[i] = f[i] + p[i]*v[i]   # Gibbs free energy

for i in range(len(v)) : # Get p-v graph minimizing g
    v_temp[i] = v[i]
    p_temp[i] = p[i]
    g_temp[i] = g[i]
    for j in range(len(v)) :
        if (abs(p[i] - p[j]) < 0.001) : # Select p minimizing g
            if (abs(i-j) < 10) : continue  # prevent picking neighborhood points
            if (g[i] > g[j]) : 
                g_temp[i] = g[j]
                v_temp[i] = v[j]
                p_temp[i] = p[j]
            else : 
                g_temp[i] = g[i]
                v_temp[i] = v[i]
                p_temp[i] = p[i]

v2 = np.flip(v_temp)
p2 = np.flip(p_temp)
g2 = np.flip(g_temp)

for i in range(len(v)) :
    g_min[i] = g2[i]
    v_min[i] = v2[i]
    p_min[i] = p2[i]
    for j in range(len(v)) :
        if (abs(p2[i] - p2[j]) < 0.0015) : # Select p minimizing g
            if (abs(i-j) < 10) : continue  # prevent picking neighborhood points
            if (g2[i] > g2[j]) : 
                g_min[i] = g2[j]
                v_min[i] = v2[j]
                p_min[i] = p2[j]
            else : 
                g_min[i] = g2[i]
                v_min[i] = v2[i]
                p_min[i] = p2[i]

plt.plot(p, v, 'b', label='original VdW graph')
plt.plot(p_min, v_min, 'r', label='stable state graph')
plt.grid()
plt.title('$p$-$v$ graph of stable state at $t = 0.95$')
plt.xlabel('v')
plt.ylabel('p')
plt.legend()
plt.show()
