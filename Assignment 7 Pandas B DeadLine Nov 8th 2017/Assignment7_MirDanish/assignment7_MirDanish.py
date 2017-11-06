import os
import pandas as pd
import numpy as np

os.chdir("C:\Users\Danish\Documents\ourNewclone\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")

BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)

DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv", sep=";",index_col=0)

windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)

# Introducing the Latitude for Piacenza = 45 deg East
latitude_location,direction = 45,"E"

# PXI value for latitude 45 deg East
PXI_NoExternal_shading = BeamIrradiance_DF["45"]["E"]+DiffuseIrradiance_DF["45"]["E"]

# Updating the value of PXI for east window
windows_DF["PXI"] = np.array([PXI_NoExternal_shading,0,0,0])

# Saving the csv file
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")