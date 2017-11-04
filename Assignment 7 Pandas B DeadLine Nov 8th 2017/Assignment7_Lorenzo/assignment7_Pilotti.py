# Assignment 7

import os

import numpy as np

import pandas as pd

os.chdir("C:/Users/Lorenzo/Dropbox_Polimi_PC/Dropbox/EETBS 2017-2018 POLIMI-PIACENZA/3 Python Files and Guidelines/Numpy - Pandas/RLF Method")


windows_DF=pd.read_csv("windows.csv", sep=";", index_col=0)


# looking for SLF east window value
windows_SLF=pd.read_csv("SLF.csv", sep=";", index_col=0)
latitude="45"
exposure="E"
SLF_eastWindow_value=windows_SLF[latitude][exposure]
windows_DF["SLF"]=np.array([SLF_eastWindow_value, 0, 0, 0])

# Permanent Shading (shaded fraction) of east window
index="east"
Fshd_eastWindow_value=(SLF_eastWindow_value*windows_DF["Doh"][index]-windows_DF["Xoh"][index])/windows_DF["Height"][index]
windows_DF["Fshd"]=np.array([Fshd_eastWindow_value, 0, 0,0])

# looking for Beam and Diffuse Irradiance
windows_BeamIrradiance=pd.read_csv("BeamIrradiance.csv", sep=";", index_col=0)
windows_DiffuseIrradiance=pd.read_csv("DiffuseIrradiance.csv", sep=";", index_col=0)
BeamIrradiance_eastWindow=windows_BeamIrradiance[latitude][exposure]
DiffuseIrradiance_eastWindow=windows_DiffuseIrradiance[latitude][exposure]

# PXI (Peak Exterior Irradiance)   
PXI_eastWindow_value=windows_DF["Tx"][index]*(DiffuseIrradiance_eastWindow+(1-windows_DF["Fshd"][index])*BeamIrradiance_eastWindow)
windows_DF["PXI"]=np.array([PXI_eastWindow_value, 0, 0, 0])

# Updating windows table and saving 

os.chdir("C:/Users/Lorenzo/Desktop/Polimi PC/Python Files")
windows_DF.to_csv("windowsPXI_updated.csv", sep=";")

