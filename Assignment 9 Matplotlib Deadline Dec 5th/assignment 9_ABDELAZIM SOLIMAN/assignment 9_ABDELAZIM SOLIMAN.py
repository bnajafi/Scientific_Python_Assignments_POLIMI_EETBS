import matplotlib.pyplot as plt

labels= ["Walls","Roof","Door"]
cols = ["r","g","b"]
heatingloads_values = [1149.2,1240,92.5]
coolingloads_values = [547.5,514.6,43]


#1. A pie chart showing the share of each component in the total heating load (opaque):

plt.pie(heatingloads_values,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')

plt.title ("Total Heating Load (Opaque)")

#2. A pie chart showing the share of each component in the total cooling load (opaque):

plt.pie(coolingloads_values,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')

plt.title("Total Cooling Load (Opaque)")

#3.A 2D plot which shows the effect of changing only the U value of the external wall on the overall heating load (opaque):


Uwall = range(0,10,1)
Qwall=[]
Qtot=[]

for U in Uwall:
    DT=24.8
    A=105.8
    Qvalue=DT*A*U
    Qwall.append(Qvalue)
    QvalueTot=Qvalue+heatingloads_values[1] + heatingloads_values [2]
    Qtot.append(QvalueTot)
print Qtot
print Qwall
plt.figure()
fig3=plt.plot(Uwall,Qtot)
plt.xlabel("U value of external wall  ")
plt.ylabel("Overall heating load")
plt.title("Effect changing U on Opaque Heating Load")












































