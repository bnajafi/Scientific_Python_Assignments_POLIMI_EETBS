#------------------------Wall Calculation Function------------------------------

# Name : Hendra Suryana Putra

#Definition
# stud_layer is the layer through the stud (without any insulation layer)
# ins_layer is the layer through the insulation (without any stud layer)
# conv_layer is the layer of air in the inside and outside of the wall
# fstud : the fraction of stud area compared to overall area
# fins : the fraction of insulation area compared to overall area
# Ustud : heat transfer coefficient of stud
# Uins : heat transfer coefficient of insulation
# Tin : Inside temperature of the wall
# Tout : Outside temperature of the wall
# Awall : The total area of the wall
# Qtot : The total heat transfer of the wall

def wallCalc_withParallel(defineYourLayer):

    material_table = {"outsideSurface":0.03,"woodBevelLappedSliding_13mm_200mm":0.14,
    "woodFiberboard_13mm":0.23,"glassFiberIns_90mm":2.52,"wood_50mm":0.44,"wood_100mm":0.88,"woodStud_38mm_90mm":0.63,
    "gypsumWallboard_13mm":0.079,"Asphalt_Shingle_Roofing":0.077,"Acoustic_Tile":0.32,"ConcreteBlockLightWeight_439mm":2.573,
    "insideSurface":0.12}
    
    conv_layer = ["outsideSurface","insideSurface"]
    
    # Calculate the total Resistance Value 
    
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
    # print result  
    return result


def wallCalc_withSeries(defineYourSeriesLayer):
    material_table = {"outsideSurface":0.03,"woodBevelLappedSliding_13mm_200mm":0.14,
    "woodFiberboard_13mm":0.23,"glassFiberIns_90mm":2.52,"wood_50mm":0.44,"wood_100mm":0.88,"woodStud_38mm_90mm":0.63,
    "gypsumWallboard_13mm":0.079,"Asphalt_Shingle_Roofing":0.077,"Acoustic_Tile":0.32,"ConcreteBlockLightWeight_439mm":2.573,
    "insideSurface":0.12}
    
    conv_layer = ["outsideSurface","insideSurface"]
    
    # Calculate the total Resistance Value 
    
    yourNewLayer = defineYourSeriesLayer + conv_layer
    
    print "The layer consist of " + str(defineYourSeriesLayer)
    
    Rtotal = 0
    Rvalue_NewLayer = []
    
    for RNewLayer in yourNewLayer:
        Rvalue_new = material_table[RNewLayer]
        Rtotal = Rtotal + Rvalue_new
        Rvalue_NewLayer.append(Rvalue_new)
        
    print "Total Resistance in this layer is " + str(Rtotal) + " (m^2 DegC/W)"
    result = {"R total":Rtotal,"All R value of New Layer":Rvalue_NewLayer}
    # print result  
    return result
