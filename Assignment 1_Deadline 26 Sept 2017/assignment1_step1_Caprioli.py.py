#Assumption that Aunit consist of 1m width
#Geometric data
Htot=float(3)
Ltot=float(5)

#Brick
Lbr=float(0.16)
Hbr=float(0.22)
kbr=float(0.72)

#Foam
Lf=float(0.03)
Hf=float(0.25)

#Plaster
Hpl1=0.25
Lpl1=0.02
Hpl2=Hpl2
Lpl2=Lpl1
kpl=0.22

#Upper and under brick
Lpc=0.16
Hpc=0.03

#Temperature
Tinf1=20
Tinf2=-10

#Convective coefficients
h1=10
h2=25

#Area
Atot=Htot*Ltot
Af=Hf*1
Apl1=Hpl1*1
Apl2=Apl1
Apc=Hpc*1

#Calculating resistence
R1=(h1*Af)**-1
Rf=Lf/(kf*Af)
Rpl1=Lpl1/(kpl*Apl1)
Rpl2=Rpl1
R2=(h2*Apl2)**-1
Rpc1=Lbr/(kpl*0.5*Apc)
Rpc2=Rpc1
Rbr=Lbr/(kbr*Abr)

#Parallel resistence and total resistence
Rparallel=((1/Rpc1)+(1/Rpc2)+(1/Rbr))**(-1) #different from class exercise Rparallel=1.03
Rtot=Rparallel+R1+Rf+Rpl1+Rpl2+R2

#Heat flowrate
Qdote=(Tinf1-Tinf2)/Rtot
Aunit=0.25*1
Qwall=Qdote*(Atot/Aunit)

#Printing results
print("the total resistence is ")+str(Rtot)+" degC/W"
print("the heat flowrate is ")+str(Qwall)+ " W"




