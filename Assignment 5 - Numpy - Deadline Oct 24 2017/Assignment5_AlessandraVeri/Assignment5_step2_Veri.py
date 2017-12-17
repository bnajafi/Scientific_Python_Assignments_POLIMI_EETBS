import numpy as np
items_names=np.array(["outsideSurface", "woodBevel", "woodFiberSheeting", "glassInsulation","woodStud", "gypsumWallboard", "insideSurface"])
res_RValues=np.array([0.03,0.14,0.23,2.45,0.63,0.079,0.12])
res_series_names=np.array(["outsideSurface", "woodBevel", "woodFiberSheeting","gypsumWallboard", "insideSurface"])
res_par_names=np.array(["glassInsulation","woodStud"])
A_ratio=float(0.75)
RValue_series = np.zeros(res_series_names.size)
for layerName in res_series_names:
    RValue_series[res_series_names==layerName] = res_RValues[items_names==layerName]
print "The values of resistances in series are: "+str(RValue_series)
RValue_par=np.zeros(res_par_names.size)
print "******************************"
R_ser_tot=RValue_series.sum()
R_vector=np.zeros(RValue_par.size)
for layerName in res_par_names:
    RValue_par[res_par_names==layerName] = res_RValues[items_names==layerName]
    R_vector=RValue_par+R_ser_tot
print "The values of resistances in parallel are: "+str(RValue_par)
Utot=A_ratio/R_vector[0]+(1-A_ratio)/R_vector[1]
print "The value of total U is: "+str(Utot)
Area=0.8*2.5*50
T_outdoor=-2
T_indoor=22
Qtot=Utot*Area*(T_indoor-T_outdoor)
print "The total heat transfer through the wall is: "+str(Qtot)