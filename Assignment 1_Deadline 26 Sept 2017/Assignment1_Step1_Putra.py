
#-------------------- ASSIGNMENT 1 STEP 1 -------------------------------

# Name : Hendra Suryana Putra

# Heat loss through a composite wall

# Thermal Conductivity and Convection Heat Transfer on Example D

kp = 0.22
kb = 0.72
kf = 0.026
h1 = 10
h2 = 25
A = 0.25


# Resistance of Inner Side Convection

Rconv1=1/(h1*A)


# Resistance of Foam Layer

Lf = 0.03
Rf=Lf/(kf*A) 


# Resistance of Plaster 1 Layer

Lp1 = 0.02
Rp1=Lp1/(kp*A) 


# Resistance of Parallel Plaster 1 Layer

Lpp1 = 0.16
App1 = 0.015
Rpp1=Lpp1/(kp*App1) 


# Resistance of Parallel Brick Layer

Lb = 0.16
Ab = 0.22
Rb=Lb/(kb*Ab) 


# Resistance of Parallel Plaster 2 Layer

Rpp2=Lpp1/(kp*App1) 


# The Total of Parallel Resistance

X=1/Rpp1
Y=1/Rb
Z=1/Rpp2

D=X+Y+Z

Rpt=1/D


# Resistance of Plaster 2 Layer

Lp2 = 0.02
Rp2=Lp2/(kp*A) 


# Resistance of Outer Side Convection

Rconv2=1/(h2*A)

# The Total Resistance

Rtot=Rconv1+Rf+Rp1+Rpt+Rp2+Rconv2

print "Thus, The Total Resistance of the System is " +str(Rtot)+ "(degC/W)"

#---------------------------------------------------------------------------

# Temperature

Tin = 20
Tout = -10

DT=Tin-Tout

#---------------------------------------------------------------------------

# Heat transfer Rate

Qtot=DT/Rtot

print "Thus, The Heat Transfer Rate through the system is " +str(Qtot)+ "(W)"

