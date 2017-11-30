import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/vipinkmr0808/Desktop/BS")
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)## seprator is ; index_col=0  to take column 1 as 0 index
print windows_DF.columns 
print windows_DF.index
windows_DF["Height"]*windows_DF["width"]
Area_values= windows_DF["Height"]*windows_DF["width"]
windows_DF["Area"]= windows_DF["Height"]*windows_DF["width"]
windows_DF.to_csv("windows_completed.csv",sep=";")
windows_DF.to_html("windows_completed.html")

## to read another file
windows_IAC_cl = pd.read_csv("IAC_cl.csv", sep=";",index_col=1)
print windows_IAC_cl.columns
print windows_IAC_cl.index.tolist()
IAC_cl_value=windows_IAC_cl["DrapesLightOpen"]["5c"]
windows_DF["IAC_cl"]=IAC_cl_value
windows_DF.to_csv("windows_completed.csv",sep=";")

 ## inserting ICL values
IAC_value=1+0.4*(IAC_cl_value-1)
windows_DF["IAC"]=IAC_value
windows_DF.to_csv("windows_completed.csv",sep=";")

## to read E_D values
windows_beam = pd.read_csv("BeamIrradiance.csv", sep=";",index_col=0)
print windows_beam.columns
print windows_beam.index.tolist()
Beam_East1=windows_beam["45"]["E"]
windows_DF["ED"]["east"]=Beam_East1
windows_DF.to_csv("windows_completed.csv",sep=";")

## to read E_d values
windows_diffuse = pd.read_csv("DiffuseIrradiance.csv", sep=";",index_col=0)
print windows_diffuse.columns
print windows_diffuse.index.tolist()

Diffuse_East2=windows_diffuse["45"]["E"]
windows_DF["Ed"]["east"]=Diffuse_East2
windows_DF.to_csv("windows_completed.csv",sep=";")
print windows_DF

## to calculate PXI
PXI=Diffuse_East2+Beam_East1
windows_DF["PXI"]["east"]=PXI

windows_DF.to_csv("windows_completed.csv",sep=";")
windows_DF.to_html("windows_completed.html")

















