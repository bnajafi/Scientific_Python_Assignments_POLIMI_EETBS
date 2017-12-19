#ASSIGNMENT 9
#Name:Shashwat Parsana

import pandas as pd
import matplotlib.pyplot as mplt

#PART 1
#make lists
label= ["walls","ceiling","door"]
col = ["r","g","b"]
Q_heating = [1149.2,1240,92.5]
Q_cooling = [547.5,514.6,43]

#Pie chart_heatingloads
mplt.pie(Q_heating,labels=label,colors=col,startangle=90, explode=(0.1,0.1,0.1), autopct='%1.1f%%')
mplt.title ("Q_heating of sharing loads for opaque surfaces")

#Pie chart_coolingloads
fig = mplt.figure()
mplt.pie(Q_cooling,labels=label,colors=col,startangle=90, explode=(0.1,0.1,0.1), autopct='%1.1f%%')
mplt.title ("Q_cooling of sharing loads for opaque surfaces")

#PART 2
#Plotting 2D plot
def Q_opaque_cal(Q_heatingwall):
    """Put the Q heating values of wall"""
    Q_opaque=Q_heatingwall+Q_heating[1]+Q_heating[2]
    return Q_opaque
Area = 105.8
T = 24.8
U = pd.Series(range(0,10,1))
Q_heatingwall = U * Area * T
Q_opaque = Q_heatingwall.apply(Q_opaque_cal)

fig2 = mplt.figure()
mplt.plot(U,Q_opaque)
mplt.xlabel("U value of external wall")
mplt.ylabel("Overall opaque heating load")
mplt.title("Effect of U-Value(External wall) on Opaque Heating Load")
    





