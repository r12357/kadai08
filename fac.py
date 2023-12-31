import sympy
sympy.init_printing()
sympy.var('m11, m12, n11, n21')
sympy.var('a11, a12, a21, a22, b11, b12, b21, b22') 
M = sympy.Matrix([
[m11,m12]
])
N = sympy.Matrix([
[n11],
[n21]
])
A = sympy.Matrix([
[a11,a12],
[a21,a22]
])
B = sympy.Matrix([
[a11+a11,a11],
[a11,a11]
])

print(sympy.simplify(A*B))