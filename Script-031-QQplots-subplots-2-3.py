from __future__ import print_function
%matplotlib inline
import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")

fig, axes = plt.subplots(2, 3, figsize=(14, 7),
                         sharey=True, sharex=True, dpi=300)
plt.suptitle('QQ statistics plots of the geology of the Mariana Trench',
             x=0.54, y=.92, fontsize=12)

bbox_props = dict(boxstyle='round, pad=0.3', fc='w',
                  edgecolor='grey', linewidth=1, alpha=0.9)

# subplot 1
fig = qqplot(df.sedim_thick, line='q', fit=True,
             linewidth=.5, alpha = .5, markerfacecolor='#00a497',
             markeredgecolor='grey', ax=axes[0, 0]
             )
axes[0, 0].annotate('A', xy=(0.05, .9), xycoords="axes fraction",
                    fontsize=12, bbox=bbox_props)

# subplot 2
fig = qqplot(df.slope_angle, line='q', fit=True,
             linewidth=.5, alpha = .5, markerfacecolor='#4d5aaf',
             markeredgecolor='grey', ax=axes[0, 1]
             )
axes[0, 1].annotate('B', xy=(0.05, .9), xycoords="axes fraction",
                    fontsize=12, bbox=bbox_props)

# subplot 3
fig = qqplot(df.plate_pacif, line='q', fit=True,
             linewidth=.5, alpha = .4, markerfacecolor='#69821b',
             markeredgecolor='grey', ax=axes[0, 2]
             )
axes[0, 2].annotate('C', xy=(0.05, .9), xycoords="axes fraction",
                    fontsize=12, bbox=bbox_props)

# subplot 4
fig = qqplot(df.plate_phill, line='q', fit=True,
             linewidth=.5, alpha = .4, markerfacecolor='#640125',
             markeredgecolor='grey', ax=axes[1, 0]
             )
axes[1, 0].annotate('D', xy=(0.05, .9), xycoords="axes fraction",
                    fontsize=12, bbox=bbox_props)

# subplot 5
fig = qqplot(df.plate_maria, line='q', fit=True,
             linewidth=.1, alpha = .4, markerfacecolor='#b44c97',
             markeredgecolor='grey', ax=axes[1, 1]
             )
axes[1, 1].annotate('E', xy=(0.05, .9), xycoords="axes fraction",
                    fontsize=12, bbox=bbox_props)

# subplot 6
fig = qqplot(df.igneous_volc, line='q', fit=True, lw=.1, alpha = .4,
             markerfacecolor='#4d5aaf', markeredgecolor='grey', ax=axes[1, 2]
             )
axes[1, 2].annotate('F', xy=(0.05, .9), xycoords="axes fraction",
                    fontsize=12, bbox=bbox_props)

# visualize and save
plt.tight_layout()
plt.subplots_adjust(top=0.85, bottom=0.08,
                    left=0.10, right=0.95,
                    hspace=0.25, wspace=0.35
                    )
fig.savefig('plot_QQ.png', dpi=300)
plt.show()
