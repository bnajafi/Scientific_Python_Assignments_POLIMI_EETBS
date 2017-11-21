#--------------------------Hendra Suryana Putra -----------------#
#---------------------------Assignment 7 -------------------------#


import os

# to see the file in particular folder
os.chdir("/Users/hendrasuryanaputra/Dropbox/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 7 Pandas B DeadLine Nov 8th 2017/Assignment7_Putra")

import numpy as np

import pandas as pd


# Read the Value of Beam Irradiance in Latitude 45 on east direction

latitude_location = "45"

beamIrradiance_DF = pd.read_csv("beamIrradiance.csv",sep=";",index_col=0)

beamIrradiance_DF[latitude_location]["E"]


# Read the Value of Diffuse Irradiance in Latitude 45 on east direction

diffuseIrradiance_DF = pd.read_csv("diffuseIrradiance.csv",sep=";",index_col=0)

diffuseIrradiance_DF[latitude_location]["E"]

# Calculate the PXI

PXI_value = beamIrradiance_DF[latitude_location]["E"] + diffuseIrradiance_DF[latitude_location]["E"]

# Read database of window

windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0) #tell pandas that separator is semicolumn & tell pandas that column 0 is index

# Update the value of PXI

windows_DF["PXI"] = np.array([PXI_value,0,0,0])

# Write PXI values for east windows in new file

windows_DF.to_csv("windows_completed_withPXI.csv",sep=";") 
