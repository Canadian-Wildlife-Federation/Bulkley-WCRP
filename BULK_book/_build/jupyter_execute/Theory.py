#!/usr/bin/env python
# coding: utf-8

# # Theories of Change & Objectives
# 
# Theories of Change are explicit assumptions around how the identified actions will achieve gains in connectivity and contribute towards reaching the goals of the plan. To develop Theories of Change, the planning team developed explicit assumptions for each strategy which helped to clarify the rationale used for undertaking actions and provided an opportunity for feedback on invalid assumptions or missing opportunities. The Theories of Change are results oriented and clearly define the expected outcome. The following theory of change models were developed by the WCRP planning team to “map” the causal (“if-then”) progression of assumptions of how the actions within a strategy work together to achieve project goals. 

# ```{figure} figure4.png
# ---
# height: 400px
# width: 1000px
# name: fig4
# ---
# Theory of change developed by the planning team for the actions identified under Strategy 1: Crossing Remediation in the Horsefly River watershed.
# ```

# ```{figure} figure5.png
# ---
# height: 400px
# width: 1000px
# name: fig5
# ---
# Theory of change developed by the planning team for the actions identified under Strategy 2: Lateral Barrier Remediation in the Horsefly River watershed.
# ```

# ```{figure} figure6.png
# ---
# height: 400px
# width: 1000px
# name: fig6
# ---
# Theory of change developed by the planning team for the actions identified under Strategy 3: Dam Remediation in the Horsefly River watershed.
# ```

# ```{figure} figure7.png
# ---
# height: 400px
# width: 1000px
# name: fig7
# ---
# Theory of change developed by the planning team for the actions identified under Strategy 4: Barrier Prevention in the Horsefly River watershed.
# ```

# In[1]:


import pandas as pd

data = pd.read_csv('tables\Table11.csv', index_col=False)

data.style.hide_index().set_properties(**{'text-align': 'left'})

