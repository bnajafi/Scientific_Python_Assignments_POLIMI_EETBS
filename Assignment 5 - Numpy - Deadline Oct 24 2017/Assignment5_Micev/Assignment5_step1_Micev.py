import numpy as np
List_of_layers=["inside surface","foam","plastic side 1", "plastic side 2","outside surface"]
layers_series=np.array(List_of_layers)
types_of_layers=["convective","conductive","conductive","conductive","convective"]
types_series=np.array(types_of_layers)
Thickness_of_layers=[None,3.0,2,2,None]
thickness_series=np.array(Thickness_of_layers)
K_of_layers=[None,0.026,0.22,0.22,None]
k_series=np.array(K_of_layers)
H_of_layers=[10.0,None,None,None,25]
h_series=np.array(H_of_layers)
A=0.25
resistance_values=np.array([0.0,0,0,0,0])
resistance_values[types_series=="convective"]=1/(A*h_series[types_series=="convective"])
resistance_values[types_series=="conductive"]=thickness_series[types_series=="conductive"]/(100*A*k_series[types_series=="conductive"])
resistance_total_series=resistance_values.sum()
layers_parallel=np.array(["plastic layer 1", "brick", "plastic layer 2"])
types_parallel=np.array(["conductive","conductive","conductive"]) #All layers transfer heat through conduction, but for applying NUMPY 
# I am using this.
thickness_parallel=np.array([16,16,16])
area_parallel=np.array([0.015,0.22,0.015])
k_parallel=np.array([0.22,0.72,0.22])
res_values_parallel=np.array([0.0,0,0])
res_values_parallel[types_parallel=="conductive"]=thickness_parallel[types_parallel=="conductive"]/(100*area_parallel[types_parallel=="conductive"]*k_parallel[types_parallel=="conductive"])
inv_res=1/res_values_parallel
resistance_total_parallel=inv_res.sum()
total_resistance=resistance_total_series+resistance_total_parallel
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

