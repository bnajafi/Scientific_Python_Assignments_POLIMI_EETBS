import os 
import numpy as np
import pandas as pd
import scipy as sp

os.chdir("/Users/chenrujing/Dropbox/Iris/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 8 Pandas C Deadline Nov 28th 2017/Assignment8_CHEN/RLF Method")
BeamIrradiance_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0) 
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0) 
DiffuseIrradiance_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0) 
    
def PXI_finder(DirectionoftheWall,Latitude):
    ED=BeamIrradiance_DF.loc[DirectionoftheWall][Latitude]
    Ed=DiffuseIrradiance_DF.loc[DirectionoftheWall][Latitude]
    PXI=ED+Ed
    return PXI   

print windows_DF.index.tolist()    
DirectionoftheWall=["E","W","S","S"]
Latitude="45" 
PXI_Values=PXI_finder(DirectionoftheWall,Latitude).tolist()

windows_DF["PXI"]=PXI_Values
windows_DF.to_html("windowsPXI.html")   



