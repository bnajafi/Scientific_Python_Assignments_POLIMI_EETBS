import os
import pandas as pd
import numpy as np
import scipy as sp
os.chdir("C:/Users/marco/Desktop/MARCO/POLIMI/BUILDING/DATA")
DF_Ed=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DF_ED=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

def PXI_finder(latitude,direction):
    DF_Ed=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    DF_ED=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    result_Ed=DF_Ed[latitude][direction]
    result_ED=DF_ED[latitude][direction]
    PXI=result_ED+result_Ed
    return PXI

i=0
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
PXI_values=[]
for index in windows_DF.index.tolist():
    print index
    PXI_values=np.append(PXI_values,PXI_finder("45",windows_DF["Direction"][index]))
    print "PXI is "+ str(PXI_values[i])
    i=i+1

windows_DF["PXI"]=PXI_values
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")


Latitude=42

name_of_columns=DF_Ed.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
# for thedirection of South
result_Ed=sp.interp(Latitude,name_of_columns_as_numbers,DF_Ed.loc["S"]) 
name_of_columns=DF_ED.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
result_ED=sp.interp(Latitude,name_of_columns_as_numbers,DF_ED.loc["S"]) 
PXI42=result_ED+result_Ed
print "PXI latitude=42 is "+str(PXI42)