import os
import numpy as np
import pandas as pd
import scipy as sp

os.chdir("C:\Users\Valeria\Desktop\Assignement")



Windows_DF= pd.read_csv("windows.csv",sep=";",index_col=0)
BeamIrradiance_ED = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_Ed = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

#Function Definition
def PXI_calculator(direction,latitude):
    name_of_columns=BeamIrradiance_ED.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED = sp.interp(latitude,name_of_columns_as_numbers,BeamIrradiance_ED.loc[direction])
    
    name_of_columns=DiffuseIrradiance_Ed.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed = sp.interp(latitude,name_of_columns_as_numbers,DiffuseIrradiance_Ed.loc[direction])
    
    PXI= ED+Ed
    return PXI
   
# Piacenza

PXI_values=[]
for index in Windows_DF.index.tolist():
    PXI_newvalue=PXI_calculator(Windows_DF["Direction"][index],45)    
    PXI_values = np.append(PXI_values,PXI_newvalue)   
print PXI_values 

Windows_DF["PXI"] = PXI_values
Windows_DF.to_csv("windows_completed_withPXI_Casalicchio.csv",sep=";")