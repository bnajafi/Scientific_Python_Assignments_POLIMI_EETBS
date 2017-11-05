Material_library={"stucco_25mm": 0.037, "faceBrick_100mm": 0.075,
    "insideSurface":0.12, "outsideSurfaceSummer":0.044, "outsideSurfaceWinter":0.030
    ,"woodfiberboard_13mm":0.23,"gypsumBoard":0.079,"woodStud":0.63,"woodBevel":0.14,
    "buildingPaper":0.011,"acousticTile":0.32,"slag_13mm":0.067,"glassFiber":2.45}

List_series=["woodBevel","woodfiberboard_13mm",
        "gypsumBoard"]
List_parallel=["glassFiber","woodStud"] #first noun of list: insulation
List_air=["outsideSurfaceWinter","insideSurface"]
f=0.75 #f insulation
R2=[]

List_complete=List_series+List_air
Rtot=0
for anyLayer in List_complete:
    R_anyLayer=Material_library[anyLayer]
    Rtot=Rtot+R_anyLayer

for i in List_parallel:
    List=List_complete.append(i)
    R=Rtot+Material_library[i]
    R2=R2+[R]
U_overall=(1/R2[0]*f)+(1/R2[1]*(1-f))    
#R2 is a list which contains value of resistances: first one for a wall made all
#of insulation, and second one for all wood stud
Area=0.8*2.5*50
Tin=22
Tout=-2

Q_overall=U_overall*Area*(Tin-Tout)
print ("the overall transmittance value is "+str(U_overall)+" W/m2/K")
print ("The overall heat rate is "+str(Q_overall)+"W")  