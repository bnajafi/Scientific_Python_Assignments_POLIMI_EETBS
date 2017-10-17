B = 1 # assume width=1m

Lf =float (raw_input(" enter the length of foam in m "))
kf = float (raw_input(" enter the thermal conductivity of foam in W/m.C "))
Hf =0.25  # height of foam in m
Af =Hf*B # cross-sectional area of foam in m2

Lp =float (raw_input(" enter the length of plaster in m "))
kp =float (raw_input("enter the thermal conductivity of plaster in W/m.C "))
Hp =0.25 #height of plaster in m
Ap =Hp*B # cross-sectional area of plaster in m2

Lbp=float (raw_input("please enter the length of brick- plaster in m "))
Hbp=0.015 # height of brick-plaster region in m
Abp=Hbp*B# cross-sectional area of brick-plaster region in m2

Lb = float (raw_input("please enter the length of  brick  in m "))
kb =float (raw_input("please enter the thermal conductivity of brick in W/m.C "))
Hb =0.22 # height of brick in m
Ab =Hb*B #cross-sectional area of brick in m2

Hi=10#heat transfer coefficient inside
Ho=25#heat transfer coefficient outside

Ri=1/(Hi*Af)#resistance on inner side of the wall
Rf=Lf/(kf*Af)#resistance in foam
Rp1=Lp/(kp*Ap) #resistance in plaster region on the inner side in (C/W)
Rb= Lb/(kb*Ab) #resistance in brick in (C/W)
Rbp1=Lbp/(kp*Abp) #resistance in brick-plaster region in (C/W)
Rbp2=Lbp/(kp*Abp)#resistance in brick-plaster region in (C/W)
Rp2=Lp/(kp*Ap)# resistance in plaster region on the outer side in (C/W)
Ro= 1/(Ho*Af)# resistance on the outer side of the wall in (C/W)

Rpr = 1/((1/Rb) +(1/Rbp1) +(1/Rbp2)) # equivalent resistance for all the parallell resistances

Rtotal= Ri + Rf + Rp1 + Rpr + Rp2 + Ro # total resistance in (C/W)

T1=20# Indoor temp of wall in C
T2=-10# outdoor temp of wall in C

Qunit =  (T1-T2)/Rtotal #total heattransfer through the wall 

Awall= 3.0*5.0

Qtotal = Qunit*(Awall/Af) # total heat transfer through the wall in w

print "total resistance through the wall is " +str(Rtotal)+  "   K/W" 
print "total heat transfer through the wall per unit width is " +str(Qunit)+ "   W"
print "the total heat transfer through the wall is " + str(Qtotal)+  "   W "


