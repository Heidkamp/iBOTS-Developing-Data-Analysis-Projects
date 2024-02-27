def plot_histogram(data, nbins=50):
    import matplotlib.pyplot as plt
    figure, ax = plt.subplots(ncols=1, nrows=1)
    ax.hist(data, bins=nbins);