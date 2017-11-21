import os
import pandas as pd

os.chdir("E:\Master's\First Semester\Buildings\Numpy - Pandas- python class7\RLF Method")
windowsDF=pd.read_csv("windows.csv",sep=";",index_col=0)


windowsBeamIrr=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0,)
windowsDiffIrr=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
lattitudeLoc='45'
windowsDF['PXI']['east']=windowsBeamIrr['45']['E']+windowsDiffIrr['45']['E']
windowsDF.to_csv("windows_completed_withPXI.csv",sep=";")