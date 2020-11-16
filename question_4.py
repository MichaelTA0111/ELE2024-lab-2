from system import System
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt


# Declare variables for helping to draw the graph
num_points = 1000  # The resolution of the graph
dt = 0.2  # Time t ranges between 0 and 0.2 seconds
t_span = np.linspace(0, dt, num_points)

# Define the input signal for the System
input_signal = np.sin(100 * t_span ** 2)

# Determine the response of the System
G_theta_t_out, G_theta_y_out, G_theta_x_out = ctrl.forced_response(System.G_theta, t_span, input_signal)
G_x_t_out, G_x_y_out, G_x_x_out = ctrl.forced_response(System.G_x, t_span, input_signal)

# Plot the rod angle against time using the results from G_theta
plt.plot(G_theta_t_out, G_theta_y_out)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Rod Angle (rad)')
plt.savefig('figures\\question_4_a.svg', format='svg')  # Save the graph as a .svg file
plt.show()

# Plot the horizontal position against time using the results from G_x
plt.plot(G_x_t_out, G_x_y_out)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('x position (m)')
plt.savefig('figures\\question_4_b.svg', format='svg')  # Save the graph as a .svg file
plt.show()
