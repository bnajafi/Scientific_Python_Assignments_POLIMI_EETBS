layers_wall_S=["woodBevel","woodFiberboard_13mm","woodStud_90mm","gypsumWallboard_13mm"]
layers_wall_I=["woodBevel","woodFiberboard_13mm","glassFiberInsulation_90mm","gypsumWallboard_13mm"]
ratio_I=0.75



def wall_calc_assignment(layers_wall_S,layers_wall_I,ratio_I):
    """This function receives two lists of layers, first one including the wood Studs, second one including the glass 
    fiber insulation, and finally the third parameter is a ratio of area corresponding to the previously mentioned criteria"""
    ratio_I=float(ratio_I)
    Material_library={"outsideSurfaceWinter":0.03,"woodBevel":0.14,"woodFiberboard_13mm":0.23,
    "glassFiberInsulation_90mm":2.45,"woodStud_90mm":0.63,"gypsumWallboard_13mm":0.079,"insideSurface":0.12}
    airOnTwoSides=["outsideSurfaceWinter","insideSurface"]
    layers_wall_complete1= layers_wall_S+airOnTwoSides
    layers_wall_complete2= layers_wall_I+airOnTwoSides
    ratio_S=1-ratio_I
    Rtot_S=0
    Rtot_I=0
    RValues_layers_S=[]
    RValues_layers_I=[]
    perimeter=50
    height=2.5
    Awall=0.8*perimeter*height
    Tin=22
    Tout=-2
    
    for anyLayer1 in layers_wall_complete1:
        RValue_layer1=Material_library[anyLayer1]
        Rtot_S=Rtot_S+RValue_layer1
        RValues_layers_S.append(RValue_layer1)
        print("this layer is "+anyLayer1)
        print("The value R for this layer is "+str(RValue_layer1)+" m2C/W")
        print("*********************************")
    Utot_S=1/Rtot_S
    print("The total R Value at Studs is "+str(Rtot_S)+" m2C/W")
    print("The total U Value at Studs is "+str(Utot_S)+" W/m2C")
    
    print("*********************************")
    print("*********************************")
    
    for anyLayer2 in layers_wall_complete2:
        RValue_layer2=Material_library[anyLayer2]
        Rtot_I=Rtot_I+RValue_layer2
        RValues_layers_I.append(RValue_layer2)
        print("this layer is "+anyLayer2)
        print("The value R for this layer is "+str(RValue_layer2)+" m2C/W")
        print("*********************************")
    Utot_I=1/Rtot_I    
    print("The total R Value between Studs is "+str(Rtot_I)+" m2C/W")
    print("The total U Value between Studs is "+str(Utot_I)+" W/m2C")
    
    print("\n")
    U_overall=Utot_S*ratio_S+Utot_I*ratio_I
    R_overall=1/U_overall
    print("The Overall R Value of the system is "+str(R_overall)+" m2C/W")
    print("The Overall U Value of the system is "+str(U_overall)+" W/m2C")
    
    
    Q_wall=Awall*U_overall*(Tin-Tout)
    
    results={"Thermal resistances layers S":RValues_layers_S,"Thermal resistances layers I":RValues_layers_I,
    "Total R of the wall":R_overall,"Total U of the wall":U_overall,"Rate of heat loss":Q_wall}
    return results
    
    
    

