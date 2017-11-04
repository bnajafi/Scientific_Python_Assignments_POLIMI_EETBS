area_total=3*5 #m^2
area_unit=0.25*1 #m^2
area_foam=0.25*1 #m^2
length_foam=0.03 #m
k_foam=0.026 #W /m C
area_plasterseries1=0.25*1 #m^2
length_plasterseries1=0.02 #m
area_plasterseries2=0.25*1 #m^2 
length_plasterseries2=0.02 #m
k_plaster=0.22 #W /m C
area_plasterparallel1=0.015*1 #m^2
length_plasterparallel1=0.16 #m
area_plasterparallel2=0.015*1 #m^2
length_plasterparallel2=0.16 #m
area_brick=0.22*1 #m^2
length_brick=0.16 #m
k_brick=0.72 #W /m C
h1=10 #W /m^2 C convective heat transfer coefficient inside
h2=25 #W /m^2 C convective heat transfer coefficient outside
t_in=20 #C temperature inside
t_out=-10 #C temperature inside
#R stands for resistance
Rp1=length_plasterparallel1/(k_plaster*area_plasterparallel1)
Rp2=length_brick/(k_brick*area_brick)
Rp3=length_plasterparallel2/(k_plaster*area_plasterparallel2)
R1=1/(h1*area_foam)
R2=length_foam/(k_foam*area_foam)
R3=length_plasterseries1/(k_plaster*area_plasterseries1)
R4=1/((1/Rp1)+(1/Rp2)+(1/Rp3))
R5=length_plasterseries2/(k_plaster*area_plasterseries2)
R6=1/(h2*area_plasterseries2)
R_total=R1+R2+R3+R4+R5+R6
Q_unit=(t_in-t_out)/R_total
Q_wall=Q_unit*(area_total/area_unit)
print 'the value of total resistance of the unit is'+' '+str(R_total)+' '+'C/W'
print 'the heat transfer rate of the unit'+' '+str(Q_unit)+' '+'W'
print 'the heat transfer rate of the wall'+' '+str(Q_wall)+' '+'W'