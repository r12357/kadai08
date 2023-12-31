from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('pendulum')
        self.create_widgets()
        self.start_up()
        self.draw_plot()

    def create_widgets(self):
        '''ウィジェットの配置'''
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(side=tk.LEFT)
        self.control_frame = tk.Frame(self)
        self.control_frame.pack(side=tk.RIGHT)

        # figureの配置
        self.fig = plt.figure(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, \
                                        expand=True)

        # スライダーの配置
        self.control_label = tk.Label(self.control_frame, text='BPM:')
        self.control_label.pack(anchor=tk.NW)
        self.control_label1 = tk.Label(self.control_frame, text = "hello")
        self.control_label1.pack(anchor=tk.NW)
        self.bpm = tk.DoubleVar()
        self.x_scale = tk.Scale(self.control_frame,
            variable=self.bpm,
            from_=30.0,
            to=200.0,
            resolution=1,
            orient=tk.HORIZONTAL,
            command=self.draw_plot)
        self.x_scale.pack(anchor=tk.NW)

    def start_up(self):
        '''各種変数、グラフの定義'''
        self.bpm.set(30.0)  # 初期はBPM:30
        self.ani = None  # アニメーションを入れる変数を用意しておく
        self.g = 9.8   # 重力加速度
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(-1.2,1.2)
        self.ax.set_ylim(-1.2,1.2)
        self.im, = self.ax.plot([], [], color='k', marker='o', \
                                    markersize=12, linestyle='None')
        self.line, = self.ax.plot([], [], color='k')

    def init_ani(self):
        '''アニメーション初期化用の関数'''
        self.im.set_xdata([np.nan])
        self.im.set_ydata([np.nan])
        self.line.set_xdata([np.nan, np.nan])
        self.line.set_ydata([np.nan, np.nan])
        return self.im, self.line

    def update_anim(self, dt):
        '''グラフ更新関数'''
        self.theta = self.theta_0 * np.cos(self.omega * dt / 100)
        x = self.l * np.sin(self.theta)
        y = - self.l * np.cos(self.theta)
        self.im.set_data(x, y)
        self.line.set_data([0, np.sin(self.theta)], [0, -np.cos(self.theta)])
        return self.im, self.line

    def draw_plot(self, event=None):
        '''
        アニメーションの作成
        最初と、スライダー変更時に呼び出される
        '''
        # すでにアニメーションが実行されている場合はevent_source.stopで停止
        if self.ani is not None:
            self.ani.event_source.stop()
            self.ax.clear()
            self.ax.set_xlim(-1.2,1.2)
            self.ax.set_ylim(-1.2,1.2)
            self.im, = self.ax.plot([], [], color='k', marker='o', 
                                markersize=12, linestyle='None')
            self.line, = self.ax.plot([], [], color='k')

        self.T = round(1 / (self.bpm.get() / 60), 2) # BPを取得し、周期の計算
        self.l = (self.T ** 2) * self.g / (4 * np.pi ** 2)  # 振り子の長さを計算
        self.theta_0 = np.pi / 4               # 初期の角度
        self.omega = np.sqrt(self.g / self.l)  # 角速度

        # Reinitialize the im and line objects


        self.ani = FuncAnimation(
                self.fig,  # Figureオブジェクト
                self.update_anim,  # グラフ更新関数
                init_func=self.init_ani,  # 初期化関数
                interval = 10,  # 更新間隔(ms)
                blit = True,
                )
        self.canvas.draw()


app = Application()
app.mainloop()