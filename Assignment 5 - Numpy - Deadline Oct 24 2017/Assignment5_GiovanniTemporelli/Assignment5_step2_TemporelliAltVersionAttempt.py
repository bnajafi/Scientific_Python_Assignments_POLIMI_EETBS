import numpy as np

#materials_names = np.array(["WoodBevelLappedSliding","WoodFiberboardSheeting","GlassFiberInsulation","Woodstud","GypsumWallboard",
#"InsideSurface","OutsideSurfaceWinter"])
Rvalues = np.array([0.14,0.23,2.45,0.63,0.079,0.12,0.03])
resistances_types = np.array(["ser","ser","par","par","ser","ser","ser"])

area_fraction_ins = 0.75
R_vector = Rvalues[resistances_types=="ser"].sum()+Rvalues[resistances_types=="par"] #R_vector is an array of two element,the first element takes into account GlassFiberInsulation, the second one takes into account Woodstud
U_overall = area_fraction_ins/R_vector[0]+(1-area_fraction_ins)/R_vector[1]

Area=0.8*2.5*50
T_outdoor=-2
T_indoor=22
Q_overall=U_overall*Area*(T_indoor-T_outdoor)

print("The overall trasmittance is: " + str(U_overall)+" W/m2K"+" the overall heat loss is: "+str(Q_overall)+" W")
