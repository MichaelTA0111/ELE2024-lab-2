import sympy as sym


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

# Define all system input variables
x1, x2, x3, x4, F = sym.symbols('x1, x2, x3, x4, F')

# Define φ (phi) according to equation 3.2a
phi = 4 * m * l * x4**2 * sym.sin(x3) + 4 * F - 3 * m * g * sym.sin(x3) * sym.cos(x3)  # Numerator
phi /= 4 * (M + m) - 3 * m * sym.cos(x3) ** 2  # Denominator

# Define ψ (psi) according to equation 3.2b
psi = m * l * x4**2 * sym.sin(x3) * sym.cos(x3) + F * sym.cos(x3) - (M + m) * g * sym.sin(x3)  # Numerator
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

# Pretty print all of the calculated partial derivatives
sym.pprint(phi_deriv_F_at_equilibrium)
sym.pprint(phi_deriv_x3_at_equilibrium)
sym.pprint(phi_deriv_x4_at_equilibrium)
sym.pprint(psi_deriv_F_at_equilibrium)
sym.pprint(psi_deriv_x3_at_equilibrium)
sym.pprint(psi_deriv_x4_at_equilibrium)

# Print the equations again in LaTeX format
print(sym.latex(phi_deriv_F_at_equilibrium))
print(sym.latex(phi_deriv_x3_at_equilibrium))
print(sym.latex(phi_deriv_x4_at_equilibrium))
print(sym.latex(psi_deriv_F_at_equilibrium))
print(sym.latex(psi_deriv_x3_at_equilibrium))
print(sym.latex(psi_deriv_x4_at_equilibrium))
