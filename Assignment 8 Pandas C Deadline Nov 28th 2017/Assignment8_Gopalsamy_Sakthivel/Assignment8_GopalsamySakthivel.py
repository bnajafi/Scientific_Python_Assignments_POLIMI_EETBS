import os
import numpy as np
import pandas as pd
import scipy as sp 
os.chdir("E:/Master's/First Semester/Buildings/Numpy - Pandas- python class7/RLF Method")
windowsDF=pd.read_csv("windows.csv",sep=";",index_col=0)
DF_BeamIrradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DF_DiffIrradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
Latitude=45
name_of_columns=DF_BeamIrradiance.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
def PXI_Finder(Direction,Lat):
    BeamIrradiance_value=sp.interp(Lat,name_of_columns_as_numbers,DF_BeamIrradiance.loc[Direction])
    DiffIrradiance_value=sp.interp(Lat,name_of_columns_as_numbers,DF_DiffIrradiance.loc[Direction])
    Tx_value=windowsDF["Tx"][index]
    PXI_value=Tx_value*(BeamIrradiance_value+DiffIrradiance_value)
    return PXI_value

PXI_values=[]
for index in windowsDF.index.tolist():
    print index
    #Tx_values=np.append(Tx_values,windowsDF["Tx"][index])
    PXI_values = np.append(PXI_values,PXI_Finder(windowsDF["Direction"][index],Latitude))

windowsDF["PXI"]=PXI_values
windowsDF.to_csv("windows_completed_withPXI.csv",sep=";")
print windowsDF["PXI"]





    