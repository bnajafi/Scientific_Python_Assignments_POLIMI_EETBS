import os
import numpy as np
import pandas as pd

import scipy as sp
os.chdir("C:\Users\Luca\Desktop\irradiace data")


def PXI_finder (Direction,Latitude):
    beam_irr_df=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    Diffuse_irr_df=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    
    col_name=beam_irr_df.columns.get_values()
    col_name_N=col_name.astype(np.int32,copy=False)
    
    ED=sp.interp(Latitude,col_name_N,beam_irr_df.loc[Direction])
    Ed=sp.interp(Latitude,col_name_N,Diffuse_irr_df.loc[Direction])
    
    PXI=ED+Ed
    return PXI
    
win_df=pd.read_csv("windows.csv",sep=";",index_col=0)
Latitude=45

Pxi_val=[]
for i in win_df.index.tolist():
    print i 
    Pxi_val=np.append(Pxi_val,PXI_finder(win_df["Direction"][i],Latitude))
    
win_df["PXI"]=Pxi_val*win_df["Tx"]
win_df.to_csv("windows_completed_with_pxi.csv",sep=";")