"""
Created on Mon May 18 20:32:10 2020
@author: DESHMUKH
SURVIVAL ANALYSIS
"""
# pip install lifelines
import pandas as pd
from lifelines import KaplanMeierFitter

# ==========================================================================================
# Business Problem - Perform Kaplan meir analysis for the given data and get the life table.
# ==========================================================================================

patient = pd.read_csv('Patient.csv')
patient.head()
patient.info()

# Summary
patient.describe()

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter(label='FollowUps vs Event')

# Fitting KaplanMeierFitter model on Followups and Event type
kmf.fit(patient.Followup, patient.Eventtype) # fit(time,events)

# Time-line estimations plot 
kmf.plot(color = 'g')

                    # ---------------------------------------------------- #
