import os
import numpy as np
import pandas as pd

import scipy as sp

os.chdir("C:/Users/ale_v/Documents/Polimi/Behzad/MyNewPandas")

def PXI_window(direction,latitude):
    DF_beamIrr=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    DF_diffIrr=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    name_of_columns_D=DF_beamIrr.columns.get_values()
    name_of_columns_as_numbers_D = name_of_columns_D.astype(np.int32, copy=False)
    ED=sp.interp(latitude,name_of_columns_as_numbers_D,DF_beamIrr.loc[direction])
    name_of_columns_d=DF_diffIrr.columns.get_values()
    name_of_columns_as_numbers_d = name_of_columns_d.astype(np.int32, copy=False)
    Ed=sp.interp(latitude,name_of_columns_as_numbers_d,DF_diffIrr.loc[direction])
    PXI_value=ED+Ed
    return PXI_value
myResult=PXI_window("S",42) #example
    
windows_DataFrame = pd.read_csv("windows.csv", sep=";",index_col=0)

windows_DataFrame.index.tolist()


exI_PXI_values=[]
latitude=45
for index in windows_DataFrame.index.tolist():
    print index
    print "PXI value for this direction is: "+str(PXI_window(windows_DataFrame["Direction"][index],latitude))
    exI_PXI_values = np.append(exI_PXI_values,PXI_window(windows_DataFrame["Direction"][index],latitude))
print "The PXI values updated list is: "+str(exI_PXI_values)
windows_DataFrame["PXI"] = exI_PXI_values

windows_DataFrame.to_csv("windows_completed_withPXI.csv" , sep=";")

        
        
