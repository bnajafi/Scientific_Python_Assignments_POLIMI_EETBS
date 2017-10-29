# ------------Assignment1_step2---------
# ------------MUHAMMAD Arslan----------

# ---Example-D Heat transfer by thermal conduction & convection----

# I would like to give length & Area; however program will ask the user for heat convection values at the time of Execution 

# Ww= 1 # Assume width of wall in meters

# Resistance for Inner wall side

hi= float(raw_input("Specify the convection coefficient of inner wall ")) # convection coefficient of Inner wall in W/m.C
Li= 0.25 # height of wall in meters
Ai= 0.25*1 # Area of wall in square meters
Ri= 1/(hi*Ai)

# Resistance for foam

kf= float(raw_input("Specify the conduction coefficient of foam ")) # conduction coefficient of foam in W/m.C
Lf= 0.03 # length of of in meters
Af= 0.25*1 # Area of foam in square meters
Rf= Lf/(kf*Af)

# Resistance for Plaster1 & Plaster2

kp= float(raw_input("Specify the conduction coefficient of Plaster ")) # conduction coefficient of Plaster in W/m.C
Lp1= 0.02 # length of palster1 in meters
Lp2= 0.02 # length of plaster2 in meters
Ap= 0.25*1 # Area of Plaster in square meters
Rp1= Lp1/(kp*Ap)
Rp2= Lp2/(kp*Ap)

# Sum of Parallel Resistances for Brick & Plaster a & b

# Brick
kb= float(raw_input("Specify the conduction coefficient of brick ")) # conduction coefficient of brick in W/m.C
Lb= 0.16 # length of brick in meters
Ab= 0.22*1 # Area of brick in square meters
Rb= Lb/(kb*Ab)

# Plaster a & b
kp= float(raw_input("Specify the conduction coefficient of Plaster ")) # conduction coefficient of Plaster in W/m.C
Lpa= 0.16 # length of palster a in meters
Lpb= 0.16 # length of plaster b in meters
Apa= 0.015*1 # Area of Plaster a in square meters
Apb= 0.015*1 # Area of Plaster b in square meters
Rpa= Lpa/(kp*Apa)
Rpb= Lpb/(kp*Apb)

# Total Rparallel will be "Rpp"
Rpp= (Rb*Rpa*Rpb)/((Rb*Rpa)+(Rpa*Rpb)+(Rb*Rpb))

# Resistance for Outer wall side

ho= float(raw_input("Specify the convection coefficient of outer wall ")) # convection coefficient of outer wall in W/m.C
Lo= 0.25 # height of wall in meters
Ao= 0.25*1 # Area of wall in square meters
Ro= 1/(ho*Ao)

# The total resistance is sum of resistance due to conduction as well as convection

Rcond= (Rf+Rp1+Rpp+Rp2)
Rconv= (Ri+Ro)

Rtot= Rcond+Rconv # that is total resistance
print "The total resistance is " + str(Rtot) + " C/W"

#----------------------------------------#


T1= float(raw_input("Specify the room temperature in degree centigrade ")) # Room temperature in C
T2= float(raw_input("Specify the outside temperature in degree centigrade ")) # outside temperature in C
Qunit=(T1-T2)/Rtot # heat transfer through the unit in w
print "The heat transfer through unit is" + str(Qunit) + "w"

# On the basis of one unit, the total heat flux through wall in w

Awall= float(raw_input("Specify the area of wall in square.meters ")) # Wall area in m2
Aunit= float(raw_input("Specify the area of unit in square.meters ")) # unit area in m2

Qwall=Qunit * Awall/Aunit # Heat transfer rate in w
print "the heat transfer through wall is" + str(Qwall) + "w"

