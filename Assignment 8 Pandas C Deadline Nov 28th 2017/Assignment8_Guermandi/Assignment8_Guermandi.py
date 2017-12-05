import os
import numpy as np
import pandas as pd
import scipy as sp
os.chdir("/Users/Fede/Documents/Polimi/EETBS/Numpy - Pandas/RLF Method")

def PXI_finder (latitude,walldirection):
    beamirradiance_DataFrame = pd.read_csv("BeamIrradiance.csv",sep=";",index_col= 0)
    diffuseirradiance_DataFrame = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col= 0)
    
    column_beam=beamirradiance_DataFrame.columns.get_values()
    column_beam_as_numbers = column_beam.astype(np.int32, copy=False)
    column_diffuse=beamirradiance_DataFrame.columns.get_values()
    column_diffuse_as_numbers = column_diffuse.astype(np.int32, copy=False)
    
    ED=sp.interp(latitude,column_beam_as_numbers,beamirradiance_DataFrame.loc[walldirection])
    EDU=sp.interp(latitude,column_diffuse_as_numbers,diffuseirradiance_DataFrame.loc[walldirection])
    #with an if-cycle, I could tell Python not to interpolate if the latitude in input
    #corresponds to the ones in the index, in order to reduce the number of calculations
    PXI=ED+EDU
    
    return PXI
    
windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)
DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)

#to check if it works
Latitude = float(raw_input("please enter the latitude "))
PXI_value=[]
for index in windows_DataFrame.index.tolist():
    PXI_value = np.append(PXI_value,PXI_finder(Latitude,windows_DataFrame["Direction"][index]))
print PXI_value
    
#in case of Piacenza ----> latitude=45
latitude=45
PXI_values=[]
for index in windows_DataFrame.index.tolist():
    PXI_values = np.append(PXI_values,PXI_finder(latitude,windows_DataFrame["Direction"][index]))
    
windows_DataFrame["PXI"] = np.array(PXI_values)
windows_DataFrame.to_csv("windows_completed_withPXI.csv",sep=";")
