# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\giugi\Desktop\University\4 anno_MAG\EETBS\Assignments\Assignment7")
BeamIrradiance_ED = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_Ed = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
print BeamIrradiance_ED.columns
print BeamIrradiance_ED.index

latitude_location= 45
BeamIrradiance_ED["45"]["E"]
DiffuseIrradiance_Ed["45"]["E"]

TotalIrradiance_Et= BeamIrradiance_ED["45"]["E"]+DiffuseIrradiance_Ed["45"]["E"]
PXI_value = TotalIrradiance_Et

windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
windows_DF["PXI"] = np.array([PXI_value,0,0,0])

windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
windows_DF.to_html("windows_completed1.html")

