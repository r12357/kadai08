from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

from numba import jit



g = 9.8  
n = 64
m = np.full(n, 1.0)
l = np.full(n, 1.0)
state = np.zeros(2 * n)
for i in range(2 * n):
    if i % 2 == 0:
        state[i] = np.random.default_rng().random() * 100
    else:
        state[i] = 0
state = np.radians(state)




@jit
def derivs(state, t):

    def pendulum(m, l, state):
        n = len(m)
        A = np.zeros((n, n))
        B = np.zeros((n,n))
        E = np.ones(n)
        
        for i in range(n):
            for j in range(n):
                for k in range(max(i,j),n):
                    A[i][j] += m[k]
                    B[i][j] += m[k]
                if i == j:
                    A[i][j] *= l[j]
                    B[i][j] *= g * np.sin(state[2 * i])
                else:
                    A[i][j] *= l[j] * np.cos(state[2 * i] - state[2 * j])
                    B[i][j] *= l[j] * state[2 * j + 1] ** 2 * np.sin(state[2 * i] - state[2 * j])
        
        return -np.linalg.inv(A) @ B @ E

    dydx = np.zeros_like(state)
    P = pendulum(m, l, state)
    count = 0
    for i in range(2 * n):
        if i % 2 == 0:
            dydx[i] = state[i + 1]
        else:
            dydx[i] = P[count]
            count += 1



    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0, 20, dt)



th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0
th3 = 20.0
w3 = 0.0
th4 = 10.0
w4 = 0.0
# initial state

# integrate your ODE using scipy.integrate.
Y = integrate.odeint(derivs, state, t)

x = np.zeros((n, len(Y[:,0])))
y = np.zeros((n, len(Y[:,0])))
for i in range(n):
    for j in range(len(Y[:,0])):
        x[i][j] = l[i] * np.sin(Y[j, 2 * i]) + x[i - 1][j]
        y[i][j] = - l[i] * np.cos(Y[j, 2 * i]) + y[i - 1][j]

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-n, n), ylim=(-n, n))
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
    thisx = list(range(n + 1))
    thisy = list(range(n + 1))
    for j in range(1, n + 1):
        thisx[j] = x[j - 1][i]
        thisy[j] = y[j - 1][i]


    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, range(1, len(Y)),
                              interval=dt*1000, blit=True, init_func=init)

# ani.save("sample6.gif", writer = "imagemagick")

plt.show()