import pandas as pd
Rinside_surface=["convective",10.0,None,None,0]
Rfoam=["conductive",None,3.0,0.026,0]
Rplastic_side1=["conductive",None,2.0,0.22,0]
Rplastic_side2=["conductive",None,2.0,0.22,0]
Routside_surface=["convective",25,None,None,0]
A=0.25
column_names=["type","h","L","k","Rvalue"]
index_names=["Rinside_surface","Rfoam","Rplastic_side1","Rplastic_side2","Routside_surface"]
Series_Layers=pd.DataFrame([Rinside_surface,Rfoam,Rplastic_side1,Rplastic_side2,Routside_surface],index=index_names,columns=column_names)
Series_Layers["Rvalue"][Series_Layers["type"]=="convective"]=1.0/(A*Series_Layers["h"][Series_Layers["type"]=="convective"])
Series_Layers["Rvalue"][Series_Layers["type"]=="conductive"]=Series_Layers["L"][Series_Layers["type"]=="conductive"]/(100*A*Series_Layers["k"][Series_Layers["type"]=="conductive"])
Rtotal_series=Series_Layers["Rvalue"].sum()
print " Total resistance for layers in series is :"+str(Rtotal_series)+" degree C/ W"
Rplastic1=["conductive",None,16.0,0.22,0.015,0]
Rplastic2=["conductive",None,16.0,0.22,0.015,0]
Rbrick=["conductive",None,16.0,0.72,0.22,0]
column_names=["type","h","L","k","Area","Rvalue"]
index_names=["Rplastic_layer1","Rbrick","Rplastic_layer2"]
Parallel_Layers=pd.DataFrame([Rplastic1,Rbrick,Rplastic2],index=index_names,columns=column_names)
Parallel_Layers["Rvalue"][Parallel_Layers["type"]=="conductive"]=Parallel_Layers["L"][Parallel_Layers["type"]=="conductive"]/(100*Parallel_Layers["Area"][Parallel_Layers["type"]=="conductive"]*Parallel_Layers["k"][Parallel_Layers["type"]=="conductive"])
Calculation_list=1/Parallel_Layers["Rvalue"][Parallel_Layers["type"]=="conductive"]
Rtotal_parallel=1/Calculation_list.sum()
print " Total resistance for layers in parallel is :"+str(Rtotal_parallel)+" degree C/ W"
total_resistance=Rtotal_series+Rtotal_parallel
print " Total resistance of this wall is :"+str(total_resistance)+" W/ degree C" 
Tin=20
Tout=-10
deltaT=Tin-Tout
Qunit=deltaT/total_resistance
print " Rate of heat transfer through one unit of area is :"+str(Qunit)+" W"
Height=3
Width=5
proportion=Height*Width/0.25
Q=Qunit*proportion
print " Heat transfer through wall is: "+str(Q)+" W"