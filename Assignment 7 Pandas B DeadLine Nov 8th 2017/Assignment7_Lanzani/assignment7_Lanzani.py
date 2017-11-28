import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/marco/Desktop/MARCO/POLIMI/BUILDING/DATA")

BI_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DI_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
Latitude="45"

Ed=BI_DF["45"]["E"]
ED=DI_DF["45"]["E"]
PXI=ED+Ed

windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
windows_DF["PXI"]=np.array([PXI,0,0,0])
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")