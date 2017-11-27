import os
os.chdir("G:/Sem 1/ENERGY AND ENVIRONMENTAL TECHNOLOGIES FOR BUILDING SYSTEMS/Canopy Files")
import numpy as np
import pandas as pd

windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
Beam_DF = pd.read_csv ("BeamIrradiance.csv", sep = ";", index_col = 0)
Diffuse_DF = pd.read_csv ("DiffuseIrradiance.csv", sep = ";", index_col = 0)

latitude_location = 45
Direction = "E"

PXI_PC = Beam_DF.loc[Direction,str(latitude_location)]+Diffuse_DF.loc[Direction,str(latitude_location)]
windows_DF["PXI"] = np.array([PXI_PC,0,0,0])
windows_DF.to_csv("windows_completed_PXI.csv", sep =";")



