from system import System
import sympy as sym


# Pretty print all of the calculated partial derivatives
sym.pprint(System.phi_deriv_F_at_equilibrium)
sym.pprint(System.phi_deriv_x3_at_equilibrium)
sym.pprint(System.phi_deriv_x4_at_equilibrium)
sym.pprint(System.psi_deriv_F_at_equilibrium)
sym.pprint(System.psi_deriv_x3_at_equilibrium)
sym.pprint(System.psi_deriv_x4_at_equilibrium)

# Print the equations again in LaTeX format
print(sym.latex(System.phi_deriv_F_at_equilibrium))
print(sym.latex(System.phi_deriv_x3_at_equilibrium))
print(sym.latex(System.phi_deriv_x4_at_equilibrium))
print(sym.latex(System.psi_deriv_F_at_equilibrium))
print(sym.latex(System.psi_deriv_x3_at_equilibrium))
print(sym.latex(System.psi_deriv_x4_at_equilibrium))
