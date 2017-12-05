# assignment 7 - Riccardi
import os
import numpy as np
import pandas as pd
os.chdir("C:\Users\Luca\Desktop\Luca\PoliMinchia\Primo anno\Energy and environmental technologies\Assignments\Assignment7")
latitude=45
direction="E"
Beam_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
Diff_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
Windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
Windows_DF["PXI"]["east"]=Beam_DF[str(latitude)][direction]+Diff_DF[str(latitude)][direction]
Windows_DF.to_csv("windows_completedwithPXI.csv",sep=";")


