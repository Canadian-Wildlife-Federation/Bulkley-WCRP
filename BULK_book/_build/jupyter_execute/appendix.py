#!/usr/bin/env python
# coding: utf-8

# # Appendix

# ## Appendix A: Modelled Anadromous Salmon Habitat Maps
# 
# High-resolution PDF maps of the Horsefly River watershed and model results can be accessed [here](https://github.com/smnorris/bcfishpass/tree/main/wcrp/pdfs). The watershed is divided into multiple maps sheets to allow for detailed examination of modelled spawning and rearing habitat, multiple barrier types, and priority barriers identified through this planning process. The locations of WCRP priority barriers and associated map sheet numbers are shown below. In each individual map sheet, priority barriers are symbolized using the following notation:   .

# ```{figure} figure8.png
# ---
# height: 400px
# width: 1000px
# name: fig8
# ---
# Horsefly River watershed overview map identifying the portions of the watershed covered by each map sheet (grey squares) and the prioritized barriers on the intermediate barrier list (orange points; see Appendix C).
# ```

# ## Appendix B: Connectivity Status Assessment Methods
# 
# The connectivity status assessment for anadromous salmonids in the Horsefly River watershed builds on existing connectivity modelling work undertaken by the BC Fish Passage Technical Working Group, resulting in a flexible, customizable open-source spatial model called "bcfishpass". The model spatially locates known and modelled barriers to fish passage, identifies potential spawning and rearing habitat for target species, and estimates the amount of habitat that is currently accessible to target species. The model uses an adapted version of the Intrinsic Potential (IP) fish habitat modelling framework (see Sheer et al. 2009 for an overview of the IP framework). The habitat model uses two geomorphic characteristics of the stream network — channel gradient and mean annual discharge — to identify potential spawning habitat and rearing habitat for each target species. The habitat model does not attempt to definitively map each habitat type nor estimate habitat quality, but rather identifies stream segments that have high potential to support spawning or rearing habitat for each species based on the geomorphic characteristics of the segment. For more details on the connectivity and habitat model structure and parameters, please see Mazany-Wright et al. 2021a. The variables and thresholds used to model potential spawning and rearing habitat for each target species are summarized in Table 15. The quantity of modelled habitat for each species was aggregated for each habitat type and represents a linear measure of potential habitat. To recognize the rearing value provided by features represented by polygons for certain species (e.g., wetlands for Coho Salmon and lakes for Sockeye Salmon) a multiplier of 1.5x the length of the stream segments flowing through the polygons was applied.
# 
# Table 15. Parameters and thresholds used to inform the Intrinsic Potential habitat model for spawning and rearing habitat for each target species in the Horsefly River watershed.

# In[1]:


from IPython.display import display, HTML
import pandas as pd
import numpy as np

data = pd.read_csv('tables\Table15.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)


data.style.hide_index().set_properties(**{'text-align': 'left'})


# ## Appendix C: Horsefly River Watershed Barrier Prioritization Summary
# 
# The primary conservation outcome of the WCRP will be the remediation of barriers to connectivity in the Horsefly River watershed. To achieve Goal 1 in this plan, it is necessary to prioritize and identify a suite of barriers that, if remediated, will provide access to a minimum of 11.7 km of spawning or rearing habitat (Table 16):
# 
# Table 16. Spawning and rearing habitat connectivity gain requirements to meet WCRP goals in the Horsefly River watershed. The measures of currently accessible and total habitat values are derived from the Intrinsic Potential habitat model described in Appendix B.
# 

# In[2]:


import requests
import json

def barrier_extent(barrier_type):

    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_barrier_extent/items.json?watershed_group_code=HORS&barrier_type=' + barrier_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    blocked_km = result[0]['all_habitat_blocked_km']
    blocked_pct = result[0]['all_habitat_blocked_pct']

    return blocked_km, blocked_pct

def barrier_count(barrier_type):
    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_barrier_count/items.json?watershed_group_code=HORS&barrier_type=' + barrier_type

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

    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_barrier_severity/items.json?watershed_group_code=HORS&barrier_type=' + barrier_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    n_assessed_barrier = result[0]['n_assessed_barrier']
    n_assess_total = result[0]['n_assess_total']
    pct_assessed_barrier = result[0]['pct_assessed_barrier']

    return n_assessed_barrier, n_assess_total, pct_assessed_barrier

def watershed_connectivity(habitat_type):

    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_watershed_connectivity_status/items.json?watershed_group_code=HORS&barrier_type=' + habitat_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    connect_stat = result[0]['connectivity_status']

    return str(round(connect_stat))

    #table 16----------------------------------------------------------------------
    #--------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib as mpl

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

df.style.hide_index()


# The barrier prioritization analysis ranked barriers by the amount of habitat blocked to produce an "intermediate barrier list" comprising more barriers than are needed to achieve the goals. A longer list of barriers is needed due to the inherent assumptions in the connectivity model, habitat model, and gaps in available data. Barriers that have been modelled (i.e., points where streams and road/rail networks intersect) are assumed to be barriers until field verification is undertaken and structures that have been assessed as "potential" barriers (e.g., may be passable at certain flow levels or for certain life history stages) require further investigation before a definitive remediation decision is made. Additionally, the habitat model identifies stream segments that have the potential to support spawning or rearing habitat for target species but does not attempt to quantify habitat quality or suitability (see Appendix B), which will require additional field verification once barrier assessments have completed. As such, the intermediate list of barriers below (Table 18) should be considered as a starting point in the prioritization process and represents structures that are a priority to evaluate further through barrier assessment and habitat confirmations because some structures will likely be passable, others will not be associated with usable habitat, and others may not be feasible to remediate because of logistic considerations. The intermediate barrier list was updated following the barrier assessments and habitat confirmations that were undertaken during the 2021 field season - some barriers were moved forward to the "priority barrier list" (see Table 19) and others were eliminated from consideration due to one or more of the considerations discussed above (see Table 17). The priority barrier list represents structures that were confirmed to be partial or full barriers to fish passage and that block access to confirmed habitat. Barriers on the priority list were reviewed by planning team members and selected for inclusion for proactive pursual of remediation.  For more details on the barrier prioritization model, please see Mazany-Wright et al. 2021a.
# 
# Table 17. List of barriers that were prioritized as part of the first iteration of the intermediate barrier list (field assessments occurred during the 2021 field season) but were removed from consideration for pursual of proactive remediation following discussion with the planning team due to these structures not existing, being passable, not be associated with usable habitat, or deemed not feasible to remediate because of logistic considerations.

# In[3]:


data = pd.read_csv('tables\Table17.csv', index_col=False)
data = data.replace(np.nan, '', regex=True)

data.style.hide_index().set_properties(**{'text-align': 'left'})


# Table 18. Updated intermediate barrier list resulting from the second barrier prioritization analysis in the Horsefly River watershed. After assessing the potential barriers on the first iteration of the intermediate list (2021 field season) and either identifying them as remediation priorities (see Table 18) or eliminating them from consideration (e.g., because they passed fish or did hot have suitable habitat upstream), the remaining potential barriers in the watershed were re-prioritized. The barriers on this list were prioritized to exceed the connectivity goals of the plan. Barriers highlighted in the same colour represent sets of barriers that have been prioritized as a group. In the Barrier Status column, P = potential barrier and B = confirmed barrier. All barrier assessment data is compiled from the BC Provincial Stream Crossing Inventory System.

# In[4]:


data = pd.read_csv('tables\Table18.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

data.style.hide_index().set_properties(**{'text-align': 'left'})


# Table 19. The Horsefly River watershed priority barrier list, which includes barriers that have undergone field assessment, been reviewed by the planning team, and selected to pursue for proactive remediation.

# In[5]:


data = pd.read_csv('tables\priority_barriers.csv', index_col=False)

#pd.options.display.max_columns=10

data = data.replace(np.nan, '', regex=True)

data.style.hide_index().set_properties(**{'text-align': 'left'})


# Out of the 20 barriers on the intermediate list, 16 require further field assessment before selection as a final barrier to pursue for remediation:
# 
# Table 20. Field assessment requirements for the intermediate barrier list in the Horsefly River watershed. The cost per barrier values are estimates based on previously completed field work. The habitat confirmation count is based on the assumption that the 12 barriers requiring barrier assessments will also require a subsequent confirmation. In the case that some barriers are identified as unsuitable candidates for habitat confirmations, the total cost will be reduced.
# 

# In[6]:


def df_style(val):
    return "font-weight: bold"


data = pd.read_csv('tables\Table20.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

last_row = pd.IndexSlice[data.index[data.index == 2], :]

data.style.applymap(df_style, subset=last_row).hide_index()


# There are currently 14 barriers on the priority barrier list, which will be pursued for proactive remediation to achieve the connectivity goals in this plan:
# 
# 
# Table 21. Preliminary barrier remediation cost estimate to reach connectivity goals in the Horsefly River watershed. Cost per barrier values are estimated based on the average cost of previously completed projects. Barrier counts and total costs are subject to change as more information is collected through the implementation of this plan.
# 

# In[7]:


data = pd.read_csv('tables\Table21.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

last_row = pd.IndexSlice[data.index[data.index == 3], :]

data.style.applymap(df_style, subset=last_row).hide_index()

