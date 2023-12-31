import sympy
import numpy as np
from sympy import sin, cos
x = sympy.Symbol("x")
y = sympy.Symbol("y")

sympy.init_printing()

sympy.var('m1, m2, m3, l1,l2,l3,state_0,state_2,state_4,state_1,state_3,state_5,g')
sympy.var('a11, a12, a21, a22, b11, b12, b21, b22') 
M = sympy.Matrix([
[-1],
[-1],
[-1]
])
A = sympy.Matrix([
[(m1 + m2 + m3)* l1, (m2 + m3)*l2 * sympy.cos(state_0 - state_2), m3* l3 * sympy.cos(state_0- state_4)],
[(m2 + m3)* l1 * sympy.cos(state_2 - state_0), (m2 + m3)* l2, m3 * l3 * sympy.cos(state_2 - state_4)],
[m3 * l1 *sympy.cos(state_4 - state_0), m3 * l2 *sympy.cos(state_2 - state_4), m3* l3]
])
B = sympy.Matrix([
[(m1 + m2 + m3)*g * sympy.sin(state_0), (m2 + m3)*l2 * state_3 ** 2* sympy.sin(state_0 - state_2), m3 * l3 * state_5 **2 *sympy.sin(state_0 -state_4)],
[(m2 + m3)*l1 * state_1 ** 2 * sympy.sin(state_2 - state_0), (m2 + m3)* g * sympy.sin(state_2), m3 * l3 *state_5 ** 2 * sympy.sin(state_2 -state_4)],
[m3 * l1 *state_1 ** 2 * sympy.sin(state_4 - state_0), m3* l2 * state_3 ** 2 *sympy.sin(state_4 - state_2), m3 * g *sympy.sin(state_4)]
])

C = A.det()*A.inv()*B*M

print(sympy.simplify(A.det()))


C0 = l2*l3*m3*(-g*m3*(-m2*cos(state_0 - state_4) + m2*cos(state_0 - 2*state_2 + state_4) - m3*cos(state_0 - state_4) + m3*cos(state_0 - 2*state_2 + state_4))*sin(state_4)/2 + g*(m2 + m3)*(m2*cos(state_0 - state_2) + m3*cos(state_0 - state_2) - m3*cos(state_0 - state_4)*cos(state_2 - state_4))*sin(state_2) - g*(m1 + m2 + m3)*(m2 - m3*cos(state_2 - state_4)**2 + m3)*sin(state_0) + l1*m3*state_1**2*(-m2*cos(state_0 - state_4) + m2*cos(state_0 - 2*state_2 + state_4) - m3*cos(state_0 - state_4) + m3*cos(state_0 - 2*state_2 + state_4))*sin(state_0 - state_4)/2 - l1*state_1**2*(m2 + m3)*(2*m2*sin(2*state_0 - 2*state_2) + m3*sin(2*state_0 - 2*state_2) - m3*sin(2*state_0 - 2*state_4) + m3*sin(2*state_2 - 2*state_4))/4 + l2*m3*state_3**2*(-m2*cos(state_0 - state_4) + m2*cos(state_0 - 2*state_2 + state_4) - m3*cos(state_0 - state_4) + m3*cos(state_0 - 2*state_2 + state_4))*sin(state_2 - state_4)/2 - l2*state_3**2*(m2 + m3)*(m2 - m3*cos(state_2 - state_4)**2 + m3)*sin(state_0 - state_2) - l3*m3*state_5**2*(m2 - m3*cos(state_2 - state_4)**2 + m3)*sin(state_0 - state_4) + l3*m3*state_5**2*(m2*cos(state_0 - state_2) + m3*cos(state_0 - state_2) - m3*cos(state_0 - state_4)*cos(state_2 - state_4))*sin(state_2 - state_4))

C1 = l1*l3*m3*(g*m3*(m1*cos(state_2 - state_4) - m2*cos(state_0 - state_2)*cos(state_0 - state_4) + m2*cos(state_2 - state_4) - m3*cos(state_0 - state_2)*cos(state_0 - state_4) + m3*cos(state_2 - state_4))*sin(state_4) - g*(m2 + m3)*(m1 + m2 - m3*cos(state_0 - state_4)**2 + m3)*sin(state_2) + g*(m1 + m2 + m3)*(m2*cos(state_0 - state_2) + m3*cos(state_0 - state_2) - m3*cos(state_0 - state_4)*cos(state_2 - state_4))*sin(state_0) - l1*m3*state_1**2*(m1*cos(state_2 - state_4) - m2*cos(state_0 - state_2)*cos(state_0 - state_4) + m2*cos(state_2 - state_4) - m3*cos(state_0 - state_2)*cos(state_0 - state_4) + m3*cos(state_2 - state_4))*sin(state_0 - state_4) + l1*state_1**2*(m2 + m3)*(m1 + m2 - m3*cos(state_0 - state_4)**2 + m3)*sin(state_0 - state_2) - l2*m3*state_3**2*(2*m1*sin(2*state_2 - 2*state_4) + m2*sin(2*state_0 - 2*state_2) - m2*sin(2*state_0 - 2*state_4) + m2*sin(2*state_2 - 2*state_4) + m3*sin(2*state_0 - 2*state_2) - m3*sin(2*state_0 - 2*state_4) + m3*sin(2*state_2 - 2*state_4))/4 + l2*state_3**2*(m2 + m3)*(2*m2*sin(2*state_0 - 2*state_2) + m3*sin(2*state_0 - 2*state_2) - m3*sin(2*state_0 - 2*state_4) + m3*sin(2*state_2 - 2*state_4))/4 + l3*m3*state_5**2*(m2*cos(state_0 - state_2) + m3*cos(state_0 - state_2) - m3*cos(state_0 - state_4)*cos(state_2 - state_4))*sin(state_0 - state_4) - l3*m3*state_5**2*(m1 + m2 - m3*cos(state_0 - state_4)**2 + m3)*sin(state_2 - state_4))

C2 = l1*l2*m3*(g*(m2 + m3)*(m1*cos(state_2 - state_4) - m2*cos(state_0 - state_2)*cos(state_0 - state_4) + m2*cos(state_2 - state_4) - m3*cos(state_0 - state_2)*cos(state_0 - state_4) + m3*cos(state_2 - state_4))*sin(state_2) - g*(m1 + m2 + m3)*(-m2*cos(state_0 - state_4) + m2*cos(state_0 - 2*state_2 + state_4) - m3*cos(state_0 - state_4) + m3*cos(state_0 - 2*state_2 + state_4))*sin(state_0)/2 - l1*state_1**2*(m2 + m3)*(m1*cos(state_2 - state_4) - m2*cos(state_0 - state_2)*cos(state_0 - state_4) + m2*cos(state_2 - state_4) - m3*cos(state_0 - state_2)*cos(state_0 - state_4) + m3*cos(state_2 - state_4))*sin(state_0 - state_2) - l2*state_3**2*(m2 + m3)*(-m2*cos(state_0 - state_4) + m2*cos(state_0 - 2*state_2 + state_4) - m3*cos(state_0 - state_4) + m3*cos(state_0 - 2*state_2 + state_4))*sin(state_0 - state_2)/2 - l3*m3*state_5**2*(-m2*cos(state_0 - state_4) + m2*cos(state_0 - 2*state_2 + state_4) - m3*cos(state_0 - state_4) + m3*cos(state_0 - 2*state_2 + state_4))*sin(state_0 - state_4)/2 + l3*m3*state_5**2*(2*m1*sin(2*state_2 - 2*state_4) + m2*sin(2*state_0 - 2*state_2) - m2*sin(2*state_0 - 2*state_4) + m2*sin(2*state_2 - 2*state_4) + m3*sin(2*state_0 - 2*state_2) - m3*sin(2*state_0 - 2*state_4) + m3*sin(2*state_2 - 2*state_4))/4 + (-g*sin(state_4) + l1*state_1**2*sin(state_0 - state_4) + l2*state_3**2*sin(state_2 - state_4))*(m1*m2 + m1*m3 - m2**2*cos(state_0 - state_2)**2 + m2**2 - 2*m2*m3*cos(state_0 - state_2)**2 + 2*m2*m3 - m3**2*cos(state_0 - state_2)**2 + m3**2))