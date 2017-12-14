# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import scipy as sp
os.chdir("D:\Michele\Universita\Building systems\Esercitazioni\RLF Method")

def PXI_finder (latitude,walldirection):
    beamirr_DataFrame = pd.read_csv("BeamIrradiance.csv",sep=";",index_col= 0)
    diffuseirr_DataFrame = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col= 0)
    
    column_beam=beamirr_DataFrame.columns.get_values()
    column_beam_as_numbers = column_beam.astype(np.int32, copy=False)
    column_diffuse=beamirr_DataFrame.columns.get_values()
    column_diffuse_as_numbers = column_diffuse.astype(np.int32, copy=False)
    
    ED=sp.interp(latitude,column_beam_as_numbers,beamirr_DataFrame.loc[walldirection])
    EDU=sp.interp(latitude,column_diffuse_as_numbers,diffuseirr_DataFrame.loc[walldirection])

    PXI=ED+EDU
    
    return PXI
    
windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)
DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)

#If we are in Piacenza the latitude is 45°
latitude=45
PXI_values=[]
for index in windows_DataFrame.index.tolist():
    PXI_values = np.append(PXI_values,PXI_finder(latitude,windows_DataFrame["Direction"][index]))
    
#this is the general case where the user can enter the desired number
Latitude = float(raw_input("please enter the latitude "))
PXI_value=[]
for index in windows_DataFrame.index.tolist():
    PXI_value = np.append(PXI_value,PXI_finder(Latitude,windows_DataFrame["Direction"][index]))
print PXI_value

    
windows_DataFrame["PXI"] = np.array(PXI_values)
windows_DataFrame.to_csv("windows_completed_withPXI.csv",sep=";")
