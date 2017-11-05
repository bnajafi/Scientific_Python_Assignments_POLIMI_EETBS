#Assignment 3#---A program to calculate U-factor,R-Value,Heat loss rate, later part is put into a function---
materialLibrary={"Wood bevel lapped siding":{"Rvalue":0.14,"length":13},"Wood fiberboard":{"Rvalue":0.23,"length":13},"Glass fiber insulation":{"Rvalue":0.68,"length":25},"Wood stud":{"Rvalue":0.63,"length":90},"Gypsum wallboard":{"Rvalue":0.079,"length":13},"insideSurface":{"Rvalue":0.12},"outsideSurfaceWinter":{"Rvalue":0.030}}
layersInseries=["insideSurface","outsideSurfaceWinter","Wood bevel lapped siding","Wood fiberboard","Gypsum wallboard"]
betweenStuds=layersInseries+["Glass fiber insulation"]
atStuds=layersInseries+["Wood stud"]
fractionBetweenstuds,RValuebetween,RValueat=0.75,0,0
for layer in betweenStuds:
    if(layer!="Glass fiber insulation"):
        RValuebetween+=materialLibrary[layer]["Rvalue"]
    else:
        RValuebetween+=materialLibrary[layer]["Rvalue"]*(90.0/materialLibrary[layer]["length"])      
for layer in atStuds:
    RValueat+=materialLibrary[layer]["Rvalue"]
Uoverall=round((fractionBetweenstuds*(1/RValuebetween)+(1-fractionBetweenstuds)*(1/RValueat)),3)
Roverall=round((1/Uoverall),2)
perimeter,height,glazingPercentage,outsideTemperature,insideTemperature=50,2.5,20,-2,22
wallArea=(1-(glazingPercentage/100.0))*perimeter*height
heatLoss=int(Uoverall*wallArea*(insideTemperature-outsideTemperature))
print("The overall heat transfer coefficient(U-factor) is : "+str(Uoverall)+" W/m^2 degC"+"\n"+"The overall unit therml resistance(R-Value) is : "+str(Roverall)+" m^2 degC/W"+"\n"+"The heat loss through the wall is: "+str(heatLoss)+" W")

