import numpy as np
import sympy as sym
import control as ctrl
from control import TransferFunction as Tf
import matplotlib.pyplot as plt


def evaluate_at_equilibrium(f):
    """
    Function to evaluate a symbolic expression with variables F, x3, and x4
    at an equilibrium point (F0, x30, x40)
    :param f: The function f with variables F, x3, and x4
    :return: The function f after evaluation at an equilibrium point (F0, x30, x40)
    """
    return f.subs([(F, F0), (x3, x30), (x4, x40)])

def pid(kp, ki, kd):
    """
    This function constructs the transfer function of a PID controller with given parameters
    :param kp: The continuous-time gain for the proportional controller
    :param ki: The continuous-time gain for the integral controller
    :param kd: The continuous-time gain for the differential controller
    :return: The transfer function for the PID controller
    """
    diff = Tf([1, 0], 1)
    intgr = Tf(1, [1, 0])
    pid_tf = kp + kd * diff + ki * intgr
    return pid_tf

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

# Define the values for constants M, m, l, and g
M_value = 0.3
m_value = 0.1
l_value = 0.35
g_value = 9.81

# Define the values for a, b, c, and d
a_value = float(a.subs([(M, M_value), (m, m_value)]))
b_value = float(b.subs([(M, M_value), (m, m_value), (g, g_value)]))
c_value = float(c.subs([(M, M_value), (m, m_value), (g, g_value), (l, l_value)]))
d_value = float(d.subs([(M, M_value), (m, m_value), (g, g_value), (l, l_value)]))

# Declare variables for helping to draw the graph
num_points = 1000  # The resolution of the graph
dt = 0.2  # Time t ranges between 0 and 0.2 seconds
t_span = np.linspace(0, dt, num_points)

# Define the input signal for the system
input_signal = np.sin(100 * t_span**2)

# Define the arrays of coefficients for the transfer functions G_theta and G_x
G_theta_num_coeffs = [c_value]
G_theta_denom_coeffs = [-1, 0, d_value]
G_x_num_coeffs = [-a_value, 0, a_value * d_value - b_value * c_value]
G_x_denom_coeffs = [-1, 0, d_value, 0, 0]

# Define the transfer functions G_theta and G_x
G_theta = Tf(G_theta_num_coeffs, G_theta_denom_coeffs)
G_x = Tf(G_x_num_coeffs, G_x_denom_coeffs)

# Determine the response of the system
G_theta_t_out, G_theta_y_out, G_theta_x_out = ctrl.forced_response(G_theta, t_span, input_signal)
G_x_t_out, G_x_y_out, G_x_x_out = ctrl.forced_response(G_x, t_span, input_signal)

# Plot the rod angle against time using the results from G_theta
plt.plot(G_theta_t_out, G_theta_y_out)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Rod Angle (rad)')
plt.savefig('figures\\question_3_a.svg', format='svg')  # Save the graph as a .svg file
plt.show()

# Plot the horizontal position against time using the results from G_x
plt.plot(G_x_t_out, G_x_y_out)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('x position (m)')
plt.savefig('figures\\question_3_b.svg', format='svg')  # Save the graph as a .svg file
plt.show()
