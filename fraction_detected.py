#Figure 5: The fraction of detectable binaries as a function of period. 

from astropy.table import Table, Column
import numpy as np
import astromet
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats
import gaiascanlaw
import pandas as pd
from tqdm import tqdm

t=pd.read_csv('GUMS_binaries_all (2).csv')
data=Table.from_pandas(t)

#defining the time baseline for each data release
N=[2,3,4,5]
tb=np.zeros(4)
for j in range(4):
    s=gaiascanlaw.tstart
    e=gaiascanlaw.gaiatimes[N[j]]
    e_yr=(e-s)
    tb[j]=e_yr
    print(f"DR{j+1}: {e_yr:.2f}")

#creating the probability distribution
nbins = 48
logPbins = np.linspace(-3, 5, nbins + 1) 
Pmids = 10**(0.5 * (logPbins[:-1] + logPbins[1:]))
fractions = np.zeros((nbins,4))
fractions_fixed = np.zeros((nbins,4))
cmap = mpl.colormaps['rainbow']
colors = cmap(np.linspace(0, 1, 10))
cs=[colors[3],colors[5],colors[7],colors[9]]
cuts=np.array([1.4,1.25,1.15,1.11])

for i in tqdm(range(nbins)):
    sel = np.flatnonzero((data['period'] > 10**logPbins[i]) & (data['period'] < 10**logPbins[i + 1]))
    if sel.size==0:
        continue
    for j in range(4):
        cut=sel[data["uwe_dr"+str(j+2)][sel]>cuts[j]]
        cut_fixed=sel[data["uwe_dr"+str(j+2)][sel]>1.4]
#        cut=sel[data["fractions_dr"+str(j+2)][sel]==1]
        fractions_fixed[i,j]=cut_fixed.size/sel.size #using a fixed threshold of 1.4 from DR2 (Penoyre+22)
        fractions[i,j]=cut.size/sel.size
cs=[colors[3],colors[5],colors[7],colors[9]]
fig, ax = plt.subplots(figsize=(8, 4))
for j in range(4):
    ax.plot(Pmids, fractions_fixed[:,j],c=cs[j], ls='--', lw=1)
    ax.plot(Pmids, fractions[:,j],c=cs[j],label="DR"+str(j+2), lw=1)
    ax.axvline(tb[j], c=cs[j], ls=':', lw=1)
ax.set_xscale("log")
#ax.set_yscale("log")
ax.set_ylim(0,1)
ax.set_ylabel('Fraction Detected')
ax.set_xlabel('P [yr]')
ax.legend(frameon=False)

plt.show()
