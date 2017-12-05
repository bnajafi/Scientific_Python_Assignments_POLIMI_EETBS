import os
import numpy as np
import pandas as pd

import scipy as sp
os.chdir("C:\Users\Lavinia\Desktop\irradiance")

def PXI_find (Direction,latitude):
    beam_irradiance=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    diffuse_irradiance=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    
    coluname=beam_irradiance.columns.get_values()
    colunamenum=coluname.astype(np.int32,copy=False)
    
    ED=sp.interp(latitude,colunamenum,beam_irradiance.loc[Direction])
    Ed=sp.interp(latitude,colunamenum,diffuse_irradiance.loc[Direction])
    
    PXI=ED+Ed
    return PXI
    
windows=pd.read_csv("windows.csv",sep=";",index_col=0)
latitude=45

PXI_values=[]
for i in windows.index.tolist():
    print i
    PXI_values=np.append(PXI_values,PXI_find(windows["Direction"][i],latitude))
    
windows["PXI"]=PXI_values*windows["Tx"]
windows.to_csv("windows_completed_with_pxi.csv",sep=";")

    