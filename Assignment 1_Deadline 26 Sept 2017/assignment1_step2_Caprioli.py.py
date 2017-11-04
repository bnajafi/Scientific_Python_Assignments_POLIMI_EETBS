#Assumption in the exD that Aunit consist of 1m width
W=float(raw_input("please enter the width Ltot in m"))
#Geometric data
Ltot=float(raw_input("please enter the lenght Ltot in m"))
Htot=float(raw_input("please enter the width Ltot in m"))
Atot=Htot*Ltot

#Brick
Lbr=float(raw_input("please enter the lenght Lbr in m"))
Hbr=float(raw_input("please enter the height Hbr in m"))
kbr=0.72
Abr=Hbr*W

#Plaster
Hpl1=float(raw_input("please enter the height Hpl1 in m"))
Lpl1=float(raw_input("please enter the lenght Lpl1 in m"))
Lpl2=Lpl1
Hpl2=Hpl1
Apl1=Hpl1*W
Apl2=Apl1
kpl=0.22

#upper and under brick
Hpl=float(raw_input("please enter the height Hpl in m"))
Lpltot=Lbr
Apl=Hpl*W

#Foam
Hf=float(raw_input("please enter the height Hf in m"))
Lf=float(raw_input("please enter the lenght Lf in m"))
kf=0.026
Af=Hf*W

#Temperature and convective coefficients
Tinf1=float(raw_input("please enter the temperature Tinf1 in degC"))
Tinf2=float(raw_input("please enter the temperature Tinf2 in degC"))
h1=10
h2=25 
Aunit=Af

#Calculating resistence
R1=1/(h1*A)
Rf=Lf/(kf*Af)
Rpl1=Lpl1/(kpl*Apl1)
Rpl2=Rpl1
R2=1/(h2*A)
Rpc1=Lbr/(kpl*Apl*0.5)
Rpc2=Rpc1
Rbr=Lbr/(kbr*Abr)

Rparallel=(1/Rpc1+1/Rpc2+1/Rbr)**-1
Rtot=Rparallel+R1+Rf+Rpl1+Rpl2+R2

#Heat flowrate
Qdote=(Tinf1-Tinf2)/Rtot
Qwall=Qdote*(Atot/Aunit)

#Printing results
print("the total resistence is ")+str(Rtot)+" degC/W" 
print("the heat flowarate is ")+str(Qwall)+" W"


