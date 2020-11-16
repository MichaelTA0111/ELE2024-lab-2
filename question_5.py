from system import System
import numpy as np
from utilities import pid
import control as ctrl
from control import impulse_response as ir
import matplotlib.pyplot as plt


# Declare variables for helping to draw the graph
num_points = 1000  # The resolution of the graph
dt = 1  # Time t ranges between 0 and 1 seconds

# Define the PID controller to be used
my_kp = 150
my_ki = 0.5
my_kd = 10
my_pid = -pid(my_kp, my_ki, my_kd)

# Use closed loop feedback to combine the PID controller with the System
tf_theta = ctrl.feedback(System.G_theta, my_pid)
t_imp, theta_imp = ir(tf_theta, T=np.linspace(0, dt, num_points))
theta_imp_deg = np.rad2deg(theta_imp)

# Plot the rod angle against time using the results from G_theta
plt.plot(t_imp, theta_imp_deg)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Rod Angle (deg)')
plt.savefig('figures\\question_5.svg', format='svg')  # Save the graph as a .svg file
plt.show()
