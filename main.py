
import sys
import tkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.integrate import odeint
from numpy import sin, cos, pi
from matplotlib.animation import FuncAnimation


G  = 9.8         # 重力加速度
L = 2            # 振り子の長さ

th1 = 60.0      # 角度の初期値[deg]
w1 = 0.0        # 角速度の初期値[deg]


def func(state, t):
    dydt = np.zeros_like(state)
    dydt[0] = state[1]
    dydt[1] = -(G/L)*sin(state[0])
    return dydt

def pendulum():


    # 初期状態
    state = np.radians([th1, w1])

    dt = 0.05
    t = np.arange(0.0, 20, dt)

    sol = odeint(func, state, t)

    theta = sol[:, 0]
    x = L * sin(theta)
    y = - L * cos(theta)

    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-L, L), ylim=(-L, L))
    ax.set_aspect('equal')
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)

    def animate(i):
        thisx = [0, x[i]]
        thisy = [0, y[i]]

        line.set_data(thisx, thisy)
        return line,

    ani = FuncAnimation(fig, animate, frames=np.arange(0, len(t)),interval=25,  blit = True)

    plt.show()

    return ani

root = tkinter.Tk()
root.title(u"title")
root.geometry("700x400")

frame = tkinter.Frame(root, height = 100, width = 200, 
                      relief = "sunken", borderwidth = "1",
                      cursor = "cross")
frame.pack()

canvas = FigureCanvasTkAgg(pendulum(), master = root)
canvas.draw()
canvas.get_tk_widget().pack()


root.mainloop()




if __name__ == "__main__":
    print("pythonですわぁ")