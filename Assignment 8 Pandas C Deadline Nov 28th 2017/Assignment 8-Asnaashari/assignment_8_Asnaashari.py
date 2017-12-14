import os
import numpy as np
import pandas as pd

import scipy as sp
os.chdir("D:/polimi note books/energy and enviromnetal technologies for building systems/assignments/Assignment 8-Asnaashari")
latitude=45

windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)
DF_BeamIrradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DF_DiffuseIrradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)

def PXI(latitude,direction):
    name_of_columns_BI=DF_BeamIrradiance.columns.get_values().astype(np.float32, copy=False)
    beam_radiation=sp.interp(latitude,name_of_columns_BI,DF_BeamIrradiance.loc[direction])
    name_of_columns_asnumbers_DI=DF_DiffuseIrradiance.columns.get_values().astype(np.float32, copy=False)
    diffuse_radiation=sp.interp(latitude,name_of_columns_asnumbers_DI,DF_DiffuseIrradiance.loc[direction])
    return beam_radiation+diffuse_radiation

PXI_value_list=[]
for index in windows_DataFrame.index:
    PXI_value_list.append((PXI(latitude,windows_DataFrame.loc[index]["Direction"])))
windows_DataFrame["PXI"]=np.array(PXI_value_list)
windows_DataFrame.to_csv("windows_completedwithPXI.csv",sep=";")  