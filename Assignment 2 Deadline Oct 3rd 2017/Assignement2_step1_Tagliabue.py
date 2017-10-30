#ASSIGNMENT 2 PART 1
A=3*5
Ap=(3.0/0.25*0.03)*5
Ab=(3/0.25*0.22)*5
RValue1=RValue2=RValue3=RValue4=RValue0=RValue5=0
Ti=20
To=10
R1=[A,0.03,0.026,RValue1] #foam: area lenght conductivity
R2=[A,0.04,0.22,RValue2] #plaster V: area,lenght,conductivity
R3=[Ap,0.16,0.22,RValue3] #plaster H: area,lenght,conductivity
R4=[Ab,0.16,0.72,RValue4] #brick: area,lenght,conductivity
R0=[A,1,10,RValue0]#indoor
R5=[A,1,25,RValue5]#outdoor
Allres=[R1,R2,R3,R4,R0,R5]
print ("This are all the resistances",Allres)
parallelres=[R3,R4]
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