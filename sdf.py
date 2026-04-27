# Figure 4: The fraction of systems below a given UWE is shown for single stars 

from astropy.table import Table, Column
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats
import pandas as pd

#importing data from single stars catalogue
s=pd.read_csv('GUMS_singles_all.csv')
data_nb=Table.from_pandas(s)

fig, ax = plt.subplots(figsize=(4, 3))
cmap = mpl.colormaps['rainbow']
colors = cmap(np.linspace(0, 1, 10))

#defining the sf for each dr
tdf_dr1=scipy.stats.t.fit(data_nb['uwe_dr1'])
tdf_dr2=scipy.stats.t.fit(data_nb['uwe_dr2'])
tdf_dr3=scipy.stats.t.fit(data_nb['uwe_dr3'])
tdf_dr4=scipy.stats.t.fit(data_nb['uwe_dr4'])
tdf_dr5=scipy.stats.t.fit(data_nb['uwe_dr5'])

x_dr1=np.sort((data_nb['uwe_dr1']-tdf_dr1[1])/tdf_dr1[2])
x_dr2=np.sort((data_nb['uwe_dr2']-tdf_dr2[1])/tdf_dr2[2])
x_dr3=np.sort((data_nb['uwe_dr3']-tdf_dr3[1])/tdf_dr3[2])
x_dr4=np.sort((data_nb['uwe_dr4']-tdf_dr4[1])/tdf_dr4[2])
x_dr5=np.sort((data_nb['uwe_dr5']-tdf_dr5[1])/tdf_dr5[2])

x_dr1=np.linspace(1,2,100)
x_dr2=np.linspace(1,2,100)
x_dr3=np.linspace(1,2,100)
x_dr4=np.linspace(1,2,100)
x_dr5=np.linspace(1,2,100)

#fitting the student's t-distribution
ax.plot(x_dr1, scipy.stats.t.sf(x_dr1, tdf_dr1[0], tdf_dr1[1], tdf_dr1[2]), c=colors[0], lw=0.8, alpha=1, linestyle=':')
ax.plot(x_dr2, scipy.stats.t.sf(x_dr2, tdf_dr2[0], tdf_dr2[1], tdf_dr2[2]), c=colors[3], lw=0.8, alpha=1, linestyle=':')
ax.plot(x_dr3, scipy.stats.t.sf(x_dr3, tdf_dr3[0], tdf_dr3[1], tdf_dr3[2]), c=colors[5], lw=0.8, alpha=1, linestyle=':')
ax.plot(x_dr4, scipy.stats.t.sf(x_dr4, tdf_dr4[0], tdf_dr4[1], tdf_dr4[2]), c=colors[7], lw=0.8, alpha=1, linestyle=':')
ax.plot(x_dr5, scipy.stats.t.sf(x_dr5, tdf_dr5[0], tdf_dr5[1], tdf_dr5[2]), c=colors[9], lw=0.8, alpha=1, linestyle=':')

#defining the resulting thresholds for each data release
#ax.axvline(x=1.35, c=colors[0], linestyle='--', linewidth=0.5)
ax.axvline(x=1.37, c=colors[3], linewidth=0.5, alpha=1)
ax.axvline(x=1.25, c=colors[5], linewidth=0.5, alpha=1)
ax.axvline(x=1.145, c=colors[7], linewidth=0.5, alpha=1)
ax.axvline(x=1.11, c=colors[9], linewidth=0.5, alpha=1)
ax2 = ax.twiny()

#plotting the survival functions as sdf=1-cdf
ax.ecdf((data_nb['uwe_dr1']), weights=None, complementary=True, orientation='vertical', compress=False, data=None, color=colors[0], linestyle='--', label='DR1'
ax.ecdf((data_nb['uwe_dr2']), weights=None, complementary=True, orientation='vertical', compress=False, data=None, color=colors[3],linestyle='--', label='DR2')
ax.ecdf((data_nb['uwe_dr3']), weights=None, complementary=True, orientation='vertical', compress=False, data=None, color=colors[5],linestyle='--', label='DR3')
ax.ecdf((data_nb['uwe_dr4']), weights=None, complementary=True, orientation='vertical', compress=False, data=None, color=colors[7],linestyle='--', label='DR4')
ax.ecdf((data_nb['uwe_dr5']), weights=None, complementary=True, orientation='vertical', compress=False, data=None, color=colors[9],linestyle='--', label='DR5')

ax.legend(loc='best', frameon=False)

num=[1.11,1.145,1.25,1.37]
labels = ['DR5','DR4','DR3','DR2']
ax.set_xticks(num)
ax.set_xticklabels(labels, fontsize=10.5, rotation=45)
ax2.set_xlim(1,1.5)
ax.set_xlim(1,1.5)
ax.set_ylim(1e-6,)
ax.set_yscale('log')

ax2.set_xlabel(r'$UWE$', fontsize=11)
ax.set_ylabel(r's.f.', fontsize=11)

plt.show()
