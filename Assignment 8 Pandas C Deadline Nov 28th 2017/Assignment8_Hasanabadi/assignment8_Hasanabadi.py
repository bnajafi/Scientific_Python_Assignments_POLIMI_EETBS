import os
import pandas as pd
import numpy as np
import scipy as sp
os.chdir("C:\Users\LENOVO\Desktop\__Guidelines__")
location_latitude=45
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=1)
beam_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffuse_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
windows=['W','S',"E"]
def PXI(location_latitude,direction):
    nameOfColumns=beam_DF.columns.get_values()
    nameOfColumnsAsNumbers=nameOfColumns.astype(np.int32,copy=False)
    EB=sp.interp(location_latitude,nameOfColumnsAsNumbers,beam_DF.loc[i])
    ED=sp.interp(location_latitude,nameOfColumnsAsNumbers,diffuse_DF.loc[i])
    PXI=EB+ED
    return PXI
for i in windows:
    windows_DF["PXI"][i]=PXI(location_latitude,i)
windows_DF.to_csv("windows_east_PXI_completed.csv",sep=";")




