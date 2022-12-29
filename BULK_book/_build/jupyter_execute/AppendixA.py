#!/usr/bin/env python
# coding: utf-8

# # Appendix A

# ## Modelled Anadromous Salmon Habitat Maps
# 
# High-resolution PDF maps of the Bulkley River watershed and model results can be accessed [here](https://github.com/smnorris/bcfishpass/tree/main/wcrp/pdfs). The watershed is divided into multiple maps sheets to allow for detailed examination of modelled spawning and rearing habitat and priority barriers identified through this planning process. The locations of WCRP priority barriers and associated map sheet numbers are shown below. In each individual map sheet, priority barriers are symbolized using the following notation:

# ```{figure} figure8.png
# ---
# height: 400px
# width: 1000px
# name: fig8
# ---
# *Bulkley River watershed overview map identifying the portions of the watershed covered by each map sheet (grey squares) and the prioritized barriers on the intermediate barrier list (orange points; see Appendix B).*
# ```

# ##  Connectivity Status Assessment Methods
# 
# The connectivity status assessment for anadromous salmonids in the Bulkley River watershed builds on existing connectivity modelling work undertaken by the BC Fish Passage Technical Working Group, resulting in a flexible, customizable open-source spatial model called "bcfishpass". The model spatially locates known and modelled barriers to fish passage, identifies potential spawning and rearing habitat for target species, and estimates the amount of habitat that is currently accessible to target species. The model uses an adapted version of the Intrinsic Potential (IP) fish habitat modelling framework (see Sheer et al. 2009 for an overview of the IP framework). The habitat model uses two geomorphic characteristics of the stream network — channel gradient and mean annual discharge — to identify potential spawning habitat and rearing habitat for each target species. The habitat model does not attempt to definitively map each habitat type nor estimate habitat quality, but rather identifies stream segments that have high potential to support spawning or rearing habitat for each species based on the geomorphic characteristics of the segment. For more details on the connectivity and habitat model structure and parameters, please see Mazany-Wright et al. 2021a. The variables and thresholds used to model potential spawning and rearing habitat for each target species are summarized in Table 13. The quantity of modelled habitat for each species was aggregated for each habitat type to inform the two KEAs — Accessible Spawning Habitat and Accessible Rearing Habitat — and represents a linear measure of potential habitat. To recognize the rearing value provided by features represented by polygons for certain species (e.g., wetlands for Coho Salmon and lakes for Sockeye Salmon) a multiplier of 1.5x the length of the stream segments flowing through the polygons was applied.

# In[1]:


from IPython.display import display, HTML
import pandas as pd
import numpy as np
import warnings
from myst_nb import glue

warnings.filterwarnings('ignore')

data = pd.read_csv('Table15.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)


data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table15", data)


# ```{glue:figure} Table15
# :name: "table15"
# 
# *Parameters and thresholds used to inform the Intrinsic Potential habitat model for spawning and rearing habitat for each target species in the Bulkley River watershed.*
# ```
