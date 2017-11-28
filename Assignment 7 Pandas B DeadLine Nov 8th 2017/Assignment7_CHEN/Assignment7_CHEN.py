#Assignment7_CHEN

import os
import pandas as pd
import numpy as np
os.chdir("/Users/chenrujing/Dropbox/Iris/RLF Method")
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0) 
windows_BI=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0) #direct irradiance
windows_DI=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0) 

latitude_location="45"
East="E"
BeamIrradiance_East=windows_BI[latitude_location][East]
DiffuseIrradiance_East=windows_DI[latitude_location][East]
PXI_East=BeamIrradiance_East+DiffuseIrradiance_East
windows_DF["PXI"]=np.array([PXI_East,0,0,0])

windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
