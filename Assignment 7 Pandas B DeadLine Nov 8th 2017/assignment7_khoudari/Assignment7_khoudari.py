import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/BOB/Desktop/assignment7_khoudari")
beam_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffuse_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
latitude_location,direction=45,"E"
PXI_without_external_shading=beam_DF.loc[direction,str(latitude_location)]+diffuse_DF.loc[direction,str(latitude_location)]
windows_DF["PXI"]=np.array([PXI_without_external_shading,0,0,0])
windows_DF.to_csv("windows_completedwithPXI.csv",sep=";")