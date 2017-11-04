#  -----------MUHAMMAD Arslan----------
#  ---Example-D (One-dimentional heat transfer through multi-layer wall)---

#   Data given
hi=10
ho=25
T1=20 
T2=-10
W=1
kp=0.22
kb=0.72
kf=0.026

# Inner convection resistance

A=0.25*1 # Area
Ri=1/(hi*A)

# Foam layer resistance

A=0.25*1 # Area
Lf=0.03 
Rf=Lf/(kf*A)

# Plaster layer1 resistance

A=0.25*1 # Area
Lp1=0.02 
Rp1=Lp1/(kp*A)

# Sum of parallel resistances

# Brick resistance
A=0.22*1 # Area
Lb=0.16 
Rb=Lb/(kb*A)

# Parallel plaster1 resistance
A=0.015*1 # Area
Lpp1=0.16 
Rpp1=Lpp1/(kp*A)

# Parallel plaster2 resistance
A=0.015*1 # Area
Lpp2=0.16 
Rpp2=Lpp2/(kp*A)

Rb=1.0101
Rpp1=48.4848
Rpp2=48.4848

Rparallel=(Rb*Rpp1*Rpp2)/(Rpp1*Rpp2+Rb*Rpp1+Rb*Rpp2)

# Plaster layer2 resistance

A=0.25*1 # Area
Lp2=0.02 
Rp2=Lp2/(kp*A)

# Outer convection resistance

A=0.25*1 # Area
Ro=1/(ho*A)

# The total resistance of wall

Rtot=Ri+Rf+Rp1+Rparallel+Rp2+Ro
print "hence, the total resistance of the system is "+str(Rtot)+ "(deg C/W)"

# Heat transfer rate for Wall & Unit

Qunit=(T1-T2)/Rtot

Awall=15
Aunit=0.25

Qwall=Qunit*Awall/Aunit
print "Thus, the heat transfer rate for wall is "+str(Qwall)+ "(W)"