import matplotlib.pyplot as plt
from matplotlib import ticker

# constants
g_0 = 9.80665      # standard gravity, g, m/s/s
p_0 = 101.326      # sea level, kPa


red = '#e31d1d'
green = '#76e146'
blue = '#709afa'

class Plot(object):

    def __init__(self, title, xlabel="", ylabel=""):

        self.ax = plt.figure(figsize=(16,9))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        self.ax.axes[0].grid(color='grey', alpha=0.2, linestyle='dashed', linewidth=0.5)

    def plot(self, x, y, color='#e31d1d', alpha=0.8, lw=0.6, label="data", log=False):
        if log:
            plt.semilogy(x, y, color, alpha=alpha, lw=lw, label=label)
        else:
            plt.plot(x, y, color, alpha=alpha, lw=lw, label=label)

    def xlim(self, lim):
        self.ax.axes[0].set_xlim(lim)

    def ylim(self, lim):
        self.ax.axes[0].set_ylim(lim)

    def legend(self, loc=1):
        plt.legend(loc=loc)

    def timex(self, sep=30):
        fmt = ticker.FuncFormatter(hms)
        loc = ticker.MultipleLocator(sep)
        self.ax.axes[0].xaxis.set_major_locator(loc)
        self.ax.axes[0].xaxis.set_major_formatter(fmt)
        plt.xticks(rotation=-40)

    def note(self, note, xy, offset):
        rad = 0.2
        if offset[0] < 0 or offset[1] < 0:
            rad = -0.2
        plt.annotate(note, xy=xy,  xycoords='data', xytext=offset,
            textcoords='offset points', arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3,rad=%0.1f" % rad) )

    def show(self):
        plt.show()

def hms(x, pos):
    m = int(x / 60)
    s = x - (m*60)
    return "%d:%02d" % (m, s)
