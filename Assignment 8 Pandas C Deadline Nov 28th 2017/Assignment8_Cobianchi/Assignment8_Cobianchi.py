import os #operative system to change directory to see the files
import numpy as np
import pandas as pd
import scipy as sp

#read the excel files in the same folder
os.chdir("C:/Users/riccardo/Desktop/Documenti/POLIMI/Exams NOT Done/BUILDING SYSTEMS/Assignment8_Cobianchi")
DF_windows = pd.read_csv("windows.csv",sep=";",index_col= 0)
DF_BeamIrradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DF_DiffuseIrradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)

#input data
Exposure = raw_input("Surface's Exposure: ")
Latitude = raw_input("Latitude of Location:  ")

#define the function TO EXTRACT the values of BI and DI and then calculate the PXI
def function(Exposure,Latitude):
    
    DF_BeamIrradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
    BeamIrradiance_value = DF_BeamIrradiance[Latitude][Exposure]
    DF_DiffuseIrradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
    DiffuseIrradiance_value = DF_DiffuseIrradiance[Latitude][Exposure]
    
    return (BeamIrradiance_value+DiffuseIrradiance_value)
    
counterA = 0 #if counterA becomes 1 it means that a value is found 
counterB = 9 #if counterB becomes 0 it means that a value is NOT found. 9 is the size of DF_BeamIrradiance.columns.tolist()
for columnA in DF_BeamIrradiance.columns.tolist():
    if (columnA == Latitude):
        counterA += 1 
if counterA == 1:
    PXI = function(Exposure,Latitude)
    print
    print ("The Value of PXI is: ")+str(PXI)
    
    
counterB = 9           
for columnC in DF_BeamIrradiance.columns.tolist():
    if (columnC != Latitude):
        counterB -= 1
if counterB == 0:
    name_of_columns = DF_BeamIrradiance.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    A = sp.interp(float(Latitude), name_of_columns_as_numbers, DF_DiffuseIrradiance.loc[Exposure]) 
       
    name_of_columns = DF_DiffuseIrradiance.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    B = sp.interp(float(Latitude), name_of_columns_as_numbers, DF_DiffuseIrradiance.loc[Exposure])
    print
    print ("The Value of PXI is: ")+str(A+B)
    
#PIACENZA
Latitude_Pc = "45"
PXI_values=[]
for index in DF_windows.index.tolist():
    PXI_values = np.append(PXI_values,function(DF_windows["Direction"][index],Latitude_Pc))
print    
print ("The PXI_values of Piacenza are: ")+str(PXI_values)
  
DF_windows["PXI"] = PXI_values
DF_windows.to_csv("windows_completed_withPXI.csv",sep=";")
DF_windows.to_html("Window_Completed_withPXI.html") 
