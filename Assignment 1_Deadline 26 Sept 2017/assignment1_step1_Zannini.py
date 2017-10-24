Lf = 0.03
Lp = 0.02
Lb = 0.16
Kf = 0.026
Kp = 0.22
Kb = 0.72
h1 = 10
h2 = 25
A1 = 0.25 # 25 cm x 1 m
A2 = 0.22 # 22 cm x 1 m
A3 = 0.015 # 1.5 cm x 1 m

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

Rparallelo= 1/(2/R4_p + 1/R4_b)