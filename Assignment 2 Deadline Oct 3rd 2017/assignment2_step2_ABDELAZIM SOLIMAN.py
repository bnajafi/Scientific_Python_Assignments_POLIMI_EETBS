# For Conductive Resistance in Series

Rf = {"name":"Foam","area":0.25,"length":0.03,"k":0.026,"ResValue":0}
Rvp = {"name":"Vertical Plaster","area":0.25,"length":0.02,"k":0.22,"ResValue":0}
Rhp =  {"name":"Horizontal Plaster","area":0.25,"length":0.02,"k":0.22,"ResValue":0}



List1 = [Rf,Rvp,Rhp]

for Rser in List1:
    L_Rser = Rser["length"]
    A_Rser = Rser["area"]
    k_Rser = Rser["k"]
    Name_Rser = Rser["name"]
    
    Rcdser = L_Rser/(A_Rser*k_Rser)
    Rser["ResValue"]=Rcdser 
    
    
print "The calculated Resist. of " + Name_Rser + " = " + str(Rcdser)+ " (degC/W)"
    
print "Total resist. of conductive series = " + str( Rcdser) + "DegC/W"
    

#For Conductive Resistance in Parallel
 
Rhp1 = {"name":"horizontal Plaster 1","area":0.015,"length":0.16,"k":0.22,"ResValue1":0}
Rbr = {"name":"Brick","area":0.22,"length":0.16,"k":0.72,"ResValue1":0}
Rhp2 = {"name":"horizontal Plaster 2","area":0.015,"length":0.16,"k":0.22,"ResValue1":0}
 
List2 = [Rhp1,Rbr,Rhp2]


for Rpara in List2:
    A_Rpara = Rpara["length"]
    L_Rpara = Rpara["area"]
    k_Rpara = Rpara["k"]
    Name_Rpara = Rpara["name"]
     
    Rpara = 1/(L_Rpara / (A_Rpara*k_Rpara) )
     
    Rcdpara=1/(Rpara)
    
print "The calculated Resistance of " + Name_Rpara + " = " + str(Rcdpara) + " (degC/W)"
     
print "Total Resist. of Conductive Parallel = " + str(Rcdpara) + " (degC/W)" 
    

# Convective Resistance in Series

Ri = {"name":"Inner Side","area":0.25,"H":10,"ResValue2":0}
Ro = {"name":"Outer Side","area":0.25,"H":25,"ResValue2":0}
 
List3 = [Ri,Ro]
 

 
for Rcvser in List3:
    A_Rcvser = Rcvser["area"]
    H_Rcvser = Rcvser["H"]
    Name_Rcvser = Rcvser["name"]
    
    Rcvserv = 1/(A_Rcvser*H_Rcvser)
    
    Rcvser["ResValue2"]= Rcvserv
     
print "The calculated Resist of =" + Name_Rcvser + " = " + str(Rcvserv) + " (degC/W)"

print " Total Resist. of Convective Series = " + str(Rcvserv) + " (degC/W)"

# Total Resistance

R_tot = Rcdser+Rcdpara+Rcvserv
 
print "Total Resist. = " + str(R_tot) + " (degC/W)"
  
  #TEMP.
Tin = 20  #Indoor Temp.
Tout = -10  #outdoor Temp.
dT= Tin - Tout

#The Heat Transfer 
Q_tot=dT/R_tot
print "The rate of Heat trans.= "+str(Q_tot)+"(W)"