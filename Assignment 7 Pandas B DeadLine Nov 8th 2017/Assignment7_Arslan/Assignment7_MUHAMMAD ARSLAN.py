
import os
import pandas as pd
import numpy as np

os.chdir("C:/Users/arslan/Desktop/Assignment7_Arslan")
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)

windows_beam = pd.read_csv("BeamIrradiance.csv", sep=";",index_col=0)
print windows_beam.columns
print windows_beam.index.tolist()
Beam_East1=windows_beam["45"]["E"]
windows_DF["ED"]["east"]=Beam_East1
windows_DF.to_csv("windows_completed.csv",sep=";")

## to read E_d values
windows_diffuse = pd.read_csv("DiffuseIrradiance.csv", sep=";",index_col=0)
print windows_diffuse.columns
print windows_diffuse.index.tolist()

Diffuse_East2=windows_diffuse["45"]["E"]
windows_DF["Ed"]["east"]=Diffuse_East2
windows_DF.to_csv("windows_completed.csv",sep=";")
print windows_DF

PXI=Diffuse_East2+Beam_East1
windows_DF["PXI"]["east"]=PXI

windows_DF.to_csv("windows_completed.csv",sep=";")
windows_DF.to_html("windows_completed.html")

