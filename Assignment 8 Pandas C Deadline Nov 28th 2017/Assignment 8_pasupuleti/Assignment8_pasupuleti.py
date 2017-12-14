import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/KRISHNA/Desktop/Assignment 8_pasupuleti")
import scipy as sp

beamIrradiance_DF=pd.read_csv("beamIrradiance.csv",sep=';',index_col=0)
diffuseIrradiance_DF=pd.read_csv("diffuseIrradiance.csv",sep=';',index_col=0)
    
def PXI_finder(latitude,directionWall):
    "This function finds the PXI values receiving latitude and direction of the wall"
    beamIrradiance_DF=pd.read_csv("beamIrradiance.csv",sep=';',index_col=0)
    diffuseIrradiance_DF=pd.read_csv("diffuseIrradiance.csv",sep=';',index_col=0)
    
    #beam irradiance value:
    name_of_columns=beamIrradiance_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    beam_irr_value=sp.interp(latitude,name_of_columns_as_numbers,beamIrradiance_DF.loc[directionWall]) 
    
    #diffuse irradiance value:
    name_of_columns2=diffuseIrradiance_DF.columns.get_values()
    name_of_columns2_as_numbers = name_of_columns2.astype(np.int32, copy=False)
    diff_irr_value=sp.interp(latitude,name_of_columns2_as_numbers,diffuseIrradiance_DF.loc[directionWall]) 
        
    #PXI:
    PXI=diff_irr_value+beam_irr_value
    return PXI

windows_DF=pd.read_csv("windows.csv",sep=';',index_col=0)
latitude=45    # RLF example 1
PXI_values=[]
for index in windows_DF.index.tolist():
    PXI_values = np.append(PXI_values,PXI_finder(latitude,windows_DF.loc[index,"Direction"]))
print PXI_values

#update the PXI column in windows dataframe:
windows_DF["PXI"] = np.array(PXI_values)
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")