mat_library={"in surface": 0.12,"100 mm common brick": 0.12, "wood lapped": 0.14,"wood sheeting": 0.23,"insulation": 2.52,
"wood stud": 0.63,"gypsum wallboard": 0.079,"out surface": 0.03, "door":0.44, "asphalt single roofing": 0.077,
"urethane rigid foam 50 mm": 1.96}
convection=["in surface", "out surface"]
def wallCalc_withParallel (layerseries, layerparallel, ratio):
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
   return Utot
def wallCalc_onlyInSeries (layerseries):
    rser=0
    series=layerseries+convection
    for anylayer in series:
        Rser=mat_library[anylayer]
        rser=rser+Rser
    Rtot=rser
    Utot=1/Rtot    
    return Utot