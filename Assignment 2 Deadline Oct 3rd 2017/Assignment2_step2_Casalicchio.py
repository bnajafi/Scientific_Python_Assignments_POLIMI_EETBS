# -*- coding: utf-8 -*-
"""
CASALICCHIO VALERIA 10424146

Step 2: you should do exactly the same procedure as step 1. The only difference is that you should define each resistance as a dictionary and not 
a list. Though you should still put resistances (each of which is a dictionary now) in three lists of “conductive resistances in series, conductive 
resistances in parallel, and convective resistances” as you had done in step 1, and then continue the calculations exactly as you had done in Step1.
"""

# List of resistances

R_in = {"type":"conv", "name":"indoor", "area":0.25, "h":10}                              # indoor convection [type, name, area [m2], h [W/m2K]]
R_out = {"type":"conv", "name":"outoor", "area":0.25, "h":25}                             # outdoor convection
R_f = {"type":"cond", "name":"foam", "area":0.25, "length":0.03, "k":0.026}                # foam layer [type, name, area [m2], length [m], k [W/mK]] 
R_p = {"type":"cond", "name":"side plaster", "area":0.25, "length":0.02, "k":0.22}         # side plaster
R_cp = {"type":"cond", "name":"center plaster", "area":0.015, "length":0.16, "k":0.22}     # center plaster
R_b = {"type":"cond", "name":"brick", "area":0.22, "length":0.16, "k":0.72}                # brick

R_Conv = [R_in, R_out]
R_Cond_parallel = [R_cp, R_b, R_cp]
R_Cond_series = [R_f, R_p, R_p]
print "-----------------------------------------------------------------"

# Calculation of the overall resistance of convective resistance

Tot_R_Conv = 0

for anyRes in R_Conv:
    Ai = anyRes["area"]
    hi = anyRes["h"]
    Ri = 1/(hi*Ai)
    print " The resistance of the " + str(anyRes["name"]) + " is: " + str(Ri) + " K/W"
    Tot_R_Conv = Tot_R_Conv + Ri
    
print "\n The total convective resistance is: " + str(Tot_R_Conv) + " K/W"
print "-----------------------------------------------------------------"

# Calculation of the overall resistance of conductive resistance (in parallel)

Tot_R_Cond_Parallel_inv = 0

for anyRes in R_Cond_parallel:
    Ai = anyRes["area"]
    Li = anyRes["length"]
    ki = anyRes["k"]
    Ri = Li/(ki*Ai)
    print " The resistance of the " + str(anyRes["name"]) + " is: " + str(Ri) + " K/W"
    Tot_R_Cond_Parallel_inv = Tot_R_Cond_Parallel_inv + 1/Ri

Tot_R_Cond_Parallel = 1/Tot_R_Cond_Parallel_inv
print "\n The total conductive resistance in parallel is: " + str(Tot_R_Cond_Parallel) + " K/W"
print "-----------------------------------------------------------------"

# Calculation of the overall resistance of conductive resistance (in series)

Tot_R_Cond_Series = 0

for anyRes in R_Cond_series:
    Ai = anyRes["area"]
    Li = anyRes["length"]
    ki = anyRes["k"]
    Ri = Li/(ki*Ai)
    print " The resistance of the " + str(anyRes["name"]) + " is : " + str(Ri) + " K/W"
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