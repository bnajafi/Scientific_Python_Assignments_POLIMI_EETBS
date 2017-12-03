import os
os.chdir("/Users/giordanozannini/Desktop/TECHNOLOGIES FOR BUILDING SYSTEMS/RLF Method Panda")
import pandas as pd
import numpy as np
import scipy as sp

windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)
BeamIrr_DataFrame = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DiffuseIrr_DataFrame = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)

def PXI_Finder(latitude,direction): ## latitude must be a numerber not a string
    BeamIrr_DataFrame = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
    DiffuseIrr_DataFrame = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
    name_of_columns=BeamIrr_DataFrame.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    
    Ed=sp.interp(latitude,name_of_columns_as_numbers,DiffuseIrr_DataFrame.loc[direction])
    Eb=sp.interp(latitude,name_of_columns_as_numbers,BeamIrr_DataFrame.loc[direction])
    PXI=Ed+Eb
    return PXI

latitude=45 ##latitude of Piacenza
windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)
windows_DataFrame.index.tolist()

PXI_values=[]
for index in windows_DataFrame.index.tolist():
    print index
    PXI_values = np.append(PXI_values,PXI_Finder(latitude,windows_DataFrame["Direction"][index]))
        
windows_DataFrame["PXI"]=PXI_values

windows_DataFrame.to_html("windows_completed_withPXI.html")