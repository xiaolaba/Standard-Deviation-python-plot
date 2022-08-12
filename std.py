## uses install libraries first
#  pip install jupyter ipython pandas

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib import pyplot

#%matplotlib notebook
'exec(%matplotlib inline)'

# First dataset 
#DataSet_A=[36,37,36,34,39,33,30,30,32,31,31,32,32,33,35]

#DataSet_A=[23.34,29.72,35.99,42.26,48.6,54.98,61.27,67.63,73.98,80.3,86.67,93.02,99.37,105.79,112.18,118.44,124.83,131.08,137.43,143.84,150.12,156.56,162.93,169.24,175.59]
#DataSet_B=[23.5,29.69,36.06,42.41,48.75,55.17,61.47,67.86,74.15,80.53,86.91,93.24,99.54,105.84,112.21,118.56,124.98,131.2,137.56,144.15,150.31,156.7,163.19,169.5,175.62]
DataSet_A=[-1.47,-1.38,-1.39,-1.38,-1.37,-1.34,-1.36,-1.3,-1.49,-1.4,-1.37,-1.48,-1.43,-1.65,-1.63,-1.55,-1.51,-1.71,-1.75,-1.44,-1.53,-1.51,-1.46,-1.33,-1.56]
DataSet_B=[-1.47,-1.38,-1.39,-1.38,-1.37,-1.34,-1.36,-1.3,-1.49,-1.4,-1.37,-1.48,-1.43,-1.65,-1.63,-1.55,-1.51,-1.71,-1.75,-1.44,-1.53,-1.51,-1.46,-1.33,-1.56]

#DataSet_A=[23.34,29.72,35.99,42.26,48.6,54.98,61.27,67.63,73.98,80.3,86.67,93.02,99.37,105.79,112.18]
#DataSet_B=[23.5,29.69,36.06,42.41,48.75,55.17,61.47,67.86,74.15,80.53,86.91,93.24,99.54,105.84,112.21]

# Second dataset 
#DataSet_B=[41,35,28,29,25,36,36,32,38,40,40,34,31,28,30]

# Caluclate the mean of datasets
Mean_DataSet_A=np.mean(DataSet_A)
Mean_DataSet_B=np.mean(DataSet_B)

# Caluclate the standard deviation of datasets
STDV_DataSet_A=np.std(DataSet_A)
STDV_DataSet_B=np.std(DataSet_B)

# Create a figure with customized size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Set the axis lables
ax.set_xlabel('Slot#', fontsize = 18)
ax.set_ylabel('tilting compensation & STD', fontsize = 18)

# X axis is day numbers from 1 to 15
#xaxis = np.array(range(1,16))
xaxis = np.array(range(1,26))

# Line color for error bar
color_DataSet_A = 'red'
color_DataSet_B = 'darkgreen'

# Line style for each dataset
lineStyle_DataSet_A={"linestyle":"--", "linewidth":2, "markeredgewidth":2, "elinewidth":2, "capsize":3}
lineStyle_DataSet_B={"linestyle":"-", "linewidth":2, "markeredgewidth":2, "elinewidth":2, "capsize":3}

# Create an error bar for each dataset
line_DataSet_A=ax.errorbar(xaxis, DataSet_A, yerr=STDV_DataSet_A, **lineStyle_DataSet_A, color=color_DataSet_A, label='tool_3')
line_DataSet_B=ax.errorbar(xaxis, DataSet_B, yerr=STDV_DataSet_B, **lineStyle_DataSet_B, color=color_DataSet_B, label='tool_6')

# Label each dataset on the graph, xytext is the label's position 
for i, txt in enumerate(DataSet_A):
        ax.annotate(txt, xy=(xaxis[i], DataSet_A[i]), xytext=(xaxis[i]+0.03, DataSet_A[i]+0.3),color=color_DataSet_A)

for i, txt in enumerate(DataSet_B):
        ax.annotate(txt, xy=(xaxis[i], DataSet_B[i]), xytext=(xaxis[i]+0.03, DataSet_B[i]+0.3),color=color_DataSet_B)
        

# Draw a legend bar
plt.legend(handles=[line_DataSet_A, line_DataSet_B], loc='upper right')

# Customize the tickes on the graph
plt.xticks(xaxis)               
#plt.yticks(np.arange(20, 47, 2))
#plt.yticks(np.arange(23.5, 180, 6.35))
plt.yticks(np.arange(-2, 0, 0.25))


# Customize the legend font and handle length
params = {'legend.fontsize': 13,
          'legend.handlelength': 2}
plt.rcParams.update(params)

# Customize the font
font = {'family' : 'Arial',
        'weight':'bold',
        'size'   : 12}
plt.rc('font', **font)


# Draw a grid for the graph
ax.grid(color='lightgrey', linestyle='-')
ax.set_facecolor('w')

plt.show()