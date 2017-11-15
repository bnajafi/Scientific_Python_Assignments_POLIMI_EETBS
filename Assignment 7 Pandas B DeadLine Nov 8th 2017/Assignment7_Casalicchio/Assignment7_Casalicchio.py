import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\Valeria\Desktop\Assignement")

WindowsBeamIrradiance=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
Windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
location_latitude="45"
WindowsDiffuseIrradiance=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

Windows_DF["ED"]["east"]=WindowsBeamIrradiance[location_latitude]["E"]

Windows_DF["Ed"]["east"]=WindowsDiffuseIrradiance[location_latitude]["E"]

Windows_DF["PXI"]["east"]=Windows_DF["ED"]["east"]+Windows_DF["Ed"]["east"]

Windows_DF.to_csv("Windows_completed_withPXI",sep=";")