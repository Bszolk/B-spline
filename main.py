import numpy as np
import matplotlib.pyplot as plt


points = [[-14, 11], [-17, 3], [-13, -4], [-6, 1], [0, -4], [5, 1], [4, 13]]  # control points
P = np.array(points)
n = P.shape[0] - 1  # n + 1 -> number of control points
k = 3  # k order B-spline (polynomials of degree k-1)
T = np.arange(0, n + k + 1)  # evenly-spaced ascending vector of knots
T = (T - min(T)) / (max(T) - min(T))  # norm the knot vector to [0;1]


def basis_function(i, k, t):
    # t ∈ [T[k - 1], T[n + 1]]
    if k == 1:
        return 1 if T[i] <= t < T[i + 1] else 0
    a = (t - T[i]) / (T[i + k - 1] - T[i]) * basis_function(i, k - 1, t)
    b = (T[i + k] - t) / (T[i + k] - T[i + 1]) * basis_function(i + 1, k - 1, t)
    return a + b


dt = 0.01
C = [np.sum([(P[i] * basis_function(i, k, t)) for i in range(n + 1)], axis=0) for t in np.arange(T[k - 1], T[n + 1], dt)]

fig, (ax1, ax2) = plt.subplots(2)
x = [c[0] for c in C]
y = [c[1] for c in C]
px = [p[0] for p in points]
py = [p[1] for p in points]
ax1.plot(x, y)
ax1.plot(px, py, 'ro')
ax1.set_title('B-spline')

ax2.set_title('basis functions')
for i in range(n + 1):
    r = np.arange(0, 1, dt)
    basis_fun = [basis_function(i, k, t) for t in r]
    ax2.plot(r, basis_fun)
    ax2.axvline(T[k - 1], linestyle=':', color='k')
    ax2.axvline(T[n+1], linestyle=':', color='k')

plt.tight_layout()
plt.show()
