# -*- coding: utf-8 -*-
"""
CASALICCHIO VALERIA 10424146

Step 1: You should solve Example D by defining each resistance as a list and then defining lists of resistances (each of which is a list itself).
Hence, you will need to define three lists of resistances: “conductive resistances in series, conductive resistances in parallel, and convective 
resistances”. You should then do the calculations for the mentioned three lists of resistances and then sum their total resistance values up in 
order to find overall resistance of the wall
"""

# List of resistances

R_in = ["conv", "indoor", 0.25, 10]                    # indoor convection [type, name, area [m2], h [W/m2K]]
R_out = ["conv", "outdoor", 0.25, 25]                  # outdoor convection [type, name, area [m2], h [W/m2K]]
R_f = ["cond", "foam", 0.25, 0.03, 0.026]               # foam layer [type, name, area [m2], length [m], k [W/mK]] 
R_p = ["cond", "side plaster", 0.25, 0.02, 0.22]        # side plaster [type, name, area [m2], length [m], k [W/mK]] 
R_cp = ["cond", "center plaster", 0.015, 0.16, 0.22]    # center plaster [type, name, area [m2], length [m], k [W/mK]] 
R_b = ["cond", "brick", 0.22, 0.16, 0.72]               # brick [type, name, area [m2], length [m], k [W/mK]] 

R_Conv = [R_in, R_out]
R_Cond_parallel = [R_cp, R_b, R_cp]
R_Cond_series = [R_f, R_p, R_p]
print "-----------------------------------------------------------------"

# Calculation of the overall resistance of convective resistance

Tot_R_Conv = 0

for anyRes in R_Conv:
    Ai = anyRes[2]
    hi = anyRes[3]
    Ri = 1/(hi*Ai)
    print " The resistance of the " + str(anyRes[1]) + " is: " + str(Ri) + " K/W"
    Tot_R_Conv = Tot_R_Conv + Ri
    
print "\n The total convective resistance is: " + str(Tot_R_Conv) + " K/W"
print "-----------------------------------------------------------------"

# Calculation of the overall resistance of conductive resistance (in parallel)

Tot_R_Cond_Parallel_inv = 0

for anyRes in R_Cond_parallel:
    Ai = anyRes[2]
    Li = anyRes[3]
    ki = anyRes[4]
    Ri = Li/(ki*Ai)
    print " The resistance of the " + str(anyRes[1]) + " is: " + str(Ri) + " K/W"
    Tot_R_Cond_Parallel_inv = Tot_R_Cond_Parallel_inv + 1/Ri

Tot_R_Cond_Parallel = 1/Tot_R_Cond_Parallel_inv
print "\n The total conductive resistance in parallel is: " + str(Tot_R_Cond_Parallel) + " K/W"
print "-----------------------------------------------------------------"

# Calculation of the overall resistance of conductive resistance (in series)

Tot_R_Cond_Series = 0

for anyRes in R_Cond_series:
    Ai = anyRes[2]
    Li = anyRes[3]
    ki = anyRes[4]
    Ri = Li/(ki*Ai)
    print " The resistance of the " + str(anyRes[1]) + " is : " + str(Ri) + " K/W"
    Tot_R_Cond_Series = Tot_R_Cond_Series + Ri

print "\n The total conductive resistance in series is: " + str(Tot_R_Cond_Series) + " K/W"
print "-----------------------------------------------------------------"

# Calculation of the overall resistance of the wall
R_Wall_Unit = Tot_R_Conv + Tot_R_Cond_Parallel + Tot_R_Cond_Series
print " The resistance of the unit of the wall is: " + str(R_Wall_Unit) + " K/W"


# Heat transfer rate
T_in = 20  # [°C]
T_out = -10  # [°C]

Area_Unit = 1*0.25  # [m2]
Q_Unit = (T_in - T_out)/R_Wall_Unit  # [W]

Area_Wall = 3 * 5  # [m2]
Q_Wall =  Q_Unit * (Area_Wall/Area_Unit)  # [W]

print "\n The heat transfer rate is: " + str(Q_Wall) + " W"
print "-----------------------------------------------------------------"