import matplotlib.pyplot as plt

#plotting pie graph of the heating opaque load
col=["b","r","g"]
labels = ["walls","ceiling","door"]
TotalHeatingLoadOpaque = [1149,1240,92.5]
plt.pie(TotalHeatingLoadOpaque,labels=labels, colors=col, startangle=90)
plt.title("Total Heating Opaque Load")
plt.close()

#plotting pie graph of the cooling opaque load
col=["c","m","y"]
labels = ["walls","ceiling","door"]
TotalCoolingLoadOpaque = [547.5,514.6,43]
plt.pie(TotalCoolingLoadOpaque,labels=labels, colors=col, startangle=90, explode=(0.1,0.1,0))
plt.title("Total Cooling Opaque Load")
plt.close()

#effect of changing the U value of the external walls on the overall heating load
#U with glass fiber=0.438 W/m2K
#U=0.546 W/m2K  (air gap instead of glass fiber) (Qwalls= 1433W)
items=[1,2]
OverallHeatingLoadValue=[2765, 2483]
labels=["Total Heating Load Air Gap","Total Heating Load Glass Fiber"]
plt.bar(items,OverallHeatingLoadValue, color="g")
plt.xticks(items,labels,color="k")