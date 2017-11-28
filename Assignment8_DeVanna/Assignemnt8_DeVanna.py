import os
import numpy as np
import pandas as pd
import scipy as sp
os.chdir("/Users/Guglielmo/Desktop/Assignment8_DeVanna")

def Value_finder(L,D):
    
    Diffuse_Irradiation = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    Beam_Irradiation = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    name_of_columns=Beam_Irradiation.columns.get_values()
    name_of_columns_as_numbers= name_of_columns.astype(np.int32, copy=False)
    name_of_columns1=Diffuse_Irradiation.columns.get_values()
    name_of_columns_as_numbers1= name_of_columns1.astype(np.int32, copy=False)
    
    BI=sp.interp(L,name_of_columns_as_numbers,Beam_Irradiation.loc[D]) 
    DI=sp.interp(L,name_of_columns_as_numbers1,Diffuse_Irradiation.loc[D]) 
    
    PXI=BI+DI

    return PXI



##PIACENZA
Windows_DF= pd.read_csv("windows.csv",sep=";",index_col=0)    
latitude_location = 45
PXI_values=[]
for index in Windows_DF.index.tolist():
    print index
    PXI_values = np.append(PXI_values,Value_finder(latitude_location,Windows_DF["Direction"][index]))    
print PXI_values 
  
Windows_DF["PXI"] = PXI_values
Windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
Windows_DF.to_html("Window_Completed_withPXI.html") 



