#!/usr/bin/env python
# coding: utf-8
# In[14]:
from __future__ import print_function
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
import seaborn as sns
import os
sns.set_style('darkgrid')

# Step-2. Import data
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")

fig, axes = plt.subplots(2, 3, figsize=(14,7), sharey=True, sharex=True)
#st = fig.suptitle('QQ statistics plots of the geology of the Mariana Trench', 
 #            fontsize=12)
plt.suptitle('QQ statistics plots of the geology of the Mariana Trench', 
             x=0.54, y=.92, fontsize=12,)

fig = qqplot(df.sedim_thick, line='q', fit=True, 
                 linewidth=.5, alpha = .5, markerfacecolor='#00a497', markeredgecolor='grey', ax=axes[0, 0])
axes[0, 0].annotate('A', xy=(0.05, .9), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

fig = qqplot(df.slope_angle, line='q', fit=True, 
                 linewidth=.5, alpha = .5, markerfacecolor='#4d5aaf', markeredgecolor='grey', ax=axes[0, 1])
axes[0, 1].annotate('B', xy=(0.05, .9), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

fig = qqplot(df.plate_pacif, line='q', fit=True, 
                 linewidth=.5, alpha = .4, markerfacecolor='#69821b', markeredgecolor='grey', ax=axes[0, 2])
axes[0, 2].annotate('C', xy=(0.05, .9), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

fig = qqplot(df.plate_phill, line='q', fit=True, 
                 linewidth=.5, alpha = .4, markerfacecolor='#640125', markeredgecolor='grey', ax=axes[1, 0])
axes[1, 0].annotate('D', xy=(0.05, .9), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

fig = qqplot(df.plate_maria, line='q', fit=True, 
                 linewidth=.1, alpha = .4, markerfacecolor='#b44c97', markeredgecolor='grey', ax=axes[1, 1])
axes[1, 1].annotate('E', xy=(0.05, .9), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

fig = qqplot(df.igneous_volc, line='q',  fit=True, 
                 lw=.1, alpha = .4, markerfacecolor='#4d5aaf', markeredgecolor='grey', ax=axes[1, 2])
axes[1, 2].annotate('F', xy=(0.05, .9), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

plt.show()
# In[ ]:
