import pandas as pd
Res1=["conv",10,None,None,0.25,0]
Res2=["conv",25,None,None,0.25,0]
Res3=["cond",None,0.03,0.026,0.25,0]
Res4=["cond",None,0.02,0.22,0.25,0]
Res5=["cond",None,0.02,0.22,0.25,0]
Res6=["cond",None,0.16,0.22,0.015,0]
Res7=["cond",None,0.16,0.22,0.015,0]
Res8=["cond",None,0.16,0.72,0.22,0]
RowHeader= ["R1","R2","R3","R4","R5","R6","R7","R8"]
columnHeader=["Res_type","h","L","k","Area","ResValue"]
ResDF=pd.DataFrame([Res1,Res2,Res3,Res4,Res5,Res6,Res7,Res8],index=RowHeader,columns=columnHeader)
ResDF["ResValue"][ResDF['Res_type']=='cond']=ResDF['L']/(ResDF['k']*ResDF['Area'])
ResDF["ResValue"][ResDF['Res_type']=='conv']=1/(ResDF['h']*ResDF['Area'])
RSeries=ResDF.loc[:"R5","ResValue"]
Rparallel=1/ResDF.loc["R6":,"ResValue"]
ResTot=round(RSeries.sum()+(1/(Rparallel.sum())),4)
area_total=3*5 #m^2
area_unit=0.25*1 #m^2
t_in=20 #C temperature inside the room
t_out=-10 #C temperature outside the room
Q_unit=(t_in-t_out)/ResTot
Q_wall=Q_unit*(area_total/area_unit)
print 'the value of total resistance of the unit is'+' '+str(ResTot)+' '+'C/W'
print 'the heat transfer rate of the unit'+' '+str(Q_unit)+' '+'W'
print 'the heat transfer rate of the wall'+' '+str(Q_wall)+' '+'W'