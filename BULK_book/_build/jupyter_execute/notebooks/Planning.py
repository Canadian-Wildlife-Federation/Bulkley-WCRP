#!/usr/bin/env python
# coding: utf-8

# ```{include} ../content/planning-md.md
# :end-before: "# Planning Team"
# ```

# # Planning Team

# In[1]:


import pandas as pd
import warnings
from myst_nb import glue
#from IPython.display import display, HTML

warnings.filterwarnings('ignore')


data = pd.read_csv('../tables/planning_team.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table1", data)


#newerror


# ```{glue:figure} Table1
# :name: "table1"
# 
# *Bulkley River watershed WCRP planning team members. Planning team members contributed to the development of this plan by participating in a series of workshops and document and data review. The plan was generated based on the input and feedback of the local groups and organizations list in this table.*
# ```

# # Key Actors
# 
# 

# In[2]:


import pandas as pd
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('../tables/key_actors.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table2", data)


# ```{glue:figure} Table2
# :name: "table2"
# 
# *Additional Key Actors in the Bulkley River watershed. Key Actors are the individuals, groups, and/or organizations, outside of the planning team, with influence and relevant experience in the watershed, whose engagement will be critical for the successful implementation of this WCRP.* 
# ```

# ```{include} ../content/planning-md.md
# :start-after: "# Project Scope"
# :end-before: "The primary geographic scope of this WCRP"
# ```

# ```{figure} ../figures/figure1.png
# ---
# height: 400px
# width: 1000px
# name: fig1
# ---
# *The primary geographic scope — the Bulkley River watershed, excluding the Morice River drainage.*
# ```

# ```{include} ../content/planning-md.md
# :start-after: "(i.e., road and rail lines) in the watershed."
# :end-before: "The Horsefly River watershed comprises parts of Secwepemcúl’ecw"
# ```

# In[3]:


import pandas as pd
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('../tables/species_names.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table3", data)


# ```{glue:figure} Table3
# :name: "table3"
# 
# *Target fish species in the Bulkley River watershed. The Gitxsanimax, Witsuwit'en, and Western common and scientific species names are provided.*
# ```

# ```{include} ../content/planning-md.md
# :start-after: "sustenance and trading economies  ({numref}`table3`; Irvine 2021)."
# :end-before: "# Target Species"
# ```

# ```{figure} ../figures/figure2.png
# ---
# height: 400px
# width: 1000px
# name: fig2
# ---
# *Potentially accessible stream segments within the Bulkley River watershed. These do not represent useable habitat types, but rather identifies the stream segments within which habitat modelling and barrier mapping and prioritization was undertaken.*
# ```

# ```{include} ../content/planning-md.md
# :start-after: "and action planning {cite}`Mazany-Wright2021-rz`."
# :end-before: "### Chinook Salmon | Ya’aa | Ggïs | Oncorhynchus tshawytscha"
# ```

# ### Chinook Salmon | Ya’aa | Ggïs | Oncorhynchus tshawytscha

# In[4]:


from IPython.display import display, HTML
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('../tables/Chinook1.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])


# 
# ```{glue:figure} Table4
# :name: "table4"
# 
# *Chinook Salmon Conservation Units assessments in the Bulkley River watershed. Assessments undertaken by the [Pacific Salmon Foundation](https://www.salmonexplorer.ca/#!/skeena/chinook)(2020).*
# ```

# ```{include} ../content/planning-md.md
# :start-after: "### Chinook Salmon | Ya’aa | Ggïs | Oncorhynchus tshawytscha"
# :end-before: "### Coho Salmon | Eek | Deedzex | Oncorhynchus kisutch"
# ```

# ### Coho Salmon | Eek | Deedzex | Oncorhynchus kisutch

# In[5]:


import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('../tables/coho1.csv', index_col=False)
data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table5", data)


# 
# 
# ```{glue:figure} Table5
# :name: "table5"
# 
# *Table 5. Coho Salmon Conservation Unit assessment in the Bulkley River Watershed. Assessments undertaken by the  [Pacific Salmon Explorer](https://www.salmonexplorer.ca/#!/skeena/chinook/middle-skeena-mainstem-tributaries&pop=ABUNDANCE_TREND&pop-detail=1)(2020).*
# ```

# ```{include} ../content/planning-md.md
# :start-after: "### Coho Salmon | Eek | Deedzex | Oncorhynchus kisutch"
# :end-before: "### Sockeye Salmon | Mi’soo | Taalook | Oncorhynchus nerka"
# ```

# ### Sockeye Salmon | Mi’soo | Taalook | Oncorhynchus nerka

# In[6]:


import warnings

warnings.filterwarnings('ignore')


data = pd.read_csv('../tables/Sockeye2.csv', index_col=False)
data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table6", data)


# 
# 
# ```{glue:figure} Table6
# :name: "table6"
# 
# *Table 6. Sockeye Salmon Conservation Unit Assessments in the Bulkley River watershed. There were not enough data to support assessments for Sockeye Salmon populations at the time of analysis. Assessments undertaken by the [Pacific salmon Foundation](https://www.salmonexplorer.ca/#!/skeena/sockeye)(2020)*
# ```

# ```{include} ../content/planning-md.md
# :start-after: "### Sockeye Salmon | Mi’soo | Taalook | Oncorhynchus nerka"
# ```
