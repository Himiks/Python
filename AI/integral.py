import sympy as sp

x = sp.Symbol('x')
f = x**2
def_intg = sp.integrate(f, (x, 0, 2))
indef_intg = sp.integrate(f, x)
print(def_intg)
print(indef_intg)



x = sp.Symbol('x')
f = sp.exp(-x)

indef_ing = sp.integrate(f, x)
print(indef_ing)


def_intg = sp.integrate(f, (x, 0, sp.oo))
print(def_intg)