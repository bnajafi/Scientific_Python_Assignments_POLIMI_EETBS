heightw=3
widthw=5
ho=0.25
hp=0.015
hb=0.22
w=1
wf=0.03
wp=0.02
wb=0.16
Kb=0.72
Kp=0.22
Kf=0.026
Tin=20
Tout=-10
h1=10
h2=25

R1=1/(h1*ho*w)
Rf=wf/(Kf*ho*w)
Rp=wp/(Kp*ho*w)
Rp1=wb/(Kp*hp*w)
Rb=wb/(Kb*hb*w)
Gpr=2*(1/Rp1)+(1/Rb)
Rpr=1/Gpr
R2=1/(h2*ho*w)

Awall=heightw*widthw
Aunit=ho*w

Rtot=R1+Rf+2*Rp+Rpr+R2
Qunit=(Tin-Tout)/Rtot

Qtot=Qunit*(Awall/Aunit)
