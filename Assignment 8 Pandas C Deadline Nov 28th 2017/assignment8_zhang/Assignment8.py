import  os
import numpy as np
import pandas as pd
os.chdir("C:/Users/Clevo/Desktop/Assignments and trainings/assignment8_zhang")

import scipy as sp

beamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col = 0)
diffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col = 0)
windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col=0)

def PXI_finder(Direction,Latitude):
    beamIrradiance_DF=pd.read_csv("BeamIrradiance.csv", sep=";", index_col=0)
    diffuseIrradiance_DF=pd.read_csv("DiffuseIrradiance.csv", sep=";", index_col=0)
    name_of_columns=beamIrradiance_DF.columns.get_values()
    name_of_columns_as_numbers=name_of_columns.astype(np.int32, copy=False)
    beamIrradiance_value=sp.interp(Latitude, name_of_columns_as_numbers, beamIrradiance_DF.loc[Direction])
    diffuseIrradiance_value=sp.interp(Latitude, name_of_columns_as_numbers, diffuseIrradiance_DF.loc[Direction])
    PXI_value=diffuseIrradiance_value+beamIrradiance_value
    return PXI_value
   
latitude_location=45

PXI_values=[]
for index in windows_DataFrame.index.tolist():
     PXI_values=np.append(PXI_values, PXI_finder(windows_DataFrame["Direction"][index], latitude_location))
        
windows_DataFrame["PXI"] = np.array([PXI_values,0,0,0])

windows_DataFrame.to_csv("windows_completed_withPXI",sep=";" )


