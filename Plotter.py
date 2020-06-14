import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker


class Plotter:
    def __init__(self, x_range):
        self.x = x_range
        self.range = np.arange(0, x_range + 0.1, 0.1)

    def plot(self):
        self.graph(self.exponential(2), '1 act per Week')
        self.graph(self.exponential(3), '2 acts per Week')
        self.graph(self.exponential(4), '3 acts per Week')

        self.format()

        plt.savefig('Graph.png', dpi=300)
        plt.show(block=False)

    def graph(self, formula, legend):
        x = self.range
        y = formula(x)
        plt.plot(x, y, label=legend)

    @staticmethod
    def exponential(value):
        def formula(x):
            return value ** x
        return formula

    def format(self):
        axs = plt.gca()

        axs.set_xlim(xmin=0, xmax=self.x)
        axs.set_ylim(ymin=0)

        axs.margins(y=0, x=0)

        plt.grid(True)

        loc = plticker.MultipleLocator(1)
        axs.xaxis.set_major_locator(loc)

        plt.legend(loc="upper left")

        plt.xlabel('Weeks')
        plt.ylabel('People Affected')

        plt.title("The Power of Kindness")


Plotter(3).plot()
