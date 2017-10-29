area_total=3*5 #m^2
area_unit=0.25*1 #m^2
Resistance_foam={'length':0.03,'conductivity':0.026,'area':0.25}
Resistance_plasterseries1={'length':0.02,'conductivity':0.22,'area':0.25}
Resistance_plasterseries2={'length':0.02,'conductivity':0.22,'area':0.25}
Resistance_plasterparallel1={'length':0.16,'conductivity':0.22,'area':0.015}
Resistance_plasterparallel2={'length':0.16,'conductivity':0.22,'area':0.015}
Resistance_brick={'length':0.16,'conductivity':0.72,'area':0.22}
Resistance_inside_conv={'ConvHTcoeff':10,'area':0.25}
Resistance_outside_conv={'ConvHTcoeff':25,'area':0.25}
t_in=20 #C temperature inside the room
t_out=-10 #C temperature outside the room
Conv_resistances=[Resistance_inside_conv,Resistance_outside_conv]
TotalConvRes=0
for everyR in Conv_resistances:
    i=1/(everyR['ConvHTcoeff']*everyR['area'])
    TotalConvRes+=i
Cond_ResistancesInParallel=[Resistance_plasterparallel1,Resistance_plasterparallel2,Resistance_brick]
x=0
for EveryR in Cond_ResistancesInParallel:
    j=EveryR['length']/(EveryR['conductivity']*EveryR['area'])
    x+=(1/j)
TotalParallelRes=(1/x)
Cond_ResistancesInSeries=[Resistance_foam,Resistance_plasterseries1,Resistance_plasterseries2]
TotalSeriesRes=0
for EveryRes in Cond_ResistancesInSeries:
    k=EveryRes['length']/(EveryRes['conductivity']*EveryRes['area'])
    TotalSeriesRes+=k
R_total=TotalSeriesRes+TotalParallelRes+TotalConvRes
Q_unit=(t_in-t_out)/R_total
Q_wall=Q_unit*(area_total/area_unit)
print 'the value of total resistance of the unit is'+' '+str(R_total)+' '+'C/W'
print 'the heat transfer rate of the unit'+' '+str(Q_unit)+' '+'W'
print 'the heat transfer rate of the wall'+' '+str(Q_wall)+' '+'W'