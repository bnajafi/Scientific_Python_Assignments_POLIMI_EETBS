heightw= input("please enter the height of the wall in meters:  ")
heightw=float(heightw)
widthw= input("please enter the width of the wall in meters:  ")
widthw=float(widthw)

hp= input("please enter the height of the plaster in parallel (hp) in meters:  " )
hp=float(hp)
hb= input("please enter the height of the brick in parallel (hb) in meters:  ")
hb=float(hb)
wf= input("please enter the width of the foam (wf) in meters:  ")
wf=float(wf)
wp= input("please enter the width of the plaster (wp) in meters:  ")
wp=float(wp)
wb= input("please enter the width of the brick (wb) in meters:  ")
wb=float(wb)
Kb= input("please enter the conductivity of the brick in W/m2:  ")
Kb=float(Kb)
Kp= input("please enter the conductivity of the plaster in W/m2:  ")
Kp=float(Kp)
Kf= input("please enter the conductivity of the foam in W/m2:  ")
Kf=float(Kf)
Tin= input("please enter the inside temperature in Centigrades:  ")
Tin=float(Tin) 
Tout= input("please enter the outside temperature in Centigrades:  ")
Tout=float(Tout)
h1= input("please enter the inside convection heat transfer coefficient (h1):  ")
h1=float(h1)
h2= input("please enter the outside convection heat transfer coefficient (h2):  ")
h2=float(h2)

w=1.0 
hO=hb+2*hp

R1=1/(h1*hO*w)

Rf=wf/(Kf*hO*w)

Rp=wp/(Kp*hO*w)

Rp1=wb/(Kp*hp*w)

Rb=wb/(Kb*hb*w)

Gpr=2*(1/Rp1)+(1/Rb)

Rpr=1/Gpr

R2=1/(h2*hO*w)


Awall=heightw*widthw
Aunit=hO*w

Rtot=R1+Rf+2*Rp+Rpr+R2


Qunit=(Tin-Tout)/Rtot

Qtot=Qunit*(Awall/Aunit)

print("\n")
print (  "The rate of heat transfer through the wall is  " + str (Qtot)+ "W" )
