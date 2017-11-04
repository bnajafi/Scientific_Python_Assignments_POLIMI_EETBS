# -*- coding: utf-8 -*-
Ri={"name":"inner_conv_res","A":10,"h":0.25,"resvalue":0} #convection resisdance °degC/W [hf,A]
Rf={"name":"foam","L":0.03,"K":0.026,"A":0.25,"resvalue":0} #Thermal resistance of foam °degC/w [Lf,Kf,A]
R_p1={"name":"plaster1_cond","L":0.02,"K":0.22,"A":0.25,"resvalue":0} #Thermal resistance inner plaster °degC/w [L,K,A]
R_pc1={"name":"plaster_cross1_cond","L":0.16,"K":0.22,"A":0.015,"resvalue":0} #Thermal resistance plaster cross section °degC/w [Lpc1,Kpc1,A]
R_pc2={"name":"plaster_cross2_cond","L":0.16,"K":0.22,"A":0.015,"resvalue":0} #Thermal resistance plaster cross section °degC/w [Lpc1,Kcp1,A]
Rb={"name":"brick","L":0.16,"K":0.72,"A":0.22,"resvalue":0} #Thermal resistance of brick degC/w [Lb1,Kb,A]
R_p2={"name":"plaster2_cond","L":0.02,"K":0.22,"A":0.25,"resvalue":0} #Thermal resistance inner plaster °degC/w [L,K,A]
Ro={"name":"outer_conv_res","A":25,"h":0.25,"resvalue":0} #Thermal resistance outer plaster °degC/w 

Parallel_ress = [R_pc1, R_pc2, Rb]

Conduction_resisdances = [Rf, R_p1,R_p2]

Convection_resisdances = [Ri,Ro]

#Calculating Parallel Resistances
total_ResParallel =99999999
for anyresistance in Parallel_ress:
    L_Ri=anyresistance["L"]
    K_Ri=anyresistance["K"]
    A_Ri=anyresistance["A"]
    name_Ri=anyresistance["name"]
    RValue = L_Ri/(K_Ri* A_Ri)
    print " calculated parallel resistance for "+name_Ri+" is"  +str(RValue) +"(°C/W)"
    total_ResParallel=1/((1/total_ResParallel)+(1/RValue))
    print "Total parallel resisdance is" +str(total_ResParallel)+"(°C/W)"
print " so the total parallel resisdance" +str(total_ResParallel)+"(°C/W)"

#Calculating Convection Resistance
Total_convres=0
for conv_res in Convection_resisdances:
    h_Ri=conv_res["h"]
    A_Ri=conv_res["A"]
    name_Ri=conv_res["name"]
    R_Value = 1/(h_Ri*A_Ri)
    print " calculated convection resistance for "+name_Ri+" is" +str(R_Value)+ "(°C/W)"
    Total_convres=Total_convres+R_Value
    print "*********************************"
print "the total convection value is" +str(Total_convres)+"(°C/W)"


#Calculating Conduction resistance

Total_conduction_res=0
for cond_res in Conduction_resisdances:
    L_Ri=cond_res["L"]
    K_Ri=cond_res["K"]
    A_Ri=cond_res["A"]
    R_value= L_Ri/(K_Ri* A_Ri)
    name_Ri=cond_res["name"]
    print "calculated Resisdance of counduction for"+name_Ri+"is" +str(R_value) +"(°C/W)"
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
