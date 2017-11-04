import numpy as np

 #this is for series resistance
 
resistance_names_s=np.array(["R1","R2","R3","R4","R5"]) #definition of list of resistances
resistance_type_s=np.array(["conv","cond","cond","cond","conv"]) #types of resistances
resistance_h=np.array([10,None,None,None,25])
resistance_k=np.array([None,0.026,0.22,0.22,None])
resistance_L=np.array([None,0.03,0.02,0.02,None])
Rvalues_serie=np.array(np.zeros(5))

Rvalues_serie[resistance_type_s=="conv"]=1.0/resistance_h[resistance_type_s=="conv"]
Rvalues_serie[resistance_type_s=="cond"]=resistance_L[resistance_type_s=="cond"]/resistance_k[resistance_type_s=="cond"]

Resistances_tot=sum(Rvalues_serie)

#now I calculate the parallel resistance

resistance_names_p=np.array(["RP1","RP2","RP3"])
resistance_type_p=np.array(["cond","cond","cond"]) 
resistance_k=np.array([0.22,0.72,0.22])
resistance_L=np.array([0.02,0.16,0.02])
Rvalues_parallel=np.array(np.zeros(3))

Rvalues_parallel[resistance_type_p=="cond"]=resistance_L[resistance_type_s=="cond"]/resistance_k[resistance_type_s=="cond"] #calcule single resistances
Resistances_parallel_sum=Rvalues_parallel.sum() #sum of resistances
Resistances_parallel_prod=Rvalues_parallel[0]*Rvalues_parallel[1]*Rvalues_parallel[2] #product of resistances
R_parallel=Resistances_parallel_prod/Resistances_parallel_sum #final parallel resistance

Resistances_tot=Resistances_tot+R_parallel #total resistance