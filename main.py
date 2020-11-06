import sympy as sym
import control as ctrl
import matplotlib.pyplot as plt

# Linearisation
# φ(F, x3, x4) ~ φ(F0, x30, x40) + (dφ/dF)(F0, x30, x40) * (F - F0)
#                                + (dφ/dx3)(F0, x30, x40) * (x3 - x30)
#                                + (dφ/dx4)(F0, x30, x40) * (x4 - x40)

# Define phi
# Define all involved symbolic variables
M, m, g, l = sym.symbols('M, m, g, l', real=True, positive=True)

# Define all system variables
x1, x2, x3, x4, F = sym.symbols('x1, x2, x3, x4, F')

# Define phi
phi = 4 * m * l * x4 ** 2 * sym.sin(x3) + 4 * F - 3 * m * g * sym.sin(x3) * sym.cos(x3)
phi /= 4 * (M + m) - 3 * m * sym.cos(x3) ** 2

# Determine the partial derivatives of phi wrt F, x3, x4
phi_deriv_F = phi.diff(F)
phi_deriv_x3 = phi.diff(x3)
phi_deriv_x4 = phi.diff(x4)

F0 = 0
x30 = 0
x40 = 0

phi_deriv_F_at_equilibrium = phi_deriv_F.subs([(F, F0), (x3, x30), (x4, x40)])
phi_deriv_x3_at_equilibrium = phi_deriv_x3.subs([(F, F0), (x3, x30), (x4, x40)])
phi_deriv_x4_at_equilibrium = phi_deriv_x4.subs([(F, F0), (x3, x30), (x4, x40)])

# x2' = aF - bx3
a = phi_deriv_F_at_equilibrium
b = -phi_deriv_x3_at_equilibrium
c = 3 / l / (4 * M + m)
d = 3 * (M + m) * g / l / (4 * M + m)

M_value = 0.3
m_value = 0.1
l_value = 0.35
g_value = 9.81

a_value = float(a.subs([(M, M_value), (m, m_value)]))
b_value = float(b.subs([(M, M_value), (m, m_value), (g, g_value)]))
c_value = float(c.subs([(M, M_value), (m, m_value), (g, g_value), (l, l_value)]))
d_value = float(d.subs([(M, M_value), (m, m_value), (g, g_value), (l, l_value)]))

# Only use numeric values from this point on
num_coeffs = [c_value]
denom_coeffs = [-1, 0, d_value]
G_theta = ctrl.TransferFunction(num_coeffs, denom_coeffs)


def pid(kp, ki, kd):
    # This function constructs the transfer function of a PID controller with given parameters
    diff = ctrl.TransferFunction([1, 0], 1)
    intgr = ctrl.TransferFunction(1, [1, 0])
    pid_tf = kp + kd * diff + ki * intgr
    return pid_tf


my_pid = -pid(10, 0.5, 3)
tf_closed_loop_system = ctrl.feedback(G_theta, my_pid)
t_imp, theta_imp = ctrl.impulse_response(tf_closed_loop_system)
t_step, theta_step = ctrl.step_response(tf_closed_loop_system)

plt.plot(t_imp, theta_imp)
plt.plot(t_step, theta_step)
plt.grid()
plt.show()
