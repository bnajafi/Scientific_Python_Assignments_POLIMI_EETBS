import os
import numpy as np
import pandas as pd

os.chdir ("C:\Users\Marica\Desktop\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")

#we have to find the beam irradiation, the diffuse irradiation, and the PXI for the city of Piacenza
#we have to read the values corresponding to the following latitute and orientation
latitude_location = "45"
orientation = "E"

#reading the files
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

#PXI calculation
PXI_east = BeamIrradiance_DF[latitude_location][orientation] + DiffuseIrradiance_DF[latitude_location][orientation]

#I update the computed value in the corresponding position in the windows data file
#and create a new file with the modified table
windows_DF["PXI"] = np.array([PXI_east,0,0,0])

windows_DF.to_csv("windows_completedWithPIX.csv",sep=";")
windows_DF.to_html("windows_completedWithPIX.html")