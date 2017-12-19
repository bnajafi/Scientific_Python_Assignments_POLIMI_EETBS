# -*- coding: utf-8 -*-
import pandas as pd

#defining each resitance

Ri1= ["conv", "series",   10,   None,  None, 0.25,  0]
Rf=  ["cond", "series",   None, 0.026, 0.03, 0.25,  0]
Rp1= ["cond", "series",   None, 0.22,  0.02, 0.25,  0]
Rpc1=["cond", "parallel", None, 0.22,  0.16, 0.015, 0]
Rb=  ["cond", "parallel", None, 0.72,  0.16, 0.22,  0]
Rpc2=["cond", "parallel", None, 0.22,  0.16, 0.015, 0]
Rp2= ["cond", "series",   None, 0.22,  0.02, 0.25,  0]
Ri2= ["conv", "series",   25.0, None,  None, 0.25,  0]

resistances = ["Ri1", "Rf", "Rp1", "Rpc1", "Rb", "Rpc2", "Rp2", "Ri2"]              #defining the names of the index (rows)
columns = ["type", "position", "h", "k","L", "A","ResValue"]                             #defining the names for the columns
ResistencesMatrix = pd.DataFrame([Ri1, Rf, Rp1, Rpc1, Rb, Rpc2, Rp2, Ri2], index=resistances, columns=columns)  #defining the resistances matrix

#ResistencesMatrix["k"][ResistencesMatrix["type"]=="cond"]  takes only conductive resistences and gives us the value of k

ResistencesMatrix["ResValue"][ResistencesMatrix["type"]=="cond"] = ResistencesMatrix["L"][ResistencesMatrix["type"]=="cond"]/ResistencesMatrix["k"][ResistencesMatrix["type"]=="cond"]/ResistencesMatrix["A"][ResistencesMatrix["type"]=="cond"] #calculating R_conductive as L/(k*A)
ResistencesMatrix["ResValue"][ResistencesMatrix["type"]=="conv"] = 1.0/ResistencesMatrix["h"][ResistencesMatrix["type"]=="conv"]/ResistencesMatrix["A"][ResistencesMatrix["type"]=="conv"]    #calculating R_convective as 1/(h*A)

Rparallel=sum(1.0/ResistencesMatrix["ResValue"][ResistencesMatrix["position"]=="parallel"])  #calculating equivalent resitance in parallel as sum of 1/Ri

Rtot = ResistencesMatrix["ResValue"][ResistencesMatrix["position"]=="series"].sum() + Rparallel  #calculating Rtot as the sum of resistances in series + the equivalence resistaces in parallel

A1=0.25*1              #front area of a single unit in m2
T1=20                  #indoor temperature in °C
T2=-10                 #outdoor temperature in °C
Awall=3*5              #area of the wall in m2
Qu=(T1-T2)/Rtot          
Qwall=Qu*(Awall/A1)

print "The total equivalent resistence is " + str(Rtot) + " °C/W"
print "The rate of heat transfer across one unit of the wall is " + str(Qu) + " W"
print "The rate of heat transfer across the whole wall is " + str(Qwall) + " W"