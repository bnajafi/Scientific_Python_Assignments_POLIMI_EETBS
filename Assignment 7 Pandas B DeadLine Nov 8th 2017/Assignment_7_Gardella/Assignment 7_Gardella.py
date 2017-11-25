import os
import pandas as pd
os.chdir ("C:\Users\Fabio\Documents\Polimi\Magistrale\Buildings\Assignments\Assignment 7 Gardella")

latitude_location = "45"


Beam_irradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)

Diffuse_irradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)



BeamIrrEast=Beam_irradiance_DF[latitude_location]["E"]
DiffuseIrrEast=Diffuse_irradiance_DF[latitude_location]["E"]

PXI_east = BeamIrrEast + DiffuseIrrEast

windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)

windows_DF["PXI"]["east"] = PXI_east

windows_DF.to_csv("windows_completedWithEastPXI.csv",sep=";")



