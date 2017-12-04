#assignment 8 - Riccardi
import os
import numpy as np
import pandas as pd

import scipy as sp

os.chdir("C:\Users\Luca\Desktop\Luca\PoliMinchia\Primo anno\Energy and environmental technologies\Assignments\RLFmethod")

DF_Windows = pd.read_csv("windows.csv",sep=";",index_col= 0)

TotalIrr_Values=[]


def pxi_finder(latitude,direction):
    DF_Beam = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
    DF_Diffuse = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
    NameOfColumns_Beam=DF_Beam.columns.get_values()
    NameOfColumnsAsNumbers_Beam = NameOfColumns_Beam.astype(np.int32, copy=False)
    ED=sp.interp(latitude,NameOfColumnsAsNumbers_Beam,DF_Beam.loc[direction])
    NameOfColumns_Diffuse=DF_Diffuse.columns.get_values()
    NameOfColumnsAsNumbers_Diffuse = NameOfColumns_Diffuse.astype(np.int32, copy=False)
    Ed=sp.interp(latitude,NameOfColumnsAsNumbers_Diffuse,DF_Diffuse.loc[direction])
    TotalIrradiance=ED+Ed
    
    return TotalIrradiance 

Latitude= 45
for direction in DF_Windows["Direction"].tolist():
    TotalIrr=pxi_finder(Latitude,direction)
    TotalIrr_Values=np.append(TotalIrr_Values,TotalIrr)

PXI_Values=TotalIrr_Values*DF_Windows["Tx"]

DF_Windows["PXI"]=PXI_Values


DF_Windows.to_csv("windows_completed_withPXI.csv",sep=";")


    
    
    
    
    
    
    
    