#!/usr/bin/env python
# coding: utf-8

# # Appendix B

# In[1]:


import requests
import json
from myst_nb import glue

def barrier_extent(barrier_type):

    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_barrier_extent/items.json?watershed_group_code=BULK&barrier_type=' + barrier_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    blocked_km = result[0]['all_habitat_blocked_km']
    blocked_pct = result[0]['all_habitat_blocked_pct']

    return blocked_km, blocked_pct

def barrier_count(barrier_type):
    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_barrier_count/items.json?watershed_group_code=BULK&barrier_type=' + barrier_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    n_passable = result[0]['n_passable']
    n_barrier = result[0]['n_barrier']
    n_potential = result[0]['n_potential']
    n_unknown = result[0]['n_unknown']

    sum_bar = (n_passable, n_barrier, n_potential, n_unknown)

    return n_passable, n_barrier, n_potential, n_unknown, sum(sum_bar)

def barrier_severity(barrier_type):

    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_barrier_severity/items.json?watershed_group_code=BULK&barrier_type=' + barrier_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    n_assessed_barrier = result[0]['n_assessed_barrier']
    n_assess_total = result[0]['n_assess_total']
    pct_assessed_barrier = result[0]['pct_assessed_barrier']

    return n_assessed_barrier, n_assess_total, pct_assessed_barrier

def watershed_connectivity(habitat_type):

    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_watershed_connectivity_status/items.json?watershed_group_code=BULK&barrier_type=' + habitat_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    connect_stat = result[0]['connectivity_status']

    return str(round(connect_stat))

import warnings

warnings.filterwarnings('ignore')

total = 526.95 #total km in HORS
access = round(total * (int(watershed_connectivity("ALL"))/100),2)
gain = round((total*0.96)-access,2)

glue("gain", str(gain))


# ```{include} ../content/appendixb-md.md
# :start-after: "# Appendix B"
# :end-before: "The barrier prioritization process comprises three stages:"
# ```

# In[2]:


#table 16----------------------------------------------------------------------
#--------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib as mpl
import warnings

warnings.filterwarnings('ignore')

total = 526.95 #total km in HORS
access = round(total * (int(watershed_connectivity("ALL"))/100),2)
gain = round((total*0.96)-access,2)

df = pd.DataFrame({"Habitat Type":["Spawning and Rearing"],
               "Currently accessible (km)":[str(access)],
               "Total": [str(total)],
               "Current Connectivity Status":[str(watershed_connectivity("ALL"))+"%"],
               "Goal": ["96%"],
               "Gain required (km)": [str(gain)]
               })

data = df.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table16", data)


# ```{glue:figure} Table16
# :name: "table16"
# 
# *Spawning and rearing habitat connectivity gain requirements to meet WCRP goals in the Horsefly River watershed. The measures of currently accessible and total habitat values are derived from the Intrinsic Potential habitat model described in Appendix B.*
# ```

# ```{include} ../content/appendixb-md.md
# :start-after: "rearing habitat ({numref}`table16`):"
# :end-before: "{glue:text}`inter_num` barriers on the intermediate"
# ```
# 

# In[3]:


data = pd.read_csv('../tables/Table17.csv', index_col=False)
data = data.replace(np.nan, '', regex=True)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table17", data)


# ```{glue:figure} Table17
# :name: "table17"
# 
# *List of crossings that were removed from the barrier prioritization list following field assessment. Crossings include those prioritized as part of the first iteration of the intermediate barrier list and additional sites selected by 2021 field crews that were removed following discussion with the planning team due to these structures not existing, being passable, not being associated with usable habitat, or deemed not feasible to remediate because of logistic considerations.*
# ```

# In[4]:


data = pd.read_csv('../tables/table18.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

#num of rows
num_p = len(data.index)

glue("Table18", data)
glue("inter_num", num_p)


# ```{glue:figure} Table18
# :figwidth: 1000px
# :align: left
# :name: "table18"
# 
# *Updated intermediate barrier list resulting from the second barrier prioritization analysis in the Bulkley River watershed. After assessing the potential barriers on the first iteration of the intermediate list (during 2021 field season) and either identifying them as remediation priorities or eliminating them from consideration (e.g., because they passed fish or did hot have suitable habitat upstream), the remaining potential barriers in the watershed were re-prioritized. The barriers on this list were prioritized to exceed the connectivity goals of the plan. Barriers highlighted in the same colour represent sets of barriers that have been prioritized as a group. In the Barrier Status column, P = potential barrier and B = confirmed barrier. All barrier assessment data is compiled from the BC Provincial Stream Crossing Inventory System.*
# ```

# In[5]:


data = pd.read_csv('../tables/priority_barriers.csv', index_col=False)

#pd.options.display.max_columns=10

data = data.replace(np.nan, '', regex=True)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

#num of rows
num_p = len(data.index)

glue("Table19", data)
glue("prior_num", num_p)


# ```{glue:figure} Table19
# :figwidth: 1100px
# :align: left
# :name: "table19"
# 
# 
# *The Bulkley River watershed priority barrier list, which includes barriers that have undergone field assessment, been reviewed by the planning team, and selected to pursue for proactive remediation.*
# ```

# ```{include} ../content/appendixb-md.md
# :start-after: "please see Mazany-Wright et al. 2021a."
# :end-before: "Based on the results of the prioritization analysis"
# ```
# 

# In[6]:


def df_style(val):
    return "font-weight: bold"


data = pd.read_csv('../tables/Table20.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

last_row = pd.IndexSlice[data.index[data.index == 2], :]

data = data.style.applymap(df_style, subset=last_row).hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table20", data)


# 
# ```{glue:figure} Table20
# :name: "table20"
# 
# *Field assessment requirements for the intermediate barrier list in the Bulkley River watershed. The cost per barrier values are estimates based on previously completed field work. The habitat confirmation count is based on the assumption that the 23 barriers requiring barrier assessments will also require a subsequent confirmation. In the case that some barriers are identified as unsuitable candidates for habitat confirmations, the total cost will be reduced.*
# ```

# ```{include} ../content/appendixb-md.md
# :start-after: "final barrier to pursue for remediation:"
# ```

# In[7]:


data = pd.read_csv('../tables/Table21.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

last_row = pd.IndexSlice[data.index[data.index == 4], :]

data = data.style.applymap(df_style, subset=last_row).hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table21", data)


# 
# ```{glue:figure} Table21
# :name: "table21"
# 
# *Preliminary barrier remediation cost estimate to reach connectivity goals in the Bulkley River watershed. Cost per barrier values are estimated based on the average cost of previously completed projects. Barrier counts and total costs are subject to change as more information is collected through the implementation of this plan.*
# ```
