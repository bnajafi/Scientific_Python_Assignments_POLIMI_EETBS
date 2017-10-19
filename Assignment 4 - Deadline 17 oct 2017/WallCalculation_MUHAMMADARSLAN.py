# 16/10/17

#----------------Assignment-4--Part-1------------------#

#---------Example (Calculation of U-Values)-----------#

#------------------MUHAMMAD ARSLAN------------------- #

#-----------------Using Function ---------------------#

#------------------Values-Defined---------------------#

Wall_material={"Wood bevel":{"Rvalue":0.14,"length":13},"Wood fiberboard":{"Rvalue":0.23,"length":13},"Glass fiber insulation":{"Rvalue":2.52,"length":90},"Wood stud":{"Rvalue":0.63,"length":90},"Gypsum wallboard":{"Rvalue":0.079,"length":13},"insideSurface":{"Rvalue":0.12},"outsideSurfaceWinter":{"Rvalue":0.030},"Wood":{"Rvalue":0.44},"Asphalt shingle roofing":{"Rvalue":0.077}}
layers_In_series=["insideSurface","outsideSurfaceWinter","Wood bevel","Wood fiberboard","Gypsum wallboard"]
fractionBetweenstuds=0.70
layers_for_Roof=["insideSurface","outsideSurfaceWinter","Wood","Asphalt shingle roofing"]
layers_for_Door=["insideSurface","outsideSurfaceWinter","Wood"]

def wallCalc_LIS(): #Layers in series

      between_Studs=layers_In_series+["Glass fiber insulation"]
      at_Studs=layers_In_series+["Wood stud"]

      Rvalue_between=0           
      Rvalue_at=0                

      for layer in between_Studs:
          Rvalue_between+=Wall_material[layer]["Rvalue"]          

      for layer in at_Studs:
          Rvalue_at+=Wall_material[layer]["Rvalue"]
          
      Uwall=(fractionBetweenstuds*(1/Rvalue_between)+(1-fractionBetweenstuds)*(1/Rvalue_at))
      return Uwall
          
print ("\The u value of wall is: "+str(wallCalc_LIS())+" wat")           
              
def wallCalc_DR():

      R_Door=0           
      R_Roof=0  
       
      
                       

      for layer in layers_for_Door:
          
           R_Door+=Wall_material[layer]["Rvalue"]
      Udoor=(1/R_Door)          

      for layer in layers_for_Roof:
          
           R_Roof+=Wall_material[layer]["Rvalue"]
      R_Roof*=6
      Uroof= (1/R_Roof)
           
      return {"U-Value of Door":Udoor,"U-value of Roof":Uroof}    
          

print ("\The u value of wall is: "+str(wallCalc_DR())+" wat")                        