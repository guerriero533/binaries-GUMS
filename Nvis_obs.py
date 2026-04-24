# Figure 1
# The distribution of the total number of observations per system, N_obs, 
# and the corresponding distribution of the number of visibility periods, N_vis, in each data release for GUMS sources within 200 pc

from astropy.table import Table, Column
import numpy as np
import astromet
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

#importing the data
t=pd.read_csv('GUMS_binaries_all (2).csv')
data=Table.from_pandas(t)

#designing the grid
fig, grid = make_grid(2, 1, figsize=(12,4), width_ratios=[1, 1])
ax1 = plt.subplot(grid[0, 0])
ax2 = plt.subplot(grid[0, 1])

cmap = mpl.colormaps['rainbow']
colors = cmap(np.linspace(0, 1, 10))

#Nobs
ax1.hist(data['n_obs_dr1'],histtype='step', bins=np.arange(0,5000,9),color=colors[0], label=r'DR1', weights=(1/9)*np.ones(data['n_obs_dr1'].size))
ax1.hist(data['n_obs_dr2'],histtype='step', bins=np.arange(0,5000,9),color=colors[3], label=r'DR2', weights=(1/9)*np.ones(data['n_obs_dr2'].size))
ax1.hist(data['n_obs_dr3'],histtype='step', bins=np.arange(0,5000,9),color=colors[5], label=r'DR3', weights=(1/9)*np.ones(data['n_obs_dr3'].size))
ax1.hist(data['n_obs_dr4'],histtype='step', bins=np.arange(0,5000,9),color=colors[7], label=r'DR4', weights=(1/9)*np.ones(data['n_obs_dr4'].size))
ax1.hist(data['n_obs_dr5'],histtype='step', bins=np.arange(0,5000,9),color=colors[9], label=r'DR5', weights=(1/9)*np.ones(data['n_obs_dr5'].size))
ax1.set_xlabel(r'$N_{obs}$', fontsize=15)
ax1.set_yscale('log')
ax1.set_ylim(0.5)

#Nvis
ax2.hist(data['vis_periods_dr1'],histtype='step', bins=np.arange(0,150,1), color=colors[0], label=r'DR1')
ax2.hist(data['vis_periods_dr2'],histtype='step', bins=np.arange(0,150,1),color=colors[3],  label=r'DR2')
ax2.hist(data['vis_periods_dr3'],histtype='step', bins=np.arange(0,150,1), color=colors[5], label=r'DR3')
ax2.hist(data['vis_periods_dr4'],histtype='step', bins=np.arange(0,150,1),color=colors[7],  label=r'DR4')
ax2.hist(data['vis_periods_dr5'],histtype='step', bins=np.arange(0,150,1), color=colors[9], label=r'DR5')
ax2.set_xlabel(r'$N_{vis}$', fontsize=15)
ax2.set_yscale('log')
ax2.set_ylim(0.5)

ax1.legend(loc='best', frameon=False, fontsize=12)
ax1.tick_params(axis='both', labelsize=14)
ax2.tick_params(axis='both', labelsize=14)
plt.tight_layout()

plt.show()
