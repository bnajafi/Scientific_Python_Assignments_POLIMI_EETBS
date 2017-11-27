import os
import numpy as np
import pandas as pd

import scipy as sc

windowsdf=pd.read.csv("windows.csv",sep=";",index_col=1)
iaccldf= pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)

def iaccl_finder(windowID,IntShadingID):
    iaccldf= pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)
    iacclvalue= iaccldf[IntShadingID][windowID]
    return iacclvalue
    
iac_val_vector=[]
for index in windowsdf.index.tolist():
    print index
    IAC_values = np.append(iacclvalue,iaccl_finder(windowsdf["Window_ID"][index],windowsdf["IntShading_ID"][index]))
     
Latitude=42
name_of_columns=df_BeamIrradiance.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)

ED=sp.interp(Latitude,name_of_columns_as_numbers,df_BeamIrradiance.loc["S"]) 