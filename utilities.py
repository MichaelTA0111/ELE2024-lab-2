from control import TransferFunction as Tf


def evaluate_at_equilibrium(f, F, F0, x3, x30, x4, x40):
    """
    Function to evaluate a symbolic expression with variables F, x3, and x4
    at an equilibrium point (F0, x30, x40)
    :param f: The function f with variables F, x3, and x4
    :param F: System variable F
    :param F0: Initial value of variable F
    :param x3: System variable x3
    :param x30: Initial value of variable x3
    :param x4: System variable x4
    :param x40: Initial value of variable x4
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
