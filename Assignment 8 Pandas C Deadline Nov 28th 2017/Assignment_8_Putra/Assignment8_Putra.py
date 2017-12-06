#---------------------------Assignment 8---------------------
#---------------------Hendra Suryana Putra--------------------

import os
import numpy as np
import pandas as pd

import scipy as sp

os.chdir("/Users/hendrasuryanaputra/Documents/Polomi Course/EETB/Assignment_8_Putra")

windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep=";",index_col=0)
Beam_Ir_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
Diffuse_Ir_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

#Define Latitude and Direction

latitude = "45"
windows_DF["Direction"][index]

#Find Beam Irradiance value

def Beam_Ir_finder(latitude,direction):  
    Beam_Ir_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    Beam_Ir_Value = Beam_Ir_DF[latitude][direction]
    return Beam_Ir_Value


#Find Diffuse Irradiance value

def Diffuse_Ir_finder(latitude,direction):   
    Diffuse_Ir_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    Diffuse_Ir_Value = Diffuse_Ir_DF[latitude][direction]    
    return Diffuse_Ir_Value

#Find PXI Value
     
Beam_Ir_values = []  
Diffuse_Ir_values = []
PXI_values = []

for index in windows_DF.index.tolist():
    print index
    
    Beam_Ir_values = np.append(Beam_Ir_values,Beam_Ir_finder(latitude,windows_DF["Direction"][index]))
    Diffuse_Ir_values = np.append(Diffuse_Ir_values,Diffuse_Ir_finder(latitude,windows_DF["Direction"][index])) 
    PXI_values = Diffuse_Ir_values + Beam_Ir_values
    
    
print PXI_values

windows_DF["PXI"] = PXI_values
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";") 


#Input for Interpolation

Latitude = 45
name_of_columns = Beam_Ir_DF.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
name_of_columns = Diffuse_Ir_DF.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
Beam_Ir_Value_itp = sp.interp(Latitude,name_of_columns_as_numbers,Beam_Ir_DF.loc["S"]) 
Diffuse_Ir_DF_itp = sp.interp(Latitude,name_of_columns_as_numbers,Diffuse_Ir_DF.loc["S"]) 



    



    
    




#function to find diffuse irradiance





