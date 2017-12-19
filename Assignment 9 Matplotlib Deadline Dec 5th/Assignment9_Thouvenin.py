# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 12:37:09 2017

@author: edoua
"""

import pandas as pd
import matplotlib.pyplot as mplt
 
labels= ["walls","ceiling","door"]
cols = ["r","g","b"]
Qheating = [1149.2,1240,92.5]
Qcooling = [547.5,514.6,43]

#Pie chart of the heating load values
 
mplt.pie (Qheating, labels = labels, colors=cols, startangle=90, explode=(0.1,0.1,0.1), autopct='%1.1f%%')
mplt.title ("Qheating sharing loads for opaque surfaces")

#Pie chart of the cooling load values

figure = mplt.figure()
mplt.pie(Qcooling, labels = labels, colors = cols, startangle=90, explode=(0.1,0.1,0.1), autopct='%1.1f%%')
mplt.title("Qcooling sharing loads for opaque surfaces")

#2D plot of the heating load of the opaque surfaces in function of the U value of the external wall

def Qopaque_heating_calculation (Qheating_serie):
    Qopaque_heating = Qheating_serie + Qheating[1] + Qheating [2]
    return Qopaque_heating

A = 105.8
deltaT = 24.8
U_serie = pd.Series(range(0,10,1))
Qheating_serie = U_serie * A * deltaT
Qopaque_heating = Qheating_serie.apply(Qopaque_heating_calculation)

figure2 = mplt.figure()
mplt.plot(U_serie,Qopaque_heating)
mplt.xlabel("U value of external wall")
mplt.ylabel("Overall opaque heating load")
mplt.title("Effect of U-Value(External wall) on Opaque Heating Load")

