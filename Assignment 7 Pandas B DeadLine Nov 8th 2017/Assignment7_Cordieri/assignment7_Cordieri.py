import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/SilviaAnna/Desktop/scuola/building sistems/RLF Method")
windows_BeamIrradiance=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
location_latitude="45"
windows_DiffuseIrradiance=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
windows_DF["ED"]["east"]=windows_BeamIrradiance[location_latitude]["E"]
windows_DF["ED"]["west"]=windows_BeamIrradiance[location_latitude]["W"]
windows_DF["ED"]["south-Fixed"]=windows_BeamIrradiance[location_latitude]["S"]
windows_DF["ED"]["south-Operable"]=windows_BeamIrradiance[location_latitude]["S"]
windows_DF["Ed"]["east"]=windows_DiffuseIrradiance[location_latitude]["E"]
windows_DF["Ed"]["west"]=windows_DiffuseIrradiance[location_latitude]["W"]
windows_DF["Ed"]["south-Fixed"]=windows_DiffuseIrradiance[location_latitude]["S"]
windows_DF["Ed"]["south-Operable"]=windows_DiffuseIrradiance[location_latitude]["S"]
windows_DF["PXI"]["east"]=windows_DF["ED"]["east"]+windows_DF["Ed"]["east"]
windows_DF["PXI"]["west"]=windows_DF["ED"]["west"]+windows_DF["Ed"]["west"]
windows_DF["PXI"]["south-Fixed"]=windows_DF["ED"]["south-Fixed"]+windows_DF["Ed"]["south-Fixed"]
windows_DF["PXI"]["south-Operable"]=windows_DF["ED"]["south-Operable"]+windows_DF["Ed"]["south-Operable"]
windows_DF.to_csv("windows_completed_withPXI",sep=";")

