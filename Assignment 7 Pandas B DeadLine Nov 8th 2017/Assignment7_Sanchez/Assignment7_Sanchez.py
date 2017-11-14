import os
import pandas as pd
import numpy as np
os.chdir("/Users/tomassanchez/Desktop/files to send/Assignment7_Sanchez")

latitude_location='45'
direction='E'
beamIrr_DF = pd.read_csv('BeamIrradiance.csv',sep=";",index_col=0)
diffuseIrr_DF= pd.read_csv('DiffuseIrradiance.csv',sep=";",index_col=0)
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)

windows_DF.loc["east","PXI"]=beamIrr_DF.loc[direction,latitude_location]+diffuseIrr_DF.loc[direction,latitude_location]

windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
