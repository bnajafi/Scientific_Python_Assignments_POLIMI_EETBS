import os 
import pandas as pd
import numpy as np
import scipy as sp 

os.chdir("C:\Users\Akwesi\Documents\GIT\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")

windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv", sep=";",index_col=0)

#Defining Latitude location and Direction
latitude = float(raw_input("please enter Latitute in deg "))

#function defining the Beam Irradiance for the Latitude location and direction choosen...Interpolation
def PXI_NoExternalShading_finder(latitude,direction):
    """this func only Gives the PXI value"""
    name_of_columns=BeamIrradiance_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    BeamIrradiance=sp.interp(latitude,name_of_columns_as_numbers,BeamIrradiance_DF.loc[direction])
    
    name_of_columns=DiffuseIrradiance_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    DiffuseIrradiance=sp.interp(latitude,name_of_columns_as_numbers,DiffuseIrradiance_DF.loc[direction])
    PXI_NoExternalShading=BeamIrradiance+DiffuseIrradiance
    return PXI_NoExternalShading

latitude = 45
	
PXI_NoExternalShading=[]
for index in windows_DF.index:#For all windows
    PXI_NoExternalShading.append((PXI_NoExternalShading_finder(latitude,windows_DF.loc[index]["Direction"])))
    
windows_DF["PXI"]=np.array(PXI_NoExternalShading) #updating the PXI value for East window
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";") #saving the csv file
