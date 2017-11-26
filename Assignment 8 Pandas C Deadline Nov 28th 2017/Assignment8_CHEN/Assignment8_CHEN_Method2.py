import os 
import numpy as np
import pandas as pd
import scipy as sp

os.chdir("/Users/chenrujing/Dropbox/Iris/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 8 Pandas C Deadline Nov 28th 2017/Assignment8_CHEN/RLF Method")
BeamIrradiance_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0) 
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0) 
DiffuseIrradiance_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0) 


Latitude=45
name_of_columns=BeamIrradiance_DF.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)

def PXI_finder(DirectionoftheWall,Latitude):
    ED=sp.interp(Latitude,name_of_columns_as_numbers,BeamIrradiance_DF.loc[DirectionoftheWall])
    Ed=sp.interp(Latitude,name_of_columns_as_numbers,DiffuseIrradiance_DF.loc[DirectionoftheWall])
    PXI=ED+Ed
    return PXI   

print windows_DF.index.tolist()
PXI_Values=[PXI_finder("E",Latitude),PXI_finder("W",Latitude),PXI_finder("S",Latitude),PXI_finder("S",Latitude)]
print PXI_Values
      
windows_DF["PXI"]=PXI_Values
windows_DF.to_html("windowsPXI.html")