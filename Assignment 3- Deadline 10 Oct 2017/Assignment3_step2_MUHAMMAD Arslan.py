# 10/10/17

#  ----------------Assignment-3--Step-2--------------------

#  ---Example-1 (Calculation of U-heat transfer co-efficient,R-thermal resistance,Q-Heat loss)---

# ------------------MUHAMMAD ARSLAN--------------------

#-------------------Using Function in this step----------------------------------------------------------#

def wallCalc():

      between_Studs=layers_In_series+["Glass fiber insulation"]
      at_Studs=layers_In_series+["Wood stud"]

      RValue_between=0           #Assumed to start process
      RValue_at=0                #Assumed to start process

      for layer in between_Studs:
          RValue_between+=Wall_material[layer]["Rvalue"]          

      for layer in at_Studs:
          RValue_at+=Wall_material[layer]["Rvalue"]
          
#-----------------Calculation-------------------------------#  
     
      Uoverall=(fractionBetweenstuds*(1/RValue_between)+(1-fractionBetweenstuds)*(1/RValue_at))  #overall heat transfer co-efficient

      Roverall=(1/Uoverall)                                                      #overall thermal resistance

      WA=(1-(glazingPercentage/100.0))*perimeter*height                          #Wall Area

      heatLoss=int(Uoverall*WA*(InsideTemperature-OutsideTemperature))           #Total heat loss    

      return{"Overall U":Uoverall,"Overall R":Roverall,"Heat loss":heatLoss}

Wall_material={"Wood bevel":{"Rvalue":0.14,"length":13},"Wood fiberboard":{"Rvalue":0.23,"length":13},"Glass fiber insulation":{"Rvalue":2.52,"length":90},"Wood stud":{"Rvalue":0.63,"length":90},"Gypsum wallboard":{"Rvalue":0.079,"length":13},"insideSurface":{"Rvalue":0.12},"OutsideSurfaceWinter":{"Rvalue":0.030}}
layers_In_series,fractionBetweenstuds,perimeter,height,glazingPercentage,OutsideTemperature,InsideTemperature=["insideSurface","OutsideSurfaceWinter","Wood bevel","Wood fiberboard","Gypsum wallboard"],0.75,50,2.5,20,-2,22
allresults=wallCalc()

print("The overall heat transfer coefficient(U-factor) is : "+str(allresults["Overall U"]))+" W/m^2 degC"
print("The overall unit therml resistance(R-Value) is : "+str(allresults["Overall R"]))+" m^2 degC/W"
print("The heat loss through the wall is: "+str(allresults["Heat loss"])+" W")
    
#--------------------End-----------------#