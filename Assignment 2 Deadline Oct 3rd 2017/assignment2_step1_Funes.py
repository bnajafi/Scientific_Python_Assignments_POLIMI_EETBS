# -*- coding: utf-8 -*-
#Solving the problem of "Composite wall" with lists

A_wall = 15
A_unit = 0.25
T81 = 20
T82 = -10

Ri = [10, 0.25] #Resistance inside [conv heat transf coeff, Area]
Ro = [25, 0.25] #Resistance outside

Rf = [0.03, 0.026, 0.25] #[thickness, cond heat transf coeff, Area]
Rp1 = [0.02, 0.22, 0.25]
Rp2 = [0.02, 0.22, 0.25]

Rpc1 = [0.16, 0.22, 0.15]
Rpc2 = [0.16, 0.22, 0.15]
Rb = [0.16, 0.72, 0.22]

Res_parallel = [Rpc1, Rpc2, Rb]

total_ResParallel = 99999999999999999999999999999999999999999999999
for anyResistance in Res_parallel:
    L_Ri = anyResistance [0]
    k_Ri = anyResistance [1]    
    A_Ri = anyResistance [2]
    RValue_Ri = L_Ri/(k_Ri*A_Ri)
    print "So the calculated resistance is "+str(RValue_Ri)+ " (°C/W)"
    total_ResParallel = 1/((1/total_ResParallel)+(1/RValue_Ri))
    print "****************"
print "So the equivalent resistance in parallel is "+str(total_ResParallel)+ " (°C/W)"

ResCond_series = [Rf, Rp1, Rp2]

TotResCond_series = 0
for anyResistance in ResCond_series:
    L_Ri = anyResistance [0]
    k_Ri = anyResistance [1]
    A_Ri = anyResistance [2]
    RValue_Ri = L_Ri/(k_Ri*A_Ri)
    print "So the calculated resistance is "+str(RValue_Ri)+ " (°C/W)"
    TotResCond_series = TotResCond_series + RValue_Ri
    print "****************"
print "So the equivalent conductive resistance in series is "+str(TotResCond_series)+ " (°C/W)"

ResConv_series = [Ri, Ro]

TotResConv_series = 0
for anyResistance in ResConv_series:
    h_Ri = anyResistance [0]
    A_Ri = anyResistance [1]
    RValue_Ri = 1/(h_Ri*A_Ri)
    print "So the calculated resistance is "+str(RValue_Ri)+ " (°C/W)"
    TotResConv_series = TotResConv_series + RValue_Ri
    print "*****************"
print "So the equivalent convective resistance in series is "+str(TotResConv_series)+ " (°C/W)"


TOTAL_Resistance = TotResCond_series + TotResConv_series + total_ResParallel
print "Finally, the total resistance of a unit of the composite wall is "+str(TOTAL_Resistance)+ " (°C/W)"

Q_unit = (T81-T82)/TOTAL_Resistance
Q_total = Q_unit*(A_wall/A_unit)
print "The total heat flux exchanged through the wall is "+str(Q_total)+" W"