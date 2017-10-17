#assignment1 step1  balaji krishnakanth.p

Lf = 0.03 #the length of form in m 
kf =0.026 # thermal conductivity of foam in degC/W
Af =0.25 # cross-sectional area of foam in m2

Lp = 0.02 # length of plaster in  m
kp =0.22 # thermal conductivity of plaster in degC/W
Ap =0.25 # cross-sectional area of plaster in m2

Lb = 0.16 #length of brick of form in m
kb =0.72# thermal conductivity of brick in degC/W
Ab =0.22 #cross-sectional area of brick in m2

Lbp= 0.16 #length of brick- plaster in m
Abp=0.015# cross-sectional area of brick-plaster region in m2

hi = 10.0 # convection heat transfer coefficient on the inner side
ho = 25.0 # convection heat transfer coefficient on the outer side 

Ri= 1/(hi*Af) # convection resistance on the inner side of the wall in (degC/W)
Rf= Lf/(kf*Af) # conductive resistance in foam in (degC/W)
Rp1=Lp/(kp*Ap) # conductive resistance in plaster on the inner side in (degC/W)
Rp2=Lp/(kp*Ap)# conductive resistance in plaster on the outer side in (degC/W)
Rb= Lb/(kb*Ab) # conductive resistance in brick in (degC/W)
Rbp1=Lbp/(kp*Abp) # conductive resistance in brick-plaster region in (degC/W)
Rbp2=Lbp/(kp*Abp)# conductive resistance in brick-plaster region in (degC/W)
Ro= 1/(ho*Af)# convection resistance on the outer side of the wall in (degC/W)

Rpr = 1/((1/Rb) +(1/Rbp1) +(1/Rbp2)) # equivalent resistance for all the parallell resistances in (degC/W)

Rtotal= Ri + Rf + Rp1 + Rpr + Rp2 + Ro # total resistance in (degC/W)

T1=20#indoor temperature
T2=-10#outdoor temperature
Awall=3.0*5.0
Qunit =  (T1-T2)/Rtotal # total heat transfer through the wall per unit width in W
Qtotal = Qunit*(Awall/Af) # total heat transfer through the wall in W

print "total resistance through the wall is " +str(Rtotal)+  "   K/W" 
print "total heat transfer through the wall per unit width is " +str(Qunit)+ "   W"
print "the total heat transfer through the wall is " + str(Qtotal)+  "   W "
