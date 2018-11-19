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


data_koriginal = np.genfromtxt('density_fic_w22m_koriginal.txt', delimiter = ' ')
density_kroiginal = data_koriginal[:,0] 
fic_koriginal = data_koriginal[:,1] 
err_koriginal = data_koriginal[:,2] 


data_kx10 = np.genfromtxt('density_fic_w22m_kx10.txt', delimiter = ' ')
density_kx10 = data_kx10[:,0] 
fic_kx10 = data_kx10[:,1] 
err_kx10 = data_kx10[:,2] 


###  PLOT  ###

#fig, ax1 = plt.subplots()
plt.plot(density_kroiginal,fic_koriginal,'b--o',mew=0.7,markersize=4,label='$\\kappa = 2.4 \\times 10^{4}$') 
plt.errorbar(density_kroiginal,fic_koriginal,err_koriginal,linestyle='none',fmt='none',color='none',ecolor='b') 

#fig, ax2 = plt.subplots()
plt.plot(density_kx10,fic_kx10,'r-s',mew=0.7,markersize=4,label='$\\kappa = 2.4 \\times 10^{5}$') 
plt.errorbar(density_kx10,fic_kx10,err_kx10,linestyle='none',fmt='none',color='none',ecolor='r') 



pylab.legend()
pylab.xticks(np.arange(4.0,5.7,0.2))
plt.xlabel('Global density ')
plt.ylabel('fracc.  clusterized indiv')
plt.ylim(0.0, 1.02)
plt.xlim(4.0,5.5)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='lower right',labelspacing=0.1,borderpad=0.1,handletextpad=0.1,fontsize=6,numpoints=1)
pylab.savefig('fracc_clusteriz_vs_density.png', format='png', dpi=300, bbox_inches='tight')

'''
############ Inset plot ############

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
#plt.text(0.01, 0.33, "0", size=4.5)
#plt.text(0.97, 0.33, "1", size=4.5)
pylab.savefig('frac_clusterized_vs_d.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('frac_clusterized_vs_d.eps', format='eps', dpi=300, bbox_inches='tight')
'''