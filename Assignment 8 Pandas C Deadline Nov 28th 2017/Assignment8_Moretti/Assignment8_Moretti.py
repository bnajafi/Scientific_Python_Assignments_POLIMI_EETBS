"""

EETBS 2017/2018 - Assignment 8 - improving the procedure of assignment 7

Giorgio Moretti (10433550)

"""

import os
import pandas as pd
import numpy as np
import scipy as sp

os.chdir("D:\Documents\Politecnico\Energy Eng. Master\Buildings (Behzad)\A.Y. 2017-2018\Assignments\excel pandas")

windows_DF = pd.read_csv("windows.csv", sep = ";", index_col = 0)

def beamIrradiance_finder(latitude,direction):
    beamIrradiance_DF = pd.read_csv("beamIrradiance.csv", sep = ";", index_col = 0)
    name_of_columns = beamIrradiance_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy = False)
    BI_int = sp.interp(latitude, name_of_columns_as_numbers, beamIrradiance_DF.loc[direction])  ## interpolated beam irradiance
    return BI_int
    
def diffuseIrradiance_finder(latitude,direction):
    diffuseIrradiance_DF = pd.read_csv("diffuseIrradiance.csv", sep = ";", index_col = 0)
    name_of_columns = diffuseIrradiance_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy = False)
    DI_int = sp.interp(latitude, name_of_columns_as_numbers, diffuseIrradiance_DF.loc[direction])  ## interpolated diffuse irradiance
    return DI_int
    
latitude = 42

## PXI calculation and substitution in windows data frame column

for index in windows_DF.index.tolist():
    windows_DF["PXI"][index] = beamIrradiance_finder(latitude,windows_DF["Direction"][index]) + diffuseIrradiance_finder(latitude,windows_DF["Direction"][index])
    
windows_DF.to_csv("windows_completed_withPXI.csv", sep = ";")
windows_DF.to_html("windows_completed_withPXI.html")