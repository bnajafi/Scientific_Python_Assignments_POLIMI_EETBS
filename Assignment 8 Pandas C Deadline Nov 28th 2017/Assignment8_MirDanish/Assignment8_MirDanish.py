import os
import numpy as np
import pandas as pd
import scipy as sp
os.chdir("C:\Users\Danish\Documents\ourNewclone\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 8 Pandas C Deadline Nov 28th 2017\Assignment8_MirDanish")

beam_Irradiance_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffuse_Irradiance_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
windowsTotal_DF=pd.read_csv("windows.csv",sep=";",index_col=0)

# Calculating the PXI values of all the Windows for Piacenza city

latitude=45 
 
def PXI_Calculator(latitude,direction_of_Wall):
    name_of_columns_asnumbers_BI=beam_Irradiance_DF.columns.get_values().astype(np.float32)
    beam_radiation_value=sp.interp(latitude,name_of_columns_asnumbers_BI,beam_Irradiance_DF.loc[direction_of_Wall])
    name_of_columns_asnumbers_DI=diffuse_Irradiance_DF.columns.get_values().astype(np.float32)
    diffuse_radiation_value=sp.interp(latitude,name_of_columns_asnumbers_DI,diffuse_Irradiance_DF.loc[direction_of_Wall])
    return beam_radiation_value+diffuse_radiation_value

PXI_value_list=[]
for index in windowsTotal_DF.index:# Updating the PXI values for all windows in the excel file
    PXI_value_list.append((PXI_Calculator(latitude,windowsTotal_DF.loc[index]["Direction"])))

windowsTotal_DF["PXI"]=np.array(PXI_value_list)
windowsTotal_DF.to_csv("windows_completedwithPXI.csv",sep=";")  