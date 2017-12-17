import numpy as np

material_library_name =np.array(["outside_surface_winter","wood_bevel","wood_fiberboard","glass_fiber","wood_stud","gypsum_wallboard","inside_surface"])
material_library_Rvalue=np.array([0.030,0.14,0.23,2.45,0.63,0.079,0.12])
resistances_types = np.array(["serie","serie","serie","parallel","parallel","serie","serie"])
Resistances_SERIE= np.array(np.zeros(5))
Resistances_SERIE = material_library_Rvalue[resistances_types=="serie"]
Resistances_PARALLEL= np.array(np.zeros(2))
Resistances_PARALLEL = material_library_Rvalue[resistances_types=="parallel"]
firstratio=float(0.75)
Resistances_Rtotserie=Resistances_SERIE.sum()
Resistances_totale_finale= np.array(np.zeros(2))
Resistances_totale_finale = Resistances_PARALLEL+Resistances_Rtotserie
U=1/Resistances_totale_finale

A=U[0]
B=U[1]
print ("the thermal resistences of the FIRST parallel layer is ")+str(A*(1-firstratio))+" m^2/(deg*W)"
print ("the thermal resistences of the SECOND parallel layer is ")+str(B*firstratio)+" m^2/(deg*W)"

Utot=(A*firstratio)+(B*(1-firstratio))
Rt=1/Utot


    
    
