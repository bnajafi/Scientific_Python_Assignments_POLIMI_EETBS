import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/ale_v/Documents/Polimi/git_fork_clone2/AnotherClone/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 7 Pandas B DeadLine Nov 8th 2017/__Guidelines__")
latitude_loc=45
beamIrr_DF = pd.read_csv("beamIrradiance.csv" , sep=";", index_col=0)
diffuseIrr_DF = pd.read_csv("diffuseIrradiance.csv" , sep=";", index_col=0)
beamIrr_DF["45"]["E"]
diffuseIrr_DF["45"]["E"]
PXI_45_E = beamIrr_DF["45"]["E"]+diffuseIrr_DF["45"]["E"]
windows_DF = pd.read_csv("windows.csv", sep=";", index_col=0)
windows_DF["PXI"] = np.array([PXI_45_E,0,0,0])
windows_DF.to_csv("windows_completed_withPXI.csv" , sep=";")
