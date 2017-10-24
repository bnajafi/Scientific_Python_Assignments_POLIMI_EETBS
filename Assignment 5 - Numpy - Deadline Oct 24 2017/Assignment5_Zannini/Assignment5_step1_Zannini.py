resistance_names = np.array(["insideSurf","outsidedurf","foam layer","plaster layer","brick","plaster layer","plaster layer"])
resistance_types1 = np.array(["conv","conv","cond","cond","cond","cond","cond"])
resistence_types2 = np.array(["series","series","series","series","parallel","parallel","series"])
resistances_h = np.array([10,25,None,None,None,None,None])
resistances_k= np.array([None,None,0.026,0.22,0.72,0.22,0.22])
resistances_L= np.array([None,None,0.03,0.02,0.16,0.16,0.02])
resistances_A= np.array([0.25,0.25,0.25,0.25,0.22,0.03,0.25])

RValues= np.array(np.zeros(7))
RValues[resistance_types1=="conv"]=1/(resistances_h[resistance_types1=="conv"]*resistances_A[resistance_types1=="conv"])
RValues[resistance_types1=="cond"]=resistances_L[resistance_types1=="cond"]/(resistances_A[resistance_types1=="cond"]*resistances_k[resistance_types1=="cond"])

Rtot=RValues[resistence_types2=="series"].sum()+ ( (1/(RValues[resistence_types2=="parallel"])).sum() )**-1
print "The value of the total resistance is " + str(Rtot) + " K/W"