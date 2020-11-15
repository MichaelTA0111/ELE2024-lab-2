import sympy as sym
from sympy import inverse_laplace_transform as ilt


def evaluate_at_equilibrium(f):
    """
    Function to evaluate a symbolic expression with variables F, x3, and x4
    at an equilibrium point (F0, x30, x40)
    :param f: The function f with variables F, x3, and x4
    :return: The function f after evaluation at an equilibrium point (F0, x30, x40)
    """
    return f.subs([(F, F0), (x3, x30), (x4, x40)])

# Linearisation
#
# φ(F, x3, x4) ~ φ(F0, x30, x40) + (dφ/dF)(F0, x30, x40)  * (F - F0)
#                                + (dφ/dx3)(F0, x30, x40) * (x3 - x30)
#                                + (dφ/dx4)(F0, x30, x40) * (x4 - x40)
#
# ψ(F, x3, x4) ~ ψ(F0, x30, x40) + (dψ/dF)(F0, x30, x40)  * (F - F0)
#                                + (dψ/dx3)(F0, x30, x40) * (x3 - x30)
#                                + (dψ/dx4)(F0, x30, x40) * (x4 - x40)

# Define all involved symbolic variables
M, m, g, l = sym.symbols('M, m, g, l', real=True, positive=True)

# Define all system variables
x1, x2, x3, x4, F = sym.symbols('x1, x2, x3, x4, F')

# Define symbols s, t, and w for laplace transformations
s, t = sym.symbols('s, t')
w = sym.symbols('w', real=True)

# Define φ (phi) according to equation 3.2a
phi = 4 * m * l * x4 ** 2 * sym.sin(x3) + 4 * F - 3 * m * g * sym.sin(x3) * sym.cos(x3)  # Numerator
phi /= 4 * (M + m) - 3 * m * sym.cos(x3) ** 2  # Denominator

# Define ψ (psi) according to equation 3.2b
psi = m * l * x4 ** 2 * sym.sin(x3) * sym.cos(x3) + F * sym.cos(x3) - (M + m) * g * sym.sin(x3)  # Numerator
psi /= (4 * (M + m) - 3 * m * sym.cos(x3)**2) * l  # Denominator
psi *= -3  # Multiplier of the fraction

# Determine the partial derivatives of φ (phi) wrt F, x3, x4
phi_deriv_F = phi.diff(F)
phi_deriv_x3 = phi.diff(x3)
phi_deriv_x4 = phi.diff(x4)

# Determine the partial derivatives of ψ (psi) wrt F, x3, x4
psi_deriv_F = psi.diff(F)
psi_deriv_x3 = psi.diff(x3)
psi_deriv_x4 = psi.diff(x4)

# Define the values of the input variables at an equilibrium point
F0 = 0
x30 = 0
x40 = 0

# Substitute the input variables at an equilibrium point into φ (phi)
phi_deriv_F_at_equilibrium = evaluate_at_equilibrium(phi_deriv_F)
phi_deriv_x3_at_equilibrium = evaluate_at_equilibrium(phi_deriv_x3)
phi_deriv_x4_at_equilibrium = evaluate_at_equilibrium(phi_deriv_x4)

# Substitute the input variables at an equilibrium point into ψ (psi)
psi_deriv_F_at_equilibrium = evaluate_at_equilibrium(psi_deriv_F)
psi_deriv_x3_at_equilibrium = evaluate_at_equilibrium(psi_deriv_x3)
psi_deriv_x4_at_equilibrium = evaluate_at_equilibrium(psi_deriv_x4)

# x2' = aF - bx3
a = phi_deriv_F_at_equilibrium
b = -phi_deriv_x3_at_equilibrium

# x4' = -cF + dx3
c = -psi_deriv_F_at_equilibrium
d = psi_deriv_x3_at_equilibrium

# Define symbols to store the partial derivatives as coefficients
a, b, c, d = sym.symbols('a, b, c, d', real=True, positive=True)

# Define the transfer functions G_theta and G_x
G_theta = c / (d - s**2)
G_x = (a * d - a * s**2 - b * c) / (d * s**2 - s**4)

# Define F in the s domain for impulse, step, and frequency response
F_s_impulse = 1
F_s_step = 1 / s
F_s_frequency = w / (s**2 + w**2)

# Define the impulse, step, and frequency responses for X3_s and X1_s (s domain)
X3_s_impulse = G_theta * F_s_impulse
X3_s_step = G_theta * F_s_step
X3_s_frequency = G_theta * F_s_frequency
X1_s_impulse = G_x * F_s_impulse
X1_s_step = G_x * F_s_step
X1_s_frequency = G_x * F_s_frequency

# Define the impulse, step, and frequency responses for x3_t and x1_t (t domain)
x3_t_impulse = ilt(X3_s_impulse, s, t)
x3_t_step = ilt(X3_s_step, s, t)
x3_t_frequency = ilt(X3_s_frequency, s, t, w)
x1_t_impulse = ilt(X1_s_impulse, s, t)
x1_t_step = ilt(X1_s_step, s, t)
x1_t_frequency = ilt(X1_s_frequency, s, t, w)

# Pretty print all of the calculated responses in the t domain
sym.pprint(x3_t_impulse.simplify())
sym.pprint(x3_t_step.simplify())
sym.pprint(x3_t_frequency.simplify())
sym.pprint(x1_t_impulse.simplify())
sym.pprint(x1_t_step.simplify())
sym.pprint(x1_t_frequency.simplify())
