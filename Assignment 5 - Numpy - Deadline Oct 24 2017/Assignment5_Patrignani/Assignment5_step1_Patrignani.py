# -*- coding: utf-8 -*-
import numpy as np

Resistences = np.array(["Ri1", "Rf", "Rp1", "Rpc1", "Rb", "Rpc2", "Rp2", "Ri2"])    #list of resistances
Res_type = np.array(["conv","cond","cond","cond","cond","cond","cond","conv"])      #types of resistances
Conv_coeff = np.array([10,None,None,None,None,None,None,25])
Cond_coeff = np.array([None, 0.026, 0.22, 0.22, 0.72, 0.22, 0.22,None])
Lenght = np.array([None, 0.03, 0.02, 0.16, 0.16, 0.16, 0.02,None])
Area = np.array([0.25, 0.25, 0.25, 0.015, 0.22, 0.015, 0.25,0.25])

RValues= np.array(np.zeros(8))          # this creates a vector of zeros which has the same length as that of layers_myWall
RValues[Res_type== "conv"] = 1.0/(Conv_coeff[Res_type=="conv"]*Area[Res_type=="conv"])          #calculating convenctive resitances
RValues[Res_type=="cond"] = Lenght[Res_type=="cond"]/(Cond_coeff[Res_type=="cond"]*Area[Res_type=="cond"])      #calculating conductive resistances

RParallel = sum(1/RValues[3:6])         #equivalent resistance in paralallel

Rtot = RValues.sum() - RValues[3:6].sum() + RParallel

T1=20                  #indoor temperature in °C
T2=-10                 #outdoor temperature in °C
Awall=3*5              #area of the wall in m2
A1=0.25*1              #front area of a single unit in m2
Qu=(T1-T2)/Rtot          
Qwall=Qu*(Awall/A1)

print "The total equivalent resistence is " + str(Rtot) + " °C/W"
print "The rate of heat transfer across one unit of the wall is " + str(Qu) + " W"
print "The rate of heat transfer across the whole wall is " + str(Qwall) + " W"