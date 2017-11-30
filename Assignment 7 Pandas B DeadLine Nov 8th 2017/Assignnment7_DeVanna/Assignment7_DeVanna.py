import os
import pandas as pd
import numpy as np
os.chdir("/Users/Guglielmo/Desktop/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 7 Pandas B DeadLine Nov 8th 2017/__Guidelines__")

latitude_location=45
Beam_Irradiation = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
Diffuse_Irradiation = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
A=Beam_Irradiation["45"]["E"]
B=Diffuse_Irradiation["45"]["E"]
PXI=A+B

windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
windows_DF["PXI"] = np.array([PXI,0,0,0])
windows_DF.to_csv("windows_completed_withPXI",sep=";")