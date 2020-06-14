import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker


# Class that does the graphing
class Plotter:
    def __init__(self, x_range):
        # x_range is the maximum value that the graph will go to

        self.x = x_range                                # Store as local var
        self.range = np.arange(0, x_range + 0.1, 0.1)   # Create the x-axis values

    # Plots and displays the graph, main function
    def plot(self):
        self.graph(self.exponential(2), '1 act per Week')   # Plot graph
        self.graph(self.exponential(3), '2 acts per Week')  # Plot graph
        self.graph(self.exponential(4), '3 acts per Week')  # Plot graph

        self.format()   # Does some formatting to make the graph look good

        plt.savefig('Graph.png', dpi=300)   # Saves to file in HD format
        plt.show()                          # Displays the graph

    # Plots the graph on the PyPlot figure
    def graph(self, formula, legend):
        # The `formula` arg is actually a python function which takes 1 int
        # This is then used to turn the x values into y values

        x = self.range  # Copy the np array to a local var to prevent accidental editing
        y = formula(x)  # Turn each value in the np array into a y value

        plt.plot(x, y, label=legend)    # Plot on graph

    # Function that returns an exponetial function based on the value passed
    @staticmethod
    def exponential(value):

        # New function
        def formula(x):
            return value ** x

        return formula

    # Formats the graph
    def format(self):
        axs = plt.gca()                     # Gets axis object

        axs.set_xlim(xmin=0, xmax=self.x)   # Set limits for x
        axs.set_ylim(ymin=0)                # Set min for y

        axs.margins(y=0, x=0)               # Remove margins, not always needed

        plt.grid(True)                      # Create a grid

        loc = plticker.MultipleLocator(1)   # Shows a grid line every 1 value
        axs.xaxis.set_major_locator(loc)    # Add to graph

        plt.legend(loc="upper left")        # Add legend

        plt.xlabel('Weeks')                 # Add axis label
        plt.ylabel('People Affected')       # Add axis label

        plt.title("The Power of Kindness")  # Add title


# Run code
Plotter(3).plot()
