def wall_dispersion (layerseries, layerparallel, ratio):
    mat_library={"in surface": 0.12,"wood lapped": 0.14,"wood sheeting": 0.23,"insulation": 2.45,
    "wood stud": 0.63,"gypsum wallboard": 0.079,"out surface": 0.03}
    convection=["in surface", "out surface"]
    rser=0
    series=layerseries+convection
    for anylayer in series:
        Rser=mat_library[anylayer]
        rser=rser+Rser
    wallresistance=[]
    
    for anyylayer in layerparallel:
        rtot=0
        rtot=mat_library[anyylayer]
        wallresistance.append(rser+rtot)
    Ufirst=ratio[0]/wallresistance[0]
    Usecond=ratio[1]/wallresistance[1] 
    Utot=Ufirst+Usecond
    Rtot=1/Utot
    resistancelayers=layerseries+layerparallel+convection
    rrr={}
    for anylay in resistancelayers:
        value=mat_library[anylay]
        add={anylay:value}
        rrr.update(add) 
    result= {'U Total':Utot,'R total':Rtot}
    result.update(rrr)
    return result

serie=["wood lapped", "wood sheeting", "gypsum wallboard"]
paral=["insulation", "wood stud"]
farea=[0.75, 0.25]

aaa = wall_dispersion(serie, paral, farea)
print ("series ")+str(serie)
print ("parallel ")+str(paral)
print ('ratio ')+str(farea)
print ("the function wall_dispersion(series, parallel, ratio) gives: ")
print ('')
print aaa

    

        
        
    

