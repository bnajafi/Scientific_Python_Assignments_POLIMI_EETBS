# For Conductive Resistance in Series

Rf = [0.03,0.25,0.026] #Length = 0.03, Area = 0.25, k = 0.026
Rvp = [0.02,0.25,0.22] #Length = 0.02, Area = 0.25, k = 0.22
Rhp = [0.02,0.25,0.22] #Length = 0.02, Area = 0.25, k = 0.22

Total_R1 = 0

List1 = [Rf,Rvp,Rhp]

for Rser in List1:
    L_Rser = Rser[0]
    A_Rser = Rser[1]
    k_Rser = Rser[2]
    
    Rser = L_Rser/(A_Rser*k_Rser)
    
    Total_Rcdser=Total_R1+Rser
    
print "Total resist. of conductive series = " + str( Total_Rcdser) + "DegC/W"
    

#For Conductive Resistance in Parallel
 
Rhp1 = [0.015,0.16,0.22] # Area = 0.015, Length = 0.16, k = 0.22
Rbr = [0.22,0.16,0.72] # Area = 0.22, Length = 0.16, k = 0.72
Rhp2 = [0.015,0.16,0.22] # Area = 0.015, Length = 0.16, k = 0.22
 
List2 = [Rhp1,Rbr,Rhp2]
 
Total_R2 = 0
 
for Rpara in List2:
    A_Rpara = Rpara[0]
    L_Rpara = Rpara[1]
    k_Rpara = Rpara[2]
     
    Rpara = 1/(L_Rpara / (A_Rpara*k_Rpara) )
     
    Total_Rcdpara=1/(Total_R2+Rpara)
     
print "Total Resist. of Conductive Parallel = " + str(Total_Rcdpara) + " (degC/W)" 
    

# Convective Resistance in Series

Ri = [0.25,10] # Area = 0.25, Hin = 10
Ro = [0.25,25] # Area = 0.25, Hout= 25
 
List3 = [Ri,Ro]
 
Total_R3 = 0
 
for Rcvser in List3:
    A_Rcvser = Rcvser[0]
    H_Rcvser = Rcvser[1]
     
    Rcvser = 1/(A_Rcvser*H_Rcvser)
     
    Total_Rcvser=Total_R3+Rcvser
    
print " Total Resist. of Convective Series = " + str(Total_Rcvser) + " (degC/W)"

#Total Resistance

R_tot = Total_Rcdser+Total_Rcdpara+Total_Rcvser
 
print "Total Resist. = " + str(R_tot) + " (degC/W)"
  
  #TEMP.
Tin = 20  #Indoor Temp.
Tout = -10  #outdoor Temp.
dT= Tin - Tout

#The Heat Transfer 
Q_tot=dT/R_tot
print "The rate of Heat trans.= "+str(Q_tot)+"(W)"