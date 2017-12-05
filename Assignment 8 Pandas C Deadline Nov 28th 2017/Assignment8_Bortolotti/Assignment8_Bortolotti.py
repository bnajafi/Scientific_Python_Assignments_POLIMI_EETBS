import os
import numpy as np
import pandas as pd
import scipy as sp

os.chdir("C:\Users//alice\Desktop\Master PC\Buildings System\EETBS 2017-2018 POLIMI-PIACENZA\Assignments\Assignment8_Bortolotti")

windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col=0)

BeamIrradiance_ED = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_Ed = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

exposure = raw_input('please enter the exposure ')
latitude_location = float(raw_input('please enter the latitude of the location '))


if latitude_location == BeamIrradiance_ED.columns.tolist(): 
    def PXI_finder(direction,latitude_location):
        BeamIrradiance_ED = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)     
        result_BeamIrradiance_ED = BeamIrradiance_ED[latitude_location][exposure]
    
        DiffuseIrradiance_Ed = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
        result_DiffuseIrradiance_Ed = DiffuseIrradiance_Ed[latitude_location][exposure]
        PXI = result_BeamIrradiance_ED + result_DiffuseIrradiance_Ed
        return PXI    

if latitude_location != BeamIrradiance_ED.columns.tolist():        
    
    name_of_columns = BeamIrradiance_ED.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED = sp.interp(latitude_location,name_of_columns_as_numbers,BeamIrradiance_ED.loc[exposure])
    
    name_of_columns = DiffuseIrradiance_Ed.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed = sp.interp(latitude_location,name_of_columns_as_numbers,DiffuseIrradiance_Ed.loc[exposure])
    PXI = ED + Ed
    print "PXI value is " + str(PXI)
    
# PXI calculation for RLF example 1 - Piacenza
        
latitude_location = "45" 
windows_DataFrame.index.tolist()
PXI_values = []
for index in windows_DataFrame.index.tolist():
    print index
    print windows_DataFrame["Direction"][index]
    PXI_values = np.append(PXI_values,PXI_finder(windows_DataFrame["Direction"][index],latitude_location))
print PXI_values
  
windows_DataFrame["PXI"] = PXI_values
windows_DataFrame.to_csv("windows_completed_withPXI.csv",sep=";")
windows_DataFrame.to_html("Window_Completed_withPXI.html")