import os
import pandas as pd
import numpy as np
 
os.chdir("C:\Users/Racho/Desktop/Assignment7_Aamrani")
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
windows_DF["Area"] = windows_DF["Height"]*windows_DF["width"]
 

DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)
 

IAC_cl_value= DF_IAC_cl["DrapesLightOpen"]["5c"]
 

index="east"
windowID= windows_DF["Window_ID"][index]
IntShadingID=windows_DF["IntShading_ID"][index]
IAC_cl_value= DF_IAC_cl[IntShadingID][windowID]
windows_DF["IAC_cl"] = np.array([IAC_cl_value,IAC_cl_value,IAC_cl_value,IAC_cl_value])
 
 
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
BeamIrradiance_value = BeamIrradiance_DF["45"]["E"]
DiffuseIrradiance_Value = DiffuseIrradiance_DF["45"]["E"]
 
PXI_E = BeamIrradiance_value + DiffuseIrradiance_Value

windows_DF["PXI"] = np.array([PXI_E,0,0,0])
 
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
BeamIrradiance_value = BeamIrradiance_DF["45"]["W"]
DiffuseIrradiance_Value = DiffuseIrradiance_DF["45"]["W"]
 
PXI_W = BeamIrradiance_value + DiffuseIrradiance_Value

windows_DF["PXI"] = np.array([PXI_E,PXI_W,0,0])
 
windows_DF.to_csv("windows_completed.csv",sep=";")
windows_DF.to_html("windows_completed.html")