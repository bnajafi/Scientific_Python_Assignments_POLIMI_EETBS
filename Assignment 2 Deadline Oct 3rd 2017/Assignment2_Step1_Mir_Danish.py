# Energy And Environmental Technologies For Building Systems : Assignment 02, Step-1

# Submitted By : Danish Ahmad Mir

# Assignment Based On Exercise-D (Heat Loss Through A Composite Wall) Total Resistance Calculation Based On Application Of "List []"

# Assumption : One-dimentional heat transfer through the wall ; Width of wall considered for unit block = 1m

# Given Data :

Tinf1 = 20  # Inside tempeature 
Tinf2 = -10 # Outside temperature
A = 0.25 # Area of unit-block of wall perpendicular to heat flow (0.25m x 1m)
Awall = 15 # Area of complete wall perpendicular to heat flow (3m x 5m)

# Step-A : Calculation Of Thermal Conductive resistances In Series. Elements mentioned in the list are [length(m), thermal conductivity(W/m C), area(m^2)] respectively.

RF = [0.03,0.026,0.25] # RF is the thermal resistance of the foam layer of the unit block of the composite wall
RPs1 = [0.02,0.22,0.25] # RPs1 is the thermal resistance of the plaster layer in series on the inside of the unit block of the composite wall
RPs2 = [0.02,0.22,0.25] # RPs2 is the thermal resistance of the plaster layer in series on the outside of the unit block of the composite wall

# Step-B : Calculation Of Thermal Convective resistances In Series. Elements mentioned in the list are [convective heat transfer coefficient(W/m^2 C) and area(m^2)] respectively.

Rin = [10,0.25] # Convective thermal resistance on inside of wall
Rout = [25,0.25] # Convective thermal resistance on outside of wall


# Step-C : Calculation Of Thermal Conductive resistances In Parallel. Elements mentioned in the list are [length(m), thermal conductivity(W/m C), area(m^2)] respectively.

Rpp1 = [0.16,0.22,0.015] # Conductive thermal resistance of plaster1 parallel to brick
Rpp2 = [0.16,0.22,0.015] # Conductive thermal resistance of plaster2 parallel to brick
Rb = [0.16,0.72,0.22] # Conductive thermal resistance of brick

# Step-A1

Cond_Res_Series = [RF, RPs1, RPs2]
Total_Cond_Res_Series = 0
for Every_CoRIS in Cond_Res_Series:
    RCoS = Every_CoRIS [0]/(Every_CoRIS [1]*Every_CoRIS[2])
    Total_Cond_Res_Series = Total_Cond_Res_Series + RCoS
print "Therefore, the total conductive thermal heat resistance in series is " +str(Total_Cond_Res_Series) + " (deg C/W)"
print "------------------------------------------------------------------------------------"

# Step-B1

Conv_Res_Series = [Rin, Rout]
Total_Conv_Res_Series = 0
for Every_CnRIS in Conv_Res_Series:
    RCnS = 1/(Every_CnRIS [0]*Every_CnRIS [1])
    Total_Conv_Res_Series = Total_Conv_Res_Series + RCnS
print "Therefore, the total convective thermal heat resistance in series is " +str(Total_Conv_Res_Series) + " (deg C/W)"
print "------------------------------------------------------------------------------------"

# Step-C1

Cond_Res_Parallel = [Rpp1, Rpp2, Rb]
Total_Cond_Res_Parallel = 0
for Every_CoRIP in Cond_Res_Parallel:
    X = Every_CoRIP[0]/(Every_CoRIP[1]*Every_CoRIP[2])
    RCoP = 1/X
    Total_Cond_Res_Parallel = Total_Cond_Res_Parallel + RCoP
print "Therefore, the total conductive thermal heat resistance in parallel is " +str(Total_Cond_Res_Parallel) + " (deg C/W)"
print "------------------------------------------------------------------------------------"

# Step-D : Calculation Of Total Thermal Resistance (Rtot)

Rtot = Total_Cond_Res_Series + Total_Conv_Res_Series + Total_Cond_Res_Parallel
print "Therefore, the complete resistance of the composite wall unit is " + str(Rtot) + " (deg C/W)"
print "------------------------------------------------------------------------------------"

# Step-D : Calculation Of Heat flow through wall

Q_un = (Tinf1 - Tinf2)/Rtot # Heat flow through unit-block of wall
print "Hence, the heat flow through unit-block of the wall is " +str(Q_un)  + " Watts"
print "------------------------------------------------------------------------------------"
Q_tot = Q_un * (Awall/A) # Heat flow through complete wall

print "Hence, the heat flow through the wall (full area) is " +str(Q_tot)  + " Watts"