# -*- coding: utf-8 -*-
#HEAT TRANSFER LOSS 
print "Let's calculate the heat flux loss with the Overall heat transfer coefficient\n"

#Dictionary with unit thermal resistance of common components used in buildings. 
Material_Library = {"Outside_surface_Summer":0.044, "Outside_surface_Winter":0.030,"Inside_surface": 0.12,
                "Insulation_Glass_Fiber_90mm":2.45, "WoodStud_90mm":0.63, "WoodFiberboard": 0.23, 
                "Stucco_25":0.037, "WoodBevel_13x200": 0.14, "Gypsum_13mm":0.079}

def wall_cal(L_WS, L_GF, A_GF):
    AirOnTwoSides = ["Outside_surface_Winter", "Inside_surface"] #List where both inside and outside of wall is defined. 
    
    Layers_WoodStud = AirOnTwoSides + L_WS # The sum of all layers.
    Rtot_Stud = 0 
    Resistances={}
    
    for anyLayer in Layers_WoodStud:
        RValue = Material_Library[anyLayer]
        Rtot_Stud = Rtot_Stud + RValue
        Dict1={anyLayer:RValue} 
        Resistances.update(Dict1)
           
    
        #FOR GLASS FIBER
    Layers_GlassFiber = AirOnTwoSides + L_GF #For this case, 
    Rtot_Fiber = 0
        
    for anyLayer in Layers_GlassFiber:
        RValue = Material_Library[anyLayer]
        Rtot_Fiber = Rtot_Fiber + RValue
        Dict1={anyLayer:RValue} 
        Resistances.update(Dict1)
    
    U_Stud = 1/(Rtot_Stud) #Overall heat transfer coefficient, which is the inverse of the specific resistance.
    U_Fiber = 1/(Rtot_Fiber)
    
    U_Total = (A_GF)*(U_Fiber) + (1-A_GF)*(U_Stud)
    R_Total = 1/U_Total
    
    results = {"U_Total":U_Total, "R_Tot": R_Total, "Dict":Resistances}
    return results 


#EXAMPLE D

Layers_Wall_Studs = ["WoodBevel_13x200","WoodFiberboard","WoodStud_90mm","Gypsum_13mm"] #A list considering just Woodstud
Layers_Wall_Fiber = ["WoodBevel_13x200","WoodFiberboard","Insulation_Glass_Fiber_90mm","Gypsum_13mm"] #Considering the layers in series including Glass fiber insulation
A_GlassFiber = 0.75

Rtotal = wall_cal(Layers_Wall_Studs,Layers_Wall_Fiber,A_GlassFiber)#FUnction

#Calculation of heat loss of a house in Las Vegas, Nevada
T_inside = 22 #Temperature inside the building
T_outside = -2 #Temperature outside, depending on the season - Winter: for this case

Q =(Rtotal["U_Total"])*(T_inside - T_outside)

Perimeter = 50
Wall_height = 2.5
Area_wall = 0.8*Perimeter*Wall_height #It is assumed to have 20% of wall area is occupied by glazing.

Qtot = Area_wall*Q

print "All the layers of the wall are ",(Rtotal["Dict"])
print "The Overall heat transfer coefficient (U) is "+str(Rtotal["U_Total"])+" W/m2*°C"
print "The total Resistance of the wall is "+str(Rtotal["R_Tot"])+" m2*°C/W" 
print "____________________________________________\n"
print "THE TOTAL HEAT LOSS throught the house is "+str(Qtot)+" W.\n"