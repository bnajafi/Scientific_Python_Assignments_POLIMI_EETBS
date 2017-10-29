k_foam=float(raw_input("please enter the thermal conductivity of the foam in W/m C  "))
k_plaster=float(raw_input("please enter the thermal conductivity of the plaster in W/m C  "))
k_brick=float(raw_input("please enter the thermal conductivity of the brick in W/m C  "))
h1=float(raw_input("please enter the inside convective heat transfer coefficient in W/m^2 C  "))
h2=float(raw_input("please enter the outside convective heat transfer coefficient in W/m^2 C  "))
t_in=float(raw_input("please enter the inside temperature in degree C  "))
t_out=float(raw_input("please enter the outside temperature in degree C  "))
area_total=float(raw_input("please enter the total area of the wall in m^2  "))
length_foam=float(raw_input("please enter the length of the foam in the unit in m  "))
width_foam=float(raw_input("please enter the width of the foam in the unit in m  "))
length_plasterseries1=float(raw_input("please enter the length of the plasterseries1 in the unit in m  "))
width_plasterseries1=float(raw_input("please enter the width of the plasterseries1 in the unit in m  "))
length_plasterseries2=float(raw_input("please enter the length of the plasterseries2 in the unit in m  "))
width_plasterseries2=float(raw_input("please enter the width of the plasterseries2 in the unit in m  "))
length_plasterparallel1=float(raw_input("please enter the length of the plasterparallel1 in the unit in m  "))
width_plasterparallel1=float(raw_input("please enter the width of the plasterparallel1 in the unit in m  "))
length_plasterparallel2=float(raw_input("please enter the length of the plasterparallel2 in the unit in m  "))
width_plasterparallel2=float(raw_input("please enter the width of the plasterparallel2 in the unit in m  "))
length_brick=float(raw_input("please enter the length of the brick in the unit in m  "))
width_brick=float(raw_input("please enter the width of the brick in the unit in m  "))
if ((width_foam==width_plasterseries1)and(width_plasterseries1==width_plasterseries2)and(length_plasterparallel1==length_plasterparallel2)and(length_plasterparallel1==length_brick)and((width_plasterparallel1+width_brick+width_plasterparallel2)==(width_foam))):
    area_unit=width_foam*1
    area_plasterparallel1=width_plasterparallel1*1
    area_plasterparallel2=width_plasterparallel2*1
    area_plasterseries1=width_plasterseries1*1
    area_plasterseries2=width_plasterseries2*1
    area_foam=width_foam*1
    area_brick=width_brick*1
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
else:
    print 'the input values are not compatible with the given problem structure'