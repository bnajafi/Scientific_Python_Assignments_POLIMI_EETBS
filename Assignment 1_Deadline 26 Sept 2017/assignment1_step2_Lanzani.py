T1=float(raw_input('please enter Tinf1 in degC '))
T2=float(raw_input('please enter Tinf2 in degC '))
h1=float(raw_input('please enter h1 in W/(degC*m2) '))
h2=float(raw_input('please enter h2 in W/(degC*m2) '))
l=float(raw_input('please enter total height in m '))
A=l*1
Lf=float(raw_input('please enter foam lenght in m '))
kf=float(raw_input('please enter foam k in W/(degC*m) '))
Lp=float(raw_input('please enter plaster lenght in m '))
kp=float(raw_input('please enter kp in W/(degC*m) '))
Lpc=float(raw_input('please enter central plaster lenght in m '))
lpc=float(raw_input('please enter central plaster height in m '))
lpb=float(raw_input('please enter brick height in m '))
kb=float(raw_input('please enter kb in W/(degC*m) '))

Rsi=1/(h1*A)
Rse=1/(h2*A)
R1=L1/(A*k1)
Rp1=Lp1/(A*kp)
Rp2=Rp1
Rpc1=Lpc/(lpc*kp)
Rpc2=Rpc1
Rb=Lpc/(lpb*kb)
invRp=1/Rpc1+1/Rpc2+1/Rb
Rp=1/invRp
RT=Rsi+Rse+R1+Rp1+Rp+Rp2
print 'Rt is '+ str(RT)+ ' degC/W'

Hw=float(raw_input('please enter wall height in m '))
Lw=float(raw_input('please enter wall lenght in m '))
Aw=Hw*Lw
Q=(T1-T2)/RT
Qw=Q*(Aw/A)
print 'Qw is '+ str(Qw)+ ' W'
