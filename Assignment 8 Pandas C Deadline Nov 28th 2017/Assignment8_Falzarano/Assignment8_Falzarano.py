import os
import numpy as np
import pandas as pd
import scipy as sp

os.chdir ("C:\Users\Marica\Desktop\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")

#reading the files
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)


def PXI_calc (latitude, orientation,Tx):
    
    #beam
    B_name_of_columns=BeamIrradiance_DF.columns.get_values()
    B_name_of_columns_as_numbers = B_name_of_columns.astype(np.int32, copy=False)
    
    Beam_value =sp.interp(latitude,B_name_of_columns_as_numbers,BeamIrradiance_DF.loc[orientation])

    #diffuse 
    D_name_of_columns=DiffuseIrradiance_DF.columns.get_values()
    D_name_of_columns_as_numbers = D_name_of_columns.astype(np.int32, copy=False)
    
    Irr_value =sp.interp(latitude,D_name_of_columns_as_numbers,DiffuseIrradiance_DF.loc[orientation])

    #PXI calculation
    PXI = Tx*(Beam_value + Irr_value)
    
    return PXI
    

latitude = 42

PXI = []
for index in windows_DF.index.tolist():
    print index
    PXI = np.append(PXI,PXI_calc(latitude,windows_DF["Direction"][index],windows_DF["Tx"][index]))
print PXI
 
        
