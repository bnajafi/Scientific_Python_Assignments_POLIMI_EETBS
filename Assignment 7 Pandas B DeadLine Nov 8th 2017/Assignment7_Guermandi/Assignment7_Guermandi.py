import os
os.chdir("/Users/Fede/Documents/Polimi/EETBS/Numpy - Pandas/RLF Method")
import pandas as pd
import numpy as np

latitude=45
beamirrad = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffirrad = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
A=beamirrad["45"]["E"]
B=diffirrad["45"]["E"]
PXI=A+B #since there is no shade
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
windows_DF["PXI"] = np.array([PXI,0,0,0])
windows_DF.to_csv("windowswithPXI.csv",sep=";")