import os
import pandas as pd
import numpy as np
import scipy as sp
os.chdir("C:/Users/USUARIO/Pictures/RLF Method")

Windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
BeamIrradiance_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

def PXI_finder(Latitude,Direction):
    BeamIrradiance_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    name_of_columns=BeamIrradiance_DF.columns.get_values()
    name_of_columns_as_numbers=name_of_columns.astype(np.int32, copy=False)
    ED_value=sp.interp(Latitude,name_of_columns_as_numbers,BeamIrradiance_DF.loc[Direction])
    DiffuseIrradiance_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    name_of_columns1=DiffuseIrradiance_DF.columns.get_values()
    name_of_columns_as_numbers1=name_of_columns1.astype(np.int32, copy=False)
    Ed_value=sp.interp(Latitude,name_of_columns_as_numbers1,DiffuseIrradiance_DF.loc[Direction])
    Tx_value=Windows_DF["Tx"][index]
    PXI_value=Tx_value*(Ed_value+ED_value)
    
    return PXI_value


PXI_values=[]
Latitude=45   
    
for index in Windows_DF.index.tolist():
    print (index)
    PXI_values=np.append(PXI_values,PXI_finder(Latitude,Windows_DF["Direction"][index]))
print (PXI_values)
Windows_DF["PXI"]=np.array(PXI_values)
Windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")



