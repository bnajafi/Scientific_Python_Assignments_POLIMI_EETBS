#Assignment 8
#Shashwat Parsana


import os
os.chdir("G:/Sem 1/ENERGY AND ENVIRONMENTAL TECHNOLOGIES FOR BUILDING SYSTEMS/Canopy Files")
import numpy as np
import pandas as pd

import scipy as sp 

windowsDF=pd.read_csv("windows.csv",sep=";",index_col=0)

BeamIrradianceDF = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DiffIrradianceDF = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)

name_of_columns=BeamIrradianceDF.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)

Latitude=45 #given

#Function
def PXI_Finder(Direction,Lat):
    BeamIrradiance_value=sp.interp(Lat,name_of_columns_as_numbers,BeamIrradianceDF.loc[Direction])
    DiffIrradiance_value=sp.interp(Lat,name_of_columns_as_numbers,DiffIrradianceDF.loc[Direction])
    Txvalue=windowsDF["Tx"][index]
    PXI_value=Txvalue*(BeamIrradiance_value+DiffIrradiance_value)
    return PXI_value

PXI_values=[]
for index in windowsDF.index.tolist():
    print index
    
    PXI_values = np.append(PXI_values,PXI_Finder(windowsDF["Direction"][index],Latitude))

windowsDF["PXI"]=PXI_values
windowsDF.to_csv("windows_completed_withPXI.csv",sep=";")
print windowsDF["PXI"]