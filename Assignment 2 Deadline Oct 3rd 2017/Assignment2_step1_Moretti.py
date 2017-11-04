# -*- coding: utf-8 -*-
"""

EETBS 2017/2018 - Assignment 2, step 1 - Overall resistance of a composite wall using lists of resistances

Giorgio Moretti (10433550)

"""

# LISTS OF RESISTANCES
# Order of data is: [type, name, area [m^2], length [m](if necessary), k [W/mK] or h [W/m^2K]]

R_in = ["conv", "indoor", 0.25, 10]                    # indoor convection
R_out = ["conv", "outdoor", 0.25, 25]                  # outdoor convection
Rf = ["cond", "foam", 0.25, 0.03, 0.026]               # foam layer
Rp = ["cond", "side plaster", 0.25, 0.02, 0.22]        # side plaster
Rpc = ["cond", "center plaster", 0.015, 0.16, 0.22]    # center plaster
Rb = ["cond", "brick", 0.22, 0.16, 0.72]               # brick

ConvRes = [R_in, R_out]
CondRes_parallel = [Rpc, Rb, Rpc]
CondRes_series = [Rf, Rp, Rp]

# CALCULATION OF THE OVERALL RESISTANCE OF ONE UNIT OF THE WALL

ConvRes_tot = 0
inv_CondRes_parallel_tot = 0
CondRes_series_tot = 0

print "\n"

for anyRes in ConvRes:
    print " Here is the new resistance: " + str(anyRes)
    Ai = anyRes[2]
    hi = anyRes[3]
    Ri = 1/(hi*Ai)
    print " The calculated resistance is: " + str(anyRes[1]) + " = " + str(Ri) + " K/W"
    print " ****************************"
    ConvRes_tot = ConvRes_tot + Ri

print "\n The total convective resistance is: ConvRes_tot = " + str(ConvRes_tot) + " K/W"
print "\n"

for anyRes in CondRes_parallel:
    print " Here is the new resistance: " + str(anyRes)
    Ai = anyRes[2]
    Li = anyRes[3]
    ki = anyRes[4]
    Ri = Li/(ki*Ai)
    print " The calculated resistance is: " + str(anyRes[1]) + " = " + str(Ri) + " K/W"
    print " ****************************"
    inv_CondRes_parallel_tot = inv_CondRes_parallel_tot + 1/Ri

CondRes_parallel_tot = 1/inv_CondRes_parallel_tot
print "\n The total conductive resistance in parallel is: CondRes_parallel_tot = " + str(CondRes_parallel_tot) + " K/W"
print "\n"

for anyRes in CondRes_series:
    print " Here is the new resistance: " + str(anyRes)
    Ai = anyRes[2]
    Li = anyRes[3]
    ki = anyRes[4]
    Ri = Li/(ki*Ai)
    print " The calculated resistance is: " + str(anyRes[1]) + " = " + str(Ri) + " K/W"
    print " ****************************"
    CondRes_series_tot = CondRes_series_tot + Ri

print "\n The total conductive resistance in series is: CondRes_series_tot = " + str(CondRes_series_tot) + " K/W"
print "\n"

Res_wall_unit = ConvRes_tot + CondRes_parallel_tot + CondRes_series_tot
print " The overall resistance of one unit of the wall is: Res_wall_unit = " + str(Res_wall_unit) + " K/W"


# HEAT TRANSFER RATE

A_unit = 1*0.25  # [m^2]
T_in = 20  # [°C]
T_out = -10  # [°C]

Qdot_unit = (T_in - T_out)/Res_wall_unit  # unit heat transfer rate [W]

A_wall = 3 * 5  # [m^2]
Qdot_wall =  Qdot_unit * (A_wall/A_unit)  # [W]

print "\n The unit heat transfer rate is: Qdot_unit = " + str(Qdot_unit) + " W"
print "\n The heat transfer rate of the wall is: Qdot_wall = " + str(Qdot_wall) + " W"