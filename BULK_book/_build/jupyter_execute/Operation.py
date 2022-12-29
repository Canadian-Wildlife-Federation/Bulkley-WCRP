#!/usr/bin/env python
# coding: utf-8

# # Operational Plan
# 
# The operational plan represents a preliminary exercise undertaken by the planning team to identify the potential leads, potential participants, and estimated cost for the implementation of each action in the Horsefly River watershed. The table below summarizes individuals, groups, or organizations that the planning team felt could lead or participate in the implementation of the plan and should be interpreted as the first step in on-going planning and engagement to develop more detailed and sophisticated action plans for each entry in the table. The individuals, groups, and organizations listed under the "Lead(s)" or "Potential Participants" columns are those that provisionally expressed interest in participating in one of those roles or were suggested by the planning team for further engagement (denoted in bold), for those that are not members of the planning team. The leads, participants, and estimated costs in the operational plan are not binding nor an official commitment of resources, but rather provide a roadmap for future coordination and engagement to work towards implementation of the WCRP. 
# 
# Table 13. Operational plan to support the implementation of strategies and actions to improve connectivity for target species in the Horsefly River watershed.

# In[1]:


from IPython.display import display
import pandas as pd
import numpy as np

def df_operation(val):
    return "background-color: black; color: white"


data = pd.read_csv('tables\Table13.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

rows = pd.IndexSlice[[0,10,16,23,26,29,30,31], :]

data.style.applymap(df_operation, subset=rows).hide_index().set_properties(**{'text-align': 'left'})

