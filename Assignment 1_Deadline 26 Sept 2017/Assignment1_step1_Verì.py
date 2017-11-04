# R indoor
hi=10
A=0.25
Ri=1/(hi*A)
# R foam
Lf=0.03
kf=0.026
Rf=Lf/(kf*A)
# R plaster1
Lp1=0.02
kp1=0.22
Rp1=Lp1/(kp1*A)
# R plaster2
Rp2=Rp1
# R outdoor
h0=25
R0=1/(h0*A)
# R plaster upper side
Lpc1=0.16
kpc1=0.22
Apc1=0.015
Rpc1=Lpc1/(kpc1*Apc1)
# R plaster lower side
Rpc2=Rpc1
# R brick
Lb=0.16
kb=0.72
Ab=0.22
Rb=Lb/(kb*Ab)
# R parallel
Rpar=1/(1/Rb+1/Rpc1+1/Rpc2)
# R total
Rtot= Ri+Rf+Rp1+Rpar+Rp2+R0
# heat transfer unit
Tindoor=20
Toutdoor=(-10)
Qunit=(Tindoor-Toutdoor)/Rtot
#heat transfer through the wall
Awall=15
Qwall=Qunit*Awall/A