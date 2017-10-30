# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.4 (Step2) Date: 16/10/2017
#RLF example

#Import functions from outside:
import os
os.chdir("C:\Users\utente\Desktop\Building Systems") 
#Simply renaming my functions as CW:
import wallCalculations_Russano as CW
#Now I define the input lists and the fraction that I use to calculate the U of tha wall:
Layers_in_series = ["gypsumBoard","CommonBrik","WoodFiberboard13mm","WoodBevel"]
Layers_in_parallel = ["WoodStud_90mm","Insulation_Glass_Fiber"]
fraction=float(0.70) 
#I calculate the overall heat transfer coefficient of the wall:
U_wall=CW.wallCalc_withParallel(Layers_in_series,Layers_in_parallel,fraction)
#I calculate the overall heat transfer coefficient of the door:
door_layer=["Wood_50mm"]
U_door=CW.wallCalc_onlyInSeries(door_layer)
#I calculate the overall heat transfer coefficient of the roof:
roof_layer=["gypsumBoard","Insulation_Glass_Fiber","AsphaltRoofing","WoodBevel"]
U_roof=CW.wallCalc_onlyInSeries(roof_layer)

#The temperature are:
T_winter= -4.8
T_inside= 20
dT_heating=T_inside-T_winter #The delta T between inside and outside in winter

#Heating Factor of each component:
HF_wall=U_wall*dT_heating
HF_door=U_door*dT_heating
HF_roof=U_roof*dT_heating

#The areas of wall, doors and roof are:
A_wall= 105.8
A_roof= 200
A_door= 2.2

#And the heat through the three components are:
Q_roof=A_roof*U_roof*dT_heating
Q_door=A_door*U_door*dT_heating
Q_wall=A_wall*U_wall*dT_heating