# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.2 (Step2) Date: 30/09/2017
#One dimensional problem:
#Example D: Heat loss through a composite wall
#Solution by dictionary
#Wall:
H_w=3.0 #wall height in m
W_w=5.0 #wall width in m
A_w=H_w*W_w #wall Area in m2
#Temperature:
T1=20.0 #indoor temperature in degC
T2=-10.0 #outdoor temperature in degC
#I have three diffefent sections: foam section, plaster-brick section, two plaster sections

#Foam section:
Rf={"length":0.03,"Area":0.25,"K":0.026}

#Plaster section:
Rp={"length":0.02,"Area":0.25,"K":0.22}

#Brick-plaster section:
Rp1={"length":0.16,"Area":0.015,"K":0.22}
Rp2={"length":0.16,"Area":0.015,"K":0.22}
Rb={"length":0.16,"Area":0.22,"K":0.72}

#The list where we store the resuslts, in order: the parallel resistances, the series and then the convective resistances
Q_R=[0,0,0]

#Calculating the conductive parallel resistances:
R_par=[Rp1,Rp2,Rb] #Three resistances in parallel

#I use the for cycle to solve the problem:
k=1

for i in R_par:
  s=i["length"]/(i["Area"]*i["K"])
  k=1/((1/k)+(1/s))
  
Q_R[0]=1/((1/k)-1)

#Calculating the conductive series resistances:
R_ser=[Rp,Rp,Rf] #Three resistances in series

#I use the for cycle to solve the problem:
k=0

for i in R_ser:
  s=i["length"]/(i["Area"]*i["K"])
  k=k+s
  
Q_R[1]=k

#Calculating the convective resistances:
R_c1={"Area":0.25,"H":10.0} #for the indoor
R_c2={"Area":0.25,"H":25.0} #for the outdoor
R_C=[R_c1,R_c2]

#I use the for cycle to solve the problem:
k=0

for i in R_C:
  s=1/(i["Area"]*i["H"])
  k=k+s
  
Q_R[2]=k

#Now I calculate the total resistance as:
R_tot=Q_R[0]+Q_R[1]+Q_R[2]
print "The total resistance is " +str(R_tot)+ "degC/W"

#I calculate the heat flux in the unit:
Q_t=(T1-T2)/R_tot
print "The heat flux in the unit is " +str(Q_t)+ "W"

#And the total heat flux in the areas:
Q_tot=Q_t*(A_w/Rf["Area"])
print "The total heat flux in the area is " +str(Q_tot)+ "W"



