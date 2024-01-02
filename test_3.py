from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

g = 9.8  # acceleration due to gravity, in m/s^2
l2 = 1.0  # length of pendulum 1 in m
l1 = 1.0  # length of pendulum 2 in m
m1 = 1.0  # mass of pendulum 1 in kg
m2 = 1.0  # mass of pendulum 2 in kg

def pendulum(m1, m2, l1, l2, th1, th2, omega1, omega2):
    A1 = np.array([
        [(m1 + m2) * l1, m2 * l2 * np.cos(th1 - th2)],
        [m2 * l1 * np.cos(th1 - th2), m2 * l2]
        ])

    B1 = np.array([
        [(m1 + m2) * g * np.sin(th1), m2 * l2 * omega2 ** 2 * np.sin(th1 - th2)],
        [m2 * l1 * omega1 ** 2 * np.sin(th2 - th1), m2 * g * np.sin(th2)]
        ])
    M = np.array([
        [-1],
        [-1]])
    return np.linalg.inv(A1) @ B1 @ M

def derivs(state, t):

    dydx = np.zeros_like(state)
    P = pendulum(m1, m2, l1, l2, state[0], state[2], state[1], state[3])
    dydx[0] = state[1]

    dydx[1] = P[0]

    dydx[2] = state[3]

    dydx[3] = P[1]

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = l1*sin(y[:, 0])
y1 = -l1*cos(y[:, 0])

x2 = l2*sin(y[:, 2]) + x1
y2 = -l2*cos(y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                              interval=dt*1000, blit=True, init_func=init)
plt.show()