import os
import numpy as np
import pandas as pd
import scipy as sp

os.chdir('E:\POLIMI\MAGISTRALE\_Energy for building')

def PXI_finder(latitude,orientation):
    windows_DF = pd.read_csv('windows.csv',sep=';',index_col=0)
    DF_BeamIrr = pd.read_csv('BeamIrradiance.csv',sep=';',index_col=0)
    DF_DiffuseIrr = pd.read_csv('DiffuseIrradiance.csv',sep=';',index_col=0)
    name_of_columns = DF_BeamIrr.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED_value = sp.interp(latitude,name_of_columns_as_numbers,DF_BeamIrr.loc[orientation])
    name_of_columns = DF_DiffuseIrr.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed_value = sp.interp(latitude,name_of_columns_as_numbers,DF_DiffuseIrr.loc[orientation])
    PXI = Tx*(ED_value+Ed_value)
    return PXI
    
latitude = 45
PXI_values = []
windows_DF = pd.read_csv('windows.csv',sep=';',index_col=0)


for j in windows_DF.index.tolist():
    Tx = windows_DF['Tx'][j]
    PXI_values = np.append(PXI_values,PXI_finder(latitude,windows_DF['Direction'][j]))
    
windows_DF['PXI'] = PXI_values
windows_DF.to_csv('windows_completed_withPXI.csv',sep=';')
    

