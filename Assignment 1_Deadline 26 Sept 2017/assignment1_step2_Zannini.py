Lf = float(raw_input("please enter the lenght of the foam layer in m: "))
Lp = float(raw_input("please enter the lenght of the plaster layer in m: "))
Lb = float(raw_input("please enter the lenght of the brick in m: "))
Kf = float(raw_input("please enter the conductivity of the foam layer in W/m C: "))
Kp = float(raw_input("please enter the conductivity of the plaster layer in W/m C: "))
Kb = float(raw_input("please enter the conductivity of the brick in W/m C: "))
h1 = float(raw_input("please enter the value of the convection heat transfer coefficients on the inner side of the wall in W/m2: "))
h2 = float(raw_input("please enter the value of the convection heat transfer coefficients on the outer side of the wall in W/m2: "))
A1 = 0.25 # 25 cm x 1 m
A2 = 0.22 # 22 cm x 1 m
A3 = 0.0015 # 1.5 cm x 1 m

R1 = 1/(h1*A1)
R2 = Lf/(Kf*A1)
R3 = Lp/(Kp*A1)
R4_p = Lb/(Kp*A3)    # R4 is the total resistence of the parellel of R4_p (twice) and R4_b
R4_b = Lb/(Kb*A2)
R5 = 1/(h2*A1)
Rtot = R1+R2+R3*2+1/(2/R4_p + 1/R4_b)+R5 
print "the value of Rtot is " + str(Rtot)+" C/W "
T1=20
T2=-10
Qtot = (T1-T2)/Rtot
print "the value of Qtot is " + str(Qtot)+" W "
Awall= 15
Qwall = Qtot*(Awall/A1)
print "the value of Qwall is " + str(Qwall)+" W "