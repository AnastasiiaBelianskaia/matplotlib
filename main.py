import matplotlib.pyplot as plt
import numpy as np


def plotting():
    """ The plot() function is used to draw points (markers) in a diagram.
    By default, the plot() function draws a line from point to point."""

    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    plt.plot(xpoints, ypoints)
    return plt.show()


def plotting_without_line():
    """ Use shortcut string notation parameter 'o'. """

    xpoints = np.array([0, 8])
    ypoints = np.array([0, 100])

    plt.plot(xpoints, ypoints, 'o')
    return plt.show()


def multiple_points():
    xpoints = np.array([0, 2, 4, 5, 8])
    ypoints = np.array([0, 6, 60, 1, 234])

    plt.plot(xpoints, ypoints)
    return plt.show()


def markers():
    """ Use the keyword argument marker to emphasize each point. """

    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker='o')
    return plt.show()


def format_strings():
    """ marker|line|color """

    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, 'o:r')
    return plt.show()


def marker_size():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker='o', ms=20)
    return plt.show()


def marker_color():
    """ mec for the edge, mfc for the face.
    Hexadecimal color values are allowed. """

    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='r')
    return plt.show()


def linestyle():
    """ 'solid' (default), 'dotted', 'dashed', 'dashdot', 'None'. """

    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, linestyle='dotted')
    return plt.show()


def linecolor():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, color='g')
    return plt.show()


def linewidth():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, linewidth='20.5')
    return plt.show()


def multiple_lines():
    y1 = np.array([3, 8, 1, 10])
    y2 = np.array([6, 2, 7, 11])

    plt.plot(y1)
    plt.plot(y2)

    # or:
    # x1 = np.array([0, 1, 2, 3])
    # y1 = np.array([3, 8, 1, 10])
    # x2 = np.array([0, 1, 2, 3])
    # y2 = np.array([6, 2, 7, 11])
    #
    # plt.plot(x1, y1, x2, y2)

    return plt.show()


def labels():
    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

    plt.title("Sports Watch Data", fontdict=font1, loc='left')
    plt.xlabel("Average Pulse", fontdict=font2)
    plt.ylabel("Calorie Burnage", fontdict=font2)

    plt.plot(x, y)
    return plt.show()


def grid():
    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

    plt.title("Sports Watch Data")
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")

    plt.plot(x, y)

    plt.grid()

    return plt.show()


def multiple_plots():
    """ subplot: rows,columns,index of the plot. """

    # plot 1:
    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])

    plt.subplot(1, 2, 1)
    plt.plot(x, y)
    plt.title('SALES')

    # plot 2:
    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 40])

    plt.subplot(1, 2, 2)
    plt.plot(x, y)
    plt.title('INCOME')

    plt.suptitle('SHOP')

    # six plots
    # x = np.array([0, 1, 2, 3])
    # y = np.array([3, 8, 1, 10])
    #
    # plt.subplot(2, 3, 1)
    # plt.plot(x, y)
    #
    # x = np.array([0, 1, 2, 3])
    # y = np.array([10, 20, 30, 40])
    #
    # plt.subplot(2, 3, 2)
    # plt.plot(x, y)
    #
    # x = np.array([0, 1, 2, 3])
    # y = np.array([3, 8, 1, 10])
    #
    # plt.subplot(2, 3, 3)
    # plt.plot(x, y)
    #
    # x = np.array([0, 1, 2, 3])
    # y = np.array([10, 20, 30, 40])
    #
    # plt.subplot(2, 3, 4)
    # plt.plot(x, y)
    #
    # x = np.array([0, 1, 2, 3])
    # y = np.array([3, 8, 1, 10])
    #
    # plt.subplot(2, 3, 5)
    # plt.plot(x, y)
    #
    # x = np.array([0, 1, 2, 3])
    # y = np.array([10, 20, 30, 40])
    #
    # plt.subplot(2, 3, 6)
    # plt.plot(x, y)

    return plt.show()


def scatter_plot():
    """ Add to plt.scatter(color = 'color', alpha=number) to change it.
    Alpha is for transparency. """

    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

    plt.scatter(x, y)
    return plt.show()


def two_scat_plots():
    """ Add to plt.scatter(color = 'color', alpha=number) to change it.
        Alpha is for transparency. """

    # day one, the age and speed of 13 cars:
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    plt.scatter(x, y)

    # day two, the age and speed of 15 cars:
    x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
    y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
    plt.scatter(x, y)

    return plt.show()


def scat_colors_transparency():
    x = np.random.randint(100, size=(100))
    y = np.random.randint(100, size=(100))
    colors = np.random.randint(100, size=(100))
    sizes = 10 * np.random.randint(100, size=(100))

    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

    plt.colorbar()

    return plt.show()


def bar():
    """ Add to plt.bar(color = "color", width = number) to change it. """

    x = np.array(["A", "B", "C", "D"])
    y = np.array([3, 8, 1, 10])

    plt.bar(x, y)
    return plt.show()


def bar_horizontal():
    """ Add to plt.bar(color = "color", height = number) to change it. """

    x = np.array(["A", "B", "C", "D"])
    y = np.array([3, 8, 1, 10])

    plt.barh(x, y)
    return plt.show()


def histogram():
    x = np.random.normal(170, 10, 250)

    plt.hist(x)
    return plt.show()


def pie_charts():
    """ Add to .pie(startangle = number) to start the first wedge at 'number' degrees. """

    y = np.array([35, 25, 25, 15])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

    plt.pie(y, labels=mylabels)
    # plt.legend(title="Four Fruits:")
    return plt.show()


def pie_charts_explode():
    """ Add to .pie(shadow = True) to add shadow. """

    y = np.array([35, 25, 25, 15])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
    myexplode = [0.2, 0, 0, 0]

    plt.pie(y, labels=mylabels, explode=myexplode)
    return plt.show()


if __name__ == '__main__':
    plotting()
    plotting_without_line()
    multiple_points()
    markers()
    format_strings()
    marker_size()
    marker_color()
    linestyle()
    linecolor()
    linewidth()
    multiple_lines()
    labels()
    grid()
    multiple_plots()
    scatter_plot()
    two_scat_plots()
    scat_colors_transparency()
    bar()
    bar_horizontal()
    histogram()
    pie_charts()
    pie_charts_explode()
