## Calculates and plots **k** order b-spline curve for given control points

$`k`$ order b-spline curve at point **t** is defined using control points $`P_i`$ and basis functions $`f_{i, k}(t)`$:
```math
C(t) = \sum_{i=0}^{n} P_i f_{i, k}(t), \quad t \in [T_{k-1}, T_{n+1}]
```

Where each basis function is recurrently defined as: 
```math 
\textrm{if } k=1 \textrm{ then} \quad f_{i, k}(t) = \left\{ \begin{array}{ c l } 1 & \quad \textrm{if } T_{i} \leq t \le T_{i+1} \\ 0 & \quad \textrm{otherwise} \end{array} \right.
```
```math
\textrm{else } \quad f_{i, k}(t) = \frac{t - T_{i}}{T_{i+k-1} - T_{i}}f_{i, k-1}(t) + \frac{T_{i+k} - t}{T_{i+k} - T_{i+1}}f_{i+1, k-1}(t)
```

T is a equally spaced ascending knot vector normalized to $`[0, 1]`$:
```math
T = (t_{0}, t_{1}, ..., t_{n+k}), \quad \textrm{where } n + 1 \textrm{ is total number of control points}
```
