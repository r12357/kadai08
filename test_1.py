from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from scipy.integrate import odeint




class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('pendulum_var.01')
        self.create_widgets()
        self.start_up()
        # self.draw_plot()

    def create_widgets(self):
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(side = tk.LEFT)
        self.control_frame = tk.Frame(self)
        self.control_frame.pack(side = tk.RIGHT)

        self.fig = plt.figure(figsize = (6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, 
                                        expand = True)
        # 設定用のwidgetを作成する
        self.control_run_button = tk.Button(self.control_frame, 
                                            text = "RUN",
                                            width = 20,
                                            height = 5,
                                            command = self.draw_plot)
        self.control_run_button.pack(side = tk.BOTTOM)
        
    def func(self, state, t):
        dydt = np.zeros_like(state)
        dydt[0] = state[1]
        dydt[1] = -(self.g / self.l)*np.sin(state[0])
        return dydt
    
    def derivs(self, state, t):
        dydx = np.zeros_like(state)
        dydx[0] = state[1]

        self.del_ = state[2] - state[0]
        self.den1 = (self.m1 + self.m2)*self.l1 - self.m2*self.l1*np.cos(self.del_)*np.cos(self.del_)
        dydx[1] = (self.m2*self.l1*state[1]*state[1]*np.sin(self.del_)*np.cos(self.del_) +
                self.m2*self.g*np.sin(state[2])*np.cos(self.del_) +
                self.m2*self.l2*state[3]*state[3]*np.sin(self.del_) -
                (self.m1 + self.m2)*self.g*np.sin(state[0]))/self.den1

        dydx[2] = state[3]

        self.den2 = (self.l2/self.l1)*self.den1
        dydx[3] = (-self.m2*self.l2*state[3]*state[3]*np.sin(self.del_)*np.cos(self.del_) +
                (self.m1 + self.m2)*self.g*np.sin(state[0])*np.cos(self.del_) -
                (self.m1 + self.m2)*self.l1*state[1]*state[1]*np.sin(self.del_) -
                (self.m1 + self.m2)*self.g*np.sin(state[2]))/self.den2
        
        return dydx
    
    def start_up(self):
        self.ani = None
        self.g = 9.8
        self.l1 = 4.0
        self.l2 = 2.0
        self.m1 = 1.0
        self.m2 = 1.0
    
        # tmp用の変数
        self.node = 2
        self.th1 = 120.0
        self.w1 = 0.0
        self.th2 = -10.0
        self.w2 = 0.0
        state = np.radians([self.th1, self.w1, self.th2, self.w2])
        self.dt = 0.05
        self.t = np.arange(0.0, 20, self.dt)
        self.sol = odeint(self.derivs, state, self.t)
        print(self.sol)
        self.theta1 = self.sol[:, 0]
        self.theta2 = self.sol[:, 2]
        self.x1 = self.l1 * np.sin(self.theta1)
        self.y1 = - self.l1 * np.cos(self.theta1)
        self.x2 = self.l2 * np.sin(self.theta2) + self.x1
        self.y2 = - self.l2 * np.cos(self.theta2) + self.y1



        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(-(self.l1 + self.l2 + 0.5), self.l1 + self.l2 + 0.5)
        self.ax.set_ylim(-(self.l1 + self.l2 + 0.5), self.l1 + self.l2 + 0.5)
        self.im, = self.ax.plot([], [], color = "k", marker = "o",
                                markersize = 10, linestyle = "None")
        self.im1, = self.ax.plot([], [], color = "k", marker = "o",
                                markersize = 10, linestyle = "None")
        self.line, = self.ax.plot([], [], color = "k")
        self.scatter = self.ax.scatter([], [], marker = "o", s = 10, color = "k")

    def init_ani(self):
        self.im.set_xdata([np.nan])
        self.im.set_ydata([np.nan])
        self.line.set_xdata([np.nan, np.nan])
        self.line.set_ydata([np.nan, np.nan])
        return self.im, self.line
    
    def update_ani(self, dt):
        self.thisx = [0, self.x1[dt], self.x2[dt]]
        self.thisy = [0, self.y1[dt], self.y2[dt]]
        
        self.line.set_data(self.thisx, self.thisy)
        self.im.set_data(self.x1[dt], self.y1[dt])
        self.im1.set_data(self.x2[dt], self.y2[dt])


        
        return self.im, self.im1, self.line, 

    def draw_plot(self, event = None):
        if self.ani is not None:
            self.ani.event_source.stop()
            self.ax.clear()
            self.ax.set_xlim(-(self.l1 + self.l2 + 0.5), self.l1 + self.l2 + 0.5)
            self.ax.set_ylim(-(self.l1 + self.l2 + 0.5), self.l1 + self.l2 + 0.5)
            self.im, = self.ax.plot([], [], color = "k", marker = "o",
                                markersize = 10, linestyle = "None")
            self.im1, = self.ax.plot([], [], color = "k", marker = "o",
                                markersize = 10, linestyle = "None")
            self.line, = self.ax.plot([], [], color = "k")

        # アニメーションの処理
        # for num in range(4):
        #     self.ax.scatter(self.x2[dt + num], self.y2[dt + num], marker = "o", s = 10, color = "k", alpha = num/(4 + 1))


        self.ani = FuncAnimation(
                self.fig,
                self.update_ani,
                init_func = self.init_ani,
                interval = 25,
                blit = True,
                )
        self.canvas.draw()
        # self.ani.save("sample4.gif", writer = "imagemagick")



app = Application()
app.mainloop()