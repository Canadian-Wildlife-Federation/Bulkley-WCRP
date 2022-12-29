#!/usr/bin/env python
# coding: utf-8

# # Connectivity Status Assessment and Action Plan

# In[1]:


import requests
import json
import pandas
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


# The planning team devised two Key Ecological Attributes (KEAs) and associated indicators to assess the current connectivity status of the watershed – Accessible Spawning Habitat and Accessible Rearing Habitat. KEAs are the key aspects of anadromous salmonid ecology that are being targeted by this WCRP. The connectivity status for the Anadromous Salmonid KEAs were used to establish goals to improve habitat connectivity in the watershed and will be the baseline against which progress is tracked over time. 
# 
# The current connectivity status assessment relies on GIS analyses to map known and modelled barriers to fish passage, identify stream reaches that have potential spawning and rearing habitat, estimate the proportion of habitat that is currently accessible to target species, and prioritize barriers for field assessment that would provide the greatest gains in connectivity. To support a flexible prioritization framework to identify priority barriers in the watershed, two assumptions are made: 1) any modelled (i.e., passability status is unknown) or partial barriers are treated as complete barriers to passage and 2) the habitat modelling is binary, it does not assign any habitat quality values. As such, the current connectivity status will be refined over time as more data on habitat and barriers are collected. For more detail on how the connectivity status assessments were conducted, see Appendix B.
# 

# In[2]:


#creating table 7
import pandas as pd
import numpy as np
import matplotlib as mpl
import warnings

warnings.filterwarnings('ignore')

df = pd.DataFrame({"Target Species":["Andromous Salmon"," "],
                   "KEA":["Available Habitat"," "],
                   "Indicator":["% of total linear spawning habitat","Current Status:"],
                   "Poor":["<50%"," "],
                   "Fair":["51-75%",watershed_connectivity("ALL")],
                   "Good":["76-90%"," "],
                   "Very Good":[">90%", " "]
                   })


def highlighttab7(val):
    red = '#ff0000;'
    yellow = '#ffff00;'
    lgreen = '#92d050;'
    dgreen = '#03853e;'

    if val=="<50%" : color = red
    elif val[0:].isdigit() and int(val) < 50 : color = red
    elif val=="51-75%"  : color = yellow
    elif val[0:].isdigit() and (int(val) >= 51 and int(val) < 75) : color = yellow
    elif val=="76-90%"  : color = lgreen
    elif val[0:].isdigit() and (int(val) >= 76 and int(val) < 90) : color = lgreen 
    elif val ==">90%": color = dgreen
    elif val[0:].isdigit() and int(val) >= 90 : color = dgreen 
    elif val == "Current Status:" : return "font-weight: bold"
    else: color = 'white'
    return 'background-color: %s' % color

df.style.applymap(highlighttab7).hide_index()



# **Comments**: Indicator rating definitions are based on the consensus decisions of the planning team. The current status is based on the CWF Barrier Prioritization Model output, which is current as of October 2022. 

# In[3]:


#creating table 7
import pandas as pd
import numpy as np
import matplotlib as mpl
import warnings
from myst_nb import glue

warnings.filterwarnings('ignore')

df = pd.DataFrame({"Target Species":["Andromous Salmon",""],
                   "KEA":["Available Overwintering Habitat",""],
                   "Indicator":["% of total linear rearing habitat accessible","Current Status:"],
                   "Poor":["<50%"," "],
                   "Fair":["51-75%","70%"],
                   "Good":["76-90%"," "],
                   "Very Good":[">90%", " "]
                   })

def highlighttab7b(val):
    red = '#ff0000;'
    yellow = '#ffff00;'
    lgreen = '#92d050;'
    dgreen = '#03853e;'

    if val=="<50%" : color = red
    elif val[0:].isdigit() and int(val) < 50 : color = red
    elif val=="51-75%"  : color = yellow
    elif val=="70%"  : color = yellow
    elif val[0:].isdigit() and (int(val) >= 51 and int(val) < 75) : color = yellow
    elif val=="76-90%"  : color = lgreen
    elif val[0:].isdigit() and (int(val) >= 76 and int(val) < 90) : color = lgreen 
    elif val ==">90%": color = dgreen
    elif val[0:].isdigit() and int(val) >= 90 : color = dgreen 
    elif val == "Current Status:" : return "font-weight: bold"
    else: color = 'white'
    return 'background-color: %s' % color

data = df.style.applymap(highlighttab7b).hide_index()

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table7", data)


# **Comments:**  Indicator rating definitions are based on the consensus decisions of the planning team. The current status is based on the CWF Barrier Prioritization Model output, which is current as of October 2022. 

# ```{glue:figure} Table7
# :name: "table7"
# 
# *Connectivity status assessment for spawning (a) and rearing (b) habitat in the Bulkley River watershed. The two KEAs - Accessible Spawning Habitat and Accessible Rearing Habitat - are evaluated by dividing the length of linear habitat (of each type) that is currently accessible to target species by the total length of all linear habitat (of each type) in the watershed.*
# ```

# # Barrier Types

# The following table highlights which barrier types pose the greatest threat to anadromous salmonids in the watershed. The results of this assessment were used to inform the subsequent planning steps, as well as to identify knowledge gaps where there is little spatial data to inform the assessment for a specific barrier type.
# 

# In[4]:


from ipywidgets import *
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

#condition
def condition(pct):
    rating1 = ""
    if pct < 30 : rating1 = "Low"
    elif (pct >= 30) and (pct < 71) : rating1 = "Medium"
    elif (pct >= 71) and (pct < 90) : rating1 = "High"
    else : rating1 = "Very High"
    return rating1

#rating classifier
def rating2(threat, barrier):
    if threat == "extent":
        if barrier == "DAM":
            pct = barrier_extent(barrier)[1]
            rating = condition(pct)
        elif barrier == "ROAD":
            pct = barrier_extent('ROAD, RESOURCE/OTHER')[1] + barrier_extent('ROAD, DEMOGRAPHIC')[1]
            rating = condition(pct)
        elif barrier == "RAIL":
            pct = barrier_extent(barrier)[1]
            rating = condition(pct)
        elif barrier == "TRAIL":
            pct = barrier_extent(barrier)[1]
            rating = condition(pct)
    elif threat == "severity":
        if barrier == "DAM":
            pct = barrier_severity(barrier)[2]
            rating = condition(pct)
        elif barrier == "ROAD":
            pct = barrier_severity('ROAD, RESOURCE/OTHER')[2] + barrier_severity('ROAD, DEMOGRAPHIC')[2]
            rating = condition(pct)
        elif barrier == "RAIL":
            pct = barrier_severity(barrier)[1]      
            rating = condition(pct)
        elif barrier == "TRAIL":
            pct = barrier_severity(barrier)[1]      
            rating = condition(pct)
    return rating
            

        




df = pd.DataFrame({"Barrier Types":["Road-Stream Crossings","Rail-Stream Crossings","Lateral Barriers","Natural Barriers","Large Dams(<3m height)","Small Dams(<3m height)","Trail-stream Crossings"],
                   "Extent":[rating2("extent", "ROAD"),rating2("extent", "RAIL"),"Medium","Medium",rating2("extent", "DAM"), "Low", rating2("extent", "TRAIL")],
                   "Severity":[rating2("severity", "ROAD"),rating2("severity", "RAIL"),"Very High","High",rating2("severity", "DAM"), rating2("severity", "DAM"), rating2("severity", "TRAIL")],
                   "Irreversibility":["Medium","Medium","Medium","Medium","High", "Medium", "Low"],
                   "Overall Threat Rating:":["High","High","Medium","Medium", "Low", "Low", "Low"]
                   }).style.set_properties(subset=["Overall Threat Rating:"], **{'font-weight': 'bold'})

def highlight(val):
    red = '#ff0000;'
    yellow = '#ffff00;'
    lgreen = '#92d050;'
    dgreen = '#03853e;'

    if val=="Very High": color = red
    elif val=="High": color = yellow
    elif val=="Medium": color = lgreen
    elif val =="Low": color = dgreen
    else: color = 'white'
    return 'background-color: %s' % color

#df = df.style.set_properties(subset=["Overall Threat Rating"], **{'font-weight': 'bold'})

data = df.applymap(highlight).hide_index()

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table8", data)




# ```{glue:figure} Table8
# :name: "table8"
# 
# *Barrier Types in the Bulkley River watershed and barrier rating assessment results. For each barrier type listed, "Extent refers to the proportion of anadromous salmonid habitat that is being blocked by that barrier type, "Severity" is the proportion of structures for each barrier type that are known to block passage for target species based on field assessments, and "Irreversibility" is the degree to which the effects of a barrier type can be reversed and connectivity restored. The amount of habitat blocked used in this exercise is a representation of total amount of combined spawning and rearing habitat.*
# ```

# In[5]:


import requests
import json
import pandas
from myst_nb import glue



#glue class for variables to allow embedding in markdown
glue("dam_km", barrier_extent('DAM')[0])
glue("dam_pct", barrier_extent('DAM')[1])
glue("total_barrier", barrier_severity('DAM')[1])

#glue class for rail-stream crossings
glue("rail_km", barrier_extent('RAIL')[0])
glue("rail_pct", barrier_extent('RAIL')[1])
glue("rail_total_barrier", barrier_severity('RAIL')[1])
glue("rail_sev", round(barrier_severity('RAIL')[2]))


# ### Small Dams (<3 m height)
# 
# There are {glue:text}`total_barrier` mapped small dams on “potentially accessible” stream segments in the watershed, blocking a total of {glue:text}`dam_km` km (~{glue:text}`dam_pct`% of the total blocked habitat) of modelled spawning and rearing habitat for anadromous salmon, resulting in a medium extent. The extent rating of these structures was confirmed by the planning team. There are two known fish-passage structures in the watershed, including on the dam at the outlet of McKinley Lake. The remaining dams likely block passage for anadromous salmon and would require significant resources to remediate. However, due to the limited extent of dams in the watershed, a final pressure rating of Medium was assigned. Four small dams were identified on the priority barrier list (see Appendix B). Three of the dams require further assessment and confirmation of upstream habitat quality, and the dam observed at the outlet of Kwun Lake does not exist. 

# In[6]:


#glue class for variables to allow embedding in markdown
glue("resource_km", barrier_extent('ROAD, RESOURCE/OTHER')[0])
glue("resource_pct", round(barrier_extent('ROAD, RESOURCE/OTHER')[1]))
glue("demo_km", barrier_extent('ROAD, DEMOGRAPHIC')[0])
glue("demo_pct", round(barrier_extent('ROAD, DEMOGRAPHIC')[1]))
glue("resource_sev", round(barrier_severity('ROAD, RESOURCE/OTHER')[2]))
glue("demo_sev", round(barrier_severity('ROAD, DEMOGRAPHIC')[2]))

sum_road = (barrier_severity('ROAD, RESOURCE/OTHER')[1], barrier_severity('ROAD, DEMOGRAPHIC')[1])


glue("sum", sum(sum_road))


# ### Road-stream Crossings
# 
# Road-stream crossings are the most abundant barrier type in the watershed, with over {glue:text}`sum` assessed and modelled crossings located on “potentially accessible” stream segments. Demographic road crossings (highways, municipal, and paved roads) block {glue:text}`demo_km` km of habitat (~{glue:text}`demo_pct`% of the total blocked habitat), with {glue:text}`demo_sev`% of assessed crossings having been identified as barriers to fish passage. Resource roads block {glue:text}`resource_km` km of habitat (~{glue:text}`resource_pct`%), with {glue:text}`resource_sev`% of assessed crossings having been identified as barriers. Significant land use and linear development throughout the valley bottom has disconnected the Bulkley River from important habitat in many tributaries, including Highway 16 which represents one of the main drivers of fragmentation in the watershed (see Appendix C - Barrier Prioritization results). The collective experience and input from the planning team resulted in a Medium irreversibility rating due to the technical complexity and resources required to remediate road-stream crossings, though it was noted that this differs considerably between resource roads and highway crossings. 

# ### Trail-stream crossings 
# 
# There is very little spatial data available on trail-stream crossings in the watershed, so the planning team was unable to quantify the true Extent and Severity of this barrier type. However, the planning team felt that trail-stream crossings are not prevalent within the watershed and that where they do exist, they rarely significantly block passage for anadromous salmonids. Given that most crossings will likely be fords or similar structures, the remediation costs associated with these barriers would be quite low. Overall, the planning team felt that the pressure rating for trail-stream crossings was likely Low.

# ### Lateral Barriers 
# 
# There are numerous types of lateral barriers that potentially occur in the watershed, including dykes, berms, and linear development (i.e., road and rail lines), all of which can restrict the ability of anadromous salmonids to move into floodplains, riparian wetlands, and other off-channel habitats. No comprehensive lateral barrier data exists within the watershed, so pressure ratings were based on qualitative local knowledge. Lateral barriers are not thought to be as prevalent as road- or rail-stream crossings but are likely very severe where they do exist. Highway 16 and the CN rail line that run along a significant stretch of the Bulkley River were identified as major lateral barriers that disconnect the mainstem river from its historic floodplain and off-channel habitat. Overall, the planning team decided that a Medium pressure rating adequately captured the effect that lateral barriers are having on connectivity in the watershed, while recognizing that the lack of data on lateral barriers in the watershed is an important knowledge gap to fill. 

# ### Natural Barriers 
# 
# Natural barriers to fish passage can include debris flows, log jams, sediment deposits, etc., but natural features that have always restricted fish passage (e.g., waterfalls) are not considered under this barrier type. Natural barriers are difficult to include in a spatial prioritization framework due to their transient nature. The planning team identified known natural barriers that occur throughout the watershed, such as beaver dams and log jams. Generally, these natural barriers are only severe impediments to fish passage during low-flow years, but reduced baseflows have become more common in recent years. Based on this, the planning team felt that natural barriers will be severe most years where they exist, but are mostly reversible, resulting in an overall pressure rating of Low. 

# # Situation Analysis 
# 
# The following situation model was developed by the WCRP partnership to “map” the project context and brainstorm potential actions for implementation. Green text is used to identify actions that were selected for implementation (see 'Strategies & Actions'), and red text is used to identify actions that the project team has decided to exclude from the current iteration of the plan, given that they were either outside of the project scope or were deemed to be ineffective by the planning team.
# 
# ```{figure} figure3.png
# ---
# height: 400px
# width: 1000px
# name: directive-fig
# ---
# *Situation analysis developed by the planning team to identify factors that contribute to fragmentation (orange boxes), biophysical results (brown boxes), and potential strategies/actions to improve connectivity (yellow hexagons) for target species in the Bulkley River watershed.*
# ```

# # Goals
# 

# In[7]:


#creating table 7
import warnings

warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np

df = pd.DataFrame({"Goal #": [1,2],
                   "Goal": ["By 2031, the percent (%) of total linear spawning habitat accessible to anadromous salmonids will increase from 88% to 95% within the Bulkley River watershed (i.e., reconnect at least 86 km of spawning habitat).",
                            "By 2031, the percent (%) of total linear rearing habitat accessible to anadromous salmonids will increase from 70% to 80% within the Bulkley River watershed (i.e., reconnect at least 211 km of rearing habitat)."]
                    })

data = df.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table9", data)


# ```{glue:figure} Table9
# :name: "table9"
# 
# *Goals to improve spawning (1) and rearing (2) habitat connectivity for target species in the Bulkley River watershed over the lifespan of the WCRP (2021-2031). The goals were established through discussions with the planning team and represent the resulting desired state of connectivity in the watershed. The goals are subject to change as more information and data are collected over the course of the plan timeline (e.g., the current connectivity status is updated based on barrier field assessments).*
# ```

# # Strategies & Actions
# 
# Effectiveness evaluation of identified conservation strategies and associated actions to improve connectivity for target species in the Bulkley River watershed. The planning team identified four broad strategies to implement through this WCRP, 1) barrier remediation, 2) barrier prevention, 3) strengthen Indigenous connections to land and water, and 4) planning and progress tracking. Individual actions were qualitatively evaluated based on the anticipated effect each action will have on realizing on-the-ground gains in connectivity. Effectiveness ratings are based on a combination of "Feasibility and "Impact", Feasibility is defined as the degree to which the project team can implement the action within realistic constraints (financial, time, ethical, etc.) and Impact is the degree to which the action is likely to contribute to achieving one or more of the goals established in this plan.
# 
# ## Strategy 1: Barrier Remediation
# 

# In[8]:


import numpy as np
from IPython.display import display
import pandas as pd

data = pd.read_csv('Strategy1.csv', index_col=False, skip_blank_lines=False )
 
def fix_table(val):
    return str(val)

def highlighttab7(val):
    red = '#ff0000;'
    yellow = '#ffff00;'
    lgreen = '#92d050;'
    dgreen = '#03853e;'


    if val=="Medium" or val=="Need more information": color = yellow
    elif val=="Very high" or val=="Very effective" or val=="Very High" or val=="Very Effective": color = lgreen
    elif val =="High" or val=="Effective": color = dgreen 
    else: color = 'white'
    return 'background-color: %s' % color

#data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)


data = data.style.applymap(highlighttab7).hide_index().set_properties(**{'text-align': 'left'})
data = data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

display(data)


# 
# ## Strategy 2: Barrier Prevention
# 

# In[9]:


data = pd.read_csv('Strategy2.csv', escapechar='\n', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data = data.style.applymap(highlighttab7).hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])


# ## Strategy 3: Strengthen Indigenous Connections to Land and Water
# 

# In[10]:


data = pd.read_csv('Strategy3.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data = data.style.applymap(highlighttab7).hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])


# ## Strategy 4: Planning and Progress Tracking
# 

# In[11]:


import pandas as pd

data = pd.read_csv('Strategy4.csv', index_col=False)




data = data.applymap(fix_table)

data = data.style.applymap(highlighttab7).hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])


# # Theories of Change & Objectives
# 
# Theories of Change are explicit assumptions around how the identified actions will achieve gains in connectivity and contribute towards reaching the goals of the plan. To develop Theories of Change, the planning team developed explicit assumptions for each strategy which helped to clarify the rationale used for undertaking actions and provided an opportunity for feedback on invalid assumptions or missing opportunities. The Theories of Change are results oriented and clearly define the expected outcome. The following theory of change models were developed by the WCRP planning team to “map” the causal (“if-then”) progression of assumptions of how the actions within a strategy work together to achieve project goals.  
# ```{figure} figure4.png
# ---
# height: 400px
# width: 1000px
# name: fig4
# ---
# *Theory of change developed by the planning team for the actions identified under Strategy 1: Barrier Remediation in the Bulkley River watershed.*
# ```
# ```{figure} figure5.png
# ---
# height: 400px
# width: 1000px
# name: fig5
# ---
# *Theory of change developed by the planning team for the actions identified under Strategy 2: Barrier Prevention in the Bulkley River watershed.*
# ```
# 

# # Operational Plan
# 
# The operational plan represents a preliminary exercise undertaken by the planning team to identify the potential leads, potential participants, and estimated cost for the implementation of each action in the Horsefly River watershed. The table below summarizes individuals, groups, or organizations that the planning team felt could lead or participate in the implementation of the plan and should be interpreted as the first step in on-going planning and engagement to develop more detailed and sophisticated action plans for each entry in the table. The individuals, groups, and organizations listed under the "Lead(s)" or "Potential Participants" columns are those that provisionally expressed interest in participating in one of those roles or were suggested by the planning team for further engagement (denoted in bold), for those that are not members of the planning team. The leads, participants, and estimated costs in the operational plan are not binding nor an official commitment of resources, but rather provide a roadmap for future coordination and engagement to work towards implementation of the WCRP. 
# 
# 

# In[12]:


from IPython.display import display
import pandas as pd
import numpy as np

def df_operation(val):
    return "background-color: black; color: white"


data = pd.read_csv('Table13.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

rows = pd.IndexSlice[[0,10,13,18,22,23,24], :]

data = data.style.applymap(df_operation, subset=rows).hide_index().set_properties(**{'text-align': 'left'})
data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table11", data)


# ```{glue:figure} Table11
# :name: "table11"
# 
# *Operational plan to support the implementation of strategies and actions to improve connectivity for target species in the Bulkley River watershed.*
# ```

# # Funding Sources

# In[13]:


from IPython.display import display
import pandas as pd

data = pd.read_csv('Table14.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table12", data)


# ```{glue:figure} Table12
# :name: "table12"
# 
# *Potential funding sources for plan implementation in the Bulkley River watershed. The Canadian Wildlife Federation and the planning team can coordinate proposal submission through these sources.*
# ```
