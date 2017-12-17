import os
import pandas as pd
import scipy as sp
import numpy as np
os.chdir("C:\Users\Pc\Desktop\politecnico\Energy and Enviromental Technologies For Building Systems\Assignment8_Micev")
windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)
windows_DataFrame.index
direct_irradiance_DF= pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffuse_irradiance_DF=pd.read_csv("DiffuseIrradiance.csv", sep=";",index_col=0)
latitude=45
side="W"
def BI_value(latitude,side):
    name_of_columns=direct_irradiance_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    direct_irradiance=sp.interp(latitude,name_of_columns_as_numbers,direct_irradiance_DF.loc[side])
    return direct_irradiance

def DI_value(latitude,side):
    name_of_columns=diffuse_irradiance_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    diffuse_irradiance=sp.interp(latitude,name_of_columns_as_numbers,diffuse_irradiance_DF.loc[side])
    return diffuse_irradiance

def PXI_WithoutExternal(latitude,side):
    PXI=BI_value(latitude,side)+DI_value(latitude,side)
    return PXI
PXI_Values=[]
for index in windows_DataFrame.index:
    PXI_Values.append((PXI_WithoutExternal(latitude,windows_DataFrame.loc[index,"Direction"])))
windows_DataFrame["PXI"]=np.array(PXI_Values)
windows_DataFrame.to_csv("windows_CompletedWithPXI.csv",sep=";")



