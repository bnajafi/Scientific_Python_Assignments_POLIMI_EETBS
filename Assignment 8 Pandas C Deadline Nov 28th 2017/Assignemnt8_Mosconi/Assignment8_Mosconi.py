import os
import numpy as np
import pandas as pd
import scipy as sp  #interpolation

os.chdir("C:\Users\Manuel\Documents\Polimi\Building systems\Assignments\Assignment 8")


windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)

beamIrradiance = pd.read_csv("BeamIrradiance.csv",sep=";",index_col= 0)
diffuseIrradiance = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col= 0)

Latitude=45
name_of_columns=beamIrradiance.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
#for doing interpolation


def beamIrradiance_finder(latitude,direction):
    beamIrradiance = pd.read_csv("BeamIrradiance.csv",sep=";",index_col= 0)
    beamIrradiance_value= sp.interp(latitude,name_of_columns_as_numbers,beamIrradiance.loc[direction])
    return beamIrradiance_value
ED=[]
for index in windows_DataFrame.index.tolist():
    ED=np.append(ED,beamIrradiance_finder(Latitude,windows_DataFrame["Direction"][index]))


def diffuseIrradiance_finder(latitude,direction):
    diffuseIrradiance = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col= 0)
    diffuseIrradiance_value= sp.interp(latitude,name_of_columns_as_numbers,diffuseIrradiance.loc[direction])
    return diffuseIrradiance_value

Ed=[]
for index in windows_DataFrame.index.tolist():
    Ed=np.append(Ed,diffuseIrradiance_finder(Latitude,windows_DataFrame["Direction"][index]))


Et=Ed+ED
PXI=[]

PXI=Et*windows_DataFrame["Tx"]

windows_DataFrame["PXI"]=PXI
windows_DataFrame.to_csv("windows_completedWithPXI.csv",sep=";")