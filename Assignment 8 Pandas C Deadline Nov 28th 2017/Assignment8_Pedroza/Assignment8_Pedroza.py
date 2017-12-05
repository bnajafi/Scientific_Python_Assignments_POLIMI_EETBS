import os
import pandas as pd
import numpy as np
import scipy as sp
os.chdir ("C:\Users\Karla\OneDrive\SECOND SEMESTER - Sept 17\Buildings\GIT\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 8 Pandas C Deadline Nov 28th 2017\Assignment8_Pedroza")

#Reading the tables
windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)
df_BeamIrradiance = pd.read_csv ("BeamIrradiance.csv", sep = ";", index_col = 0)
diffuse_DF = pd.read_csv ("DiffuseIrradiance.csv", sep = ";", index_col = 0)

#Values for Piacenza



def PXI_cal(Latitude, Direction,Tx):
    name_of_columns=df_BeamIrradiance.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)

    ED=sp.interp(Latitude,name_of_columns_as_numbers,df_BeamIrradiance.loc[Direction])
    Ed = sp.interp(Latitude,name_of_columns_as_numbers,diffuse_DF.loc[Direction])
    PXI_cal = Tx*(Ed + ED)
    return PXI_cal

PXI_values=[]    

for index in windows_DataFrame.index.tolist():
    Latitude = 45
    PXI_values = np.append(PXI_values,PXI_cal(Latitude,windows_DataFrame["Direction"][index], windows_DataFrame["Tx"][index]))

print PXI_values
    
windows_DataFrame["PXI"] =PXI_values
windows_DataFrame.to_csv("windows_completed_PXI_Karla2.csv", sep =";")





