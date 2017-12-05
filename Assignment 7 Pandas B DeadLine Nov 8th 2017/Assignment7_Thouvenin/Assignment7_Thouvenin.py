# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 12:12:58 2017

@author: edoua
"""

import os
import pandas as pd
import numpy as np

os.chdir("C:\Users\edoua\Dropbox\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\Assignment7_Thouvenin")

windows_DF = pd.read_csv("windows_completed1.csv",sep=';',index_col=0)

BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=';',index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=';',index_col=0)

latitude = "45"
Tx = 1
Fshd = 0

BeamIrr_EastPC = BeamIrradiance_DF.loc["E",latitude]
DiffIrr_EastPC = DiffuseIrradiance_DF.loc["E",latitude]

PXI_EastPC = Tx*(DiffIrr_EastPC + (1-Fshd)*BeamIrr_EastPC)

windows_DF ["PXI"] = np.array([PXI_EastPC,0,0,0])

windows_DF.to_csv("windows_completed_withPXI.csv", sep=';')




