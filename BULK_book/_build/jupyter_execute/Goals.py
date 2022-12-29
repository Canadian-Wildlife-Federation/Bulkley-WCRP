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

