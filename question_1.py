from main import *
import sympy as sym


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
