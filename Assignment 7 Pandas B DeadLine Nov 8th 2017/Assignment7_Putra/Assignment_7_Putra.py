import os


# to see the file in particular folder
os.chdir("/Users/hendrasuryanaputra/Dropbox/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 7 Pandas B DeadLine Nov 8th 2017/Assignment7_Putra")

import numpy as np

import pandas as pd

#call the data on csv format inside the folder above



# Read the Value of Beam Irradiance in Latitude 45 on east direction

latitude_location = "45"


beamIrradiance_DF = pd.read_csv("beamIrradiance.csv",sep=";",index_col=0)

print beamIrradiance_DF.columns

print beamIrradiance_DF.index

beamIrradiance_DF[latitude_location]["E"]


# Read the Value of Diffuse Irradiance in Latitude 45 on east direction


diffuseIrradiance_DF = pd.read_csv("diffuseIrradiance.csv",sep=";",index_col=0)

print diffuseIrradiance_DF.columns

print diffuseIrradiance_DF.index

diffuseIrradiance_DF[latitude_location]["E"]

# Calculate the PXI

PXI_value = beamIrradiance_DF[latitude_location]["E"] + diffuseIrradiance_DF[latitude_location]["E"]


# Read database of window


windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0) #tell pandas that separator is semicolumn & tell pandas that column 0 is index

# let's see what the column are

print windows_DF.columns #to read what is the name of each column

print windows_DF.index #to read what is the name of index

# Update the value of PXI

windows_DF["PXI"] = np.array([PXI_value,0,0,0])

# Write PXI values for east windows in new file

windows_DF.to_csv("windows_completed_withPXI.csv",sep=";") 

