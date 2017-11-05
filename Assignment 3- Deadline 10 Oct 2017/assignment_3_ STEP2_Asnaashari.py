
def Heat_Transfer_Calculate(layers_atStuds,layers_betweenStuds,f_insulation,f_stud):
    material_library={"out_Surface":0.03,"woodBevel":0.14,"woodFiberboard13mm":0.23,"GlassFiber90mm":2.45,"woodStud90":0.63,"gypsumWallboard13mm":0.079,"inside_Surface":0.12}
    layers_atstuds=["gypsumWallboard13mm","woodStud90","woodFiberboard13mm","woodBevel"]     
    Layers_between_Studs=["gypsumWallboard13mm","GlassFiber90mm","woodFiberboard13mm","woodBevel"]  
    air=["out_Surface","inside_Surface"]
    T_in=22
    T_out=-2
    hight=2.5
    perimeter=50
    wall_area = 0.8*hight*perimeter
    f_insulation=0.75 
    f_stud=0.25
    
    wall_layers_atstuds = layers_atstuds+air
    wall_layers_betweenstuds = Layers_between_Studs+air
    
    Rtot_betweenstuds=0
    Rtot_atstuds=0
    R_values1=[]
    R_values2=[]
    
    for anylayers in wall_layers_atstuds:
        R_value=material_library[anylayers]
        R_values1.append(R_value)
        Rtot_atstuds=Rtot_atstuds+R_value
    print "R value for the material at studs is" +str( R_values1)
    print "The total thermal resistance unit calculated at studs is : "+str( Rtot_atstuds)+ " m^2(degC)/W"
    U_at_studs=1/Rtot_atstuds
    print " so  heat transfer coefficent at studs is" +str(U_at_studs)
    print "********************************"
    
    
    for anylayers in wall_layers_betweenstuds:
        R_value=material_library[anylayers]
        R_values2.append(R_value)
        Rtot_betweenstuds=Rtot_betweenstuds+R_value
    print "R value for the material at studs is" +str( R_values2)
    print "The total thermal resistance unit calculated between studs is : "+str(Rtot_betweenstuds)+ " m^2(degC)/W"
    U_betweenstuds=1/ Rtot_betweenstuds
    print " so  heat transfer coefficent in between is" +str(U_betweenstuds)
    print "**************************************************"
    
    U_overall=(U_betweenstuds*f_insulation)+(U_at_studs*f_stud)
    print "total overall heat transfer coefficent is" +str(U_overall)
    
    #calculating  total heat transfer
    
    Q_Wall=U_overall*wall_area*(T_in-T_out)
    print " the rate of heat loss through the walls of the house " +str(Q_Wall)

layers_atStuds = ["gypsumWallboard13mm","woodStud90","woodFiberboard13mm","woodBevel"] 
layers_betweenStuds= ["gypsumWallboard13mm","GlassFiber90mm","woodFiberboard13mm","woodBevel"] 

results= Heat_Transfer_Calculate(layers_atStuds,layers_betweenStuds,0.75,0.25)