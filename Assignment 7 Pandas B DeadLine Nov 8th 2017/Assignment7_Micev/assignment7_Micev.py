import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\Pc\Desktop\politecnico\Energy and Enviromental Technologies For Building Systems\Assignment7_Micev")
direct_irradiance = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffuse_irradiance = pd.read_csv("DiffuseIrradiance.csv", sep=";",index_col=0)
windows=pd.read_csv("windows.csv",sep=";",index_col=0)
print direct_irradiance.columns
print diffuse_irradiance.columns
print windows.index
latitude="45"
side="E"
PXI=direct_irradiance[latitude][side]+diffuse_irradiance[latitude][side]
windows["PXI"]=np.array([PXI,0,0,0]) 
print windows
windows.to_csv("windows_completedWithIAC.csv",sep=";")
windows.to_html("windows_completedWithIAC.html")