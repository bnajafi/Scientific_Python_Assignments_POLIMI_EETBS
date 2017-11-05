# -*- coding: utf-8 -*-
# SOLVING EXAMPLE D WITH LISTS

print "Hi mate, welcome to this program for calculating the heat loss through a composite wall"

print"..." 

print "We are going to assume 1 m width of the wall to start all the calculations!"

#CONDUCTION
R_F= [0.25,0.03,0.026] #Resistivity of Foam -- Area, Length, Conductivity
R_P_S1= [0.25,0.02,0.22] #Resistivity of Plaster -- Area, Length, Conductivity
R_P_S2= [0.25,0.02,0.22] #Resistivity of Plaster -- Area, Length, Conductivity

R_B= [0.22,0.16,0.72] #Resistivity of Brick -- Area, Length, Conductivity
R_P1= [0.015,0.16,0.22] #Resistivity of Plaster -- Area, Length, Conductivity
R_P2= [0.015,0.16,0.22] #Resistivity of Plaster -- Area, Length, Conductivity

#CONVECTION
R_Conv_1=[0.25,10] #Resistivity of inside of building -- Area, Convection coefficcient
R_Conv_2=[0.25,25] #Resistivity of outside of building -- Area, Convection coefficcient

#LIST OF RESISTANCES
List_Par = [R_B,R_P1,R_P2] #Parallel resistances
List_Cv = [R_Conv_1,R_Conv_2] #Convection resistances
List_Ser = [R_F,R_P_S1,R_P_S2] #Series resistances

TotalPar_R=0
Sum_Par=0
for anyR_Par in List_Par:
    A_anyR=anyR_Par[0]
    L_anyR=anyR_Par[1]
    k_anyR=anyR_Par[2]
    R_par = 1/(L_anyR/(A_anyR*k_anyR))
    TotalPar_R = TotalPar_R + (R_par)
Sum_Par=Sum_Par+(1/TotalPar_R)
print "The conductive resistance in parallel is "+str(Sum_Par)+" °C/W"

    
TotalConv_R=0
for anyR_Conv in List_Cv:
    A_anyR=anyR_Conv[0]
    h_anyR=anyR_Conv[1]
    R_conv = 1/(A_anyR*h_anyR)
    TotalConv_R = TotalConv_R + (R_conv)
print "The convective resistance is "+str(TotalConv_R)+" °C/W"     
    

TotalSer_R=0
for anyR_Ser in List_Ser:
    A_anyR=anyR_Ser[0]
    L_anyR=anyR_Ser[1]
    k_anyR=anyR_Ser[2]
    R_Ser = (L_anyR/(A_anyR*k_anyR))
    TotalSer_R = TotalSer_R + (R_Ser)
print "The conductive resistance in series is "+str(TotalSer_R)+" °C/W"  

print"....." 
print"....."

TOT_RES = TotalSer_R+TotalConv_R+Sum_Par
print "So, the TOTAL RESISTANCE is "+str(TOT_RES)+" °C/W" 

print"******************************************************"  
print"******************************************************"  

print "Now, let's calculate the heat flux loss of the wall..."

T1=float(raw_input("Let's start with the inside temperature of the building in degC "))
T2 = float(raw_input("Please enter the outside temperature of the building in degC "))

Q_unit = (T1-T2)/TOT_RES
print"The heat transfer loss per unit "+str(Q_unit)+" W/unit"

print"....." 
print"....." 

print "Assuming a wall of 3 m of high and 5 m of wide... "
H_w = 3 # High of wall in m
W_w = 5 # Wide of wall in m
A = 0.25 

A_wall = H_w*W_w
Q_wall = Q_unit*A_wall/A
print "The TOTAL HEAT LOSS of the composite wall is "+str(Q_wall)+ " W"
