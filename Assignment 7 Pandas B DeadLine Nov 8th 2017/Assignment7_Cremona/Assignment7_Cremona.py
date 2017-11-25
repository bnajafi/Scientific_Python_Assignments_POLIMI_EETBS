import os
import numpy as np
import pandas as pd
os.chdir('C:\Users\Cremona\Dropbox\GIT\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\Assignment7_Cremona')
os


latitude_location= '45'
orientation = 'E'

DF_BeamIrradiance = pd.read_csv('BeamIrradiance.csv',sep=';',index_col=0)
DF_BeamIrradiance_value_east = DF_BeamIrradiance[latitude_location][orientation]
DF_DiffuseIrradiance = pd.read_csv('DiffuseIrradiance.csv',sep=';',index_col=0)
DF_DiffuseIrradiance_value_east = DF_DiffuseIrradiance[latitude_location][orientation]
windows_DF = pd.read_csv('windows.csv',sep=';',index_col=0)
windows_DF['ED'] = np.array([DF_BeamIrradiance_value_east,0,0,0])
windows_DF['Ed'] = np.array([DF_DiffuseIrradiance_value_east,0,0,0])
Tx = windows_DF['Tx']['east']
PXI_value_east = Tx*(DF_BeamIrradiance_value_east+DF_DiffuseIrradiance_value_east)
windows_DF['PXI'] = np.array([PXI_value_east,0,0,0])
windows_DF.to_csv('windows_completed_withPXI.csv',sep=';')
