# -*- coding: utf-8 -*-
#assignment 2
#Ashima Pottekat

#Step 1

# list of resistances
R_foam = [0.03,0.026,0.25]
R_p1 = [0.02,0.22,0.25] #resistance of plaster of inner surface 
R_p2 = [0.22,0.16,0.015] #resistance of plaster above brick
R_p3 = R_p2 #resistance of plaster below brick
R_brick = [0.72,0.16,0.22]
R_p4 = R_p1 #resistance of plaster of outer surface
R_i = [10,0.25] #Inner wall
R_o = [25,0.25] #Outer wall
 
# for conductive resistances

#parallel
R_tot = 0
parallel_res = [R_brick,R_p2,R_p3]

print'********************************************************'
print'The calculated resistances in parallel are as follows:'
print'******'
for anyresistance in parallel_res:
    L_anyresistance=anyresistance[0]
    k_anyresistance=anyresistance[1]
    A_anyresistance=anyresistance[2]
    Tot_value=L_anyresistance/(k_anyresistance*A_anyresistance)
    R_tot=R_tot+(1/Tot_value)
    total_par=1/R_tot
    print'The calculated Resistance is '+str(Tot_value) +' (degC/W)'
    print'******'
print'So,The total sum of resistance in Parallel is '+str(total_par)+' (degC/W)'
 
# for series
series_res=[R_foam,R_p1,R_p4]
total_sres=0
print'*******************************************************'
print'The calculated resistances in series are as follows :'
print'******'
for anyresistance in series_res:
    L_anyresistance=anyresistance[0]
    k_anyresistance=anyresistance[1]
    A_anyresistance=anyresistance[2]
    Tot_value1=L_anyresistance/(k_anyresistance*A_anyresistance)
    total_sres=total_sres+Tot_value1
    print'The calculated Resistance is '+str(Tot_value1)+' (degC/W)'
    print'******'
print'So,The total sum of resistance in series is '+str(total_sres)+' (degC/W)'
 
# for convective resistances in series

Resistance_Conv_series=[R_i,R_o]
total_conv_sres=0
print'************************************************************************************************'
print'Below are the individual calculated resistance in series of inner and outer surface respectively:'
print'******'
for anyresistance in Resistance_Conv_series:
    h_anyresistance=anyresistance[0]
    A_anyresistance=anyresistance[1]
    Res_value=1/(h_anyresistance*A_anyresistance)
    total_conv_sres=total_conv_sres+Res_value
    print'The calculated Resistance is '+str(Res_value)+' (degC/W)'
    print'******'
print'So,The total sum of convective resistance in series is '+str(total_conv_sres)+' (degC/W)'
 
R_Total=total_par+total_sres+total_conv_sres #Total Thermal Resistance
 
T0=20 #Indoor Temperature
T1=-10 #outdoor Temperature
W_Height=3 #Total Height of wall
W_Wide=5 #Total width of wall
A_total=W_Height*W_Wide #total area of wall
 
Q=(T0-T1)/R_Total #Heat Transfer through unit wall
 
QFinal=(Q*A_total)/0.25 #Total Heat Transfer
print'************************************************************************************************'
print'The total thermal resistance is '+str(R_Total) +'(degC/W)'+' and Total heat transfer across the wall is '+str(QFinal) +'(W)'