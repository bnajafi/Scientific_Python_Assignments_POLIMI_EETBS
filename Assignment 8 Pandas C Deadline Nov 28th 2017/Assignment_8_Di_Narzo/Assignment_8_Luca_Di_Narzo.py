import os
import numpy as np
import pandas as pd
import scipy as sp

os.chdir('C:\Users\Utente\Desktop\Building\RLF Method')


Beam_irr=pd.read_csv('BeamIrradiance.csv',sep=';',index_col=0)
Diffuse_irr=pd.read_csv('DiffuseIrradiance.csv',sep=';',index_col=0)
windows_DF = pd.read_csv("windows_completed1.csv",sep=";",index_col=0)

name_of_columns=Beam_irr.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
name_of_columns=Diffuse_irr.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)


def Et_function(latitude,Direction):
    ED=sp.interp(latitude,name_of_columns_as_numbers,Beam_irr.loc[Direction])
    DI=sp.interp(latitude,name_of_columns_as_numbers,Diffuse_irr.loc[Direction])
    Et=(ED+DI)
    return Et   

latitude=45
Et_values=[]
for index in windows_DF.index.tolist():
    print index
    Et_values= np.append(Et_values,Et_function([latitude],windows_DF['Direction'][index]))
   

PXI=Et_values*windows_DF['Tx']
windows_DF['PXI']=PXI
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")