import os 
import pandas as pd 
import numpy as np
os.chdir("C:/Users/user/Desktop/CAnoPY/Numpy - Pandas/RLF Method")

windows_DF=pd.read_csv("windows_completed1.csv",sep=";",index_col=0)

latitude = "45"

BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=';',index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=';',index_col=0)


BeamIrr_EastPC = BeamIrradiance_DF.loc["E",latitude]
DiffIrr_EastPC = DiffuseIrradiance_DF.loc["E",latitude]

PXI_EastPC = 1*(DiffIrr_EastPC + (1-0)*BeamIrr_EastPC)

windows_DF ["PXI"] = np.array([PXI_EastPC,0,0,0])


windows_DF.to_csv("windows_completed_withPXI.csv", sep=';')




windows_DF.to_csv("windows_completed1.csv",sep=";") #to create a new excel file 
windows_DF.to_html("windows_completed1.html")


windows_IAC_cl = pd.read_csv("IAC_cl.csv",sep=";",index_col=1)
print windows_IAC_cl.columns
print windows_IAC_cl.index.tolist()

IAC_value = windows_IAC_cl["BlindsDark"]["5c"]

ID_intShading_eastWindow = windows_DF["Intshading_ID"]["east"]

ID_window_eastWindow = windows_DF["Window_ID"]["east"]
IAC_value_eastWindow = windows_IAC_cl  [ID_intShading_eastWindow] [ID_window_eastWindow]
windows_DF["IAC_cl"]= np.array([IAC_value_eastWindow ,0,0,0])
