import os
import numpy as np
import pandas as pd
import scipy as sp
os.chdir("C:\Users\Lorenzo\Desktop\git_fork_clone\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 8 Pandas C Deadline Nov 28th 2017\Assignment8_Ferre")


windowsDF = pd.read_csv("windows.csv",sep=";",index_col= 0)

latitude = raw_input('please enter the latitude of the location ')
wall_direction = raw_input('please enter the exposure ')
latitude_number = float(latitude)

def PXI_calc(latitude,wall_direction):
    beam_irradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
    diffuse_irradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
    beam_irradiance_value = beam_irradiance[latitude][wall_direction]
    diffuse_irradiance_value = diffuse_irradiance[latitude][wall_direction]
    PXI = beam_irradiance_value + diffuse_irradiance_value
    return (PXI)
    
def PXI_calc_with_interpolation(latitude,wall_direction):
    beam_irradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
    diffuse_irradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
    name_of_columns_beam = beam_irradiance.columns.get_values()
    name_of_columns_as_numbers_beam = name_of_columns_beam.astype(np.int32, copy=False)
    ED = sp.interp(latitude_number,name_of_columns_as_numbers_beam,beam_irradiance.loc[wall_direction])
    name_of_columns_diffuse =diffuse_irradiance.columns.get_values()
    name_of_columns_as_numbers_diffuse = name_of_columns_diffuse.astype(np.int32, copy=False)
    Ed = sp.interp(latitude_number,name_of_columns_as_numbers_diffuse,diffuse_irradiance.loc[wall_direction])
    PXI_with_interpolation = ED + Ed
    return (PXI_with_interpolation)

counter = 0
i=-1
beam_irradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
diffuse_irradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)

while i <=7 :
    i=i+1
    if counter == 0:
        latitude_array = beam_irradiance.columns.get_values()
        latitude_array_as_numbers = latitude_array.astype(np.int32, copy=False)
        f=latitude_array_as_numbers[i]
        if (f == latitude_number):
            counter1 =1

if (counter == 1):
    PXI = PXI_calc(latitude,wall_direction)
    print ("PXI value: ") + str(PXI)
    
if (counter == 0):
     PXI = PXI_calc_with_interpolation(latitude,wall_direction)
     print ("PXI value: ") + str(PXI)

#Piacenza:
Piacenza_latitude="45"
PXI_values=[]
j=0
for index in windowsDF.index.tolist():
    print index
    PXI_values = np.append(PXI_values,PXI_calc(Piacenza_latitude,windowsDF["Direction"][index]))
    print PXI_values[j]
    j=j+1
    
windowsDF["PXI"] = PXI_values
windowsDF.to_csv("windows_completed_withPXI.csv",sep=";")
windowsDF.to_html("Window_Completed_withPXI.html")