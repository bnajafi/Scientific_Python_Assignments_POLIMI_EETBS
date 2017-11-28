# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/USUARIO/Dropbox/Assignments EETBS 2017-2018 Polimi Piacenza/Assignment 7 In case of issues with GIT Submission/Assignment7_Diaz")


BeamIrradiance_DF=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)

DiffuseIrradiance_DF=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)

latitude_location=45

BeamIrradiance_East=BeamIrradiance_DF.loc["E",str(latitude_location)]
DiffuseIrradiance_East=DiffuseIrradiance_DF.loc["E",str(latitude_location)]

PeakTotalIrradiance_East=DiffuseIrradiance_East+BeamIrradiance_East

Windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0) 

PXIValue_eastWindow=PeakTotalIrradiance_East*Windows_DF["Tx"]["east"]
Windows_DF["PXI"]=np.array([PXIValue_eastWindow,0,0,0])

Windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
