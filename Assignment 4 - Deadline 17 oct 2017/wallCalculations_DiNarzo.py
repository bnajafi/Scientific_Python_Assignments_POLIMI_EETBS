# -*- coding: utf-8 -*-
def wall_calc_with_parallel(list_between_studs,list_at_studs,farea):
    Materials= {'Wood_bevel_lapped':0.14,'Wood_fiberboard':0.23,'Glass_fiber':2.45,'Wood_stud':0.63,'Gypsum':0.079,
    'Outside_sourface':0.03,'Inside_surface':0.12}
    Air= ['Outside_sourface','Inside_surface']
 
    #RESISTENCES
    #Calculating the wood stud
    
    Wall_wood= list_at_studs + Air
    
    R_wood_tot=0
    for anylayer in Wall_wood:
        R_wood=Materials[anylayer]
        R_wood_tot=R_wood_tot+R_wood
        print 'The R value of ' + str(anylayer) +' is ' + str(R_wood) +' °C/W'
        print ' '
    print 'The total value of R assuming a wall with stud is ' +str(R_wood_tot) +' °C/W'
    
    #Calculating for glass fiber
    
    Wall_glass=list_between_studs + Air
    
    R_glass_tot=0
    for anylayer1 in Wall_glass:
        R_glass=Materials[anylayer1]
        R_glass_tot= R_glass_tot+R_glass
        print 'The R value of ' + str(anylayer1) +' is ' + str(R_glass) +' °C/W'
        print ' '
    print 'The total value of R assuming a wall with glass is ' +str(R_glass_tot) +' °C/W'
    
    #HEAT TRANSFER COEFFICIENT
    
    U_stud= farea[1]/R_wood_tot
    U_glass= farea[0]/R_glass_tot
    U_tot= U_glass+U_stud
    
    print' '
    print 'The overall heat transfer coefficient is ' +str(U_tot) +' W/°C'
    
    R_tot=1/U_tot
    print ' '
    print 'The total resistence is ' +str(R_tot) +' °C/W'
    results= {'U_Total':U_tot,'R_total':R_tot}
    return results

def wallCalc_onlyInSeries(list_of_layers):
    Materials_s= {'Wood_bevel_lapped':0.14,'Wood_fiberboard':0.23,'Wood_5cm':0.44,'Glass_fiber':2.45,'Wood_stud':0.63,'Gypsum':0.079,
    'Outside_sourface':0.03,'Inside_surface':0.12}
    Air= ['Outside_sourface','Inside_surface']
    
    Layer_plus_air= list_of_layers+Air
    R_Tot_series=0
    for anylayer in Layer_plus_air:
        R_value=Materials_s[anylayer]
        R_Tot_series=R_Tot_series+R_value
        print 'The R value of ' + str(anylayer) +' is ' + str(R_value) +' °C/W'
        print ' '
    U_series=1/R_Tot_series
    print 'The U-Value is ' +str(U_series) +' W/°C'
    results_s= {'U_Total_series':U_series,'R_total_series':R_Tot_series}
    return results_s 