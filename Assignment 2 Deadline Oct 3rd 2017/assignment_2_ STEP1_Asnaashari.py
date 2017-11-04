# -*- coding: utf-8 -*-
Ri=[10,0.25] #convection resisdance °degC/W [hf,A]
Rf=[0.03,0.026,0.25] #Thermal resistance of foam °degC/w [Lf,Kf,A]
R_p1=[0.02,0.22,0.25] #Thermal resistance inner plaster °degC/w [L,K,A]
R_pc1=[0.16,0.22,0.015] #Thermal resistance plaster cross section °degC/w [Lpc1,Kcp1,A]
R_pc2=[0.16,0.22,0.015] #Thermal resistance plaster cross section °degC/w [Lpc1,Kcp1,A]
Rb=[0.16,0.72,0.22] #Thermal resistance of brick degC/w [Lb1,Kb,A]
R_p2=[0.02,0.22,0.25] #Thermal resistance inner plaster °degC/w [L,K,A]
Ro=[25,0.25] #Thermal resistance outer plaster °degC/w 

Parallel_ress = [R_pc1, R_pc2, Rb]

Conduction_resisdances = [Rf, R_p1,R_p2]

Convection_resisdances = [Ri,Ro]

#Calculating Parallel Resistances
total_ResParallel = 99999999

for anyresistance in Parallel_ress:
    L_Ri=anyresistance[0]
    K_Ri=anyresistance[1]
    A_Ri=anyresistance[2]
    RValue = L_Ri/(K_Ri* A_Ri)
    print " calculated parallel resistance is" +str(RValue) +"(°C/W)"
    total_ResParallel=1/((1/total_ResParallel)+(1/RValue))
    print "Total parallel resisdance is" +str(total_ResParallel)+"(°C/W)"
print " so the total parallel resisdance" +str(total_ResParallel)+"(°C/W)"

#Calculating Convection Resistance
Total_convres=0
for conv_res in Convection_resisdances:
    h_Ri=conv_res[0]
    A_Ri=conv_res[1]
    R_Value = 1/(h_Ri*A_Ri)
    print " calculated convection resistance is" +str(R_Value)+ "(°C/W)"
    Total_convres=Total_convres+R_Value
    print "*********************************"
print "the total convection value is" +str(Total_convres)+"(°C/W)"


#Calculating Conduction resistance

Total_conduction_res=0
for cond_res in Conduction_resisdances:
    L_Ri=cond_res[0]
    K_Ri=cond_res[1]
    A_Ri=cond_res[2]
    R_value= L_Ri/(K_Ri* A_Ri)
    print "calculated Resisdance of counduction" +str(R_value) +"(°C/W)"
    print"**********************"
    Total_conduction_res=Total_conduction_res+R_value
print "Total calculated conduction" +str(Total_conduction_res) +"(°C/W)"

#Calculating total resistance:
Total_resisdance=0
Total_resisdance=Total_resisdance+Total_conduction_res+Total_convres+total_ResParallel
print "********************"
print " finally total_res is" +str(Total_resisdance)

#Calculating heat transfer
T1 = 20
T2 = -10
A_unit = 0.25
A_tot = 15
Q_unit = (T1-T2)/Total_resisdance
Q_wall = Q_unit*(A_tot/A_unit)
print "***************"

print "total heat flux is "+str(Q_wall)+" W"
