import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\LENOVO\Desktop\__Guidelines__")
location_latitude='45'
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
beam_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffuse_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
windows_DF["PXI"]["east"]=beam_DF[location_latitude]["E"]+diffuse_DF[location_latitude]["E"]
windows_DF.to_csv("windows_east_PXI_completed.csv",sep=";")
