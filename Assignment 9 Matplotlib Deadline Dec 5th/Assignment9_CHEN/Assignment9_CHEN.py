import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

labels = ["wall", "roof", "door"]
HeatingLoadValues = [1149.2,1240,92.5]
CoolingLoadValues= [547.5,514.6,43]
cols=["r","b","g"]

#first question
plt.figure()
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.title(" This is the share in the opaque heating load")

#second question
plt.figure()
plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.title(" This is the share in the opaque cooling load")

#third question
U=[0.2,0.4,0.6]
U_series = pd.Series(U)  

def ourFunction(U):
    Q=(105.8*U+200*0.25+2.2*1.694)*24.8
    return Q

Q_series =U_series.apply(ourFunction)

#Area=[105.8,200,2.2]
#DeltaT=24.8
#U=[0.438,0.25,1.694] #here chaging new value

plt.plot(U_series,Q_series)
plt.show()
plt.xlabel(" Uvalue of the wall  W/m2")
plt.ylabel(" Total heat load of opaque area W")
plt.title(" The relationship between Uvalue of the wall and Total heat load")


