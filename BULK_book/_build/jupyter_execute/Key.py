#!/usr/bin/env python
# coding: utf-8

# # Key Actors

# Table 2. Additional Key Actors in the Horsefly River watershed. Key Actors are the individuals, groups, and/or organizations, outside of the planning team, with influence and relevant experience in the watershed, whose engagement will be critical for the successful implementation of this WCRP. 

# In[1]:


from IPython.display import display
import pandas as pd

data = pd.read_csv('tables\key_actors.csv', index_col=False)

data.style.hide_index().set_properties(**{'text-align': 'left'})

