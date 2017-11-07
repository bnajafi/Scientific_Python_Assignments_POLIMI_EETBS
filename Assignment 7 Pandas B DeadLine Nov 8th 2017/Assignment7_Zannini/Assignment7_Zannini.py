import os
os.chdir("/Users/giordanozannini/Desktop/TECHNOLOGIES FOR BUILDING SYSTEMS/RLF Method Panda")
import pandas as pd
import numpy as np

windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
BeamIrradiance_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
latitude_location=45

Ebeam=BeamIrradiance_DF[str(latitude_location)]["E"]
Ediff=DiffuseIrradiance_DF[str(latitude_location)]["E"]

Etot=Ebeam+Ediff
PXI=windows_DF["Tx"]["east"]*Etot
windows_DF["PXI"]["east"]=PXI
windows_DF.to_csv("windows_completedwithPXI.csv",sep=";")