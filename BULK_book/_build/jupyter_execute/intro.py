#!/usr/bin/env python
# coding: utf-8

# In[1]:


from docx import Document
from myst_nb import glue
from IPython.display import display, Markdown, display_markdown
from functions import head2txt

document = Document('MASTER_Horsefly_WCRP.docx')


par1 = head2txt(document,'Acknowledgements', 3)[0]
par2 = head2txt(document,'Acknowledgements', 3)[1]
par3 = head2txt(document,'Acknowledgements', 3)[2]


# # Bulkley River Watershed (Laxyip | Wedzin Kwah) Connectivity Remediation Plan: 2021 - 2031
# 
# 
# ![foto](spawn.jpg.jpg)
# 
# 
# **Canadian Wildlife Federation**
# 
# **350 Michael Cowpland Drive** 
# 
# **Kanata, Ontario K2M 2W1** 
# 
# **Telephone: 1-877-599-5777 | 613-599-9594** 
# 
# **www.cwf-fcf.org** 
# 
# **© 2022**
# 
# Suggested Citation: 
# 
# Mazany-Wright, N., S. M. Norris, J. Noseworthy, B. Rebellato, S. Sra, and N. W. R. Lapointe. 2022. Bulkley River Watershed Connectivity Remediation Plan: 2021- 2031. Canadian Wildlife Federation. Ottawa, Ontario, Canada.  
# 
# [Download full PDF here!](https://github.com/Canadian-Wildlife-Federation/Horsefly-WCRP/raw/master/Tutorials/Jupyter_Book/mynewbook/_build/pdf/book.pdf)
# 
#  
# 
# 
# # Acknowledgements
# 
# This plan represents the culmination of a collaborative planning process undertaken in the Bulkley River watershed over many months of work with a multi-partner planning team of individuals and groups passionate about the conservation and restoration of freshwater ecosystems and the species they support. Plan development was funded by the BC Salmon Restoration and Innovation Fund and the RBC Bluewater Project. We were fortunate to benefit from the feedback, guidance, and wisdom of many groups and individuals who volunteered their time throughout this process — this publication would not have been possible without the engagement of our partners and the planning team (see {numref}`table1`). 
# 
# We recognize the incredible fish passage and connectivity work that has occurred in the Bulkley River watershed to date, and we are excited to continue partnering with local groups and organizations to build up existing initiatives and provide a road map to push connectivity remediation forward over the next 10 years and beyond.
# 
# The Canadian Wildlife Federation recognizes that the lands and waters that form the basis of this plan are the traditional unceded territory of the Wet'suwet'en and Gitxsan peoples. We are grateful for the opportunity to learn from the stewards of this land and work together to benefit Pacific Salmon and Steelhead. A special thank you to Dallas Nikal, Mike Ridsdale, and Elaine Sampson for sharing the traditional Witsuwit'en and Gitxsanimax names used in this plan.
# 
# 
