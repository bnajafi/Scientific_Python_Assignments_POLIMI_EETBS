import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\jude\Desktop\judes script code\WEEK 7")

BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv", sep=";",index_col=0)
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)

# Defining Latitude location of 45 deg East
latitude_location,direction=45,"E"

# PXI value for latitude 45 deg East
PXI_NoExternal_shading=BeamIrradiance_DF["45"]["E"]+DiffuseIrradiance_DF["45"]["E"]

windows_DF["PXI"]=np.array([PXI_NoExternal_shading,0,0,0]) #updating the PXI value for East window
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";") #saving the csv file