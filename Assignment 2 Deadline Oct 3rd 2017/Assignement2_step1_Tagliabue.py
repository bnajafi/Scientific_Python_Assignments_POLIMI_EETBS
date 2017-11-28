#ASSIGNMENT 2 PART 1
RValue1=RValue2=RValue3=RValue4=RValue0=RValue5=0
Awall=15 #m2
Ti=20
To=-10
R1=[0.25,0.03,0.026,RValue1] #foam: area lenght conductivity
R2=R6=[0.25,0.02,0.22,RValue2] #plaster V: area,lenght,conductivity
R3=R7=[0.015,0.16,0.22,RValue3] #plaster H: area,lenght,conductivity
R4=[0.22,0.16,0.72,RValue4] #brick: area,lenght,conductivity
R0=[0.25,1,10,RValue0]#indoor
R5=[0.25,1,25,RValue5]#outdoor0
Allres=[R1,R2,R3,R4,R0,R5]
print ("This are all the resistances",Allres)
parallelres=[R3,R4,R7]
gp=rp=0
seriesres=[R1,R2]
convres=[R0,R5]
i=0
for res in Allres: 
    res[3]=res[1]/(res[0]*res[2])
    print ("Value of resistance",i, "is" ,res[3])
    i=i+1
for pres in parallelres:
    gp=(1/pres[3]+gp)
Req=1/gp    
print ("The equivalent parallel resistance is Rp=",Req)

for sres in seriesres:
    Req=Req+sres[3]
for resis in convres:
    Req=Req+resis[3]
print ("The equivalent total resistance is Req=", Req)
#rate of heat tranfer
Q=(Ti-To)/Req
print ("The rate of heat transfer is Q=", Q)
Qwall=Q*Awall/0.25
