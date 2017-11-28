import os
import pandas as pd
import numpy as np
os.chdir("D:\MIS DOCUMENTOS\Documents\Master Energy Engineering\RLF Method")

latitude_location = "45"
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep = ";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep = ";",index_col=0)
print BeamIrradiance_DF.columns
print DiffuseIrradiance_DF.columns
print BeamIrradiance_DF.index

BeamIrradiance_value = BeamIrradiance_DF[latitude_location]["E"]
DiffuseIrradiance_value = DiffuseIrradiance_DF[latitude_location]["E"]

PXI_value = BeamIrradiance_value+DiffuseIrradiance_value

windows_DF = pd.read_csv("windows.csv",sep = ";")
windows_DF["PXI"] = np.array([PXI_value,0,0,0])

windows_DF.to_csv("windows_completedWithPXI.csv",sep=";")
windows_DF.to_html("windows_completedWithPXI.html")