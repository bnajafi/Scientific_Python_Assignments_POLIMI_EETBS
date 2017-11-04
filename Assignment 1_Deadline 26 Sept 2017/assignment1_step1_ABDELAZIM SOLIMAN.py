#Heat Tranfer Ex. D 

#GIVEN:
  # FOR WALL 
Hwall = 3  #height
Wwall = 5  #width
Dwall = 1  #depth (assumption)
Awall = (Hwall*Wwall)  #area 
Aunit = 0.25 #unit area

  #FOR BRICK 
Lbr = 0.22 #length
Wbr = 0.16 #width
Dbr = 1.0 #depth
Abr = (Lbr*Dbr) #area brick
Kbr = 0.72 #TH.COND. of Brick

#FOR PLASTER 
Lver = 0.02   #length of vertical plaster
Lhor = 0.015  # length of Horizontal plaster 
Kpla = 0.22   #TH.COND. of PLASTER
Apla = (Lhor*Dwall) #area of plaster

#FOR FOAM 
Kf =  0.026   #TH.COND. of Foam
Lf = 0.03 #foam Length

#TEMP.
Tin = 20  #Indoor Temp.
Tout = -10  #outdoor Temp.

# CONVECTION H.T.C 
Hin = 10  #inner side
Hout = 25 # outer side


# The Six Resistance 
Ri = 1/(Hin*Aunit)  #inner side convection resist.
Ro = 1/(Hout*Aunit) #outer side convec. resist.
Rf = Lf/(Kf*Aunit)   # foam cond. resist.
Rbr = Lbr/(Kbr*Abr)  #brick cond. resist
Rvp = Lver/(Kpla*Aunit)  # Vertical plaster cond. resist.
Rhp= Lbr/(Kpla*Apla)  # Horiz. plaster cond. resist.

#Total Resistance
Rparallel = 1/((1/Rbr)+(1/Rhp)+(1/Rvp))
Rtot = Rparallel+Ri+Ro+Rf+Rvp+Rvp

#The Heat Transfer 
Qunit = (Tin -Tout)/ Rtot # H.T per unit
Qwall = Qunit * (Awall/Aunit)  #Total H.T 

print "Total Resist.is"+str(Rtot)
print "The rate of Heat trans. is "+str(Qwall)