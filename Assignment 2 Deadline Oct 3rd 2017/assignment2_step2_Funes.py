# -*- coding: utf-8 -*-
#Solving the problem of "Composite wall" with lists

A_wall = 15
A_unit = 0.25
T81 = 20
T82 = -10

Ri = {"name":"inside", "h_Ri" : 10, "A_Ri" : 0.25, "ResValue" : 0} #Resistance inside 
Ro = {"name": "outside", "h_Ri":25, "A_Ri":0.25, "ResValue" : 0} #Resistance outside

Rf = {"name":"foam", "L_Ri":0.03, "k_Ri":0.026, "A_Ri":0.25, "ResValue":0} #[thickness, conv heat transf coeff, Area]
Rp1 = {"name":"plaster_series1", "L_Ri":0.02, "k_Ri":0.22, "A_Ri":0.25,"ResValue":0}
Rp2 = {"name":"plaster_series2", "L_Ri":0.02, "k_Ri":0.22, "A_Ri":0.25,"ResValue":0}

Rpc1 = {"name":"plaster_parallel1","L_Ri":0.16, "k_Ri":0.22, "A_Ri":0.15,"ResValue":0}
Rpc2 = {"name":"plaster_parallel2","L_Ri":0.16, "k_Ri":0.22, "A_Ri":0.15,"ResValue":0}
Rb = {"name":"brick","L_Ri":0.16, "k_Ri":0.72, "A_Ri":0.22,"ResValue":0}

Res_parallel = [Rpc1, Rpc2, Rb]

total_ResParallel = 99999999999999999999999999999999999999999999999
for anyResistance in Res_parallel:
    name_anyResistance = anyResistance ["name"]    
    L_Ri = anyResistance ["L_Ri"]
    k_Ri = anyResistance ["k_Ri"]    
    A_Ri = anyResistance ["A_Ri"]
    RValue_Ri = L_Ri/(k_Ri*A_Ri)
    anyResistance ["ResValue"] = RValue_Ri 
    print "So the calculated resistance for "+name_anyResistance+"is "+str(RValue_Ri)+ " (°C/W)"
    total_ResParallel = 1/((1/total_ResParallel)+(1/RValue_Ri))
    print "****************"
print "So the equivalent resistance in parallel is "+str(total_ResParallel)+ " (°C/W)"

ResCond_series = [Rf, Rp1, Rp2]

TotResCond_series = 0
for anyResistance in ResCond_series:
    name_anyResistance = anyResistance ["name"]
    L_Ri = anyResistance ["L_Ri"]
    k_Ri = anyResistance ["k_Ri"]
    A_Ri = anyResistance ["A_Ri"]
    RValue_Ri = L_Ri/(k_Ri*A_Ri)
    anyResistance ["ResValue"] = RValue_Ri 
    print "So the calculated resistance for "+name_anyResistance+"is "+str(RValue_Ri)+ " (°C/W)"
    TotResCond_series = TotResCond_series + RValue_Ri
    print "****************"
print "So the equivalent conductive resistance in series is "+str(TotResCond_series)+ " (°C/W)"

ResConv_series = [Ri, Ro]

TotResConv_series = 0
for anyResistance in ResConv_series:
    name_anyResistance = anyResistance ["name"]

    h_Ri = anyResistance ["h_Ri"]
    A_Ri = anyResistance ["A_Ri"]
    RValue_Ri = 1/(h_Ri*A_Ri)
    anyResistance ["ResValue"] = RValue_Ri 
    print "So the calculated resistance for "+name_anyResistance+"is "+str(RValue_Ri)+ " (°C/W)"
    TotResConv_series = TotResConv_series + RValue_Ri
    print "*****************"
print "So the equivalent convective resistance in series is "+str(TotResConv_series)+ " (°C/W)"

TOTAL_Resistance = TotResCond_series + TotResConv_series + total_ResParallel
print "Finally, the total resistance of a unit of the composite wall is "+str(TOTAL_Resistance)+ " (°C/W)"

Q_unit = (T81-T82)/TOTAL_Resistance
Q_total = Q_unit*(A_wall/A_unit)
print "The total heat flux exchanged through the wall is "+str(Q_total)+" W"