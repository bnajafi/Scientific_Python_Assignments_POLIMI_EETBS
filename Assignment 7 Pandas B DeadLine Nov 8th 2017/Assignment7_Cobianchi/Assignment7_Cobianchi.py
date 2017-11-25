import os
import pandas as pd
import numpy as np

os.chdir("C:\Users/riccardo/Desktop/Assignment7_Cobianchi")
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
windows_DF["Area"] = windows_DF["Height"]*windows_DF["width"]

# How to read IAC_cl.csv file
DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)

# How to extract a value:
IAC_cl_value= DF_IAC_cl["DrapesLightOpen"]["5c"]

# or taking the inputs from the windows_DF
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
#print PXI
windows_DF["PXI"] = np.array([PXI_E,0,0,0])

BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
BeamIrradiance_value = BeamIrradiance_DF["45"]["W"]
DiffuseIrradiance_Value = DiffuseIrradiance_DF["45"]["W"]

PXI_W = BeamIrradiance_value + DiffuseIrradiance_Value
#PXI_W
windows_DF["PXI"] = np.array([PXI_E,PXI_W,0,0])

# How to write the modified Table to a new file.
windows_DF.to_csv("windows_completed.csv",sep=";")
windows_DF.to_html("windows_completed.html")

