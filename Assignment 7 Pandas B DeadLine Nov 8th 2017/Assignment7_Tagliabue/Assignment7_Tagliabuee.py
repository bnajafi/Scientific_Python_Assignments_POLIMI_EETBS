#Assignment 7 Tagliabue Camilla 
import os 
import numpy as np
import pandas as pd
os.chdir("/Users/camillatagliabue/Desktop/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 8 Pandas C Deadline Nov 28th 2017/Assignment7_Tagliabue")
beam_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffuse_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
latitude_location= 45
direction="E"
PXI_without_external_shading=beam_DF.loc[direction,str(latitude_location)]+diffuse_DF.loc[direction,str(latitude_location)]
windows_DF["PXI"]=np.array([PXI_without_external_shading,0,0,0])
windows_DF.to_csv("windows_completedwithPXI.csv",sep=";")