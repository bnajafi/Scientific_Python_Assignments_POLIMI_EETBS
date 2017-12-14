#ASSIGNMENT 8

import os
import numpy as np
import pandas as pd

import scipy as sp

os.chdir("/Users/Fede/Desktop/RLF Method")

Windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)

def Irrad (L,D):

     Beam_Irradiation=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
     Diffuse_Irradiation=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

     name_of_columns=Beam_Irradiation.columns.get_values()
     name_of_columns_as_numbers=name_of_columns.astype(np.int32, copy=False)
     name_of_columns1=Diffuse_Irradiation.columns.get_values()
     name_of_columns_as_numbers1=name_of_columns1.astype(np.int32, copy=False)
    
     Beam_Irradiation_def=sp.interp(L,name_of_columns_as_numbers,Beam_Irradiation.loc[D]) 
     Diffuse_Irradiation_def=sp.interp(L,name_of_columns_as_numbers1,Diffuse_Irradiation.loc[D])

     PXI=Beam_Irradiation_def+Diffuse_Irradiation_def

     return PXI

#Piacenza_case

latitude_location = 45
PXI_values=[]
for index in Windows_DF.index.tolist():
    print index
    PXI_values = np.append(PXI_values,Irrad(latitude_location,Windows_DF["Direction"][index]))    
print PXI_values 
  
Windows_DF["PXI"] = PXI_values
Windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
Windows_DF.to_html("Window_Completed_withPXI.html") 




