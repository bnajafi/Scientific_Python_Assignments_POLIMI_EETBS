# -*- coding: utf-8 -*-
import pandas as pd
area=0.25
in_convection=["conv", 10, None, None, None, 0]
foam=["cond", None, 0.026,0.03, None, 0]
plaster=["cond",None,0.22,0.02, None, 0]
p_plaster=["parallel cond", None, 0.22, 0.16, 0.03, 0]
brick=["parallel cond",None, 0.72, 0.16, 0.22, 0]
plaster2=["cond",None,0.22,0.02, None, 0]
out_convection=["conv", 25, None, None, None, 0]
resistances_names=["in convection","foam","plaster","bricks (parallel)","plaster (parallel)", "plaster again", "out convection"]
column_names=["type","h","k","L","area","Rvalue"]
Rtab=pd.DataFrame([in_convection, foam, plaster, p_plaster, brick, plaster2, out_convection], index=resistances_names, columns=column_names)
Rtab["Rvalue"][Rtab["type"]=='conv']=1.0/Rtab["h"][Rtab["type"]=='conv']/area
Rtab["Rvalue"][Rtab["type"]=='cond']=Rtab["L"][Rtab["type"]=='cond']/Rtab["k"][Rtab["type"]=='cond']/area
Rtab["Rvalue"][Rtab["type"]=='cond']=Rtab["L"][Rtab["type"]=='cond']/Rtab["k"][Rtab["type"]=='cond']/area
Rtab["Rvalue"][Rtab["type"]=='parallel cond']=Rtab["L"][Rtab["type"]=='parallel cond']/Rtab["k"][Rtab["type"]=='parallel cond']/Rtab["area"][Rtab["type"]=='parallel cond']
R=(Rtab["Rvalue"][Rtab["type"]!='parallel cond']).sum()+((1.0/Rtab["Rvalue"][Rtab["type"]=='parallel cond']).sum())**(-1)
print ''
print 'the total resistance is '+str(R)+' (for a 0.25 m^2 wall)'
print ''
print 'the heat transfer for a delta T of 25°C and an area of 15 m^2 is '+str(25/R*15/0.25)+ ' W'
print ''