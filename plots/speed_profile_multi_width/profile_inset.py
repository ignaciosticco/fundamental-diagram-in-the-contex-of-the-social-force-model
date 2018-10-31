import matplotlib.pyplot as plt
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

ancho_w15 = data_w15[:,0] 
v_media_w15 = data_w15[:,1] 
err_media_w15 = data_w15[:,2] 
ancho_w15 = np.true_divide(ancho_w15,15.0)

ancho_w22 = data_w22[:,0] 
v_media_w22 = data_w22[:,1] 
err_media_w22 = data_w22[:,2] 
ancho_w22 = np.true_divide(ancho_w22,22.0)

ancho_w40 = data_w40[:,0] 
v_media_w40 = data_w40[:,1] 
err_media_w40 = data_w40[:,2] 
ancho_w40 = np.true_divide(ancho_w40,40.0)


###  PLOT  ###

fig, ax1 = plt.subplots()
ax1.plot(ancho_w4,v_media_w4,'b--x',mew=0.7,markersize=4,label='width=4m') 
#ax1.errorbar(ancho_w4,v_media_w4,err_media_w4,linestyle='none',fmt='none',color='none',ecolor='b') 

ax1.plot(ancho_w15[::2],v_media_w15[::2],'g:^',mew=0.7,markerfacecolor='none',markersize=4,markeredgecolor='g',label='width=15m') 
#ax1.errorbar(ancho_w15,v_media_w15,err_media_w15,linestyle='none',fmt='none',color='none',ecolor='g') 

ax1.plot(ancho_w22[::2],v_media_w22[::2],'y-.o',mew=0.7,markerfacecolor='none',markeredgecolor='y',markersize=4,zorder=3,label='width=22m') 
#ax1.errorbar(ancho_w22,v_media_w22,err_media_w22,linestyle='none',fmt='none',color='none',ecolor='y') 

ax1.plot(ancho_w40[::2],v_media_w40[::2],'-rs',mew=0.7,markerfacecolor='none',markeredgecolor='r',markersize=4,label='width=40m') 
#ax1.errorbar(ancho_w40,v_media_w40,err_media_w40,linestyle='none',fmt='none',color='none',ecolor='r') 


pylab.legend()
#pylab.xticks(np.arange(0,9,2))
#ax1.yticks(np.arange(0,1.1,0.25))
plt.xlabel('y-position~/~width ')
plt.ylabel('Velocity (m/s)')
plt.ylim(0.1, 1.5)
#ax1.xlim(0, 1.02)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
ax1.legend(frameon=False,loc='upper left',labelspacing=0.1,borderpad=0.1,handletextpad=0.1,fontsize=6,numpoints=1)
#pylab.savefig('v(y)_multi_width_k24.png', format='png', dpi=300, bbox_inches='tight')


############ Insert plot ############



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

left, bottom, width, height = [0.62, 0.62, 0.28, 0.28]
ax2 = fig.add_axes([left, bottom, width, height])

ax2.plot(ancho_w4,v_media_w4,'b--x',lw=0.5,markersize=2,label='width=4m') 
ax2.plot(ancho_w15[::3],v_media_w15[::3],'g:^',lw=0.5,markerfacecolor='none',markersize=2,markeredgecolor='g',label='width=15m') 
ax2.plot(ancho_w22[::3],v_media_w22[::3],'y-.o',lw=0.5,markerfacecolor='none',markeredgecolor='y',markersize=2,label='width=22m') 
ax2.plot(ancho_w40[::3],v_media_w40[::3],'-rs',lw=0.3,markerfacecolor='none',markeredgecolor='r',markersize=2,label='width=40m') 


pylab.yticks(np.arange(0,1.1,1),size='4.5')
pylab.xticks(np.arange(0,1.1,1),size='0.0')
pylab.xlabel('y-position~/~width ',size='4.5',labelpad=-5)
pylab.ylabel('v~/~v$_{max}$ ',size='5.5',labelpad=1)
pylab.ylim(0.3, 1.1)
pylab.xlim(0, 1.02)
ax2.tick_params(axis='y', pad=-4)
plt.tick_params(axis='both',which='both',bottom=False,top=False,labelbottom=False) 
ax2.xaxis.set_ticks_position('none') 
ax2.yaxis.set_ticks_position('none') 
plt.text(0.01, 0.33, "0", size=4.5)
plt.text(0.97, 0.33, "1", size=4.5)
pylab.savefig('v(y)_multi_width.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('v(y)_multi_width.eps', format='eps', dpi=300, bbox_inches='tight')
