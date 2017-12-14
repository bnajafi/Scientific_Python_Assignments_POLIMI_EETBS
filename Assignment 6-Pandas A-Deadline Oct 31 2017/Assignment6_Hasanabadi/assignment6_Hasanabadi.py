import pandas as pd


#materials
R1=["conv",10,None,None, 0.25 ,0]
R2=["cond",None,0.026,0.03, 0.25 ,0]
R3=["cond",None,0.22,0.02, 0.25 ,0]
R4=["condP",None,0.22,0.16, 0.015 ,0]
R5=["condP",None,0.72,0.16, 0.22 ,0]
R6=["condP",None,0.22,0.16, 0.015 ,0]
R7=["cond",None,0.22,0.02, 0.25 ,0]
R8=["conv",25,None,None, 0.25 ,0]

index=["indoorSurface","foam","sidePlaster1","centerPlaster1","brick","centerPlaster2","sidePlaster2","outdoorSurface"]
columns=["type","h","K","L","A","RValue"]

Table=pd.DataFrame([R1,R2,R3,R4,R5,R6,R7,R8],index=index,columns=columns)

Table["RValue"][Table["type"]=="conv"]=1/(Table["h"][Table["type"]=="conv"]*Table["A"][Table["type"]=="conv"])

Table["RValue"][Table["type"]=="cond"]=Table["L"][Table["type"]=="cond"]/(Table["K"][Table["type"]=="cond"]*Table["A"][Table["type"]=="cond"])

#Series

Table["RValue"][Table["type"]=="condP"]=Table["L"][Table["type"]=="condP"]/(Table["K"][Table["type"]=="condP"]*Table["A"][Table["type"]=="condP"])

RParallel=1/Table["RValue"][Table["type"]=="condP"]
Rtot=Table["RValue"][Table["type"]=="conv"].sum()+Table["RValue"][Table["type"]=="cond"].sum()+1/RParallel.sum()
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print Table
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print ("total Resistance Value is "+str((Rtot)))
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print("total heat transfer through the wall is " +str(round(15/0.25*30/Rtot)) + "W")



