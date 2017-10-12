http://176.32.89.45/~hideaki/res/histogram.html gives a sample python code for implementing the optimal histogram bin width algorithm. It uses matplotlib.pyplot.hist to compute the number of data points in given bins. For larger datasets, this method is slow. http://176.32.89.45/~hideaki/res/code/python/histsample_torii.py uses numpy.histogram to compute the number of data points in the given bins.
The current implementation uses numpy.bincount to achieve the same. This implementaion also implements the shifts of bin-edges as given in https://raw.githubusercontent.com/shimazaki/density_estimation/master/matlab/sshist.m

The current implementaion is faster than using numpy.histogram or matplotlib.pyplot.hist

Tested on:
numpy  1.11.1
python 2.7
matplotlib 2.0.0

