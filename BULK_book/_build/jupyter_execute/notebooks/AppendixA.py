#!/usr/bin/env python
# coding: utf-8

# # Appendix A

# ```{include} ../content/appendixa-md.md
# :start-after: "# Appendix A"
# :end-before: "##  Connectivity Status Assessment Methods"
# ```

# ```{figure} ../figures/figure8.png
# ---
# height: 400px
# width: 1000px
# name: fig8
# ---
# *Bulkley River watershed overview map identifying the portions of the watershed covered by each map sheet (grey squares) and the prioritized barriers on the intermediate barrier list (orange points; see Appendix B).*
# ```

# ##  Connectivity Status Assessment Methods

# ```{include} ../content/appendixa-md.md
# :start-after: "##  Connectivity Status Assessment Methods"
# ```

# In[1]:


from IPython.display import display, HTML
import pandas as pd
import numpy as np
import warnings
from myst_nb import glue

warnings.filterwarnings('ignore')

data = pd.read_csv('../tables/Table15.csv', index_col=False)

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
