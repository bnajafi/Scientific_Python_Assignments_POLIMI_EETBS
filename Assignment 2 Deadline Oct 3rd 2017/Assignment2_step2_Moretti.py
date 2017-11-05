# -*- coding: utf-8 -*-
"""

EETBS 2017/2018 - Assignment 2, step 2 - Overall resistance of a composite wall dictionaries

Giorgio Moretti (10433550)

"""

# RESISTANCES DEFINED AS DICTIONARIES

R_in = {"type":"conv", "name":"indoor", "area":0.25, "h":10}                              # indoor convection
R_out = {"type":"conv", "name":"outoor", "area":0.25, "h":25}                             # outdoor convection
Rf = {"type":"cond", "name":"foam", "area":0.25, "length":0.03, "k":0.026}                # foam layer
Rp = {"type":"cond", "name":"side plaster", "area":0.25, "length":0.02, "k":0.22}         # side plaster
Rpc = {"type":"cond", "name":"center plaster", "area":0.015, "length":0.16, "k":0.22}     # center plaster
Rb = {"type":"cond", "name":"brick", "area":0.22, "length":0.16, "k":0.72}                # brick

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
    Ai = anyRes["area"]
    hi = anyRes["h"]
    Ri = 1/(hi*Ai)
    print " The calculated resistance is: " + str(anyRes["name"]) + " = " + str(Ri) + " K/W"
    print " ****************************"
    ConvRes_tot = ConvRes_tot + Ri

print "\n The total convective resistance is: ConvRes_tot = " + str(ConvRes_tot) + " K/W"
print "\n"

for anyRes in CondRes_parallel:
    print " Here is the new resistance: " + str(anyRes)
    Ai = anyRes["area"]
    Li = anyRes["length"]
    ki = anyRes["k"]
    Ri = Li/(ki*Ai)
    print " The calculated resistance is: " + str(anyRes["name"]) + " = " + str(Ri) + " K/W"
    print " ****************************"
    inv_CondRes_parallel_tot = inv_CondRes_parallel_tot + 1/Ri

CondRes_parallel_tot = 1/inv_CondRes_parallel_tot
print "\n The total conductive resistance in parallel is: CondRes_parallel_tot = " + str(CondRes_parallel_tot) + " K/W"
print "\n"

for anyRes in CondRes_series:
    print " Here is the new resistance: " + str(anyRes)
    Ai = anyRes["area"]
    Li = anyRes["length"]
    ki = anyRes["k"]
    Ri = Li/(ki*Ai)
    print " The calculated resistance is: " + str(anyRes["name"]) + " = " + str(Ri) + " K/W"
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