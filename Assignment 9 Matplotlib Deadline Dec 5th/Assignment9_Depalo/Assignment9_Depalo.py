#Assignment 9 - Depalo

import pandas as pd
import matplotlib.pyplot as plt

#pie chart for heating loads through opaque components:
labels = ["wall","roof","door"]
HeatingLoadValues = [1149.2,1240,92.5]
cols=["yellow","g","aqua"]
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90, autopct='%1.1f%%')
plt.title("Share of each opaque component in the total heating load")

#pie chart for cooling loads through opaque components:
plt.figure(2)
CoolingLoadValues = [547.5,514.6,43]
cols2=["crimson","darkviolet","lightsalmon"]
plt.pie(CoolingLoadValues,labels=labels,colors=cols2,startangle=90, autopct='%1.1f%%')
plt.title("Share of each opaque component in the total cooling load")

#effect of changing the U value of the external wall on the overall heating and cooling loads:
Unew=0.75        #ratio between U new wall and U old
HeatingLoadValuesNew = [Unew*1149.2,1240,92.5]
CoolingLoadValuesNew = [Unew*547.5,514.6,43]
LoadSum=[sum(HeatingLoadValues), sum(CoolingLoadValues)]
LoadSumNew=[sum(HeatingLoadValuesNew), sum(CoolingLoadValuesNew)]
plt.figure(3)
items = [1,2]
labels = ["Heating","Cooling"]
plt.bar(items,LoadSum,color=['yellow',"crimson"])
plt.bar(items,LoadSumNew,color=['lightyellow',"palevioletred"])
plt.xticks(items,labels,color="grey")
plt.title("Effect of 25% reduction of the U value of the external wall on loads")