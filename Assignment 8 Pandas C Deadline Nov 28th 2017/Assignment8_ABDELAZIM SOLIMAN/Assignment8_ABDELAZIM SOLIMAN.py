import os
import numpy as np
import pandas as pd
import scipy as sp

os.chdir("C:/Users/user/Desktop/_EETBS/Numpy - Pandas/RLF Method")

Windows_DF= pd.read_csv("windows.csv",sep=";",index_col=0)

BeamIrradiance_ED = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_Ed = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

direction = raw_input('please enter the diretion of the wall ')
latitude = float(raw_input('please enter the latitude of the location '))


if latitude == BeamIrradiance_ED.columns.tolist(): 
    def PXI_calc(direction,latitude):
        BeamIrradiance_ED = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)     
        result_BeamIrradiance_ED= BeamIrradiance_ED[latitude][direction]
    
        DiffuseIrradiance_Ed = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
        result_DiffuseIrradiance_Ed= DiffuseIrradiance_Ed[latitude][direction]
        PXI= result_BeamIrradiance_ED+result_DiffuseIrradiance_Ed
        return PXI
    
if latitude != BeamIrradiance_ED.columns.tolist():        
    name_of_columns=BeamIrradiance_ED.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED=sp.interp(latitude,name_of_columns_as_numbers,BeamIrradiance_ED.loc[direction])
    
    name_of_columns=DiffuseIrradiance_Ed.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed=sp.interp(latitude,name_of_columns_as_numbers,DiffuseIrradiance_Ed.loc[direction])
    PXI= ED+Ed
    print "PXI value is " +str(PXI)
    
# PXI calculation for RLF example 1    

latitude_location= "45" 
PXI_values=[]
for index in Windows_DF.index.tolist():
    print index
    print Windows_DF["Direction"][index]
    PXI_values = np.append(PXI_values,PXI_calc(Windows_DF["Direction"][index],latitude_location))
                              
print PXI_values 

Windows_DF["PXI"] = PXI_values
Windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
Windows_DF.to_html("Window_Completed_withPXI.html") 
