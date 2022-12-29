#!/usr/bin/env python
# coding: utf-8

# # Goals
# 
# Table 9. Goals to improve (1) spawning and rearing and (2) overwintering habitat connectivity for target species in the Horsefly River watershed over the lifespan of the WCRP (2021-2040). The goals were established through discussions with the planning team and represent the resulting desired state of connectivity in the watershed. The goals are subject to change as more information and data are collected over the course of the plan timeline (e.g., the current connectivity status is updated based on barrier field assessments). 

# In[1]:


#creating table 7
import pandas as pd
import numpy as np

df = pd.DataFrame({"Goal #": [1,2],
                   "Goal": ["By 2040, the percent (%) of total linear habitat accessible to anadromous salmon will increase from 94% to 96% within the Horsefly River watershed (i.e., reconnect at least 11.7 km of habitat).",
                            "By 2024, the total area of overwintering habitat accessible to Anadromous Salmon will increase by 1,500 m2 within the Horsefly River watershed. "]
                    })

df.style.hide_index().set_properties(**{'text-align': 'left'})


# # Strategies & Actions
# 
# Table 10. Effectiveness evaluation of identified conservation strategies and associated actions to improve connectivity for target species in the Horsefly River watershed. The planning team identified five broad strategies to implement through this WCRP, 1) crossing remediation, 2) lateral barrier remediation, 3) dam remediation, 4) barrier prevention, and 5) communication and education. Individual actions were qualitatively evaluated based on the anticipated effect each action will have on realizing on-the-ground gains in connectivity. Effectiveness ratings are based on a combination of "Feasibility and "Impact", Feasibility is defined as the degree to which the project team can implement the action within realistic constraints (financial, time, ethical, etc.) and Impact is the degree to which the action is likely to contribute to achieving one or more of the goals established in this plan.
# 
# ## Strategy 1: Crossing Remediation

# In[2]:


import numpy as np
from IPython.display import display
import pandas as pd

data = pd.read_csv('tables\Strategy1.csv', index_col=False)

def fix_table(val):
    return str(val)

def highlighttab7(val):
    red = '#ff0000;'
    yellow = '#ffff00;'
    lgreen = '#92d050;'
    dgreen = '#03853e;'

    if val=="Medium" or val=="Need more information": color = yellow
    elif val=="Very high" or val=="Very effective" : color = lgreen
    elif val =="High" or val=="Effective": color = dgreen
    else: color = 'white'
    return 'background-color: %s' % color

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data.style.applymap(highlighttab7).hide_index().set_properties(**{'text-align': 'left'})


# ## Strategy 2: Lateral Barrier Remediation	

# In[3]:


data = pd.read_csv('tables\Strategy2.csv', escapechar='\n', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data = data.style.applymap(highlighttab7).hide_index().set_properties(**{'text-align': 'left'})

display(data)


# ## Strategy 3: Dam Remediation

# In[4]:


data = pd.read_csv('tables\Strategy3.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data.style.applymap(highlighttab7).hide_index().set_properties(**{'text-align': 'left'})


# ## Strategy 4: Barrier Prevention

# In[5]:


import pandas as pd

data = pd.read_csv('tables\Strategy4.csv', index_col=False)




data = data.applymap(fix_table)

data.style.applymap(highlighttab7).hide_index().set_properties(**{'text-align': 'left'})

#display(data)


# ## Strategy 5: Communication and Education

# In[6]:


data = pd.read_csv('tables\Strategy5.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data.style.applymap(highlighttab7).hide_index().set_properties(**{'text-align': 'left'})

