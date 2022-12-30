#!/usr/bin/env python
# coding: utf-8

# # Plan Purpose, Apporach and Scope
# 
# 
# 
# The following Watershed Connectivity Remediation Plan (WCRP) represents the culmination of a one-year collaborative planning effort for the Bulkley River watershed (excluding the Morice River, see Project Scope), the overall aim of which is to clarify and reduce the threat of aquatic barriers to anadromous salmonids and the livelihoods that they support, including the values and laws of First Nations, as well their continued sustenance, cultural, and ceremonial needs both now and into the future. This 10-year plan was developed to identify priority actions that the Bulkley River WCRP planning team (see Planning Team for a list of team members) will undertake between 2021-2031 to conserve and restore fish passage in the watershed through strategies aimed at barrier remediation, barrier prevention, and strengthening Indigenous connections to land and water. 
# 
# WCRPs are long-term, actionable plans that blend local stakeholder and rightsholder knowledge with innovative GIS analyses to gain a shared understanding of where remediation efforts will have the greatest benefit for anadromous salmonids. The planning process is inspired by the [Conservation Standards](https://cmp-openstandards.org/wp-content/uploads/2020/07/CMP-Open-Standards-for-the-Practice-of-Conservation-v4.0.pdf) (v.4.0), which is a conservation planning framework that allows planning teams to systematically identify, implement, and monitor strategies to apply the most effective solutions to high priority conservation problems. There is a rich history of connectivity and fish passage planning and remediation work in the Bulkley River watershed that this WCRP builds upon, including the work undertaken by the BC Fish Passage Technical Working Group, the Skeena Fisheries Commission, the Office of the Wet’suwet’en, the Wet'suwet'en First Nation, and the Society for Ecosystem Restoration in Northern British Columbia (SERNbc), among others (Wilson and Rabnett 2007, McCarthy and Fernando 2015, Smith 2018, Casselman and Stanley 2010, Irvine 2018). The Canadian Wildlife Federation will continue to engage and coordinate with local partners and existing initiatives, in part through the Skeena Environmental Stewardship Initiative. SERNbc is also currently undertaking [fish passage work](https://www.newgraphenvironment.com/fish_passage_bulkley_2020_reporting/Bulkley.pdf) in the Bulkley River watershed, with some overlap and some differences in scope compared to the work and processes described in this WCRP. The SERNbc project relies on expert knowledge and field assessments in both the Bulkley and Morice watersheds to improve passage for all fish, including fluvial and resident species, and focuses on stream crossings that act as barriers (Irvine 2021). This WCRP focuses specifically on improving connectivity for anadromous salmonid species and uses consensus-based planning exercises and spatial model implementation to develop watershed-scale status assessments, goal setting, and prioritization for multiple barrier types. SERNbc and the WCRP planning team are currently collaborating on the development of the [bcfishpass](https://github.com/smnorris/bcfishpass) connectivity model and will continue to work together to promote coordination and collaboration between the two initiatives moving forward.
# 
# The planning team compiled existing barrier location and assessment data, habitat data, and previously identified priorities, and combined this with local and Indigenous knowledge to create a strategic watershed-scale plan to improve connectivity. To expand on this work, the Bulkley River WCRP planning team applied the WCRP planning framework to define the "thematic" scope of freshwater connectivity and refine the "geographic" scope to identify those portions of the watershed where barrier prioritization will be conducted, and subsequent remediation efforts will take place. Additionally, the team selected target fish species, assessed their current connectivity status in the watershed, defined concrete goals for gains in connectivity, and developed a priority list of barriers for remediation to achieve those goals. During the 2021 field season, 28 barrier assessments and 21 habitat confirmations were completed. Seventeen barriers were added to the intermediate barrier list based on 2021 field assessments, and an additional 17 crossings were removed from the list, due to being passable, not existing, or having low quality habitat ({numref}`table16`). The preliminary barriers list was further divided this year into an "intermediate barriers" list ({numref}`table16`), which includes barriers that require further assessment, and a "priority barriers" list ({numref}`table17`), which includes barriers that are actively being pursued for design and remediation. While the current version of this plan is based on the best-available information at the time of publishing, WCRPs are intended to be “living plans” that are updated regularly as new information becomes available, or if local priorities and contexts change. As such, this document should be interpreted as a current “snap-shot” in time, and future iterations of this WCRP will build upon the material presented in this plan to continuously improve aquatic barrier remediation for migratory fish in the Bulkley River watershed. For more information on how WCRPs are developed, see {cite}`Mazany-Wright2021-hs`. 
# 
# # Vision Statement 
# 
# *Healthy, well-connected streams and rivers within the Bulkley River watershed support thriving populations of migratory and resident fish. In turn, these fish provide the continued sustenance, cultural, and ceremonial needs of the Wet’suwet’en and Gitxsan peoples, as they have since time immemorial. First Nations, residents, and visitors to the watershed work together for environmental stewardship to clarify, implement, and assess the effectiveness of actions to mitigate the negative effects of aquatic barriers, improving the resiliency of streams and rivers for the benefit and appreciation of all.*

# # Planning Team

# In[1]:


import pandas as pd
import warnings
from myst_nb import glue
#from IPython.display import display, HTML

warnings.filterwarnings('ignore')


data = pd.read_csv('planning_team.csv', index_col=False)

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

data = pd.read_csv('key_actors.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table2", data)


# ```{glue:figure} Table2
# :name: "table2"
# 
# *Additional Key Actors in the Bulkley River watershed. Key Actors are the individuals, groups, and/or organizations, outside of the planning team, with influence and relevant experience in the watershed, whose engagement will be critical for the successful implementation of this WCRP.* 
# ```

# # Project Scope
# 
# Connectivity is a critical component of freshwater ecosystems that encompasses a variety of factors related to ecosystem structure and function, such as the ability of aquatic organisms to disperse and/or migrate, the transportation of energy and matter (e.g., nutrient cycling and sediment flows), and temperature regulation {cite}`Seliger2018-be`. Though each of these factors are important when considering the health of a watershed, for the purposes of this WCRP the term "connectivity" is defined as the degree to which aquatic organisms can disperse and/or migrate freely through freshwater systems. Within this context, connectivity is primarily constrained by physical barriers including anthropogenic infrastructure such as dams, weirs, and stream crossings, and natural features such as waterfalls and debris flows. This plan is intended to focus on the direct remediation and prevention of localized, physical barriers instead of the broad land-use patterns that are causing chronic connectivity issues in the watershed. The planning team decided that the primary focus of this WCRP is addressing barriers to longitudinal connectivity (i.e., along the upstream-downstream plane) due to the magnitude of the threat posed by linear development (i.e., road and rail lines) in the watershed. 
# 
#  

# ```{figure} figure1.png
# ---
# height: 400px
# width: 1000px
# name: fig1
# ---
# *The primary geographic scope — the Bulkley River watershed, excluding the Morice River drainage.*
# ```

# The primary geographic scope of this WCRP is the Bulkley River watershed, located in the mid-eastern portion of the Skeena River drainage basin in northwestern British Columbia ({numref}`fig1`). The scope constitutes the Bulkley River "watershed group" as defined by the [British Columbia Freshwater Atlas](https://catalogue.data.gov.bc.ca/dataset/freshwater-atlas-watershed-groups) (FWA), which excludes the Morice River drainage area due to an effort made to standardize spatial scales of the watershed groups. A consistent spatial framework was necessary to undertake a watershed-selection process at the provincial scale to identify target watersheds to improve connectivity for salmonids. The Bulkley River watershed was identified by the BC Fish Passage Restoration Initiative as one of four target watersheds for WCRP development {cite}`Mazany-Wright2021-do`. The Bulkley River watershed has a drainage area of 776,200 ha, spanning from Bulkley Lake in the southeast to the confluence with the Skeena River in the northwest. The watershed is generally divided into the "lower" Bulkley River and the "upper" Bulkley River by the confluence with the Morice River near the town of Houston. Culturally and economically important populations of Chinook Salmon (Oncorhynchus tshawytscha), Coho Salmon (Oncorhynchus kisutch), Sockeye Salmon (Oncorhynchus nerka), and Steelhead (Oncorhynchus mykiss) are all found in the watershed, which historically supported Indigenous sustenance and trading economies  ({numref}`table3`; Irvine 2021). 

# In[3]:


import pandas as pd
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('species_names.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table3", data)


# ```{glue:figure} Table3
# :name: "table3"
# 
# *Target fish species in the Bulkley River watershed. The Gitxsanimax, Witsuwit'en, and Western common and scientific species names are provided.*
# ```

# The Horsefly River watershed comprises parts of Secwepemcúl’ecw, the traditional territory of the Northern Secwepemc te Qelmucw (NStQ), represented by the Northern Shuswap Tribal Council and four member communities or autonomous nations:
# 
# - **Gitxsan** peoples– the traditional Gitxsan Laxyip spans the northern portion of the watershed, including the Suskwa River, and is governed by a hereditary system of 60 Wilps or House Groups who are represented by Simgigyat (hereditary chiefs). Each Wilp has jurisdiction over several Anaat, or fishing sites. The Wilp groups that have territory coinciding with the Bulkley River watershed include Djogaslee, Gyet’m Galdo’o, Luutkudziiwas, Axtii Tsex, Yagosip, and Spookw (G. Sebastian pers. comm.). The Gitxsan steward the land and waters based on Ayookw (Gitxsan law) and Adaakw (oral histories; Gitxsan 2019, Irvine 2021). It is necessary to receive permission from the individual Wilp chief for any work to occur on their territory.
# 
# - **Wet’suwet’en** peoples– the Wedzin Kwah (Bulkley River watershed) is part of the larger Wet’suwet’en traditional territory. The hereditary territory is governed by a system made up of five clans – Gilseyhu (Big Frog), Laksilyu (Small Frog), Tsayu (Beaver), Gitdumden (Wolf/Bear) and Laksamshu (Fireweed) – each of which comprises multiple Yikhs (House Groups) represented by hereditary chiefs. The Wet’suwet’en steward the land based on Inuk Nu’at’en (Wet'suwet'en law), and the principle of Yintahk, meaning everything is connected to the land (Office of the Wet’suwet’en 2013, Irvine 2021). It is necessary to receive permission from the appropriate bands (Witset First Nation or Wet'suwet'en first Nation, Skin Tyee, Nee Tahi Buhn, or Burns Lake Band), nation representatives (Office of the Wet’suwet’en), and the individual Yikh chiefs for any work to occur on their territory.
# 
# The geographic scope of this WCRP was further refined by identifying “potentially accessible” stream segments, which are defined as streams that target species should be able to access in the absence of anthropogenic barriers ({numref}`fig1`). Potentially accessible stream segments were spatially delineated using fish species observation and distribution data, as well as data on "exclusionary points", which are waterfalls greater than 5 m in height and gradient barriers based on species-specific swimming abilities. These maps were explored by the planning team to incorporate additional local knowledge, ensure accuracy, and finalize the constraints on potentially accessible stream segments. All other stream segments were removed from the scope for further consideration. The "constrained geographic scope" formed the foundation for all subsequent analyses and planning steps, including mapping and modelling useable habitat types, quantifying the current connectivity status, goal setting, and action planning {cite}`Mazany-Wright2021-rz`. 

# ```{figure} figure2.png
# ---
# height: 400px
# width: 1000px
# name: fig2
# ---
# *Potentially accessible stream segments within the Bulkley River watershed. These do not represent useable habitat types, but rather identifies the stream segments within which habitat modelling and barrier mapping and prioritization was undertaken.*
# ```

# # Target species
# Target species represent the ecologically and culturally important species for which habitat connectivity is being conserved and/or restored in the watershed. In the Bulkley River watershed, the planning team selected Anadromous Salmonids as the target species group, which comprises Chinook Salmon, Coho Salmon, Sockeye Salmon, and Steelhead. Anadromous salmonids also include Pink Salmon (Oncorhynchus gorbuscha) and Chum Salmon (Oncorhynchus keta) as beneficiary species (i.e., species that are not actively targeted through the planning process but will also benefit from connectivity improvements for target anadromous species in the watershed). The selection of these target species was driven primarily by the target species of the primary fund supporting this planning work. The planning team also identified other culturally and ecologically important species within the watershed to consider for inclusion in future iterations of the WCRP, including Pacific Lamprey (Entosphenus tridentatus) and Bull Trout (Salvelinus confluentus).
# ### Anadromous Salmonids
# Anadromous salmonids are cultural and ecological keystone species that contribute to productive ecosystems by contributing marine-derived nutrients to the watershed and forming an important food source for grizzly bears and other species (Schindler et al. 2003). Salmon have enduring food, social, and ceremonial value for the Gitxsan and Wet’suwet’en peoples and contribute significant economic value for recreational and commercial fisheries. Salmon have sustained the culture and economies of Indigenous peoples in the watershed since time immemorial – providing the primary food source for communities, supporting wide-ranging trade systems, and helping pass knowledge and ceremony to future generations through fishing and fish processing (SSAF 2021, Office of the Wet’suwet’en 2013, Rescan 2012).
# 
# Anadromous salmonid populations in the Bulkley River watershed have declined significantly in recent decades, leading both the Gitxsan and Wet’suwet’en nations to declare harvest moratoriums or fishing bans in their territories (Office of the Wet’suwet’en 2013, Gitxsan Huwilp Government 2019). The stewardship of these resources in their territories are imbued in the spirit and culture of these nations through a symbiotic relationship with these fish species – threats to the fish are threats to the well-being of the Wet’suwet’en and Gitxsan peoples (SSAF 2021). The stewardship of their waters continues through the work of the [Gitksan Watershed](http://gitksanwatershed.com/) and the [Wet’suwet’en Fisheries Program](http://www.wetsuweten.com/departments/fisheries-and-wildlife/), as well as collaborative initiatives like the Skeena Environment Stewardship Initiative. 
# 
# For the purposes of this WCRP, anadromous salmonid populations are defined using Fisheries and Oceans Canada's Conservation Units. A Conservation Unit (CU) is a group of wild Pacific salmon sufficiently isolated from other groups that, if extirpated, is very unlikely to recolonize naturally within an acceptable timeframe, such as a human lifetime or a specified number of salmon generations. Conservation Units are not defined for Steelhead, as such there is no assessment information to provide for the Bulkley River watershed population. See Appendix A for maps of modelled anadromous salmonid spawning and rearing habitat in the Bulkley River watershed.
# 
# ### Chinook Salmon | Ya’aa | Ggïs | Oncorhynchus tshawytscha
# 
# 

# In[4]:


from IPython.display import display, HTML
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('Chinook1.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])


# 
# ```{glue:figure} Table4
# :name: "table4"
# 
# *Chinook Salmon Conservation Units assessments in the Bulkley River watershed. Assessments undertaken by the [Pacific Salmon Foundation](https://www.salmonexplorer.ca/#!/skeena/chinook)(2020).*
# ```

# The Middle Skeena – Mainstem Tributaries Chinook Salmon spawn in the mainstem Bulkley River (downstream of the confluence with the Morice River) and in key tributaries, including Telkwa River, Goathorn Creek, Howson Creek, Kathlyn Creek, Suskwa River, Harold Price Creek, and Natlan Creek. The Middle Skeena Chinook Salmon stocks have seen a decline in recent years, particularly over the last three generations of spawners [Pacific Salmon Explorer](https://www.salmonexplorer.ca/#!/skeena/chinook/middle-skeena-mainstem-tributaries&pop=ABUNDANCE_TREND&pop-detail=1). 
# 
# The upper Bulkley River Chinook Salmon (upstream of the confluence with the Morice River) are the first salmon to return in the year, usually early-to-mid June, marking the start of the salmon fishery in the watershed (Office of the Wet’suwet’en 2013). The upper Bulkley River population is known to spawn in the mainstem and tributaries of the Bulkley River, including Buck Creek, Byman Creek, Richfield Creek, Maxan Creek, and Foxy Creek. In some years, low water flows prevent adult Chinook Salmon from migrating past Bulkley Falls. The upper Bulkley Chinook Salmon stocks have been observed to be in decline and are threatened, in part, by habitat degradation, including linear development (e.g., highway, rail, and road infrastructure) that fragments tributaries (Office of the Wet’suwet’en 2013, [Pacific Salmon Explorer](https://www.salmonexplorer.ca/#!/skeena/chinook/middle-skeena-mainstem-tributaries&pop=ABUNDANCE_TREND&pop-detail=1)).
# 
# ### Coho Salmon | Eek | Deedzex | Oncorhynchus kisutch

# In[5]:


import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('coho1.csv', index_col=False)
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

# 
# Coho Salmon are the most widely dispersed anadromous salmonid species in the Bulkley River watershed due to their ability to move into smaller tributaries, including headwater streams. Coho Salmon spawning migration peaks in early-to-mid August, though traditionally the main Coho Salmon fishery occurs later in the season (Office of the Wet’suwet’en 2013). Spawning and rearing of the Middle Skeena population is known to occur within the watershed in the mainstem channels of the Bulkley, Telkwa, and Suskwa Rivers, and key tributaries, including Buck Creek, Aitken Creek, McQuarrie Creek, Byman Creek, Richfield Creek, Ailport Creek, and Maxan Creek. In recent decades, Coho Salmon distribution has often been limited to areas downstream of Bulkley Falls, but in years with sufficient flow, tributaries upstream of the falls are well-used by rearing juveniles (M. Risdale pers. comm.). The Coho Salmon population in the watershed appeared to begin recovering around 1998 but has since declined over the last three generations of spawners (Office of the Wet’suwet’en 2013, PSF 2014). Additionally, since 1989, tens of thousands of Coho Salmon fry have been released into the upper Bulkley River mainstem from the Toboggan Hatchery on Toboggan Creek (Office of the Wet’suwet’en 2013).
# 
# ### Sockeye Salmon | Mi’soo | Taalook | Oncorhynchus nerka
# 
# 

# In[6]:


import warnings

warnings.filterwarnings('ignore')


data = pd.read_csv('Sockeye2.csv', index_col=False)
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

# Sockeye Salmon have cultural and commercial importance within the watershed, especially for First Nations communities, in part due to their fat content which is optimal for the smoke-drying process. Limitations on the Sockeye Salmon harvest in the watershed have hindered the ability of the Wet’suwet’en and Gitxsan to practice important cultural activities and the associated sharing of oral traditions and histories (SSAF 2021, Office of the Wet’suwet’en 2013). The Sockeye Salmon runs generally follow the spring Chinook Salmon migrations in the Bulkley River system, but Bulkley Falls and flows in some parts of Maxan Creek can limit migration during low-flow years. Data are insufficient for population assessments; however, it is believed that the Bulkley/Maxan populations are at risk of extirpation. There are two Sockeye Salmon populations present in the watershed with distinct life histories – the lake-type and the river-type (Office of the Wet’suwet’en 2013, PSF 2014). Two lake-type Sockeye Salmon sub-populations spawn and rear in and around Bulkley Lake and Maxan Lake, and a third lake-type sub-population was extirpated from Toboggan Lake. River-type Sockeye distribution and habitat use within the Bulkley River watershed is not well documented; however, there are records of Sockeye Salmon river spawners in the mainstem Bulkley River around Richfield Creek, McQuarrie Creek, the Morice River confluence, and the Suskwa River mainstem near Natlan Creek.
# 
# ### Steelhead | Milit | Tësdlï | Oncorhynchus mykiss
# 
# Steelhead migrations coincide with the arrival of Coho Salmon in the watershed and are an important traditional food source to augment winter stores (Office of the Wet’suwet’en 2013). Steelhead are known to spawn and rear in the mainstem Bulkley River and important tributaries, including the Telkwa River, Hubert Creek, Buck Creek, McQuarrie Creek, Byman Creek, Richfield Creek, Ailport Creek, Johnny David Creek, and Robert Hatch Creek. In the lower part of the watershed, Steelhead are known to spawn and rear throughout the Suskwa River system, all the way up through Harold Price Creek and Blunt Creek. Local knowledge indicates that Steelhead populations have been declining in recent decades and are currently in poor condition throughout the entire watershed. In response, some stocking enhancement actions have been undertaken in an attempt to increase the population in the watershed (Office of the Wet’suwet’en 2013, Chudyk 1979).
