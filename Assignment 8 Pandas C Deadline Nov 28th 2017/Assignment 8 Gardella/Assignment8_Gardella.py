import os
import numpy as np
import pandas as pd

import scipy as sp 

os.chdir ("C:\Users\Fabio\Documents\Polimi\Magistrale\Buildings\Assignments\Assignment 8 Gardella")



def PXI_calculator (Latitude,WallDirection):
    
    Beam_DF=pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
    Diffuse_DF = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
    
    name_of_columns = Beam_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)

    Beam_irradiance = sp.interp(Latitude,name_of_columns_as_numbers,Beam_DF.loc[WallDirection])
    Diffuse_irradiance = sp.interp(Latitude,name_of_columns_as_numbers,Diffuse_DF.loc[WallDirection])
    
    PXI = Diffuse_irradiance + Beam_irradiance
    
    return PXI


windows_DF = pd.read_csv("windows.csv",sep=";",index_col= 0)

PXI_values = []
for index in windows_DF.index.tolist():
    PXI_values = np.append(PXI_values,PXI_calculator(45,windows_DF["Direction"][index]))

windows_DF["PXI"] = PXI_values

windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
 

