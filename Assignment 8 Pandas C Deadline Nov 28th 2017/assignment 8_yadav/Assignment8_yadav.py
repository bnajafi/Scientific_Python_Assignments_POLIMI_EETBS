import os
import numpy as np
import pandas as pd
import scipy as sp
os.chdir("C:/Users/vipinkmr0808/Desktop/assignment 8_yadav")

beam_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffuse_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
latitude=45  #Piacenza city

#Function to return PXI value at particular direction of window for a provided city 
def PXI_finder(latitude,direction_of_Wall):
    name_of_columns_asnumbers_BI=beam_DF.columns.get_values().astype(np.float32, copy=False)
    beam_radiation_value=sp.interp(latitude,name_of_columns_asnumbers_BI,beam_DF.loc[direction_of_Wall])
    name_of_columns_asnumbers_DI=diffuse_DF.columns.get_values().astype(np.float32, copy=False)
    diffuse_radiation_value=sp.interp(latitude,name_of_columns_asnumbers_DI,diffuse_DF.loc[direction_of_Wall])
    return beam_radiation_value+diffuse_radiation_value

PXI_value_list=[]
for index in windows_DF.index:#For all windows
    PXI_value_list.append((PXI_finder(latitude,windows_DF.loc[index]["Direction"])))

windows_DF["PXI"]=np.array(PXI_value_list)
windows_DF.to_csv("windows_completedwithPXI.csv",sep=";")  




