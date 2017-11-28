#ASSIGNMENT 7

import os
import numpy as np
import pandas as pd

os.chdir("/Users/Fede/Desktop/RLF Method")

Beamirradiance_DF=pd.read_csv("Beamirradiance.csv",sep=";",index_col=0)
Diffuseirradiance_DF=pd.read_csv("Diffuseirradiance.csv",sep=";",index_col=0)

Beamirradiance_DF.loc["E","45"]
Diffuseirradiance_DF.loc["E","45"]

PXI=Beamirradiance_DF.loc["E","45"]+Diffuseirradiance_DF.loc["E","45"]

windowsDF=pd.read_csv("windows.csv",sep = ";",index_col=1)

PXI_windowsDF_value=windowsDF.loc["E","PXI"]
windowsDF.loc["E","PXI"]=PXI

print windowsDF

windowsDF.to_csv("windows_completedWithPXI.csv",sep=";")