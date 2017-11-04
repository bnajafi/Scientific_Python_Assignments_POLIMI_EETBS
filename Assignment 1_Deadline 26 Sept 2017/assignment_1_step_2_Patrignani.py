A1= float(raw_input("please enter the outern area of a single unit in m2  "))
h1= float(raw_input("please enter the first convection heat transfer coefficient in W/m2  "))
Ri=1/(h1*A1)
print "The first convective resistence is " + str(Ri) + " degC/W"


h2= float(raw_input("please enter the second convection heat transfer coefficient in W/m2  "))
Ri2=1/(h2*A1)
print "The second convective resistence is " + str(Ri2) + " degC/W"


kf= float(raw_input("please enter the conductivity of the foam in W/mK  "))
Lf= float(raw_input("please enter the thickness of the foam in m  "))
Rf=Lf/(kf*A1)
print "The resistence of the foam layer is " + str(Rf) + " degC/W"


kp1= float(raw_input("please enter the conductivity of the plaster layer in W/mK  "))
Lp1= float(raw_input("please enter the thickness of the vertical plaster layer in m  "))
Rp1=Lp1/(kp1*A1)
print "The resistence of the vertical plaster layer is " + str(Rp1) + " degC/W"


Lb= float(raw_input("please enter the thickness of the brick in m  "))
A2= float(raw_input("please enter the front area of the horizontal plaster layer in m2  "))
Rpc1=Lb/(kp1*A2)
print "The resistence of the horizontal plaster layer is " + str(Rpc1) + " degC/W"


kb= float(raw_input("please enter the conductivity of the brick in W/mK  "))
Ab= float(raw_input("please enter the front area of the brick in m2  "))
Rb=Lb/(kb*Ab)
print "The resistence of the brick is " + str(Rb) + " degC/W"


Rparallel=(2/Rpc1)+(1/Rb)
Rseries=Ri + Rf + Rp1 + Rparallel + Rp1 + Ri2
print "The equivalent in parallel resistence is equal to 1/Rpc1 + 1/Rpc2 + 1/Rb = " + str(Rparallel) + " degC/W"
print "The equivalent in series resistence is equal to Ri + Rfoam + Rp1 + Rparallel + Rp2 + Ri2 = " + str(Rseries) + " degC/W"


T1= float(raw_input("please enter the indoor temperature "))
T2= float(raw_input("please enter the outdoor temperature "))
Qu=(T1-T2)/Rseries
Qwall=Qu*60.0
print "The rate of heat transfer across one unit of the wall is " + str(Qu) + " W"
print "The rate of heat transfer across the whole wall is " + str(Qwall) + "W"