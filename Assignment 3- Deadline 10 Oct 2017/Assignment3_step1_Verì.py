#Rseries
Material_library={"outsideSurface":0.03, "woodBevel":0.14, "woodFiberSheeting":0.23, "glassInsulation": 2.45,"woodStud":0.63, "gypsumWallboard":0.079, "insideSurface":0.12}
layers_series=["outsideSurface","woodBevel","woodFiberSheeting","gypsumWallboard","insideSurface"] 
layers_par=["glassInsulation", "woodStud"]
fArea1=0.75
fArea2=0.25
Rtot=0
RValues_series=[]
for anyLayer in layers_series:
    RValue_layer = Material_library[anyLayer]
    Rtot=Rtot+RValue_layer
    RValues_series.append(RValue_layer)
    print "this layer is: "+ anyLayer
    print "The value of R for this layer is: "+ str(RValue_layer)
    print "***************************************"
print "the total R Value is "+ str(Rtot)
print "**************************************"
print "**************************************"
#Rparallels:
RValues_par=[]
for anyLayer in layers_par:
    RValue_layer = Material_library[anyLayer]
    RValues_par.append(RValue_layer)
    print "this layer is: "+ anyLayer
    print "The value of R for this layer is: "+ str(RValue_layer)
    print "***************************************"
    print "***************************************"
R1=Rtot+RValues_par[0]
R2=Rtot+RValues_par[1]
U1=1/R1*fArea1
U2=1/R2*fArea2
Uoverall=U1+U2
Tin=22
Tout=-2
Areal=125
Ablazing=25
Awall=Areal-Ablazing
Qwall=Uoverall*Awall*(Tin-Tout)

