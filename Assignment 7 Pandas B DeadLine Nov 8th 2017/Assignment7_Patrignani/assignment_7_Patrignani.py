import os 
import numpy as np
import pandas as pd
os.chdir("C:/Users/stefy/Desktop/POLIMI/I ANNO/1 Semestre/Buildings/LESSON 7 RLF Method")

latitude_location = 45
direction = "E"

#reading from tables
beamIrradiance_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
diffuseIrradiance_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)

#reading the precise value from the matrix 
beamIrradiance_value = beamIrradiance_DF["45"]["E"]
diffuseIrradiance_value = diffuseIrradiance_DF["45"]["E"]

#calculating PXI
PXI = beamIrradiance_value + diffuseIrradiance_value

#modifing the table windows with the new vector containing the new value of PXI 
windows_DF["PXI"] = np.array([PXI,0,0,0])

#writing new modified tables 
windows_DF.to_csv("windows_completedWithPXI.csv",sep=";")
windows_DF.to_html("windows_completedWithPXI.html")