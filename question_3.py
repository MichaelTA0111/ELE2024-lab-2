import main
import sympy as sym
from sympy import inverse_laplace_transform as ilt

# Define symbols to store the partial derivatives as coefficients
main.a, main.b, main.c, main.d = sym.symbols('a:d', real=True, positive=True)

# Define the transfer functions G_theta and G_x
G_theta = main.c / (main.d - main.s**2)
G_x = (main.a * main.d - main.a * main.s**2 - main.b * main.c) / (main.d * main.s**2 - main.s**4)

# Define F in the s domain for impulse, step, and frequency response
F_s_impulse = 1
F_s_step = 1 / main.s
F_s_frequency = main.w / (main.s**2 + main.w**2)

# Define the impulse, step, and frequency responses for X3_s and X1_s (s domain)
X3_s_impulse = G_theta * F_s_impulse
X3_s_step = G_theta * F_s_step
X3_s_frequency = G_theta * F_s_frequency
X1_s_impulse = G_x * F_s_impulse
X1_s_step = G_x * F_s_step
X1_s_frequency = G_x * F_s_frequency

# Define the impulse, step, and frequency responses for x3_t and x1_t (t domain)
x3_t_impulse = ilt(X3_s_impulse, main.s, main.t)
x3_t_step = ilt(X3_s_step, main.s, main.t)
x3_t_frequency = ilt(X3_s_frequency, main.s, main.t, main.w)
x1_t_impulse = ilt(X1_s_impulse, main.s, main.t)
x1_t_step = ilt(X1_s_step, main.s, main.t)
x1_t_frequency = ilt(X1_s_frequency, main.s, main.t, main.w)

# Pretty print all of the calculated responses in the t domain
sym.pprint(x3_t_impulse.simplify())
sym.pprint(x3_t_step.simplify())
sym.pprint(x3_t_frequency.simplify())
sym.pprint(x1_t_impulse.simplify())
sym.pprint(x1_t_step.simplify())
sym.pprint(x1_t_frequency.simplify())

# Print the equations again in LaTeX format
print(sym.latex(x3_t_impulse.simplify()))
print(sym.latex(x3_t_step.simplify()))
print(sym.latex(x3_t_frequency.simplify()))
print(sym.latex(x1_t_impulse.simplify()))
print(sym.latex(x1_t_step.simplify()))
print(sym.latex(x1_t_frequency.simplify()))
