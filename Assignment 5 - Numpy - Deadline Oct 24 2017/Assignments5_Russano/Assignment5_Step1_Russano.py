# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.5 (Step1) Date: 23/10/2017
#One dimensional problem:
#Example D: Heat loss through a composite wall
#Solution by Numpy:
import numpy as np
#I define a list with the name of resistances:
Resistance_names= np.array(["Inside surface","OutsideSurface","Foam layer","Brick","Plaster_layer","Plaster_layer"])
#The type of resistance (Conductive or Convective):
Resistance_type1=np.array(["conv","conv","cond","cond","cond","cond","cond"])
#The type of resistance (In series or in parallel):
Resistance_type2=np.array(["series","series","series","series","parallel","parallel","series"])
#Array with convective coefficient:
Resistance_h=np.array([10,25,None,None,None,None,None])
#Array with conductive coefficient:
Resistance_K=np.array([None,None,0.026,0.22,0.72,0.22,0.22])
#Array with lengths:
Resistance_L=np.array([None,None,0.03,0.02,0.16,0.16,0.02])
#Array with areas:
Resistance_A=np.array([0.25,0.25,0.25,0.25,0.22,0.03,0.25])
#I define the temperatures:
T_in=20.0
T_out=-10.0
#I define an empty vector, and after i put the value of the resistances:
Resistance_RValues= np.array(np.zeros(7))
#I calculate the values of conductive resistances:
Resistance_RValues[Resistance_type1=="cond"] = Resistance_L[Resistance_type1=="cond"]/ (Resistance_K[Resistance_type1=="cond"]*Resistance_A[Resistance_type1=="cond"])
#I calculate the values of convective resistances:
Resistance_RValues[Resistance_type1=="conv"] = 1.0 /( Resistance_h[Resistance_type1=="conv"]*Resistance_A[Resistance_type1=="conv"])
#I calculate the total resistance of the wall:
Resistance_Rtot=Resistance_RValues[Resistance_type2=="series"].sum()+((1.0/(Resistance_RValues[Resistance_type2=="parallel"])).sum())**-1
print "The total resistance is:" +str(Resistance_Rtot)
#I calculate the heat flux in the unit:
Q_t=(T_in-T_out)/Resistance_Rtot
print "The heat flux in the unit is " +str(Q_t)+ "W"










