#!/usr/bin/env python
# coding: utf-8

# # Progress Tracking Plan

# In[1]:


from IPython.display import display
import pandas as pd

data = pd.read_csv('tables\Table12.csv', index_col=False)

data.style.hide_index().set_properties(**{'text-align': 'left'})

