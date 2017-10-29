# Energy And Environmental Technologies For Building Systems : Assignment 01, Step-2

# Submitted By : Danish Ahmad Mir

# Assignment Based On Exercise-D (Heat Loss Through A Composite Wall)

# Assumption : One-dimentional heat transfer through the wall ; Width of wall considered for unit block = 1m

# Given Data :
 
Kb = 0.72  #Thermal Conductivity of the brick (W/m-C)
Kp = 0.22  #Thermal Conductivity of the plaster (W/m-C)
Kf = 0.026 #Thermal Conductivity of the foam (W/m-C)

Tinf1 = 20  #Inside tempeature (deg-C)
Tinf2 = -10 #Outside temperature (deg-C)

Awall = 15 #Area of complete wall perpendicular to heat flow (5m x 3m)


#Step-1 : Calculation of Convective thermal resistance (Rin) on inside of wall

A = float(raw_input("please enter the Area of Inner Side in m2 "))  #Area of unit-block of wall perpendicular to heat flow (1m X 0.25m)
h1 = float(raw_input("please enter the convective heat transfer coefficient of inner layer in W/m2 DegC ")) #Convective heat transfer co-efficient on inside

Rin = 1/(h1*A) #Convective thermal resistance on inside of wall

#Step-2 : Calculation of Convective thermal resistance (Rout) on outside of wall

A = float(raw_input("please enter the Area of outer Side in m2 "))  #Area of unit-block of wall perpendicular to heat flow (1m X 0.25m)
h2 = float(raw_input("please enter the convective heat transfer coefficient of outer layer in W/m2 DegC ")) #Convective heat transfer co-efficient on outside

Rout = 1/(h2*A) #Convective thermal resistance on outside of wall

#Step-3 : Calculation of Conductive thermal resistance (Rf) for foam

A = float(raw_input("please enter the Area of foam in m2 "))  #Area of foam on unit- block wall perpendicular to heat flow (1m X 0.25m)
Kf = float(raw_input("please enter the Thermal Conductivity of foam layer in W/m DegC ")) #Thermal Conductivity of the foam (W/m-C)
Lf = float(raw_input("please enter the Lenght of foam layer in m ")) #Length/thickness of foam parallel to heat flow

Rf = Lf/(Kf*A) #Conductive thermal resistance of foam

#Step-4 : Calculation of Conductive thermal resistance (Rp) for plaster

A = float(raw_input("please enter the Area of plaster in m2 "))  #Area of plaster on unit- block perpendicular to heat flow (1m X 0.25m)
Kp = float(raw_input("please enter the Thermal Conductivity of plaster layer in W/m DegC ")) #Thermal Conductivity of the plaster (W/m-C)
Lp = float(raw_input("please enter the Lenght of plaster layer in m ")) #Length/thickness of plaster parallel to heat flow

Rp = Lp/(Kp*A) #Conductive thermal resistance of plaster

#Step-5 : Calculation of Conductive thermal resistance (Rb) for brick

Ab = float(raw_input("please enter the Area of brick in m2 "))  #Area of brick perpendicular to heat flow (1m X 0.22m)
Kp = float(raw_input("please enter the Thermal Conductivity of brick in W/m DegC ")) #Thermal Conductivity of the brick (W/m-C)
Lb = float(raw_input("please enter the Lenght of brick layer in m ")) #Length/thickness of brick parallel to heat flow

Rb = Lb/(Kb*Ab) #Conductive thermal resistance of brick

#Step-6 : Calculation of Conductive thermal resistance (Rpp) for plaster parallel to brick

App = float(raw_input("please enter the Area of plaster parallel to bick in m2 "))  #Area of plaster(par. to brick) perpendicular to heat flow (1m X 0.015m)
Kp = float(raw_input("please enter the Thermal Conductivity of plaster layer in W/m DegC ")) #Thermal Conductivity of the plaster (W/m-C)
Lpp = float(raw_input("please enter the Lenght of plaster parallel to bick in m ")) #Length/thickness of plaster(par. to brick) parallel to heat flow

Rpp = Lpp/(Kp*App) #Conductive thermal resistance of plaster parallel to brick

#Step-7 : Calculation for Req : Equivalent thermal resistance of the elements in parallel

X = (1/Rb) + (1/Rpp) + (1/Rpp)

Req = 1/X #Equivalent thermal resistance of brick and plaster in parallel

Rtot = Rin + Rf + Rp + Req + Rp + Rout #Total thermal resistance of the unit

print "Therefore, the complete resistance of the composite wall unit is " + str(Rtot) + " (deg C/W)"

#Step-8 : Calculations for Q_un : Heat flow through unit-block of wall

Tinf1 = float(raw_input("please enter the Inner Temperature in DegC "))  #Inside tempeature (deg-C)
Tinf2 = float(raw_input("please enter the Outer Temperature in DegC ")) #Outside temperature (deg-C)

Q_un = (Tinf1 - Tinf2)/Rtot #Heat flow through unit-block of wall

#Step-9 : Calculations for Q_tot : Heat flow through unit-block of 

Q_un = float(raw_input("please enter the Heat flow through unit-block of wall in Watts ")) #Heat flow through complete wall
Awall = float(raw_input("please enter the Area of complete wall in m2 ")) #Area of complete wall perpendicular to heat flow (5m x 3m)
A = float(raw_input("please enter the Area of unit-block of wall in m2 "))  #Area of unit-block of wall (1m x0.25m)

Q_tot = Q_un * (Awall/A) #Heat flow through complete wall

print "Hence, the heat flow through the wall (full area) is " +str(Q_tot)  + " Watts"
