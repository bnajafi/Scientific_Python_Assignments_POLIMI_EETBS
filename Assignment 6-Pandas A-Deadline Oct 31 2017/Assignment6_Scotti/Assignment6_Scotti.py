import pandas as pd
 
#Defining a Matrix for series Resistances
resistance_names = ["R1","R2","R3","R4","R5"]
resistances_types = ["conv","cond","cond","cond","conv"]
resistances_h = [10,None,None,None,25]
resistances_k=  [None,0.026,0.22,0.22,None]
resistances_L= [None,0.03,0.02,0.2,None]
resistances_RValues=[0,0,0,0,0]

resistances_ListOfLists  = [resistances_types,resistances_h,resistances_k,resistances_L,resistances_RValues]

resistances_DataFrame = pd.DataFrame(resistances_ListOfLists,index=["type","h","k","L","Rvalues"], columns=resistance_names)



resistances_DataFrame.loc["Rvalues"][resistances_DataFrame.loc["type"]=="conv"]=1.0/resistances_DataFrame.loc["h"][resistances_DataFrame.loc["type"]=="conv"]
resistances_DataFrame.loc["Rvalues"][resistances_DataFrame.loc["type"]=="cond"]=resistances_DataFrame.loc["L"][resistances_DataFrame.loc["type"]=="cond"]/resistances_DataFrame.loc["k"][resistances_DataFrame.loc["type"]=="cond"]

print resistances_DataFrame   
print ""


#Defining a Matrix with info about resistances in parallel
resistance_names_p = ["R1","R2","R3"]
resistances_types_p = ["cond","cond","cond"]
resistances_k_p=  [0.22,0.72,0.22]
resistances_L_p= [0.02,0.16,0.22]
resistances_RValues_p=[0,0,0]

resistancesp_ListOfLists  = [resistances_types_p,resistances_k_p,resistances_L_p,resistances_RValues_p]
resistancesp_DataFrame = pd.DataFrame(resistancesp_ListOfLists,index=["type","k","L","Rvalues"], columns=resistance_names_p)
resistancesp_DataFrame.loc["Rvalues"][resistancesp_DataFrame.loc["type"]=="cond"]=resistancesp_DataFrame.loc["L"][resistancesp_DataFrame.loc["type"]=="cond"]/resistancesp_DataFrame.loc["k"][resistancesp_DataFrame.loc["type"]=="cond"]

print resistancesp_DataFrame

