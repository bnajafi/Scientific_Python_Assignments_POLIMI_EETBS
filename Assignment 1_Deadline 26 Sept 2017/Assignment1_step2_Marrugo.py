# -*- coding: utf-8 -*-
#              Assigment 1 Calculation of the example D with user input parameters
#
print "Assigment 1 Calculation of the example D with user input parameters"
#
# Input parameters
#
h=3.# High of the wall in [m]
w=5.# Wide of the wall in [m]
Lp=0.03# Thickness of the foam layer in [m]
Lbh=0.02# Thickness of the vertical plaster layers of the brick in [m]
Lbw=0.16# Thickness of the horizontal plaster layers of the brick in [m]
Lair=0.16# Thickness of the cross horizontal section on the brick in [m]
Kair=float(raw_input("Please enter the conductivity of the cross horizontal section on the brick in [W/m*C] : "))# Conductivity of cross horizontal section on the brick in [W/m*ºC]
Kb=float(raw_input("Please enter the conductivity of the plaster on the brick in [W/m*C] : "))# Conductivity of the plaster layers of the brick in [W/m*ºC]
Kp=float(raw_input("Please enter the conductivity of the foam on the brick in [W/m*C] : "))# Conductivity of the foam layer in [W/m*ºC]
tin=float(raw_input("Please enter the indoor temperature in [C]: "))# Indoor temperature in [ºC] 
tout=float(raw_input("Please enter the indoor temperature in [C]: "))# Outdoor temperature in [ºC] 
h1=float(raw_input("Please enter the heat transfer coefficient of the inner side in [W/m^2] : "))# Heat transfer coefficient of inner side in [W/m^2]
h2=float(raw_input("Please enter the heat transfer coefficient of the outer side in [W/m^2] : \n"))# Heat transfer coeeficient of outer side in [W/m^2]
print('')
#
#             Areas of each part equivalent resistance 
#
# 1m of wide was defined for the areas calculations 
#
Ap=0.25# Area of the resistance of convention of the foam in [m^2]
Abh=0.25# Area of the resistance of conduction of the vertical plaster in [m^2]
Abw=0.015# Area of the resistance of conduction of the horizontal plaster  1 in [m^2]
Aair=0.22# Area of the resistance of conduction of cross horizontal section on the brick 1 in [m^2]
#
#           Calculation of the equivalent resistance in series 
#
R1in=(1/(h1*Ap))# Resistance of convention of the foam in [ºC/W]
R2=(Lp/(Kp*Ap))# Resistance of conduction of the foam in [ºC/W]
R3=(Lbh/(Kb*Abh))# Resistance of conduction of the vertical plaster in [ºC/W]
R7=R3# Resistance for the second vertical plaster in [ºC/W]
R8out=(1/(h2*Abh))#Resistance of convention of the vertical plaster in [ºC/W]
#
#           Calculation of the equivalent resistance in parallel 
#
R4=(Lbw/(Kb*Abw))# Resistance of conduction of the horizontal plaster in [ºC/W]
R5=R4# Resistance of conduction of second horizontal plaster in [ºC/W]
R6air=(Lair/(Kair*Aair))# Resistance of conduction of the cross horizontal section on the brick in [ºC/W]
RP=1/((1/R4)+(1/R5)+(1/R6air))# Total resistance in parallel in [ºC/W]
#
#           Calculation total equivalent resistance
#
Rtotal=R1in+R2+R3+RP+R7+R8out# Total Equivalent resistance in [ºC/W]
#
print "The total thermal resistance is "+str(Rtotal)+" ºC/W\n"
#
#           Calculation of the heat transfer of the wall
#
Qb=(tin-tout)/Rtotal# Rate of heat transfer of one brick in [W]
Nb=(h*w)/Abh# Number of bricks in the wall
Qtotal=Qb*Nb# Rate of heat tranfer of the wall in [W]
#
print "The heat transfer through the wall is "+str(Qtotal)+" W"