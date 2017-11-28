import os
import pandas as pd
import numpy as np
os.chdir ("C:\Users\Karla\OneDrive\SECOND SEMESTER - Sept 17\Buildings\GIT\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")

#Reading the tables
windows_DF = pd.read_csv("windows.csv", sep=";", index_col=0)
beam_DF = pd.read_csv ("BeamIrradiance.csv", sep = ";", index_col = 0)
diffuse_DF = pd.read_csv ("DiffuseIrradiance.csv", sep = ";", index_col = 0)

#Values for Piacenza
latitude_location = 45
Direction = "E"

PXI_PC = beam_DF.loc[Direction,str(latitude_location)]+diffuse_DF.loc[Direction,str(latitude_location)]
windows_DF["PXI"] = np.array([PXI_PC,0,0,0])
windows_DF.to_csv("windows_completed_PXI_Karla.csv", sep =";")


