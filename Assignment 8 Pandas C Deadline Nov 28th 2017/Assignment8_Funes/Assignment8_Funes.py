import os
import numpy as np
import pandas as pd

import scipy as sp
os.chdir("D:\MIS DOCUMENTOS\Documents\Master Energy Engineering\RLF Method\Assignment8_Funes")


windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)

DF_BeamIrradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DF_DiffuseIrradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)

def PXI_finder(Direction,latitudeID):
    DF_BeamIrradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
    name_of_columns=DF_BeamIrradiance.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    BeamIrradiance_value=sp.interp(latitudeID,name_of_columns_as_numbers,DF_BeamIrradiance.loc[Direction])
    DF_DiffuseIrradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
    DiffuseIrradiance_value=sp.interp(latitudeID,name_of_columns_as_numbers,DF_DiffuseIrradiance.loc[Direction])
    PXI_value_int=BeamIrradiance_value+DiffuseIrradiance_value
    Tx_value=windows_DataFrame["Tx"][index]
    PXI_value=Tx_value*PXI_value_int
    return PXI_value
    

PXI_values=[]
Latitude_ID=45
for index in windows_DataFrame.index.tolist():
    print index
    print windows_DataFrame["Direction"][index]
    PXI_values = np.append(PXI_values,PXI_finder(windows_DataFrame["Direction"][index],Latitude_ID))
print PXI_values
windows_DataFrame["PXI"]=PXI_values
windows_DataFrame.to_csv("windows_completedWithPXI.csv",sep=";")
windows_DataFrame.to_html("windows_completedWithPXI.html")
