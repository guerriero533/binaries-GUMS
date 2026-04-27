# Example of binary detectability plot as a function of the orbital period
# Figure 6: binary detectability as a function of period and eccentricity for DR3, DR4, and DR5. 

from astropy.table import Table, Column
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

t=pd.read_csv('GUMS_binaries_all (2).csv')
data=Table.from_pandas(t)

# introducing Flags according to the nominal thresholds found in 'sdf.py'
# --> all the sources exceeding the corresponding threshold are identified as binary systems, and single sources otherwise.
data['flags_astromet_dr3']=0.
data['flags_astromet_dr3'][data['uwe_dr3']>1.25]=1

data['flags_astromet_dr4']=0.
data['flags_astromet_dr4'][data['uwe_dr4']>1.145]=1

data['flags_astromet_dr5']=0.
data['flags_astromet_dr5'][data['uwe_dr5']>1.11]=1

data['flags']=0.
data['flags'][data['ruwe']>1.25]=1

# setting up the grid
fig,grid = make_grid(3,1,figsize=(10,3),width_ratios=[1,1,1.2])
cmap = mpl.colormaps['rainbow']
colors = cmap(np.linspace(0, 1, 10))

## dr3
ax=plt.subplot(grid[0,0])
ax.hexbin(data['period'],data['eccentricity'], gridsize=64,C=data['flags_astromet_dr3'], cmap='Spectral', xscale='log', extent=[-4,5,0,1])

## dr4
ax1=plt.subplot(grid[0,1])
ax1.hexbin(data['period'],data['eccentricity'], gridsize=64,C=data['flags_astromet_dr4'], cmap='Spectral', xscale='log', extent=[-4,5,0,1])

## dr5
ax2=plt.subplot(grid[0,2])
im=ax2.hexbin(data['period'],data['eccentricity'], gridsize=64,C=data['flags_astromet_dr5'], cmap='Spectral', xscale='log', extent=[-4,5,0,1])
plt.colorbar(im, label=r'Fraction detected')

# axis and title
ax.set_xlabel(r'P[yr]')
ax1.set_xlabel(r'P[yr]')
ax2.set_xlabel(r'P[yr]')
ax.set_ylabel(r'e')
ax.set_title(r'DR3', fontsize=11)
ax1.set_title(r'DR4', fontsize=11)
ax2.set_title(r'DR5', fontsize=11)

plt.tight_layout()
plt.show()
