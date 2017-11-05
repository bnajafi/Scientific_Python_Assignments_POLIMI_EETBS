import numpy as np

res_array=np.array(["Rci","Rco","Rf","Rp1","Rp2","Rpc1","Rpc2","Rb"])
res_types=np.array(["conv","conv","cond","cond","cond","cond","cond","cond"])
res_h=np.array([10.0,25.0,None,None,None,None,None,None])
res_k=np.array([None,None,0.026,0.22,0.22,0.22,0.22,0.72])
res_L=np.array([None,None,0.03,0.02,0.02,0.16,0.16,0.16])
res_A=np.array([0.25,0.25,0.25,0.25,0.25,0.015,0.015,0.22])
res_values=np.array(np.zeros(8))
res_values[res_types=="conv"]=1./(res_h[res_types=="conv"]*res_A[res_types=="conv"])
res_values[res_types=="cond"]=res_L[res_types=="cond"]/(res_k[res_types=="cond"]*res_A[res_types=="cond"])
res_values_series=np.array(res_values[0:len(res_values)-3])
res_values_parallel=np.array(1./res_values[len(res_values)-3:])

res_series_total=res_values_series.sum()
res_parallel_total=1./res_values_parallel.sum()
res_total=round((res_series_total+res_parallel_total),2)
T1,T2,Unit=20,-10,(3*5)/0.25
Qtotal=int(Unit*((T1-T2)/res_total))

print("The total effective thermal resistance is: "+str(res_total)+" degC/W")
print("The rate of heat transfer through the wall is "+str(Qtotal)+" Watt")

