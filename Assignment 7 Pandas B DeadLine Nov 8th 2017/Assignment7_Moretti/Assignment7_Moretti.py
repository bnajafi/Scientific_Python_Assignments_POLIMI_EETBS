"""

EETBS 2017/2018 - Assignment 7 - reading and writing on excel files with pandas

Giorgio Moretti (10433550)

"""

import os
import pandas as pd
import numpy as np

os.chdir("D:\Documents\Politecnico\Energy Eng. Master\Buildings (Behzad)\A.Y. 2017-2018\git_forks\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")
 
beamIrradiance_DF = pd.read_csv("beamIrradiance.csv", sep = ";", index_col = 0)
diffuseIrradiance_DF = pd.read_csv("diffuseIrradiance.csv", sep = ";", index_col = 0)

latitude_location = 45

beam_value = beamIrradiance_DF[str(latitude_location)]["E"]
diffuse_value = diffuseIrradiance_DF[str(latitude_location)]["E"]

PXI = beam_value + diffuse_value

windows_DF = pd.read_csv("windows.csv", sep = ";", index_col = 0)

windows_DF["PXI"]["east"] = PXI

windows_DF.to_csv("windows_completed_withPXI.csv", sep = ";")
windows_DF.to_html("windows_completed_withPXI.html")




