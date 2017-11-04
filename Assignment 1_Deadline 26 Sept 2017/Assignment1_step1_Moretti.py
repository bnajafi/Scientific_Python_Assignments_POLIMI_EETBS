# -*- coding: utf-8 -*-
"""

EETBS 2017/2018 - Assignment 1, step 1 - Heat transfer rate through a composite wall

Giorgio Moretti (10433550)

"""

# HEAT TRANSFER RATE THROUGH ONE UNIT OF THE WALL (thickness = 1 m)

# data
T_in = 20            # inner temperature [°C]
T_out = -10          # outer temperature [°C]
h_in = 10            # inner convection heat transfer coefficient [W/m^2°C]
h_out = 25           # outer convection heat transfer couefficient [W/m^2°C]
kb = 0.72            # conductivity of thw brick [W/m°C]
kp = 0.22            # conductivity of the plaster [W/m°C]
kf = 0.026           # conductivity of the foam [W/m°C]

A_unit = 0.25 * 1    # area of the unit of the wall [m^2]

A_in = 0.25 * 1             # inner area [m^2]
R_in = 1/(h_in * A_in)      # inner convective resistance [°C/W]

Af = 0.25 * 1           # foam area [m^2]
Lf = 0.03               # foam thickness [m]
Rf = Lf/(kf * Af)       # foam conductive resistance [°C/W]

Ap = 0.25 * 1           # side plaster area [m^2]
Lp = 0.02               # side plaster thickness [m]
Rp = Lp/(kp * Ap)       # side plaster conductive resistance [°C/W]

Apc = 0.015 * 1         # center plaster area [m^2]
Lpc = 0.16              # center plaster thickness [m]
Rpc = Lpc/(kp * Apc)    # center plaster resistance [°C/W]

Ab = 0.22 * 1           # brick area [m^2]
Lb = 0.16               # brick thickness [m]
Rb = Lb/(kb * Ab)       # brick resistance [°C/W]

A_out = 0.25 * 1            # outer area [m^2]
R_out = 1/(h_out * A_out)   # outer convective resistance [°C/W]

# resistances in parallel
R_parallel = 1/Rpc + 1/Rb + 1/Rpc

# total resistance
R_tot = R_in + Rf + Rp + R_parallel + Rp + R_out

# unit heat transfer rate [W]
Qr_unit = (T_in - T_out)/R_tot

# HEAT TRANSFER RATE OF THE WHOLE WALL [W]
A_wall = 3 * 5 # [m^2]
Qr_wall =  Qr_unit * (A_wall/A_unit)

print "\n The total resistance of the unit is:   R_tot = " + str(R_tot) + " °C/W"
print "\n The unit heat transfer rate is:   Qr_unit = " + str(Qr_unit) + " W"
print "\n The heat transfer rate of the wall is:   Qr_wall = " + str(Qr_wall) + " W"