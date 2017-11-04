import numpy as np

layername= np.array(["inside","gypsum","woodfiber","woodbevel","outside","woodstud","glass"]) 
layervalue =np.array([0.12,0.079,0.23,0.14,0.03,0.63,2.45])

Studs=np.array(["inside","gypsum",
"woodfiber","woodbevel","outside",
"glass"
])

No_studs=np.array(["inside","gypsum",
"woodfiber","woodbevel","outside",
"woodstud"
])

Studsvalue=np.array(np.zeros(6))
No_studsvalue=np.array(np.zeros(6))

for ln in Studs:
    Studsvalue[Studs==ln] = layervalue[layername==ln]
    
for ln in No_studs:
    No_studsvalue[No_studs==ln] = layervalue[layername==ln]
    
Studstot= Studsvalue.sum()
No_studstot= No_studsvalue.sum()

Uover=0.25/No_studstot+0.75/Studstot
A=50*2.5*0.8
T1=22
T2=-2
Q=Uover*A*(T1-T2)

print "The value of the resistances in the insulated is the following: "+ str(No_studstot)
print "The value of the resistances in the studs is the following: "+ str(Studstot)
print "The total value of U is: "+str(Uover)
print "The total heat flux is: "+str(Q)
