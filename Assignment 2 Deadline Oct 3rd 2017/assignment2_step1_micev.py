#Assignment 2 - Step 1

#Rate of transfer heat through composite wall (values are taken from Example D) 

#dimenssions of wall that is considered
Height_of_wall=3 #height of wall in [m]
Width_of_wall=5 #width of wall in [m] 

#Convective Resistances 
Ri=[10,0.25] #Inner Convective Resistance: heat transfer coefficient [W/m^2 degree C], unit area [m^2]
Rout=[25,0.25] #Outside Convective Resistance: heat transfer coefficient[W/m^2*degree C], unit area [m^2]

#Series Conductive Resistances 
Rfoam=[3,0.25,0.026] #Conductive Resistance of Foam: thickness of foam layer [cm], unit area [m^2], thermal conductivity of foam [W/m*degree C]
Rpside1=[2,0.25,0.22] #Conductive Resistance of side Plastic layer: thickness of plastic layer [cm],unit area [m^2], thermal conductivity of plastic [W/m*degree C]
Rpside2=[2,0.25,0.22] #Conductive Resistance of side Plastic layer: thickness of plastic layer [cm],unit area [m^2], thermal conductivity of plastic [W/m*degree C]

#Parallel Conductive Resistances 
Rbrick=[16,0.22,0.72] #Conductive Resistance of Brick: depth of brick [cm], unit area [m^2], thermal conductivity of brick [W/m*degree C]
Rpcenter1=[16,0.015,0.22] #Conductive Resistance of Plastic layer over brick: thickness of plastic layer [cm],unit area [m^2], thermal conductivity of plastic [W/m*degree C]
Rpcenter2=[16,0.015,0.22] #Conductive Resistance of Plastic layer under brick: thickness of plastic layer [cm],unit area [m^2], thermal conductivity of plastic [W/m*degree C]
 
#temperatures
T1=20 #indoor temperature in [degree C]  
T2=-10 #outdoor temperature in [degree C] 

#List of Resistances 
Rconv=[Ri,Rout] #List of convective resistances
Rcdseries=[Rfoam,Rpside1,Rpside2] #List of series conductive resistances 
Rcdpar=[Rbrick,Rpcenter1,Rpcenter2] #List of parallel conductive resistances

#Calculating Resistances 
sum_convective=0
counter=0
print " Calculating convective resistances: "
print " "
for R in Rconv:
    h_R=R[0]
    A_R=R[1]
    Res=1/(h_R*A_R)
    counter=counter+1
    print "Convective resistance number "+str(counter)+" is equal to "+str(Res)+" W/degree C"
    print " "
    sum_convective=sum_convective+Res
print " Total convective resistance is "+str(sum_convective)+" W/degree C"
print "**************************************"
print " "

sum_conductive=0
counter=0
print " Calculating conductive resistances : "
print " "
for R in Rcdseries:
    L_R=R[0]
    k_R=R[1]
    A_R=R[2]
    Res=L_R/(100*k_R*A_R)
    counter=counter+1
    print "Conductive resistance number "+str(counter)+" is equal to "+str(Res)+" W/degree C" 
    print " "
    sum_conductive=sum_conductive+Res
print " Total series conductive resistance is "+str(sum_conductive)+" W/degree C"
print "**************************************"
print " " 
    
sum_cond_paralel=0
counter=0
print " Calculating conductive resitances : "
print " "
for R in Rcdpar:
    L_R=R[0]
    k_R=R[1]
    A_R=R[2]
    Res=L_R/(100*k_R*A_R)
    sum_cond_paralel=sum_cond_paralel+(1/Res)
    counter=counter+1
    print "Conductive resistance is: "+str(Res)+" W/degree C"
    print " " 
sum_cond_par=1/sum_cond_paralel
print "Total parallel conductive resistance is "+str(sum_cond_par)+" W/degree C"
print "**************************************"
print " "
total_resistance=sum_conductive+sum_convective+sum_cond_par
print(" Total thermal resistance of a composite wall is "+str(total_resistance)+ " [degree C/W] ")
print "**************************************"
print " "
#calculation of rate of heat transfer through the one unit of composite wall
Qunit=(T1-T2)/total_resistance
print(" The rate of heat transfer through one unit of composite wall is "+str(Qunit)+" W")
print "**************************************"
print " "
#calculation of rate of heat transfer through the composite wall
proportion=(Height_of_wall*Width_of_wall)/0.25
Q=Qunit*proportion
print(" The rate of heat transfer through the entire wall is "+ str(Q) + " W")
print "**************************************"
print " "

    
    
       
    




