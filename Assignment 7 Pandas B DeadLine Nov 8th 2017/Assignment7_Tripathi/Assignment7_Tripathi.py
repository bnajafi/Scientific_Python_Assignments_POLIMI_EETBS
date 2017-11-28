import os
import pandas as pd

os.chdir("C:/Users/hp/Desktop/Assignment7_Tripathi")
windowsDF=pd.read_csv("windows.csv",sep=";",index_col=0)

windows_beam = pd.read_csv("BeamIrradiance.csv", sep=";",index_col=0)
print windows_beam.columns
print windows_beam.index.tolist()
Beam_East1=windows_beam["45"]["E"]
windowsDF["ED"]["east"]=Beam_East1
windowsDF.to_csv("windows_completed.csv",sep=";")

windows_diffuse = pd.read_csv("DiffuseIrradiance.csv", sep=";",index_col=0)
print windows_diffuse.columns
print windows_diffuse.index.tolist()
Diffuse_East2=windows_diffuse["45"]["E"]
windowsDF["Ed"]["east"]=Diffuse_East2
windowsDF.to_csv("windows_completed.csv",sep=";")

PXI=Diffuse_East2+Beam_East1

windowsDF['PXI']['east']=PXI
windowsDF.to_csv("windows_completed_withPXI.csv",sep=";")
windowsDF.to_html("windows_completed_withPXI.html")