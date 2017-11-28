import os
import pandas as pd
import numpy as np
os.chdir("C:\Users//alice\Desktop\Master PC\Buildings System\EETBS 2017-2018 POLIMI-PIACENZA\Lessons\RLF")

latitude_location = "45"

windows_BI = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
windows_DI = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

print windows_BI.index
print windows_BI.columns
print windows_DI.index
print windows_DI.columns

beam_irr = windows_BI[latitude_location]["E"] #how to extract the value
diffuse_irr = windows_DI[latitude_location]["E"] #column and then index
PXI = (beam_irr+diffuse_irr)

windows = pd.read_csv("windows.csv",sep=";",index_col=0)
print windows.index
print windows.columns

windows["PXI"] = np.array([PXI,0,0,0])