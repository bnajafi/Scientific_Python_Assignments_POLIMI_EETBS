import os
import pandas as pd
import numpy as np

import scipy as sp

os.chdir ("C:\Users\TOSHIBA\Documents\Italia\Building\Git\git_fork\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 8 Pandas C Deadline Nov 28th 2017\Assignment8_Wong")

latitude_location = 45
beam_irra = pd.read_csv("beamIrradiance.csv",sep=";",index_col=0)
diffuse = pd.read_csv("diffuseIrradiance.csv",sep = ";",index_col=0)
windows = pd.read_csv("windows.csv",sep=";",index_col=0)

print beam_irra.columns
print beam_irra.index
print diffuse.columns
print diffuse.index
print windows.columns
print windows.index

Latitude=42
name_of_columns=beam_irra.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)

name_of_columns1=diffuse.columns.get_values()
name_of_columns_as_numbers1 = name_of_columns1.astype(np.int32, copy=False)

def Beamfinder(windowDI,lat):

    beamvalue=sp.interp(lat,name_of_columns_as_numbers,beam_irra.loc[windowDI])
    
    return beamvalue
    
def diffusefinder(windowDI,lat):
    diffusevalue=sp.interp(lat,name_of_columns_as_numbers1,diffuse.loc[windowDI])
    
    return diffusevalue

    
direct=[]
for index in windows.index.tolist():
    print index
    direct = np.append(direct,Beamfinder(windows["Direction"][index],latitude_location))
    
diff=[]
for index in windows.index.tolist():
    print index
    diff = np.append(diff,diffusefinder(windows["Direction"][index],latitude_location))

i=0
for index in windows.index.tolist():
    windows["PXI"][index]=(direct[i]+diff[i])*windows["Tx"][index]
    i=i+1
    print windows["PXI"][index]

# How to write the modified Table to a new file.
windows.to_csv("windows_completed_withPXI.csv",sep=";")
