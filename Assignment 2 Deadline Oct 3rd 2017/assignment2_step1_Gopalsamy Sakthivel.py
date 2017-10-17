area_total=3*5 #m^2
area_unit=0.25*1 #m^2
#the following list datatypes give the values of length(m), thermal conductivity(W/m C) and area(m^2) (in the same order) for each layer of the compound wall
Resistance_foam=[0.03,0.026,0.25]
Resistance_plasterseries1=[0.02,0.22,0.25]
Resistance_plasterseries2=[0.02,0.22,0.25]
Resistance_plasterparallel1=[0.16,0.22,0.015]
Resistance_plasterparallel2=[0.16,0.22,0.015]
Resistance_brick=[0.16,0.72,0.22]
#the following list datatypes give the values of  convective heat transfer coefficient(W/m^2 C) and surface area(m^2) (in the same order) for the convection inside and outside the room
Resistance_inside_conv=[10,0.25]
Resistance_outside_conv=[25,0.25]
t_in=20 #C temperature inside the room
t_out=-10 #C temperature outside the room
Conv_resistances=[Resistance_inside_conv,Resistance_outside_conv]
print(Conv_resistances)
TotalConvRes=0
for everyR in Conv_resistances:
    i=1/(everyR[0]*everyR[1])
    TotalConvRes+=i
Cond_ResistancesInParallel=[Resistance_plasterparallel1,Resistance_plasterparallel2,Resistance_brick]
x=0
for EveryR in Cond_ResistancesInParallel:
    j=EveryR[0]/(EveryR[1]*EveryR[2])
    x+=(1/j)
TotalParallelRes=(1/x)
Cond_ResistancesInSeries=[Resistance_foam,Resistance_plasterseries1,Resistance_plasterseries2]
TotalSeriesRes=0
for EveryRes in Cond_ResistancesInSeries:
    k=EveryRes[0]/(EveryRes[1]*EveryRes[2])
    TotalSeriesRes+=k
R_total=TotalSeriesRes+TotalParallelRes+TotalConvRes
Q_unit=(t_in-t_out)/R_total
Q_wall=Q_unit*(area_total/area_unit)
print 'the value of total resistance of the unit is'+' '+str(R_total)+' '+'C/W'
print 'the heat transfer rate of the unit'+' '+str(Q_unit)+' '+'W'
print 'the heat transfer rate of the wall'+' '+str(Q_wall)+' '+'W'