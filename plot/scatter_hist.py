# scatter hist plot


def marginal_plot(x, y,
                  xlabel=None,
                  ylabel=None,
                  title=None,
                  alpha=None,
                  figsize=(8, 8)):
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    spacing = 0.005

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom + height + spacing, width, 0.2]
    rect_histy = [left + width + spacing, bottom, 0.2, height]

    # start with a square Figure
    fig = plt.figure(figsize=figsize)

    xmin = numpy.min(x) - 1
    xmax = numpy.max(x) + 1
    ymin = numpy.min(y) - 1
    ymax = numpy.max(y) + 1

    ax = fig.add_axes(rect_scatter)
    ax.xmin, ax.xmax = xmin, xmax
    ax.ymin, ax.ymax = ymin, ymax
    ax_histx = fig.add_axes(rect_histx, sharex=ax)
    ax_histy = fig.add_axes(rect_histy, sharey=ax)

    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y, alpha=alpha)

    # now determine nice limits by hand:
    binwidth = 0.25
    

    xbins = numpy.arange(xmin, xmax, binwidth)
    ybins = numpy.arange(ymin, ymax, binwidth)
    ax_histx.hist(x, bins=xbins)
    ax_histy.hist(y, bins=ybins, orientation='horizontal')

    # set labels
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if title:
        fig.suptitle(title)
    
    return None
