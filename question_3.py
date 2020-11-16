from System import System
import sympy as sym
from sympy import inverse_laplace_transform as ilt

# Define symbols to store the partial derivatives as coefficients
System.a, System.b, System.c, System.d = sym.symbols('a:d', real=True, positive=True)

# Define the transfer functions G_theta and G_x
G_theta = System.c / (System.d - System.s ** 2)
G_x = (System.a * System.d - System.a * System.s ** 2 - System.b * System.c) / (System.d * System.s ** 2 - System.s ** 4)

# Define F in the s domain for impulse, step, and frequency response
F_s_impulse = 1
F_s_step = 1 / System.s
F_s_frequency = System.w / (System.s ** 2 + System.w ** 2)

# Define the impulse, step, and frequency responses for X3_s and X1_s (s domain)
X3_s_impulse = G_theta * F_s_impulse
X3_s_step = G_theta * F_s_step
X3_s_frequency = G_theta * F_s_frequency
X1_s_impulse = G_x * F_s_impulse
X1_s_step = G_x * F_s_step
X1_s_frequency = G_x * F_s_frequency

# Define the impulse, step, and frequency responses for x3_t and x1_t (t domain)
x3_t_impulse = ilt(X3_s_impulse, System.s, System.t).simplify()
x3_t_step = ilt(X3_s_step, System.s, System.t).simplify()
x3_t_frequency = ilt(X3_s_frequency, System.s, System.t, System.w).simplify()
x1_t_impulse = ilt(X1_s_impulse, System.s, System.t).simplify()
x1_t_step = ilt(X1_s_step, System.s, System.t).simplify()
x1_t_frequency = ilt(X1_s_frequency, System.s, System.t, System.w).simplify()

# Pretty print all of the calculated responses in the t domain
sym.pprint(x3_t_impulse)
sym.pprint(x3_t_step)
sym.pprint(x3_t_frequency)
sym.pprint(x1_t_impulse)
sym.pprint(x1_t_step)
sym.pprint(x1_t_frequency)

# Print the equations again in LaTeX format
print(sym.latex(x3_t_impulse))
print(sym.latex(x3_t_step))
print(sym.latex(x3_t_frequency))
print(sym.latex(x1_t_impulse))
print(sym.latex(x1_t_step))
print(sym.latex(x1_t_frequency))
