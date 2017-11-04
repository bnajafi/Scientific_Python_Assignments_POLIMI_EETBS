# -*- coding: utf-8 -*-
"""
CASALICCHIO VALERIA 10424146

Step 1: You should first define the material library as a dictionary (based on unit thermal resistances table), as we already did in our last lesson. 
Next, you will need to define the material names of layers only in series as one list, (as we did in the lesson), material names of the two layers in 
parallel as another list, and define the ratio between the area of the first parallel layer to the total one (e.g. 0.75) as a float. Next, the unit 
thermal resistance for each layer should be looked up from the defined material library, and the total unit resistances for the layers in series should 
be found. Similarly, for the two layers in parallel the unit thermal resistances should be looked up. Afterwards, the total unit thermal resistance is 
first found once just considering the first layer of the parallel ones, and then by considering the second one. Finally, the U values of each case is 
found and total U value is eventually determined using the corresponding equation.
"""

#Definition of the materials' library
Library_Material = {"Outside_Surface_Winter":0.030,
                    "Wood_Bevel_Lapped_Siding": 0.14,
                    "Wood_Fiberboard_Sheeting": 0.23,  
                    "Glass_Fiber_Insulation":2.45, 
                    "Wood_Stud":0.63,
                    "Gypsum_Wallboard":0.079,
                    "Inside_Surface": 0.12}

#Definition of the lists of the materials in series and in parallel
Layers_In_Series=["Outside_Surface_Winter","Wood_Bevel_Lapped_Siding","Wood_Fiberboard_Sheeting","Gypsum_Wallboard","Inside_Surface"]
Layers_In_Parallel=["Glass_Fiber_Insulation","Wood_Stud"]

#Definition of the relationship between the area of the first parallel layer and the total one
Ratio_Insulation=float(0.75)       

#Monitor the serie and parallel layers
Tot_R_Series=0
for anyLayer in Layers_In_Series:
    Tot_R_Series=Tot_R_Series+Library_Material[anyLayer]

List_R=[]  
for anyLayer in Layers_In_Parallel:
    R_Parallel=Tot_R_Series+Library_Material[anyLayer]
    List_R.append(R_Parallel)
 
#Calculate  the total global heat transfer coefficient and the total thermal resistance
Tot_U=round(Ratio_Insulation/List_R[0]+(1-Ratio_Insulation)/List_R[1],4)
Tot_R=round(1/Tot_U,4)

print "\n***********************************************************************\n"
print " GLOBAL HEAT TRANSFER COEFFICIENT= "+str(Tot_U)+" [W/m2°C]"   
print " \n TOTAL THERMAL RESISTANCE = "+str(Tot_R)+" [m2°C/W]"   
print "\n***********************************************************************\n"