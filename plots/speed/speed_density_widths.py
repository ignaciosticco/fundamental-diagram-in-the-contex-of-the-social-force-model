# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

'''

'''

import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
#import numarray

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			    # width  in inches
fig_height = fig_width*golden_mean          # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
          'axes.linewidth': 0.5, 
          'axes.grid': True,
          'axes.labelweight': 'normal',  
          'font.family': 'serif',
          'font.size': 8.0,
          'font.weight': 'normal',
          'text.color': 'black',
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'legend.fontsize': 8,
          'figure.dpi': 300,
          'figure.figsize': fig_size,
          'savefig.dpi': 300,
         }

pylab.rcParams.update(params)

### DATA ###
data_2m = np.genfromtxt("speed-density_vd1_pasillo2m.txt",delimiter = ' ') 
density_2m = data_2m[:,0]
speed_2m = data_2m[:,1]

data_4m = np.genfromtxt("speed-density_vd1_pasillo4m.txt",delimiter = ' ') 
density_4m = data_4m[:,0]
speed_4m = data_4m[:,1]

data_10m = np.genfromtxt("speed-density_vd1_pasillo10m.txt",delimiter = ' ') 
density_10m = data_10m[:,0]
speed_10m = data_10m[:,1]

data_15m = np.genfromtxt("speed-density_vd1_pasillo15m.txt",delimiter = ' ') 
density_15m = data_15m[:,0]
speed_15m = data_15m[:,1]

data_22m = np.genfromtxt("speed-density_vd1_pasillo22m.txt",delimiter = ' ') 
density_22m = data_22m[:,0]
speed_22m = data_22m[:,1]


###  PLOT  ###

pylab.figure(1)
pylab.clf()

plt.plot(density_2m,speed_2m,'-ob',markersize=3.5,label='width = 2m')
plt.plot(density_4m,speed_4m,'-og',markersize=3.5,label='width = 4m')
plt.plot(density_10m,speed_10m,'-oy',markersize=3.5,label='width = 10m')
plt.plot(density_15m,speed_15m,'-or',markersize=3.5,label='width = 15m')
plt.plot(density_22m,speed_22m,'-ok',markersize=3.5,label='width = 22m')


pylab.grid(False)
#pylab.xlabel('time~$(s)$')
pylab.xlabel('Density~(p~/m$^{2}$)')
pylab.ylabel('Speed~(m/s)')
#pylab.legend()
#pylab.ylim(0.0, 60.0)
#pylab.ylim(0.0, 3.6)
#pylab.yticks(np.arange(3,11,2))
#pylab.xlim(0.5, 8)
#pylab.xticks(np.arange(0,1100,200))
#pylab.xlim(0, 8)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(loc='lower left',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 
pylab.savefig('speed-density_vd1_multiple_widths.eps', format='eps', dpi=300, bbox_inches='tight')