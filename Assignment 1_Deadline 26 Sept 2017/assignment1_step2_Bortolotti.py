#Data

Lf = float(raw_input("please enter the length of the foam layer in m ")) #L foam 
Lp = float(raw_input("please enter the length of the plaster layer in m "))#L plaster1 and plaster2
Lb = float(raw_input("please enter the length of the brick in m ")) #L Brick
Hw = float(raw_input("please enter the height of the wall in m ")) #H wall
Ww = float(raw_input("please enter the widht of the wall in m "))#W wall

A = 0.25
Aw = Hw*Ww #Area Wall
Au = 0.25 #Area Unit represents the area of series layers
Ap = 0.015
Ab = 0.22

h1 = float(raw_input("please enter the internal convection heat transfer coefficient in W/m2 degC ")) #convection int
h2 = float(raw_input("please enter the external convection heat transfer coefficient in W/m2 degC ")) #convection ext
Kf = float(raw_input("please enter the conductivity of the foam layer in W/m deg C ")) #k foam
Kp = float(raw_input("please enter the conductivity of the plaster layer in W/m deg C ")) #k plaster
Kb = float(raw_input("please enter the conductivity of the brick in W/m deg C ")) #k Brick

T1 = float(raw_input("please enter the internal temperature in deg C ")) #temp int
T2 = float(raw_input("please enter the external temperature in deg C ")) #temp ext


R1 = 1/(h1*A)
Rf = Lf/(Kf*A)
Rp1 = Lp/(Kp*A)
Rp2= Rp1
Rpc1 = Lb/(Kp*Ap)
Rpc2 = Rpc1
Rb = Lb/(Kb*Ab)
R2 = 1/(h2*A)

Rparallel = (1/Rb + 1/Rpc1 + 1/Rpc2 )**(-1)

Rtot = R1 + Rf + Rp1 + Rparallel + Rp2 + R2
print "the total resistance of the wall is " + str(Rtot) + "(deg C/W)"

Qunit = (T1 - T2)/Rtot
print "the rate of heat transfer thought the wall per each unit is " + str(Qunit) + "(W)"

Qwall = (Qunit*Aw)/Au
print "the total heat transfer thought the wall is " + str(Qwall) + "(W)"
