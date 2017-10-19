#assignment 3 step 1 
#example 1 
#definitions
wallcomposition = {"WoodLapSiding":{"Rvalue":0.14,"length":0.013},"Woodfiberboard":{"Rvalue":0.23,"length":0.013},
                   "GypsumWall":{"Rvalue":0.079,"length":0.013},"Insidesur":{"Rvalue":0.12},"Outsidesur":{"Rvalue":0.030},
                   "Glassfiberinsulation":{"Rvalue":2.45,"length":0.025},"Woodstud":{"Rvalue":0.63,"length":0.090}}
print (wallcomposition)
print ("***")

seriesbtw= ["Outsidesur","WoodLapSiding","Woodfiberboard","GypsumWall","Insidesur","Glassfiberinsulation"]
seriesat=["Glassfiberinsulation", "Woodstud","Insidesur","Outsidesur"]
ratio=0.75
tempvar=24
area =(0.8*50*2.5)
convectionlayers=["Insidersur","Outsidesur"]
res1=res2=0.00

for anymat in seriesbtw:
    res1=res1+wallcomposition[anymat]["Rvalue"]
print ("the resistance in serie between the stud is:", res1)
print ("***")

for ANYMAT in seriesat:
    res2=1/(1/res2+1/wallcomposition[anymat]["Rvalue"])
print ("The Resistance in serie at stud is:",res2)
print ("***")

U= ratio*(1/res1)+(1-ratio)*(1/res2)
print ("The overall heat transfer coefficient is ", U)
print ("***")

Roverall= 1/U
print ("The overall thermal resistance is ", Roverall)
print ("***")

Q= U*area*tempvar
print ("The overall heat loss is ", Q)
print ("***")