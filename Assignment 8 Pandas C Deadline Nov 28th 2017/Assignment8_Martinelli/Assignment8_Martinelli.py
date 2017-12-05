import os
import numpy as np
import pandas as pd

import scipy as sp # You need to import Scipy in order to interpolate

os.chdir("C:\Users\Utente\Desktop\Assignment 8")

windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)

def PXI_finder(latitude_location,wall_direction):
    windows_BI = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    windows_DI = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    
    name_of_columnsBI=windows_BI.columns.get_values()
    name_of_columns_as_numbersBI = name_of_columnsBI.astype(np.int32, copy=False)
    
    beam_irr = sp.interp(latitude_location,name_of_columns_as_numbersBI,windows_BI.loc[wall_direction])
    
    name_of_columnsDI=windows_DI.columns.get_values()
    name_of_columns_as_numbersDI = name_of_columnsBI.astype(np.int32, copy=False)
    
    diffuse_irr = sp.interp(latitude_location,name_of_columns_as_numbersDI,windows_DI.loc[wall_direction])

    PXI = beam_irr + diffuse_irr
    return PXI

latitude = 45
PXI_values = []
for index in windows_DataFrame.index.tolist():
    #print index
    PXI_value = PXI_finder(latitude,windows_DataFrame["Direction"][index])
    print PXI_value
    PXI_values = np.append(PXI_values,PXI_value)

windows_DataFrame["PXI"] = PXI_values


windows_DataFrame.to_csv("windows_completed_withPXI.csv",sep=";")
