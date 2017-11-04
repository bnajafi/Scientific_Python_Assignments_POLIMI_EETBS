# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.2 (Step1) Date: 30/09/2017
#One dimensional problem:
#Example D: Heat loss through a composite wall
#Solution by lists
#Wall:
H_w=3.0 #wall height in m
W_w=5.0 #wall width in m
A_w=H_w*W_w #wall Area in m2
#Temperature:
T1=20.0 #indoor temperature in degC
T2=-10.0 #outside temperature in degC
#I have three diffefent sections: foam section, plaster-brick section, two plaster sections

#Foam section:
Rf=[0.03,0.25,0.026] #in order: length, Area, conduction coefficient of foam

#Plaster section
Rp=[0.02,0.25,0.22] #in order: length, Area, conduction coefficient of plaster

#Brick-plaster section:
Rp1=[0.16,0.015,0.22] #in order: length Area, conduction coefficient of plaster1
Rp2=[0.16,0.015,0.22] #in order: length, Area, conduction coefficient of plaster2
Rb=[0.16,0.22,0.72] #in order: length, Area, conduction coefficient of brick

#The list where we store the resuslts, in order: the parallel resistances, the series and then the convective resistances
Q_R=[0,0,0]

#Calculating the conductive parallel resistances:
R_par=[Rp1,Rp2,Rb] #Three resistances in parallel

#I use the for cycle to solve the problem:
k=1

for i in R_par:
  s=i[0]/(i[1]*i[2])
  k=1/((1/k)+(1/s))
  
Q_R[0]=1/((1/k)-1)

#Calculating the conductive series resistances:
R_ser=[Rp,Rp,Rf] #Three resistances in series

#I use the for cycle to solve the problem:
k=0

for i in R_ser:
  s=i[0]/(i[1]*i[2])
  k=k+s
  
Q_R[1]=k

#Calculating the convective resistances:
R_c1=[0.25,10.0] #Area and convection coefficient in the indoor
R_c2=[0.25,25.0] #Area and convection coefficient in the outdoor
R_C=[R_c1,R_c2] #Two convective resistances

#I use the for cycle to solve the problem:
k=0

for i in R_C:
  s=1/(i[0]*i[1])
  k=k+s
  
Q_R[2]=k

#Now i calculate the total resistance as:
R_tot=Q_R[0]+Q_R[1]+Q_R[2]
print "The total resistance is " +str(R_tot)+ "degC/W"

#I calculate the heat flux in the unit:
Q_t=(T1-T2)/R_tot
print "The heat flux in the unit is " +str(Q_t)+ "W"

#And the total heat flux in the areas:
Q_tot=Q_t*(A_w/Rf[1])
print "The total heat flux in the area is " +str(Q_tot)+ "W"


  
  
