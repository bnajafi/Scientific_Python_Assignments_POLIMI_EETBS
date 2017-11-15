import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\Utente\Desktop\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\Assignment7_Martinelli")

latitude_location = "45"

windows_BI = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
windows_DI = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

print windows_BI.index
print windows_BI.columns
print windows_DI.index
print windows_DI.columns

beam_irr = windows_BI[latitude_location]["E"]
diffuse_irr = windows_DI[latitude_location]["E"]

PXI = beam_irr + diffuse_irr

windows = pd.read_csv("windows.csv",sep=";",index_col=0)

print windows.index
print windows.columns

windows["PXI"] = np.array([PXI,0,0,0])

windows.to_csv("windows_completed_withPXI.csv",sep=";")
