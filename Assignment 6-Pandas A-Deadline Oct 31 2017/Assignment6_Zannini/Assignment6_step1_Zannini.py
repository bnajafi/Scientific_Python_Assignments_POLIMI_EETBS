import pandas as pd

R1=["conv","series",10,None,None,0.25,0]   #lists of resistances
R2=["conv","series",25,None,None,0.25,0]
R3=["cond","series",None,0.026,0.03,0.25,0]
R4=["cond","series",None,0.22,0.02,0.25,0]
R5=["cond","parallel",None,0.72,0.16,0.22,0]
R6=["cond","parallel",None,0.22,0.16,0.03,0]
R7=["cond","series",None,0.22,0.02,0.25,0]

Rnames=["insideSurf","outsidedurf","foam layer","plaster layer","brick","plaster layer","plaster layer"] #index
columns=["type1","type2","H","K","L","A","Rvalue"]
resistancesDf=pd.DataFrame([R1,R2,R3,R4,R5,R6,R7],Rnames,columns) #create the matrix
resistancesDf["Rvalue"][resistancesDf["type1"]=="conv"]=1/(resistancesDf["H"][resistancesDf["type1"]=="conv"]*resistancesDf["A"][resistancesDf["type1"]=="conv"])
resistancesDf["Rvalue"][resistancesDf["type1"]=="cond"]=resistancesDf["L"][resistancesDf["type1"]=="cond"]/(resistancesDf["K"][resistancesDf["type1"]=="cond"]*resistancesDf["A"][resistancesDf["type1"]=="cond"])

Rtot=resistancesDf["Rvalue"][resistancesDf["type2"]=="series"].sum()+((1/resistancesDf["Rvalue"][resistancesDf["type2"]=="parallel"]).sum())**-1
print "******** The value of the total resistance is " + str(Rtot) + " K/W ********"
