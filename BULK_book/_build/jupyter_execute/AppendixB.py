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


# ## Horsefly River Watershed Barrier Prioritization Summary
# 
# The primary conservation outcome of the WCRP will be the remediation of barriers to connectivity in the Horsefly River watershed. To achieve Goal 1 in this plan, it is necessary to prioritize and identify a suite of barriers that, if remediated, will provide access to a minimum of {glue:text}`gain` km of spawning or rearing habitat ({numref}`table16`):
# 

# In[2]:


from IPython.display import Markdown, display

Markdown("markdown-file.md")


# In[3]:


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

# The barrier prioritization process comprises three stages:
# -	Stage 1: preliminary barrier list
# -	Stage 2: intermediate barrier list
# -	Stage 3: priority barrier list
# 
# Initially, the barrier prioritization analysis ranked all barriers in the watershed by the amount of habitat blocked to produce a "preliminary barrier list", which also accounted for assessing "sets" of barriers for which remediation could be coordinated to maximize connectivity gains. From this list, the top-ranking subset of barriers - comprising more barriers than are needed to achieve the goals - is selected to produce an "intermediate barrier list". Barriers that did not rank highly in the model results, but were identified as priority barriers by the local partners were also added to the intermediate barrier list. A longer list of barriers is needed due to the inherent assumptions and uncertainty in the connectivity and habitat models and gaps in available data. Barriers that have been modelled (i.e., points where streams and road/rail networks intersect) are assumed to be barriers until field verification is undertaken and structures that have been assessed as "potential" barriers (e.g., may be passable at certain flow levels or for certain life history stages) require further investigation before a definitive remediation decision is made. Additionally, the habitat model identifies stream segments that have the potential to support spawning or rearing habitat for target species but does not attempt to quantify habitat quality or suitability (see Appendix B), which will require additional field verification once barrier assessments have completed. As such, the intermediate barrier list below (Table 16) should be considered as a starting point in the prioritization process and represents structures that are a priority to evaluate further through barrier assessment and habitat confirmations because some structures will likely be passable, others will not be associated with usable habitat, and others may not be feasible to remediate because of logistic considerations.
# 
# The intermediate barrier list was updated following the barrier assessments and habitat confirmations that were undertaken during the 2021 field season - some barriers were moved forward to the "priority barrier list" (Table 17) and others were eliminated from consideration due to one or more of the considerations discussed in Table 15. The priority barrier list represents structures that were confirmed to be partial or full barriers to fish passage and that block access to confirmed habitat. Barriers on the priority list were reviewed by planning team members and selected for inclusion for proactive pursual of remediation.  For more details on the barrier prioritization model, please see Mazany-Wright et al. 2021a.
# 

# In[4]:


data = pd.read_csv('Table17.csv', index_col=False)
data = data.replace(np.nan, '', regex=True)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table15", data)


# ```{glue:figure} Table15
# :name: "table15"
# 
# *List of crossings that were removed from the barrier prioritization list following field assessment. Crossings include those prioritized as part of the first iteration of the intermediate barrier list and additional sites selected by 2021 field crews that were removed following discussion with the planning team due to these structures not existing, being passable, not being associated with usable habitat, or deemed not feasible to remediate because of logistic considerations. *
# ```

# In[5]:


data = pd.read_csv('table18.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

#num of rows
num_p = len(data.index)

glue("Table16", data)
glue("inter_num", num_p)


# ```{glue:figure} Table16
# :figwidth: 1000px
# :align: left
# :name: "table16"
# 
# *Updated intermediate barrier list resulting from the second barrier prioritization analysis in the Bulkley River watershed. After assessing the potential barriers on the first iteration of the intermediate list (during 2021 field season) and either identifying them as remediation priorities or eliminating them from consideration (e.g., because they passed fish or did hot have suitable habitat upstream), the remaining potential barriers in the watershed were re-prioritized. The barriers on this list were prioritized to exceed the connectivity goals of the plan. Barriers highlighted in the same colour represent sets of barriers that have been prioritized as a group. In the Barrier Status column, P = potential barrier and B = confirmed barrier. All barrier assessment data is compiled from the BC Provincial Stream Crossing Inventory System.*
# ```

# In[6]:


data = pd.read_csv('priority_barriers.csv', index_col=False)

#pd.options.display.max_columns=10

data = data.replace(np.nan, '', regex=True)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

#num of rows
num_p = len(data.index)

glue("Table17", data)
glue("prior_num", num_p)


# ```{glue:figure} Table17
# :figwidth: 1100px
# :align: left
# :name: "table17"
# 
# 
# *The Bulkley River watershed priority barrier list, which includes barriers that have undergone field assessment, been reviewed by the planning team, and selected to pursue for proactive remediation.*
# ```

# {glue:text}`inter_num` barriers on the intermediate list require short-term field assessments before selection as a final barrier to pursue for remediation:
# 

# In[7]:


def df_style(val):
    return "font-weight: bold"


data = pd.read_csv('Table20.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

last_row = pd.IndexSlice[data.index[data.index == 2], :]

data = data.style.applymap(df_style, subset=last_row).hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table18", data)


# 
# ```{glue:figure} Table18
# :name: "table18"
# 
# *Field assessment requirements for the intermediate barrier list in the Bulkley River watershed. The cost per barrier values are estimates based on previously completed field work. The habitat confirmation count is based on the assumption that the 23 barriers requiring barrier assessments will also require a subsequent confirmation. In the case that some barriers are identified as unsuitable candidates for habitat confirmations, the total cost will be reduced.*
# ```

# Based on the results of the prioritization analysis, {glue:text}`inter_num` barriers from the intermediate barrier list are required to be remediated to achieve the connectivity goals in this plan:

# In[8]:


data = pd.read_csv('Table21.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

last_row = pd.IndexSlice[data.index[data.index == 4], :]

data = data.style.applymap(df_style, subset=last_row).hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table19", data)


# 
# ```{glue:figure} Table19
# :name: "table19"
# 
# *Preliminary barrier remediation cost estimate to reach connectivity goals in the Bulkley River watershed. Cost per barrier values are estimated based on the average cost of previously completed projects. Barrier counts and total costs are subject to change as more information is collected through the implementation of this plan.*
# ```
