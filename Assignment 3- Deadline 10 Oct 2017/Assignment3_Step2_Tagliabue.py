#assignment 3 step 2 
#example 1 
wallcomposition = {"WoodLapSiding":{"Rvalue":0.14,"length":0.013},"Woodfiberboard":{"Rvalue":0.23,"length":0.013},
                   "GypsumWall":{"Rvalue":0.079,"length":0.013},"Insidesur":{"Rvalue":0.12},"Outsidesur":{"Rvalue":0.03},
                   "Glassfiberinsulation":{"Rvalue":2.45,"length":0.025},"Woodstud":{"Rvalue":0.63,"length":0.090}}
print (wallcomposition)
print ("***")
tempvar=24
area =(0.8*50*2.5)
series= ["Outsidesur","WoodLapSiding","Woodfiberboard","GypsumWall","Insidesur"]
parallel=["Glassfiberinsulation", "Woodstud"]
def function (listA,listB,composition):
    r1=0
    for i in listA:
        r1=r1+composition[i]["Rvalue"]
    print ("rserie is ",r1) 
    g2=r2=0
    for j in listB:
        g2=(g2+1/composition[j]["Rvalue"])
        r2=1/g2
    print ("rparal is ",r2)    
    ratio=0.75
    U=ratio*(1/r1)+(1-ratio)*(1/r2)
    return U

Ufactor= function (series,parallel,wallcomposition)
print ("The overall heat transfer coefficient is ", Ufactor)
print ("***")
Rtot= 1/Ufactor
print ("The overall thermal resistance is ", Rtot)
print ("***")
Q=(Ufactor*area*tempvar)
print ("The overall heat loss is ",Q)
print ("***")