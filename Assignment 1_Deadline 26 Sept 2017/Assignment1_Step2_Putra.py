
#-------------------- ASSIGNMENT 1 STEP 2 --------------------------------

# Name : Hendra Suryana Putra

# Heat loss through a composite wall

# I prefer to chose all of the variable (k,h,L,A) could be modify 
# So that we could determine the optimum Heat transfer rate base on that variable

# Thermal Conductivity and Convection Heat Transfer on Example D

# kp = 0.22
# kb = 0.72
# kf = 0.026
# h1 = 10
# h2 = 25

# Resistance of Inner Side Convection

Acv1 = float(raw_input("please enter the Area of Inner Side in m2 "))
h1 = float(raw_input("please enter the heat transfer coefficient of inner layer in W/m2 DegC "))

Rconv1=1/(h1*Acv1)

print "The resistance of Inner Side Convection is " +str(Rconv1)+ "(degC/W)"


# Resistance of Foam Layer

Lf = float(raw_input("please enter the Lenght of Foam Layer in m "))
Af = float(raw_input("please enter the Area of Foam Layer in m2 "))
kf = float(raw_input("please enter the Thermal Conductivity of foam layer in W/m DegC "))

Rf=Lf/(kf*Af) 

print "The resistance of foam layer is " +str(Rf)+ "(degC/W)"


# Resistance of Plaster 1 Layer

Lp1 = float(raw_input("please enter the Lenght of Plaster 1 Layer in m "))
Ap1 = float(raw_input("please enter the Area of Plaster 1 Layer in m2 "))
kp = float(raw_input("please enter the Thermal Conductivity of Plaster 1 layer in W/m DegC "))

Rp1=Lp1/(kp*Ap1) 

print "The resistance of Plaster 1 layer is " +str(Rp1)+ "(degC/W)"


# Resistance of Parallel Plaster 1 Layer

Lpp1 = float(raw_input("please enter the Lenght of Parallel Plaster 1 Layer in m "))
App1 = float(raw_input("please enter the Area of Parallel Plaster 1 Layer in m2 "))
kp = float(raw_input("please enter the Thermal Conductivity of Parallel Plaster 1 layer in W/m DegC "))

Rpp1=Lpp1/(kp*App1) 

print "The resistance of Parallel Plaster 1 layer is " +str(Rpp1)+ "(degC/W)"


# Resistance of Parallel Brick Layer

Lb = float(raw_input("please enter the Lenght of Parallel Brick Layer in m "))
Ab = float(raw_input("please enter the Area of Parallel Brick Layer in m2 "))
kb = float(raw_input("please enter the Thermal Conductivity of Brick layer in W/m DegC "))

Rb=Lb/(kb*Ab) 

print "The resistance of Parallel Brick layer is " +str(Rb)+ "(degC/W)"


# Resistance of Parallel Plaster 2 Layer

Lpp2 = float(raw_input("please enter the Lenght of Parallel Plaster 2 Layer in m "))
App2 = float(raw_input("please enter the Area of Parallel Plaster 2 Layer in m2 "))
kp = float(raw_input("please enter the Thermal Conductivity of Parallel Plaster 2 layer in W/m DegC "))

Rpp2=Lpp2/(kp*App2) 

print "The resistance of Parallel Plaster 2 layer is " +str(Rpp2)+ "(degC/W)"


# The Total of Parallel Resistance

A=1/Rpp1
B=1/Rb
C=1/Rpp2

D=A+B+C

Rpt=1/D

print "The Total of Parallel Resistance Layer is " +str(Rpt)+ "(degC/W)"

# Resistance of Plaster 2 Layer


Lp2 = float(raw_input("please enter the Lenght of Plaster 2 Layer in m "))
Ap2 = float(raw_input("please enter the Area of Plaster 2 Layer in m2 "))
kp = float(raw_input("please enter the Thermal Conductivity of Plaster 2 layer in W/m DegC "))

Rp2=Lp2/(kp*Ap2) 

print "The resistance of Plaster 2 layer is " +str(Rp2)+ "(degC/W)"


# Resistance of Outer Side Convection

Acv2 = float(raw_input("please enter the Area of Outer Side in m2 "))
h2 = float(raw_input("please enter the heat transfer coefficient of outer layer in W/m2 DegC "))

Rconv2=1/(h2*Acv2)

print "The resistance of Outer Side Convection is " +str(Rconv2)+ "(degC/W)"

# The Total Resistance

Rtot=Rconv1+Rf+Rp1+Rpt+Rp2+Rconv2

print "Thus, The Total Resistance of the System is " +str(Rtot)+ "(degC/W)"



#---------------------------------------------------------------------------

# Temperature

Tin = float(raw_input("please enter the Inner Temperature in DegC "))
Tout = float(raw_input("please enter the Outer Temperature in DegC "))

DT=Tin-Tout

print "The Temperature Difference of the System is " +str(DT)+ "(degC)"


#---------------------------------------------------------------------------

# Heat transfer Rate

Qtot=DT/Rtot

print "Thus, The Heat Transfer Rate through the system is " +str(Qtot)+ "(W)"

#---------------------------------------------------------------------------

# Heat transfer in various size of wall Area

print "We could also calculate the rate of heat transfer rate in various size of the wall"

Awall = float(raw_input("please enter Area of new preferred size of the wall in m2 "))

Qwall=Qtot*(Awall/Acv1)

print "Thus, The Heat transfer rate of the new preferred size of the wall will be " + str(Qwall) + "W"

