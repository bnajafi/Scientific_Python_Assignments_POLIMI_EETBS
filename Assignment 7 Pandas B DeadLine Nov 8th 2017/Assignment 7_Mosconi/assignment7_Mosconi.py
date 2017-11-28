import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\Manuel\Documents\Polimi\Building systems\Assignments\Assignment 7\__Guidelines__")

latitudeLocation=45

beamIrradiance_DF= pd.read_csv("beamIrradiance.csv",sep=";",index_col=0)
diffuseIrradiance_DF= pd.read_csv("diffuseIrradiance.csv",sep=";",index_col=0)

beamIrradiance=beamIrradiance_DF.loc["E",str(latitudeLocation)]
diffuseIrradiance=diffuseIrradiance_DF.loc["E",str(latitudeLocation)]

Tx=1
PXI=(beamIrradiance+diffuseIrradiance)*Tx


windows_DF= pd.read_csv("windows.csv",sep=";",index_col=0)
PXIwindows=[PXI,0,0,0]

windows_DF["PXI"] = np.array(PXIwindows)

windows_DF.to_csv("windows_completedWithPXI.csv",sep=";")