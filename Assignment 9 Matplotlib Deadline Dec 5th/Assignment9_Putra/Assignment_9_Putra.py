#---------------------------Assignment 9---------------------
#---------------------Hendra Suryana Putra--------------------

import matplotlib.pyplot as plt


# Opaque Heating Load Pie Chart

labels = ["Wall","Roof","Door"]
Heating_Load = [1149.2,1240,92.4]
col1 = ["orange","purple","blue"]
plt.pie(Heating_Load,labels=labels,colors=col1, startangle = 90, explode = (0.05,0.05,0.05), autopct='%1.1f%%')
plt.title("Heating Load Value on Opaque")

# Opaque Cooling Load Pie Chart

plt.figure(2)
Cooling_Load = [543.8,514.6,43]
col2 = ["yellow","green","red"]
plt.pie(Cooling_Load,labels=labels,colors=col2, startangle = 90, explode = (0.05,0.05,0.05), autopct='%1.1f%%')
plt.title("Cooling Load Value on Opaque")

# External Wall U Value Changing

U_New = 0.5 # U new and U Old Ratio
Heating_Load_New = [U_New*1149.2,1240,92.4]
Cooling_Load_New = [U_New*543.8,514.6,43]
Total_Load = [sum(Heating_Load), sum(Cooling_Load)]
Total_Load_New = [sum(Heating_Load_New), sum(Cooling_Load_New)]
plt.figure(3)
items = [1,2]
labels = ["Total Heating Load","Total Cooling Load"]
plt.bar(items,Total_Load,color=["Green","Purple"])
plt.bar(items,Total_Load_New,color=["brown","yellow"])
plt.xticks(items,labels,color="red")
plt.title("50% Reduction of External wall effect in Total Heating and Cooling Load")


