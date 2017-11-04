import pandas as pd


Y = 3 #y is the height of the wall in m
print "the height of the wall is "+str(Y)+ "m"
X = 5 #X is the width of the wall in m
print "the width of the wall is "+str(X)+ "m"
print " "
print "At first, we're going to calculate the rate of heat transfer through a unit of 0.25m high and 1m deep"
print " "
Tinfinity1 = 20.0 #Tinfinity1 corresponds to then indoor temperature
print "the indoor temperature T infinity1 is "+str(Tinfinity1)+ " degrees"
print " "
Tinfinity2 = -10.0 #Tinfinity2 corresponds to the outer temperature
print "the outer temperature T infinity2 is "+str(Tinfinity2)+ " degrees"
print " "


Rnames = ["inner_convection","foam_layer","vertical_plaster_layer1","upper_horizontal_plaster_layer","brick","lower_horizontal_plaster_layer","vertical_plaster_layer2","outer_convection"]
Rtype = ["conv","cond_ser","cond_ser","cond_par","cond_par","cond_par","cond_ser","conv"]
R_h = [10.0, None , None , None , None , None , None , 25.0]
R_k=  [None, 0.026, 0.22, 0.22, 0.72, 0.22, 0.22, None]
Rlength= [None, 0.03, 0.02, 0.16, 0.16, 0.16, 0.02, None]
Rarea=[0.25, 0.25, 0.25, 0.015, 0.22, 0.015, 0.25, 0.25]
Rvalue=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
Rvalue_inv=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
resistances_ListOfLists  = [Rtype,R_h,R_k,Rlength,Rarea,Rvalue,Rvalue_inv]

resistances_DataFrame = pd.DataFrame(resistances_ListOfLists,index=["type","h","k","L","Rarea","Rvalue","Rvalue_inv"], columns=Rnames)

resistances_DataFrame.loc["Rvalue"][resistances_DataFrame.loc["type"]=="conv"]=1.0/resistances_DataFrame.loc["h"][resistances_DataFrame.loc["type"]=="conv"]
resistances_DataFrame.loc["Rvalue"][resistances_DataFrame.loc["type"]=="cond_ser"]=resistances_DataFrame.loc["L"][resistances_DataFrame.loc["type"]=="cond_ser"]/(resistances_DataFrame.loc["k"][resistances_DataFrame.loc["type"]=="cond_ser"]*resistances_DataFrame.loc["Rarea"][resistances_DataFrame.loc["type"]=="cond_ser"])
resistances_DataFrame.loc["Rvalue"][resistances_DataFrame.loc["type"]=="cond_par"]=resistances_DataFrame.loc["L"][resistances_DataFrame.loc["type"]=="cond_par"]/(resistances_DataFrame.loc["k"][resistances_DataFrame.loc["type"]=="cond_par"]*resistances_DataFrame.loc["Rarea"][resistances_DataFrame.loc["type"]=="cond_par"])


resistances_DataFrame.loc["Rvalue_inv"][resistances_DataFrame.loc["type"]=="cond_par"]= 1/resistances_DataFrame.loc["Rvalue"][resistances_DataFrame.loc["type"]=="cond_par"]
Rcondpara = 1/resistances_DataFrame.loc["Rvalue_inv"][resistances_DataFrame.loc["type"]=="cond_par"].sum()

Rcondser = resistances_DataFrame.loc["Rvalue"][resistances_DataFrame.loc["type"]=="cond_ser"].sum()
Rconv = resistances_DataFrame.loc["Rvalue"][resistances_DataFrame.loc["type"]=="conv"].sum()

Rtot = Rcondser + Rcondpara + Rconv


print "Then, The total thermal resistance of the medium is "+str(Rtot)+ " degrees/W"
print " "


Q= (Tinfinity1-Tinfinity2)/Rtot 
print "This implies that the steady rate of heat transfer through the 0.25 m2 surface area is "+str(Q)+ " W"
print " "
Aw= 3*5 #Aw is the total area of the wall
Aunit= 0.25
Qtot= Q*Aw/Aunit
print "Hence, the rate of heat trasnfer through the entire wall becomes "+str(Qtot)+ " W"