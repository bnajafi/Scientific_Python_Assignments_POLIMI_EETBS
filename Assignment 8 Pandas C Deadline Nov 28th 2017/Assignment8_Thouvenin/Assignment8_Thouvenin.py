# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:06:30 2017

@author: edoua
"""

import os
import numpy as np
import pandas as pd

import scipy as sp

def PXI_finder (latitude, orientation, Tx, Fshd):
    os.chdir("C:\Users\edoua\Documents\Piacenza\Double Diplome\Corsi\Building systems\Assignments\Ass 8")

    BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv" , sep=';', index_col=0)
    DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv", sep=';', index_col=0)
        
    #interpolation
    BeamIrr_name_of_columns = BeamIrradiance_DF.columns.get_values()
    BeamIrr_name_of_columns_as_number = BeamIrr_name_of_columns.astype(np.int32, copy=False)
    
    Beam_Irradiance_value=sp.interp(latitude,BeamIrr_name_of_columns_as_number,BeamIrradiance_DF.loc[orientation])
    
    DiffuseIrr_name_of_columns = DiffuseIrradiance_DF.columns.get_values()
    DiffuseIrr_name_of_columns_as_number = DiffuseIrr_name_of_columns.astype(np.int32, copy=False)
    
    Diffuse_Irradiance_value=sp.interp(latitude,DiffuseIrr_name_of_columns_as_number,DiffuseIrradiance_DF.loc[orientation])
    
    PXI_value = Tx*(Diffuse_Irradiance_value + (1-Fshd)*Beam_Irradiance_value)
    
    return PXI_value



BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv" , sep=';', index_col=0)

latitude = 45
Tx=1
Fshd=0

PXI_values = []

for index in BeamIrradiance_DF.index.tolist():
    print index
    PXI_values = np.append(PXI_values, PXI_finder(latitude, index, Tx, Fshd))
    print PXI_values

Windows_DF = pd.read_csv("windows.csv", sep=';', index_col=0)

PXI_EASTPC = PXI_values[3]
PXI_WESTPC = PXI_values[4]
PXI_SOUTHPC = PXI_values[7]

Windows_DF ["PXI"] = np.array ([PXI_values[3], PXI_values[4],PXI_values[7], PXI_values[7]] )
print Windows_DF ["PXI"]
Windows_DF.to_csv("windows_completed_withPXI.csv", sep=';')

