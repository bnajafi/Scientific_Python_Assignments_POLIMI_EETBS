#Data
Lf = 0.03 #L foam 
Lp = 0.02 #L plaster1 and plaster2
Lb = 0.16 #L Brick
Hw = 3.0 #H wall
Ww = 5.0 #W wall

h1 = 10.0 #convection int
h2 = 25.0 #convection ext
Kf = 0.026 #k foam
Kp = 0.22 #k plaster
Kb = 0.72 #k Brick

T1 = 20.0 #temp int
T2 = -10.0 #temp ext

A = 0.25
Aw = Hw*Ww #Area Wall
Au = 0.25 #Area Unit represents the area of series layers
Ap = 0.015
Ab = 0.22

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
