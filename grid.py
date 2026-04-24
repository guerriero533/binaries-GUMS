# Figure 2. Example astrometric tracks and fits for seven different binaries from GUMS, of increasing period

from astropy.table import Table, Column
import numpy as np
import astromet
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import gaiascanlaw
import pandas as pd
from tqdm import tqdm

#importing data
t=pd.read_csv('GUMS_binaries_all (2).csv')
data=Table.from_pandas(t)
gaiaepochs=np.array([2015,2015.5,2016,2017,2020])

#selecting the sources by period
s01=np.flatnonzero((data['period']>0.1)&(data['period']<0.11))
s03=np.flatnonzero((data['period']>0.3)&(data['period']<0.31))
s1=np.flatnonzero((data['period']>1.)&(data['period']<1.1))
s3=np.flatnonzero((data['period']>3.)&(data['period']<3.1))
s10=np.flatnonzero((data['period']>10)&(data['period']<10.1))
s30=np.flatnonzero((data['period']>30)&(data['period']<30.1))
s100=np.flatnonzero((data['period']>100)&(data['period']<100.1))
indexs=np.array([s01[1],s03[1],s1[1],s3[1],s10[1],s30[1],s100[1]])

cmap = mpl.colormaps['rainbow']
colors = cmap(np.linspace(0, 1, 10))
colors = [colors[5], colors[7], colors[9]]
N = [1, 2, 3, 4, 5]

fig, grid = make_grid(4, 7, figsize=(16, 16), height_ratios=[1, 1, 1, 1, 1, 1, 1], width_ratios=[1, 1, 1, 1])

# defining the system, plotting the astrometric track, and the single body solution for each period
for k in range(len(indexs)): 
    for j in range(3):
        ax = plt.subplot(grid[k, j])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # defining params for each astrometric track
        params = astromet.params()
        params.ra = data['ra'][indexs[k]]  # [deg]l
        params.dec = data['dec'][indexs[k]]  # [deg]
        params.drac = 0  # [mas]
        params.ddec = 0  # [mas]
        params.pmrac = 1  # [mas/yr]
        params.pmdec = 1  # [mas/yr]
        params.parallax = data['parallax'][indexs[k]]
        params.period = data['period'][indexs[k]]  # [yr]
        params.a = data['a_true'][indexs[k]]  # [AU]
        params.e = data['eccentricity'][indexs[k]]
        params.q = data['q'][indexs[k]]
        params.l = data['l'][indexs[k]]
        params.vphi = data['vphi'][indexs[k]]  # [rad]
        params.vtheta = data['vtheta'][indexs[k]]  # [rad]
        params.vomega = data['vomega'][indexs[k]]  # [rad]
        Mtot = data['Mtot'][indexs[k]]
        params.tperi = data['tperi'][indexs[k]]
        epoch = gaiaepochs[j+2]
        params.epoch = epoch
        pts = np.linspace(gaiascanlaw.gaiatimes[0], gaiascanlaw.gaiatimes[j + 3], 1000)
        sts, sphis = gaiascanlaw.scanlaw(params.ra, params.dec, gaiascanlaw.gaiatimes[0], gaiascanlaw.gaiatimes[j + 3])

        racs, decs = astromet.track(pts, params)
        sracs, sdecs = astromet.track(sts, params)
        ax.plot(racs, decs, c=colors[j])

        t_obs, x_obs, phi_obs, rac_obs, dec_obs = astromet.mock_obs(sts, sphis * 180 / np.pi, sracs, sdecs, err=data['sigma'][indexs[k]])
        #results = astromet.fit(t_obs, x_obs, phi_obs, data['sigma'][index], params.ra, params.dec, epoch=epoch)

        ax.scatter(rac_obs, dec_obs, color=colors[j], s=5, alpha=0.5, zorder=1)
        ax.scatter(rac_obs[0], dec_obs[0], facecolor='none',edgecolor='k', s=30, marker='^', zorder=2)

        for i in range(8):  # plotting 16 random realizations of the single-star fit including error
            fit_params = astromet.params()
            fit_params.epoch = epoch
            fit_params.ra = params.ra
            fit_params.dec = params.dec
            fit_params.drac = data['drac_dr' + str(int(N[j + 2]))][indexs[k]] + np.random.randn() * data['drac_error_dr' + str(int(N[j + 2]))][indexs[k]]
            fit_params.ddec = data['ddec_dr' + str(int(N[j + 2]))][indexs[k]] + np.random.randn() * data['ddec_error_dr' + str(int(N[j + 2]))][indexs[k]]
            fit_params.pmrac = data['pmrac_dr' + str(int(N[j + 2]))][indexs[k]] + np.random.randn() * data['pmrac_error_dr' + str(int(N[j + 2]))][indexs[k]]
            fit_params.pmdec = data['pmdec_dr' + str(int(N[j + 2]))][indexs[k]] + np.random.randn() * data['pmdec_error_dr' + str(int(N[j + 2]))][indexs[k]]
            fit_params.parallax = data['parallax_dr' + str(int(N[j + 2]))][indexs[k]] + np.random.randn() * data['parallax_error_dr' + str(int(N[j + 2]))][indexs[k]]

            fitracs, fitdecs = astromet.track(pts, fit_params)
            ax.plot(fitracs, fitdecs, c='gray', alpha=0.1)

    # 4th column, specific values
    ax = plt.subplot(grid[k, 3]) 
    ax.axis('off')  
    ax.text(0, 0.75, r'$UWE_{DR3}=$' + '{:.2f}'.format(data['uwe_dr3'][indexs[k]]), ha='left', va='center', fontsize=15)
    ax.text(0, 0.6, r'$UWE_{DR4}=$' + '{:.2f}'.format(data['uwe_dr4'][indexs[k]]), ha='left', va='center', fontsize=15)
    ax.text(0, 0.45, r'$UWE_{DR5}=$' + '{:.2f}'.format(data['uwe_dr5'][indexs[k]]), ha='left', va='center', fontsize=15)
    ax.text(0, 0.9, r'$P=$' + '{:.2f}'.format(data['period'][indexs[k]]) + r'$\ yr$', ha='left', va='center', fontsize=15)
    ax.text(0.53, 0.9, r'$\varpi_{true}=$' + '{:.2f}'.format(data['parallax'][indexs[k]]) + r'$\ mas$', ha='left', va='center', fontsize=15)
    ax.text(0, 0.3, r'$\varpi_{DR3}=$' + '{:.2f}'.format(data['parallax_dr3'][indexs[k]]) + r'$\pm$' + '{:.2f}'.format(data['parallax_error_dr3'][indexs[k]]) + r'$\ mas$', ha='left', va='center', fontsize=15)
    ax.text(0, 0.15, r'$\varpi_{DR4}=$' + '{:.2f}'.format(data['parallax_dr4'][indexs[k]]) + r'$\pm$' + '{:.2f}'.format(data['parallax_error_dr4'][indexs[k]]) + r'$\ mas$', ha='left', va='center', fontsize=15)
    ax.text(0, 0, r'$\varpi_{DR5}=$' + '{:.2f}'.format(data['parallax_dr5'][indexs[k]]) + r'$\pm$' + '{:.2f}'.format(data['parallax_error_dr5'][indexs[k]]) + r'$\ mas$', ha='left', va='center', fontsize=15)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

ax_lbl = plt.subplot(grid[6, 0])
ax_lbl.set_xlabel(r'$\Delta\alpha\ cos(\delta$) [mas]', fontsize=20)
ax_lbl.set_ylabel(r'$\Delta\delta$ [mas]', fontsize=20)
labels=['DR3','DR4','DR5','Results']
for i in range(4):
    ax_dr=plt.subplot(grid[0, i])
    ax_dr.set_title(labels[i], fontsize=20)

plt.tight_layout()
plt.show()
