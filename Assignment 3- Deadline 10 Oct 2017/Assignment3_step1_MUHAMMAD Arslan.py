# 08/10/17
#  ----------------Assignment-3--Step-1--------------------
#  ---Example-1 (Calculation of U-heat transfer co-efficient,R-thermal resistance,Q-Heat loss)---

# ------------------MUHAMMAD ARSLAN--------------------

# Here, I have split the problem on two basis; "Btw the studs" & "At the studs"

#-----------------------------------------------------------------------------#

Wall_material={"Wood bevel":{"Rvalue":0.14,"length":13},"Wood fiberboard":{"Rvalue":0.23,"length":13},"Glass fiber insulation":{"Rvalue":2.52,"length":90},"Wood stud":{"Rvalue":0.63,"length":90},"Gypsum wallboard":{"Rvalue":0.079,"length":13},"insideSurface":{"Rvalue":0.12},"outsideSurfaceWinter":{"Rvalue":0.030}}

layers_In_series=["insideSurface","outsideSurfaceWinter","Wood bevel","Wood fiberboard","Gypsum wallboard"]

between_Studs=layers_In_series+["Glass fiber insulation"]

at_Studs=layers_In_series+["Wood stud"]

fractionBetweenstuds=0.75  #Given in data
RValue_between=0           #Assumed to start process
RValue_at=0                #Assumed to start process

for layer in between_Studs:
    RValue_between+=Wall_material[layer]["Rvalue"]
          
for layer in at_Studs:
    RValue_at+=Wall_material[layer]["Rvalue"]

#------overall heat transfer co-efficient-----#
        
Uoverall=(fractionBetweenstuds*(1/RValue_between)+(1-fractionBetweenstuds)*(1/RValue_at))
print ("The overall heat transfer coefficient(U-factor) is : "+str(Uoverall)+" W/m^2 degC")

#------overall thermal resistance-----#

Roverall=(1/Uoverall)
print("The overall unit therml resistance(R-Value) is : "+str(Roverall)+" m^2 degC/W")

#--------------------End-----------------#

#--------Wall Area---------#

perimeter=50
height=2.5
glazingpercent=20

WA=(1-(glazingpercent/100.0))*perimeter*height

#-------Total heat loss----#

out_T=-2
in_T=22

heatLoss=int(Uoverall*WA*(in_T-out_T))
print("The heat loss through the wall is: "+str(heatLoss)+" W")
