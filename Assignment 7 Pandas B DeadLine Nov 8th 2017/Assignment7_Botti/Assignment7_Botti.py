import os
import pandas as pd
os.chdir("C:\Users\Giulia\Desktop\Assignment7_Botti")

Latitude_Location = "45"

BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)

BeamIrradianceEast = BeamIrradiance_DF[Latitude_Location]["E"]
DiffuseIrradianceEast = DiffuseIrradiance_DF[Latitude_Location]["E"]

PXI_East = BeamIrradianceEast+DiffuseIrradianceEast

windows_DF["PXI"]["east"] = PXI_East

windows_DF.to_csv("Windows_Completed_withPXI.csv",sep=";")