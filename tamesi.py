import sympy
import numpy 

t = sympy.Symbol("t")

x = sympy.Function("x")(t)

eq = sympy.Eq(sympy.Derivative(x,t,2),-9.8*sympy.sin(x))

a = sympy.dsolve(eq,x, ics={x.subs(t,0):1/10})

print("a")