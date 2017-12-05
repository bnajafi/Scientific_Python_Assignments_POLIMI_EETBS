# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\Utente\Desktop\Ingegneria Magistrale\Building systems\Python lessons\lesson7 (pandas+excel)")

#Excel files reading
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

#Latitude definition
latitude_location = "45"

#Data extraction 
BeamIrradiace_value = BeamIrradiance_DF[latitude_location]["E"]
DiffuseIrradiance_value = DiffuseIrradiance_DF[latitude_location]["E"]

#PXI calculation
PXI_value = BeamIrradiace_value+DiffuseIrradiance_value

#windows.csv updating
windows_DF["PXI"] = np.array([PXI_value,0,0,0])
windows_DF.to_csv("windows_completed_with_PXI.csv",sep=";")
windows_DF.to_html("windows_completed_with_PXI.html")



