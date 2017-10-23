# Energy And Environmental Technologies For Building Systems : Assignment 03, Step-1

# Submitted By : Danish Ahmad Mir

# Assignment Based On Exercise-1 From Topic 1.3 (Determine the overall unit thermal resistance and the overall heat transfer coefficient)

def wallCalc_parallel(defineYourLayer):

    material_table = {"outsideSurface":0.03,"woodBevelLappedSliding_13mm_200mm":0.14,
    "woodFiberboard_13mm":0.23,"glassFiberIns_90mm":2.52,"woodStud_38mm_90mm":0.63,
    "gypsumWallboard_13mm":0.079,"insideSurface":0.12}
    
    conv_layer = ["outsideSurface","insideSurface"]
    
    
    yourNewLayer = defineYourLayer + conv_layer
    
    print "The layer consist of " + str(defineYourLayer)
    
    Rtotal = 0
    Rvalue_NewLayer = []
    
    for RNewLayer in yourNewLayer:
        Rvalue_new = material_table[RNewLayer]
        Rtotal = Rtotal + Rvalue_new
        Rvalue_NewLayer.append(Rvalue_new)
        
    print "Total Resistance in this layer is " + str(Rtotal) + " (m^2 DegC/W)"
    result = {"R total":Rtotal,"All R value of New Layer":Rvalue_NewLayer}
 
    return result


def wallCalc_series(defineYourLayer):

    material_table = {"outsideSurface":0.03,"woodBevelLappedSliding_13mm_200mm":0.14,
    "woodFiberboard_13mm":0.23,"glassFiberIns_90mm":2.52,"woodStud_38mm_90mm":0.63,
    "gypsumWallboard_13mm":0.079,"insideSurface":0.12,"wood50mm":0.44, "specialRoofUrethaneRigidFoam":3.85 }
    
    conv_layer = ["outsideSurface","insideSurface"]
     
    
    yourNewLayer = defineYourLayer + conv_layer
    
    print "The layer consist of " + str(defineYourLayer)
    
    Rtotal = 0
    Rvalue_NewLayer = []
    
    for RNewLayer in yourNewLayer:
        Rvalue_new = material_table[RNewLayer]
        Rtotal = Rtotal + Rvalue_new
        Rvalue_NewLayer.append(Rvalue_new)
        
    print "Total Resistance in this layer is " + str(Rtotal) + " (m^2 DegC/W)"
    result = {"R total":Rtotal,"All R value of New Layer":Rvalue_NewLayer}
 
    return result