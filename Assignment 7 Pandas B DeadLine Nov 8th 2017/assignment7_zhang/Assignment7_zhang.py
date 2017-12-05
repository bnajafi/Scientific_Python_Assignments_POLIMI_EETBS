import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\Clevo\Desktop\Assignment7")

beamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col = 0)
diffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col = 0)
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)

beamIrradiance_value = beamIrradiance_DF["45"]["E"]
diffuseIrradiance_value = diffuseIrradiance_DF["45"]["E"]
PXI_value = beamIrradiance_value+diffuseIrradiance_value

windows_DF["PXI"] = np.array([PXI_value,0,0,0])

windows_DF.to_csv("windows_completed_withPXI",sep=";" )