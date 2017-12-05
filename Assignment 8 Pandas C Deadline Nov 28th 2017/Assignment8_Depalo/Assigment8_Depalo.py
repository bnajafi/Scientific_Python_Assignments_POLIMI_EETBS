#Assignment 8 - Depalo

import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\MonicaDepp\Dropbox\GitBash\gitForkClone\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")
import scipy as sp

beamIrradiance_DF=pd.read_csv("beamIrradiance.csv",sep=';',index_col=0)
diffuseIrradiance_DF=pd.read_csv("diffuseIrradiance.csv",sep=';',index_col=0)
    
def PXI_finder(latitude,directionWall):
    "This function finds the PXI values (Tx factor not taken into account) receiving latitude and direction of the wall"
    beamIrradiance_DF=pd.read_csv("beamIrradiance.csv",sep=';',index_col=0)
    diffuseIrradiance_DF=pd.read_csv("diffuseIrradiance.csv",sep=';',index_col=0)
    
    #definition of beam irradiance value:
    name_of_columns=beamIrradiance_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    beam_irr_value=sp.interp(latitude,name_of_columns_as_numbers,beamIrradiance_DF.loc[directionWall]) 
    
    #definition of diffuse irradiance value:
    name_of_columns2=diffuseIrradiance_DF.columns.get_values()
    name_of_columns2_as_numbers = name_of_columns2.astype(np.int32, copy=False)
    diff_irr_value=sp.interp(latitude,name_of_columns2_as_numbers,diffuseIrradiance_DF.loc[directionWall]) 
        
    #PXI:
    PXI=diff_irr_value+beam_irr_value
    return PXI

#creating dataframe with windows data:
windows_DF=pd.read_csv("windows.csv",sep=';',index_col=0)

latitude=45    #latitude of Piacenza, RLF example 1
#writing a for loop to do the look up of PXI for all windows using the developed function:
PXI_values=[]
for index in windows_DF.index.tolist():
    Tx=windows_DF.loc[index,'Tx']              #taking into account the presence of insect nets
    PXI_values = np.append(PXI_values,Tx*PXI_finder(latitude,windows_DF.loc[index,"Direction"]))

print PXI_values

#updating the PXI column in windows dataframe:
windows_DF["PXI"] = np.array(PXI_values)

#writing the modified table to a new .csv file:
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")