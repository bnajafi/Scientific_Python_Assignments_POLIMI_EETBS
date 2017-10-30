import numpy as np

Mlist=np.array(["Sout_Winter","Sin","Glass Insul.", "WoodStud", "Woodfiber", "WoodBevel", "Gyp.wall"])

Mvalues=np.array([0.03,0.12,2.52,0.63,0.23,0.14,0.079])

Mtype= np.array(["series","series","parallel","series","parallel","series","series"]) 

AreaRtio=0.75

R = Mvalues[Mtype =="series"].sum() + Mvalues[Mtype =="parallel"]

Uoll = AreaRtio / R[0] + ( 1- AreaRtio)/ R[1] 


Roll = 1 / Uoll
