#!/usr/bin/env python
# coding: utf-8

# In[74]:


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

fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(1, 6, sharey=True)
st = fig.suptitle('QQ statistics plots of the geology of the Mariana Trench', 
             fontsize=12)

ax1.plt = qqplot(df.sedim_thick, line='q', ax=ax1, fit=True, 
                 linewidth=.5, alpha = .5, markerfacecolor='#00a497', markeredgecolor='grey',)
ax1.annotate('A', xy=(0.1, .92), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

ax2.plt = qqplot(df.slope_angle, line='q', ax=ax2, fit=True, 
                 linewidth=.5, alpha = .5, markerfacecolor='#4d5aaf', markeredgecolor='grey',)
ax2.annotate('B', xy=(0.1, .92), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

ax3.plt = qqplot(df.plate_pacif, line='q', ax=ax3, fit=True, 
                 linewidth=.5, alpha = .4, markerfacecolor='#69821b', markeredgecolor='grey',)
ax3.annotate('C', xy=(0.1, .92), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

ax4.plt = qqplot(df.plate_phill, line='q', ax=ax4, fit=True, 
                 linewidth=.5, alpha = .4, markerfacecolor='#640125', markeredgecolor='grey',)
ax4.annotate('D', xy=(0.1, .92), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

ax5.plt = qqplot(df.plate_maria, line='q', ax=ax5, fit=True, 
                 linewidth=.1, alpha = .4, markerfacecolor='#b44c97', markeredgecolor='grey',)
ax5.annotate('E', xy=(0.1, .92), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

ax6.plt = qqplot(df.igneous_volc, line='q',  ax=ax6, fit=True, 
                 lw=.1, alpha = .4, markerfacecolor='#4d5aaf', markeredgecolor='grey',)
ax6.annotate('F', xy=(0.1, .92), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

plt.show()


# In[ ]:




