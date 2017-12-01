import pandas as pd
import matplotlib.pyplot as plt

x=range(-10,11)
x_series = pd.Series(x)

def ourFunction(x):
    y=x**2-5
    return y

y_series = x_series.apply(ourFunction)


x1=[1,3,5,8]
y1=[12,18,28,39]

plt.plot(x1,y1)
plt.show()
plt.xlabel(" This is the name of my x axis")
plt.ylabel(" This is the name of my y axis")
plt.title(" This is just a random useless plot!")

x2=[2,4,7,8]
y2=[10,21,25,42]
plt.plot(x2,y2, hold=False)

plt.close("all")
plt.plot(x_series,y_series)

fig1 = plt.figure()
plt.close(fig1)
plt.figure(1)

plt.figure()
# How to plot scatter plots !!
x4=[3,4,5,8,12]
y4=[45,58,87,95,115]
x5=[4,5,9,10,11]
y5=[23,29,65,82,80]
plt.scatter(x4,y4,label="The first one",color="b",marker="*",s=50)
plt.scatter(x5,y5,label="The second one",color="r",marker="o",s=50)
plt.legend()
plt.close("all")

items = [1,2,3]
labels = ["wall","roof","door"]
HeatingLoadValues = [2500,1800,150]
cols=["r","b","g"]

plt.bar(items,HeatingLoadValues,color="g")
plt.xticks(items,labels,color="r")

# How to plot a pie chart !
plt.close("all")
plt.figure()
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%'))


       