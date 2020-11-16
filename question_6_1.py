from System import System
import numpy as np
from Utilities import Utilities
import control as ctrl
from control import impulse_response as ir
import matplotlib.pyplot as plt


# Declare variables for helping to draw the graph
num_points = 1000  # The resolution of the graph
dt = 1  # Time t ranges between 0 and 1 seconds

# Use the same PID controller from Question 5
my_kp = 150
my_ki = 0.5
my_kd = 10
my_pid = -Utilities.pid(my_kp, my_ki, my_kd)

# Use closed loop feedback to combine the PID controller with the System
tf_x = ctrl.feedback(System.G_x, my_pid)
t_imp, x_imp = ir(tf_x, T=np.linspace(0, dt, num_points))

# Plot the rod angle against time using the results from G_theta
plt.plot(t_imp, x_imp)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('x Position (m)')
plt.savefig('figures\\question_6_1.svg', format='svg')  # Save the graph as a .svg file
plt.show()
