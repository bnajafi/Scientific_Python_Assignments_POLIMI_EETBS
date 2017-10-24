Materials=np.array(["WoodBevelLappedSidings","FoamInsulation",
"GlassFiber_90mm","WoodStud","GypsumBoard","WoodFiberboardSheeting_13mm",
"insideSurf","outsideSurfSummer","outsideSurfWinter"])
Materials_values=np.array([0.14,0.98,2.45,0.63,0.079,0.23,0.12,0.044,0.03])

LayersSeries=np.array(["WoodBevelLappedSidings",None,None,None,"GypsumBoard","WoodFiberboardSheeting_13mm","insideSurf",None,"outsideSurfWinter"])
LayersParallel=["WoodStud","GlassFiber_90mm"]
RatioParallel=0.75
    
Rtot1=float(Materials_values[Materials==LayersSeries].sum() + Materials_values[Materials==LayersParallel[0]])
Rtot2=float(Materials_values[Materials==LayersSeries].sum() + Materials_values[Materials==LayersParallel[1]])

print "The value of the resistance of the wall with only Woodstud is: " + str(Rtot1)
print "The value of the resistance of the wall with only GlassFiber is: " + str(Rtot2)

Utot=( (Rtot1**-1)*(1-RatioParallel) )+( (Rtot2**-1) * RatioParallel )
print "the value of the total heat transfert coefficient (Utotal) is " +str(Utot) +" W/k m^2 "