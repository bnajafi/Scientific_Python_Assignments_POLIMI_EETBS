# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\Lorenzo\Desktop\git_fork_clone\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\Assignment7_Ferre")

beam_irradiance = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
diffuse_irradiance = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0) 

latitude_Piacenza = "45"
beam_irradiance_east = beam_irradiance[latitude_Piacenza]["E"]
diffuse_irradiance_east = diffuse_irradiance[latitude_Piacenza]["E"]

PXI_east = windows_DF["Tx"]["east"]*(beam_irradiance_east+diffuse_irradiance_east)
windows_DF["PXI"]=np.array([PXI_east,0,0,0])

windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
windows_DF.to_html("windows_completedWithPXI.html")