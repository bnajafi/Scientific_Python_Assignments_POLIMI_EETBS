#Assignment 2 - Step 1

#Rate of transfer heat through composite wall (values are taken from Example D) 

#dimenssions of wall that is considered
Height_of_wall=3 #height of wall in [m]
Width_of_wall=5 #width of wall in [m] 

#Convective Resistances 
Ri={"type":"convection","heat transfer coefficient":10,"area":0.25} 
Rout={"type":"convection","heat transfer coefficient":25,"area":0.25} 

#Series Conductive Resistances 
Rfoam={"type":"foam","thickness":3,"area":0.25,"thermal coefficient":0.026} 
Rpside1={"type":"plastic","thickness":2,"area":0.25,"thermal coefficient":0.22} 
Rpside2={"type":"plastic","thickness":2,"area":0.25,"thermal coefficient":0.22} 

#Parallel Conductive Resistances 
Rbrick={"type":"brick","length":16,"area":0.22,"thermal coefficient":0.72}
Rpcenter1={"type":"plastic","length":16,"area":0.015,"thermal coefficient":0.22}
Rpcenter2={"type":"plastic","length":16,"area":0.015,"thermal coefficient":0.22}
 
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
print "Calculating convective resistances: "
print " "
for R in Rconv:
    h_R=R["heat transfer coefficient"]
    A_R=R["area"]
    Res=1/(h_R*A_R)
    counter=counter+1
    print "Convective resistance number "+str(counter)+" is equal to "+str(Res)+" W/degree C"
    print " "
    sum_convective=sum_convective+Res
print "Total convective resistance is "+str(sum_convective)+" W/degree C"
print "**************************************"
print " "

sum_conductive=0
counter=0
print "Calculating conductive resistances that are in series: "
print " "
for R in Rcdseries:
    L_R=R["thickness"]
    k_R=R["thermal coefficient"]
    A_R=R["area"]
    Res=L_R/(100*k_R*A_R)
    counter=counter+1
    print "Conductive resistance number "+str(counter)+" is equal to "+str(Res)+" W/degree C" 
    print " "
    sum_conductive=sum_conductive+Res
print "Total series conductive resistance is "+str(sum_conductive)+" W/degree C"
print "**************************************"
print " " 
    
sum_cond_paralel=0
counter=0
print "Calculating conductive resitances that are in parallel:"
print " "
for R in Rcdpar:
    L_R=R["length"]
    k_R=R["thermal coefficient"]
    A_R=R["area"]
    Res=L_R/(100*k_R*A_R)
    sum_cond_paralel=sum_cond_paralel+(1/Res)
    counter=counter+1
    print "Conductive resistance number "+str(counter)+" is equal to "+str(Res)+" W/degree C" 
    print " " 
sum_cond_par=1/sum_cond_paralel
print "Total parallel conductive resistance is "+str(sum_cond_par)+" W/degree C"
print "**************************************"
print " "
total_resistance=sum_conductive+sum_convective+sum_cond_par
print("Total thermal resistance of a composite wall is "+str(total_resistance)+ " [degree C/W] ")
print "**************************************"
print " "
#calculation of rate of heat transfer through the one unit of composite wall
Qunit=(T1-T2)/total_resistance
print("The rate of heat transfer through one unit of composite wall is "+str(total_resistance)+" W")
print "**************************************"
print " "
#calculation of rate of heat transfer through the composite wall
proportion=(Height_of_wall*Width_of_wall)/0.25
Q=Qunit*proportion
print("The rate of heat transfer through the entire wall is "+ str(Q) + " W")
print "**************************************"
print " "

    
    
       
    




