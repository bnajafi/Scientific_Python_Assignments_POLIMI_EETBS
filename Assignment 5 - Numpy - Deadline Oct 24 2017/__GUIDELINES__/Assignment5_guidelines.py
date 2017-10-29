import numpy as np

# Guidelines for Assignment 5, Step 1


# Here is a calculation which is similar to the one which is needed to calcualte the RValue of the resistances in series
# Pay attention that here the specfic resistance (per unit area) is calcualted
    
resistance_names = np.array(["R1","R2","R3","R4","R5"])
resistances_types = np.array(["conv","cond","cond","cond","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.8,1.5,0.05,None])
resistances_L= np.array([None,0.5,0.3,0.6,None])
Resistances_RValues= np.array(np.zeros(5))
Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/ resistances_k[resistances_types=="cond"]
Resistances_RValues[resistances_types=="conv"] = 1.0 / resistances_h[resistances_types=="conv"]
Resistances_Rtot=Resistances_RValues.sum()



# Guidelines for Assignment 5, Step 2

# Here is how you can define a material library using NumPy Arrays

materials_names= np.array(["stucco","faceBreak_100mm","woodFiberboard_13mm"]) # clearly this library is very limited and you should expand it
materials_Rvalues =np.array([0.023,0.075,0.23])

# now to choose The index for any material you can write:
thisLayer_name = "stucco"
thisLayer_Rvalue = materials_Rvalues[materials_names==thisLayer_name]

#  I can also define the names of different layers of wall as a numpy array

layerNames_myWall = np.array(["faceBreak_100mm","woodFiberboard_13mm"]) # this is just a very simple example wall

RValue_myWall = np.zeros(layerNames_myWall.size) # this creates a vector of zeros which has the same length as that of layers_myWall

# pay attention that for finding the Rvalue, you will still need to use for loop, since you have not yet learnt other commands that help applying an operation over an array 

for layerName in layerNames_myWall:
    RValue_myWall[layerNames_myWall==layerName] = materials_Rvalues[materials_names==layerName]
    

    
