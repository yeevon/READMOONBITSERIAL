import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

class GraphData:

    def __init__(self):
        # Create data lists
        self._interval = []
        self._light = []
        self._temp = []

        # Figures/axes/lines
        self._fig, (self._ax1, self._ax2) = plt.subplots(2, 1, sharex=True)
        self._line_light, = self._ax1.plot([], [])
        self._ax1.set_title("Light")
        self._ax1.set_xlabel("Interval")
        self._ax1.set_ylabel("Light Value")

        self._line_temp, = self._ax2.plot([], [])
        self._ax2.set_title("Temp")
        self._ax2.set_xlabel("Interval")
        self._ax2.set_ylabel("°C")

        plt.tight_layout()
        plt.ion()
        plt.show()

        
    def input_plot_data(self, interval, light, temp):
        self._interval.append(interval)
        self._light.append(light)
        self._temp.append(temp)
        self.update_graph()


    def update_graph(self):

        self._line_light.set_data(self._interval, self._light)
        self._line_temp.set_data(self._interval, self._temp)
        self._ax1.relim(); self._ax1.autoscale_view()
        self._ax2.relim(); self._ax2.autoscale_view()
        self._fig.canvas.draw_idle(); plt.pause(0.05)

    def stop_graph(self):
        self._fig.savefig("../logs/final_graph.png")
        plt.close(self._fig)
