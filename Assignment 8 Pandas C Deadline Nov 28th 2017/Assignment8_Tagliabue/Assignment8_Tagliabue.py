import os
import numpy as np
import pandas as pd
import scipy as sp
os.chdir("/Users/camillatagliabue/Desktop/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 8 Pandas C Deadline Nov 28th 2017/Assignment8_Tagliabue")
windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)
#beam irradiation, diffuse irradiation and PXI
def BeamDiffusePXI (lat, direction):
    BeamI=pd.read_csv("BeamIrradiance.csv",sep=";",index_col= 0)
    DiffuseI=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col= 0)
    PXI_without_external_shading=BeamI.loc[direction,str(lat)]+DiffuseI.loc[direction,str(lat)]
    return PXI_without_external_shading
#EXAMPLE ONE 
latitude=45
i=0  
PXIvalues=[0,0,0,0]
for anywindow in windows_DataFrame.index.tolist():
    print (anywindow)
    PXIvalues[i]=BeamDiffusePXI(latitude,windows_DataFrame["Direction"][anywindow])
    windows_DataFrame["PXI"][anywindow]=PXIvalues[i]
    i=i+1
print (PXIvalues)
windows_DataFrame["PXI"]
windows_DataFrame.to_csv("windows_completedwithPXI.csv",sep=";")
windows_completed_DataFrame = pd.read_csv("windows_completedwithPXI.csv",sep=";",index_col= 0)

#INTERPOLATION PROCEDURE
#name_of_columnsB=BeamI.columns.get_values()
#name_of_columns_as_numbersB = name_of_columnsB.astype(np.int32, copy=False)
#ED=sp.interp(latitude,name_of_columns_as_numbers,BeamI.loc["Direction"])
#name_of_columnsD=BeamI.columns.get_values()
#name_of_columns_as_numbersD = name_of_columnsD.astype(np.int32, copy=False)
#ED=sp.interp(latitude,name_of_columns_as_numbersB,DiffuI.loc["Direction"])


