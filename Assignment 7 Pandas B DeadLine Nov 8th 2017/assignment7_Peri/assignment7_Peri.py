import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\Luca\Desktop\irradiace data")

lat="45"
expo="E"

Diffuse_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
Beam_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
print Diffuse_DF.index
print Diffuse_DF.columns
print Beam_DF.index
print Beam_DF.columns


D_value=Diffuse_DF[lat][expo]
B_value=Beam_DF[lat][expo]

PXI=D_value+B_value

windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)

windows_DF["PXI"]["east"]=PXI

windows_DF.to_csv("windows_completedWithPXI.csv",sep=";")
