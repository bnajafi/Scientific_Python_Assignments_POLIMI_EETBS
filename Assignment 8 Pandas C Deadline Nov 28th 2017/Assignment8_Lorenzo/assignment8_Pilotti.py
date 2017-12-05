# Assignment 8

import os

import numpy as np
import pandas as pd
import scipy as sp

os.chdir("C:/Users/Lorenzo/Dropbox_Polimi_PC/Dropbox/EETBS 2017-2018 POLIMI-PIACENZA/3 Python Files and Guidelines/Numpy - Pandas/RLF Method")

def PXI_finder(ExposureDirection,Latitude):
    """ This function, given the exposure and the latitude of a building surface,
        find the value of the Beam and Diffuse Irradiance in the tables and 
        computes the value of the PXI as their sum"""
    Beam_DF=pd.read_csv("BeamIrradiance.csv", sep=";", index_col=0)
    Diffuse_DF=pd.read_csv("DiffuseIrradiance.csv", sep=";", index_col=0)
    
    # interpolation
    name_of_columns=Beam_DF.columns.get_values()
    name_of_columns_as_numbers=name_of_columns.astype(np.int32, copy=False)
    
    BeamIrr_value=sp.interp(Latitude, name_of_columns_as_numbers, Beam_DF.loc[ExposureDirection])
    DiffuseIrr_value=sp.interp(Latitude, name_of_columns_as_numbers, Diffuse_DF.loc[ExposureDirection])
    
    # PXI
    PXI_value=DiffuseIrr_value+BeamIrr_value
    return PXI_value
    

# Piacenza example
windows_DF=pd.read_csv("windows.csv", sep=";", index_col=0)
latitude_location=42.5

PXI_values=[]
for index in windows_DF.index.tolist():
     PXI_values=np.append(PXI_values, PXI_finder(windows_DF["Direction"][index], latitude_location))
        
windows_DF["PXI"]=PXI_values*windows_DF["Tx"]


# updating and saving
os.chdir("C:/Users/Lorenzo/Desktop/Polimi PC/Python Files")
windows_DF.to_csv("windows_completed_withPXI.csv", sep=";")


