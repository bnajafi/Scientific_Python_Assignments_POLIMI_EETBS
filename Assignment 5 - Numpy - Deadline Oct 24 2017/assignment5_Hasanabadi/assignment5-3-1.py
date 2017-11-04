import numpy as np

jointLayer=np.array(["outsidesurface","gypsumwallboard","woodfiber","woodbevellapped","insidesurface"])
jointR=np.array([0.03,0.079,0.23,0.14,0.12])

parLayer=np.array(["glassfiberinsulation","woodstud"])
parR=np.array([0.7*90/25,0.63])

ratio=0.75
wallArea=50*2.5
deltaT=24
glazingRatio=0.2


[Utot,Rtot]=[((ratio/(jointR.sum()+parR[parLayer=="glassfiberinsulation"])+(1-ratio)/(jointR.sum()+parR[parLayer=="woodstud"]))),1/(ratio/(jointR.sum()+parR[parLayer=="glassfiberinsulation"])+(1-ratio)/(jointR.sum()+parR[parLayer=="woodstud"]))]
Q=int((1-glazingRatio)*wallArea*deltaT*Utot)
print "Total Heat Transfer Coefficient is " +str(Utot)+" W/m2.degreeC"
print "Total Heat Resistance is " +str(Rtot)+" m2.degreeC/W"
print "Total Heat Transfered through the Wall is " +str(Q)+" W"




