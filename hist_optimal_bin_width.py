#######################################################################################################################
#Author   : Dr. Arun B Ayyar
#
#Based on : Shimazaki H. and Shinomoto S., A method for selecting the bin size of a time histogram Neural Computation (2007)
#	   Vol. 19(6), 1503-1527
#
#Data     : The duration for eruptions of the Old Faithful geyser in Yellowstone National Park (in minutes) 
#	   or normal distribuition.
#	   given at http://176.32.89.45/~hideaki/res/histogram.html
#
#Comments : Implements a faster version than using hist from matplotlib and histogram from numpy libraries	
#           Also implements the shifts for the bin edges
#
########################################################################################################################


import numpy as np
from numpy.random import normal
from scipy import linspace
import array
from matplotlib import rcParams


from matplotlib.pyplot import figure,  plot, xlabel, ylabel,\
	title, show, savefig, hist

data = normal(0, 1, 100000) #Data placeholder.. Use this to input your data
#data = [4.37,3.87,4.00,4.03,3.50,4.08,2.25,4.70,1.73,4.93,1.73,4.62,\
#3.43,4.25,1.68,3.92,3.68,3.10,4.03,1.77,4.08,1.75,3.20,1.85,\
#4.62,1.97,4.50,3.92,4.35,2.33,3.83,1.88,4.60,1.80,4.73,1.77,\
#4.57,1.85,3.52,4.00,3.70,3.72,4.25,3.58,3.80,3.77,3.75,2.50,\
#4.50,4.10,3.70,3.80,3.43,4.00,2.27,4.40,4.05,4.25,3.33,2.00,\
#4.33,2.93,4.58,1.90,3.58,3.73,3.73,1.82,4.63,3.50,4.00,3.67,\
#1.67,4.60,1.67,4.00,1.80,4.42,1.90,4.63,2.93,3.50,1.97,4.28,\
#1.83,4.13,1.83,4.65,4.20,3.93,4.33,1.83,4.53,2.03,4.18,4.43,\
#4.07,4.13,3.95,4.10,2.27,4.58,1.90,4.50,1.95,4.83,4.12]

data_max = max(data) #lower end of data
data_min = min(data) #upper end of data
n_min = 2   #Minimum number of bins Ideal value = 2
n_max = 200  #Maximum number of bins  Ideal value =200
n_shift = 30     #number of shifts Ideal value = 30
N = np.array(range(n_min,n_max))
D = float(data_max-data_min)/N    #Bin width vector
Cs = np.zeros((len(D),n_shift)) #Cost function vector
#Computation of the cost function
for i in xrange(np.size(N)):
	shift = linspace(0,D[i],n_shift)
	for j in xrange(n_shift):
		edges = linspace(data_min+shift[j]-D[i]/2,data_max+shift[j]-D[i]/2,N[i]+1) # shift the Bin edges
		binindex = np.digitize(data,edges) #Find binindex of each data point
		ki=np.bincount(binindex)[1:N[i]+1] #Find number of points in each bin
		k = np.mean(ki) #Mean of event count
		v = sum((ki-k)**2)/N[i] #Variance of event count
		Cs[i,j]+= (2*k-v)/((D[i])**2) #The cost Function
C=Cs.mean(1)

#Optimal Bin Size Selection
loc = np.argwhere(Cs==Cs.min())[0]
cmin = C.min()
idx  = np.where(C==cmin)
idx = idx[0][0]
optD = D[idx]
print 'Optimal Bin Number :',N[idx]
print 'Optimal Bin Width :',optD

#Plot
edges = linspace(data_min+shift[loc[1]]-D[idx]/2,data_max+shift[loc[1]]-D[idx]/2,N[idx]+1)
rcParams.update({'figure.autolayout': True})
fig = figure()
ax = fig.add_subplot(111)
ax.hist(data,edges)
title(u"Histogram")
ylabel(u"Frequency")
xlabel(u"Value")
savefig('Hist.png')         
fig = figure()
plot(N,C,'.b',N[idx],cmin,'*r')
xlabel('Number of bins')
ylabel('Cobj')
savefig('Fobj.png')
