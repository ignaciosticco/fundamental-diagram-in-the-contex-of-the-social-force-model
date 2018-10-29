# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import math

golden_mean = (math.sqrt(5)-1.0)/2.0       # Aesthetic ratio
fig_width = 3+3/8                          # width  in inches
fig_height = fig_width*golden_mean         # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
          'axes.linewidth': 0.5, 
          'axes.grid': False,
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

###  DATA  ###


data_w4 = np.genfromtxt('speed_profile_w4_density6_kappa24.txt', delimiter = '')
data_w15 = np.genfromtxt('speed_profile_w15_density6_kappa24.txt', delimiter = '')
data_w22 = np.genfromtxt('speed_profile_w22_density6_kappa24.txt', delimiter = '')
data_w40 = np.genfromtxt('speed_profile_w40_density6_kappa24.txt', delimiter = '')

ancho_w4 = data_w4[:,0] 
v_media_w4 = data_w4[:,1] 
err_media_w4 = data_w4[:,2] 
ancho_w4 = np.true_divide(ancho_w4,4.0)
v_media_w4 = np.true_divide(v_media_w4,max(v_media_w4))

ancho_w15 = data_w15[:,0] 
v_media_w15 = data_w15[:,1] 
err_media_w15 = data_w15[:,2] 
ancho_w15 = np.true_divide(ancho_w15,15.0)
v_media_w15 = np.true_divide(v_media_w15,max(v_media_w15))


ancho_w22 = data_w22[:,0] 
v_media_w22 = data_w22[:,1] 
err_media_w22 = data_w22[:,2] 
ancho_w22 = np.true_divide(ancho_w22,22.0)
v_media_w22 = np.true_divide(v_media_w22,max(v_media_w22))

ancho_w40 = data_w40[:,0] 
v_media_w40 = data_w40[:,1] 
err_media_w40 = data_w40[:,2] 
ancho_w40 = np.true_divide(ancho_w40,40.0)
v_media_w40 = np.true_divide(v_media_w40,max(v_media_w40))


###  PLOT  ###


plt.plot(ancho_w4,v_media_w4,'bo',markersize=4,zorder=3,label='width=4m') 
plt.plot(ancho_w4,v_media_w4,'b',lw=0.6,zorder=2)
plt.errorbar(ancho_w4,v_media_w4,err_media_w4,linestyle='-',fmt='.',color='w',ecolor='b',zorder=1) 

plt.plot(ancho_w15,v_media_w15,'go',markersize=4,zorder=3,label='width=15m') 
plt.plot(ancho_w15,v_media_w15,'g',lw=0.6,zorder=2)
plt.errorbar(ancho_w15,v_media_w15,err_media_w15,linestyle='-',fmt='.',color='w',ecolor='g',zorder=1) 

plt.plot(ancho_w22,v_media_w22,'yo',markersize=4,zorder=3,label='width=22m') 
plt.plot(ancho_w22,v_media_w22,'y',lw=0.6,zorder=2)
plt.errorbar(ancho_w22,v_media_w22,err_media_w22,linestyle='-',fmt='.',color='w',ecolor='y',zorder=1) 

plt.plot(ancho_w40,v_media_w40,'ro',markersize=4,zorder=3,label='width=40m') 
plt.plot(ancho_w40,v_media_w40,'r',lw=0.6,zorder=2)
plt.errorbar(ancho_w40,v_media_w40,err_media_w40,linestyle='-',fmt='.',color='w',ecolor='r',zorder=1) 



pylab.legend()
#pylab.xticks(np.arange(0,9,2))
pylab.yticks(np.arange(0,1.1,0.25))
pylab.xlabel('y-position~/~width ')
pylab.ylabel('v~/~v$_{max}$ ')
pylab.ylim(0, 1.02)
pylab.xlim(0, 1.02)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(loc='best',labelspacing=0.1,borderpad=0.1,handletextpad=0.1,fontsize=6,numpoints=1)
pylab.savefig('v(y)_multi_width_normalizado.png', format='png', dpi=300, bbox_inches='tight')
