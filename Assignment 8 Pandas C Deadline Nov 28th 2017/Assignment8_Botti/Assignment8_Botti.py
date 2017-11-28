import os
import numpy as np
import pandas as pd

import scipy as sp

os.chdir("C:\Users\Giulia\Desktop\Buildings\python\Assignment\Assignment8_Botti")

windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)

# Defining Function for calculating PXI
def PXI_calculator(Latitude,WallDir):
    DF_BeamIrradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
    DF_DiffuseIrradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)

    name_of_columns = DF_BeamIrradiance.columns.get_values() #To interpolate
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    
    BeamIrradiance_value=sp.interp(Latitude,name_of_columns_as_numbers,DF_BeamIrradiance.loc[WallDir])
    DiffuseIrradiance_value = sp.interp(Latitude,name_of_columns_as_numbers,DF_DiffuseIrradiance.loc[WallDir])
    
    PXI_value = BeamIrradiance_value+DiffuseIrradiance_value
    
    return PXI_value

# Prove the function with interpolation
PXI_interpolation = PXI_calculator(42,"N")

# writing a for loop to do the look up of PXI for all windows using the developed function
Latitude = 45
PXI_values = []
for index in windows_DataFrame.index.tolist():
    PXI_values = np.append(PXI_values,PXI_calculator(Latitude,windows_DataFrame["Direction"][index]))
    
#Updating values on Excel
windows_DataFrame["PXI"] = PXI_values
windows_DataFrame.to_csv("Windows_completed_with_PXI.csv",sep=";")