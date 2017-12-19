import pandas as pd

def series_array():
    resistance_names = ["R1","R2","R3","R4","R5"]
    resistances_types = ["conv","cond","cond","cond","conv"]
    resistances_h = [10,None,None,None,25]
    resistances_k=  [None,0.026,0.22,0.22,None]
    resistances_L= [None,0.03,0.02,0.02,None]
    Resistances_RValues= [0,0,0,0,0]
    complete_resistence_array=pd.DataFrame([resistances_types,resistances_h,resistances_k,resistances_L,Resistances_RValues],
    index=['types','h','k','L', 'RVal'],columns=resistance_names)
    area=0.25
    complete_resistence_array.loc['RVal'][complete_resistence_array.loc['types']=='cond']=complete_resistence_array.loc['L']/(complete_resistence_array.loc['k']*area)
    complete_resistence_array.loc['RVal'][complete_resistence_array.loc['types']=='conv']=1.0/(complete_resistence_array.loc['h']*area)
    return complete_resistence_array

def parallel_array():
    resistance_names = ["R1","R2", "R3"]
    area=[0.015,0.22, 0.015]
    resistances_k=  [0.22,0.72,0.22]
    resistances_L= 0.16
    Resistances_RValues=[0.0,0.0,0.0]
    complete_resistence_array=pd.DataFrame([area, resistances_k, Resistances_RValues], index=['A','k','RVal'], columns=resistance_names)
    complete_resistence_array.loc['RVal']=resistances_L/(complete_resistence_array.loc['k']*complete_resistence_array.loc['A'])
    return complete_resistence_array
    
R_Total=(1.0/((1.0/parallel_array().loc['RVal']).sum()))+(series_array().loc['RVal'].sum())